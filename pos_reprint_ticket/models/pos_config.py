# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_receipt_design_reprint_id = fields.Many2one("pos.receipt.design", string="Custom Reprint Receipt")
