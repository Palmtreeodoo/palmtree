# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class BarcodeRule(models.Model):
    _inherit = "barcode.rule"

    # adding value to type field in barcode.rule
    type = fields.Selection(selection_add=[
        ('price_to_weight', _('Priced Product (Computed Weight)')),
        ('price_to_piece', _('Priced Product (Computed Piece)'))
    ])



