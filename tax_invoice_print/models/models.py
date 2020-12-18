# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    company_in_print = fields.Char(string="Name in Print")

