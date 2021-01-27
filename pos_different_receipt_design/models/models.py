# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosReceiptDesign(models.Model):
    _name = 'pos.receipt.design'
    _description = 'POS different receipt design'

    name = fields.Char(string="Name")
    receipt_design = fields.Text(string="Receipt", required=True)


class PosConfig(models.Model):
    _inherit = 'pos.config'

    use_custom_receipt = fields.Boolean(string="Use Custom Receipt")
    pos_receipt_design_id = fields.Many2one("pos.receipt.design", string="Custom Receipt")
