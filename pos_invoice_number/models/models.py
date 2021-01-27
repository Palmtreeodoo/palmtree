# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PosConfigInvoiceSequence(models.Model):
    _name = 'pos.config.invoice.sequence'
    _description = "Point of Sale Invoice Sequence Configuration"
    name = fields.Char(string='Name', required=True)
    invoice_prefix = fields.Char(string='Prefix', required=True)
    invoice_seq = fields.Integer(string='Next Number', required=True)
    seq_size = fields.Integer(string='Sequence size', required=True)
    company_id = fields.Many2one('res.company', string='Company', default=lambda self: self.env.company)

class PosConfig(models.Model):
    _inherit = 'pos.config'

    # def _domain_invoice_sequence(self):
    #     pos_configs = self.search([('invoice_sequence_id', '!=', False)])
    #     used_invoice_sequence = []
    #     for config in pos_configs:
    #         used_invoice_sequence.append(config.invoice_sequence_id.id)
    #     domain = [('company_id', '=', self.env.company.id), ('id', 'not in', used_invoice_sequence)]
    #     return domain

    show_invoice_number = fields.Boolean(string='Receipt show invoice number', default=False)
    # invoice_prefix = fields.Char(string='Prefix', required=True)
    # invoice_seq = fields.Integer(string='Next Number', required=True)
    # seq_size = fields.Integer(string='Sequence size', required=True)
    invoice_sequence_id = fields.Many2one('pos.config.invoice.sequence', string='Invoice Sequence')


class PosOrder(models.Model):
    _inherit = 'pos.order'

    pos_invoice_number = fields.Char(string='Pos Invoice Ref', store=True, readonly=True)
    invoice_seq = fields.Integer(string='Next Number')

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)
        res.update({
            'pos_invoice_number': ui_order.get('pos_invoice_number', False),
            'invoice_seq': ui_order.get('invoice_seq', False),
        })
        return res

    @api.model
    def _process_order(self, order, draft, existing_order):
        res = super(PosOrder, self)._process_order(order, draft, existing_order)
        order = order['data']
        pos_session = self.env['pos.session'].browse(order['pos_session_id'])
        if pos_session.config_id.invoice_sequence_id and pos_session.config_id.invoice_sequence_id.invoice_seq <= order['invoice_seq']:
            pos_session.config_id.invoice_sequence_id.write({'invoice_seq': order['invoice_seq'] + 1})
        return res

    def _prepare_invoice_vals(self):
        """
        Prepare the dict of values to create the new invoice for a pos order.
        """
        res = super(PosOrder, self)._prepare_invoice_vals()
        res.update({'pos_invoice_number': self.pos_invoice_number})
        return res

    def refund(self):
        res = super(PosOrder, self).refund()
        order = self.browse(res['res_id'])
        if order.session_id.config_id.invoice_sequence_id:
            number = order.session_id.config_id.invoice_sequence_id.invoice_prefix + "" + str(order.session_id.config_id.invoice_sequence_id.invoice_seq).zfill(order.session_id.config_id.invoice_sequence_id.seq_size)
            order.pos_invoice_number = number
            order.invoice_seq = order.session_id.config_id.invoice_sequence_id.invoice_seq
            order.session_id.config_id.invoice_sequence_id.write({'invoice_seq': order.session_id.config_id.invoice_sequence_id.invoice_seq + 1})
        return res


class AccountMove(models.Model):
    _inherit = 'account.move'

    pos_invoice_number = fields.Char(string='Pos Invoice Ref', store=True, readonly=True)
