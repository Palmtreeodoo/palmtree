# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class duplicate_tax_invoice_print(models.Model):
#     _name = 'duplicate_tax_invoice_print.duplicate_tax_invoice_print'
#     _description = 'duplicate_tax_invoice_print.duplicate_tax_invoice_print'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
