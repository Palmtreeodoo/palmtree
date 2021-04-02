# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ResCompany(models.Model):
    _inherit = 'res.company'

    company_in_print = fields.Char(string="Name in Print")


class AccounMove(models.Model):
    _inherit = "account.move"

    vehicle_no = fields.Char(
        string='Vehicle No',
        track_visibility='onchange',
        help="Vehicle No of transporter"
    )

    transportation_mode = fields.Selection(
        [
            ('1', 'Road'),
            ('2', 'Rail'),
            ('3', 'Air'),
            ('4', 'Ship')
        ],
        string='Transportation Mode',
        help="""
        Mode of transport is a term used to distinguish substantially different ways to perform.
        The different modes of transport are air, road, rail and ship transport.
        """
    )


    ewaybill_no = fields.Char(
        string="E-Way Bill No",
        help="E-Way Bill Attachment"
    )


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _prepare_invoice(self):
        invoice_vals = super(SaleOrder, self)._prepare_invoice()

        if self.vehicle_no:
            invoice_vals['vehicle_no'] = self.vehicle_no
        if self.transportation_mode:
            invoice_vals['transportation_mode'] = self.transportation_mode
        if self.ewaybill_no:
            invoice_vals['ewaybill_no'] = self.ewaybill_no

        return invoice_vals



