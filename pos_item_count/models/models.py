# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class pos_item_count(models.Model):
#     _name = 'pos_item_count.pos_item_count'
#     _description = 'pos_item_count.pos_item_count'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
