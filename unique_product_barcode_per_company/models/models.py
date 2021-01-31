# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    @api.constrains('company_id')
    def _check_barcode(self):
        if self.barcode:
            product_rec = self.env['product.product'].search_count(
                [('barcode', '=', self.barcode), ('company_id', '=', self.company_id.id)])
            if product_rec > 1:
                raise ValidationError(_('A barcode can only be assigned to one product !'))


class ProductProduct(models.Model):
    _inherit = "product.product"

    _sql_constraints = [
        ('barcode_uniq', 'Check(1=1)', "A barcode can only be assigned to one product !"),
    ]

    @api.constrains('barcode', 'company_id')
    def _check_barcode(self):
        if self.barcode:
            product_rec = self.env['product.product'].search_count(
                [('barcode', '=', self.barcode), ('company_id', '=', self.company_id.id)])
            if product_rec > 1:
                raise ValidationError(_('A barcode can only be assigned to one product !'))


