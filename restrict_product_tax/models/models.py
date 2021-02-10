# -*- coding: utf-8 -*-

from odoo import models, fields, api


class AccountTax(models.Model):
    _inherit = 'account.tax'

    not_in_product = fields.Boolean(string='Not in Product', default=False,
                                    help="If you choose true then this tax will not be available in Product master")


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    taxes_id = fields.Many2many('account.tax', 'product_taxes_rel', 'prod_id', 'tax_id',
                                help="Default taxes used when selling the product.", string='Customer Taxes',
                                domain=[('type_tax_use', '=', 'sale'), ('not_in_product', '=', False)],
                                default=lambda self: self.env.company.account_sale_tax_id)
    supplier_taxes_id = fields.Many2many('account.tax', 'product_supplier_taxes_rel', 'prod_id', 'tax_id',
                                         string='Vendor Taxes', help='Default taxes used when buying the product.',
                                         domain=[('type_tax_use', '=', 'purchase'), ('not_in_product', '=', False)],
                                         default=lambda self: self.env.company.account_purchase_tax_id)





