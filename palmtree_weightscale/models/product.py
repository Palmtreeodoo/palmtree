# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import base64

class ProductPrices(models.TransientModel):
    _name = 'product.price'

    product_id = fields.Many2one('product.product', string="Product")
    sale_price = fields.Integer(string="Sale Price")
    is_export = fields.Boolean(string='Export')
    to_weight = fields.Boolean(related='product_id.to_weight', string='To Weigh With Scale',
                               help="Check if the product should be weighted using the hardware scale integration")
    pricelist_id = fields.Many2one('product.pricelist', string='Pricelist')

    # update product price
    def change_product_price(self):
        prod_obj = self.env['product.product'].browse(self.product_id.id)
        # prod_value = {'list_price': self.sale_price, 'standard_price': self.cost_price}
        prod_value = {'list_price': self.sale_price}
        obj = prod_obj.write(prod_value)
        return obj

    # onchange sale price value to sale price of product
    @api.onchange('product_id')
    def get_price(self):
        prod_obj = self.env['product.product'].browse(self.product_id.id)
        self.sale_price = prod_obj.list_price

    # File creation
    def text_export_pricelist(self):
        prod_obj = self.env['product.product'].search([('to_weight', '=', True)])

        product_disc ={}

        for p in prod_obj:

            product_disc[p.product_tmpl_id.id] = {

                'plu':p.plu,
                'barcode':p.barcode,
                'name':p.name,
                'price':p.lst_price,
                'piece': '1' if p.is_piece else '0',

            }

        pricelist_items = self.pricelist_id.mapped('item_ids')

        for list in pricelist_items:

            if list.product_tmpl_id.id in product_disc:
                product_disc[list.product_tmpl_id.id]['price'] = list.fixed_price

        file_pro = ''
        if product_disc:
            for pro in product_disc:
                no = str(product_disc[pro]['piece'])
                file_pro += str(product_disc[pro]['plu']) + ',' + str(product_disc[pro]['barcode']) + ',' + str(product_disc[pro]['name']) + ',' + str(
                    product_disc[pro]['price']) + ',' + str(no) + '\r\n'
        data_bytes = file_pro.encode("utf-8")

        filename = '10,1001,Apple,250.00,1'

        filename += '\r\n'

        filename = filename + '4,1002,Orange,50.00,1'

        filename += '\r\n'

        filename = filename + '3,1003,grape,50.00,1'

        filename += '\r\n'

        filename = filename + '7,1013,Carrot,60.00,1'


        values = {

            'name': "plu.txt",

            # 'datas_fname': 'plu.txt',
            # 'res_name': 'plu.txt',

            'res_model': 'ir.ui.view',

            'res_id': False,

            'type': 'binary',

            'public': True,

            # 'datas': filename.encode('utf8').encode('base64'),
            'datas': base64.b64encode(data_bytes),
            # 'datas': base64.b64encode(file_pro),

        }

        # Using your data create as attachment.

        attachment_id = self.env['ir.attachment'].sudo().create(values)

        # Prepare your download URL download_url = '/web/content/' + str(attachment_id.id) + '?download=True'

        download_url = '/web/content/' + str(attachment_id.id) + '?download=True'
        # download_url = '/web/content/' + str(file) + '?download=True'
        base_url = self.sudo().env['ir.config_parameter'].get_param('web.base.url')

        # Return so it will download in your system return {
        return {

            "type": "ir.actions.act_url",

            "url": str(base_url) + str(download_url),

            "target": "new",

        }

    def text_export(self):
        prod_obj = self.env['product.product'].search([('to_weight', '=', True)])
        file_pro = ''
        if prod_obj:
            for pro in prod_obj:
                no = '1' if pro.is_piece else '0'

                file_pro += str(pro.plu) + ',' + str(pro.barcode) + ',' + str(pro.name) + ',' + str(pro.lst_price) + ',' + str(no) + '\r\n'


        filename = '10,1001,Apple,250.00,1'

        filename += '\r\n'

        filename = filename + '4,1002,Orange,50.00,1'

        filename += '\r\n'

        filename = filename + '3,1003,grape,50.00,1'

        filename += '\r\n'

        filename = filename + '7,1013,Carrot,60.00,1'


        values = {

            'name': "Name of text file.txt",

            'datas_fname': 'plu.txt',

            'res_model': 'ir.ui.view',

            'res_id': False,

            'type': 'binary',

            'public': True,

            # 'datas': filename.encode('utf8').encode('base64'),
            #'datas': base64.b64encode(filename),
            'datas': base64.b64encode(file_pro),

        }

        # Using your data create as attachment.

        attachment_id = self.env['ir.attachment'].sudo().create(values)

        # Prepare your download URL download_url = '/web/content/' + str(attachment_id.id) + '?download=True'


        download_url = '/web/content/' + str(attachment_id.id) + '?download=True'
        # download_url = '/web/content/' + str(file) + '?download=True'
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')

        # Return so it will download in your system return {
        return {

            "type": "ir.actions.act_url",

            "url": str(base_url) + str(download_url),

            "target": "new",

        }

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    plu = fields.Char(string='PLU', related='product_variant_ids.plu', readonly=False)
    is_piece = fields.Boolean(string='Is Piece', related='product_variant_ids.is_piece', readonly=False)



    @api.model
    def create(self, vals):
        product_template_id = super(ProductTemplate, self).create(vals)
        related_vals = {}
        if vals.get('plu'):
            related_vals['plu'] = vals['plu']
        if vals.get('is_piece'):
            related_vals['is_piece'] = vals['is_piece']

        if related_vals:
            product_template_id.write(related_vals)

        return product_template_id


class ProductProduct(models.Model):
    _inherit = 'product.product'

    plu = fields.Char(string='PLU')
    is_piece = fields.Boolean(string='Piece', default=False)

    _sql_constraints = [
        ('plu_uniq', 'unique(plu)', _("A plu can only be assigned to one product !")),
    ]

    # calls barcode sequence for updating barcode while creating product
    @api.model
    def create(self, vals):
        res = super(ProductProduct, self).create(vals)
        if not vals.get('barcode'):
            res['barcode'] = self.env['ir.sequence'].next_by_code('product.barcode')

        return res
