# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime


class PosOrder(models.Model):
    _inherit = "pos.order"

    # passing values to take reprint from pos
    @api.model
    def get_orderlines(self, ref):
        discount = 0
        subtotal = 0
        result = []
        order = self.env['pos.order'].sudo().search([('id', '=', ref)], limit=1)
        lines = self.env['pos.order.line'].search([('order_id', '=', ref)])
        # session = self.env['pos.session'].search([('session_id', '=', self.session_id)])

        payment_lines = []
        order_details = {}
        details = {}
        change = 0
        payment_dict = {}


        for o in order:
            order_details = {
                'state_id': o.partner_id.state_id.name if o.partner_id.state_id.name else " ",
                'vat': o.partner_id.vat if o.partner_id.vat else False,
                'street': o.partner_id.street if o.partner_id.street else " ",
                'city': o.partner_id.city if o.partner_id.city else " ",
                'date_order': str(o.date_order),
                'is_gstin': True if o.partner_id.vat else False,
                'account_move': o.account_move.id if o.account_move else False,
                'partner_id': o.partner_id.id if o.partner_id else False,
                'partner_name': o.partner_id.name if o.partner_id else False,
                'phone': o.partner_id.phone if o.partner_id.phone else False,
                'partner_barcode': o.partner_id.barcode if o.partner_id else False,
                'id': o.id,
                'name': o.pos_reference,
                'pos_reference': o.pos_reference,
                'tot_amount': o.amount_total,
                'tot_tax': o.amount_tax,
                'tot_without_tax': o.amount_total - o.amount_tax,
                # 'loyalty_points': o.partner_id.loyalty_points if o.partner_id else 0,
                # 'ean13_barcode': o.ean13_barcode if o.ean13_barcode else 0,
                # 'ean':barcode.get('ean13', o.ean13_barcode, writer=ImageWriter())

            }
            for payment in o.payment_ids:
                if o.amount_total>0:
                    if payment.amount > 0:
                        payment_dict = {
                            'name': payment.payment_method_id.name if payment.payment_method_id.name else " ",
                            'amount': payment.amount if payment.amount else " "
                        }
                        payment_lines.append(payment_dict)
                    else:
                        change += payment.amount*-1
                else:
                    if payment.amount < 0:
                        payment_dict = {
                            'name': payment.payment_method_id.name if payment.payment_method_id.name else " ",
                            'amount': payment.amount if payment.amount else " "
                        }
                        payment_lines.append(payment_dict)
                    else:
                        change += payment.amount

            # for tax_line in o.account_move.tax_line_ids:
            #     if tax_line.tax_id.id not in details:
            #         taxable = 0
            #         invoice_lines = o.account_move.invoice_line_ids
            #         for line in lines:
            #             if o.fiscal_position_id:
            #                 for tax in line.tax_ids_after_fiscal_position:
            #                     if tax.children_tax_ids:
            #                         for child in tax.children_tax_ids:
            #                             if child.id == tax_line.tax_id.id:
            #                                 taxable += line.price_subtotal
            #                     else:
            #                         if tax_line.tax_id.id == tax.id:
            #                             taxable += line.price_subtotal
            #             else:
            #                 for tax in line.tax_ids:
            #                     if tax.children_tax_ids:
            #                         for child in tax.children_tax_ids:
            #                             if child.id == tax_line.tax_id.id:
            #                                 taxable += line.price_subtotal
            #                     else:
            #                         if tax_line.tax_id.id == tax.id:
            #                             taxable += line.price_subtotal
            #         details[tax_line.tax_id.id] = {
            #             'amount': round(tax_line.amount, 2),
            #             'name': tax_line.name,
            #             'taxable': taxable
            #         }
            #     else:
            #         details[tax_line.tax_id.id]['amount'] += round(tax_line.amount, 2)
            #         # details[tax_line.tax_id.id]['taxable'] += round(tax_line.base, 2)

        for line in lines:
            total_tax = line.price_subtotal_incl - line.price_subtotal
            for tax in line.tax_ids_after_fiscal_position:
                if tax.children_tax_ids:
                    for child in tax.children_tax_ids:
                        if child.id not in details:
                            details[child.id] = {
                                            'amount': round((total_tax*child.amount)/tax.amount, 2),
                                            'name': child.name,

                                        }
                        else:
                            details[child.id]['amount'] += round((total_tax*child.amount)/tax.amount, 2)
                if tax.amount_type == 'fixed':
                    if tax.id not in details:
                        details[tax.id] = {
                            'amount': round(total_tax, 2),
                            'name': tax.name,
                        }
                    else:
                        details[child.id]['amount'] += round(total_tax, 2)
                if tax.amount_type in ['percent', 'division']:
                    if tax.id not in details:
                        details[tax.id] = {
                            'amount': round(total_tax, 2),
                            'name': tax.name,
                        }
                    else:
                        details[tax.id]['amount'] += round(total_tax, 2)


            tax_id = line.tax_ids_after_fiscal_position.ids
            # tax_name = self.env["account.tax"].browse(tax_id).name if line.tax_ids else "None"

            new_vals = {
                'product_id': line.product_id.name,
                'unit': line.product_uom_id.name,
                'qty': line.qty,
                'price_unit': '%.2f' % line.price_unit,
                'discount': '%.2f' % line.discount,
                'price_subtotal': '%.2f' % line.price_subtotal,
                'display_price': '%.2f' % line.price_subtotal_incl if line.order_id.config_id.iface_tax_included =='total' else '%.2f' % line.price_subtotal,
                'tax': line.price_subtotal_incl - line.price_subtotal if line.price_subtotal_incl != 0 else 0,
                'price_subtotal_incl': '%.2f' % line.price_subtotal_incl,
                'tax_ids': line.tax_ids_after_fiscal_position.ids if line.tax_ids_after_fiscal_position else False,
            }
            discount += (line.price_unit * line.qty * line.discount) / 100
            subtotal += line.price_subtotal_incl
            result.append(new_vals)

        taxwithout = {}

        detail = []
        tax = 0

        for tax in details:
            detail.append({'amount': round(float(details[tax]['amount']), 2), 'name': details[tax]['name']})

        return [result, discount, payment_lines, change, order_details, detail, subtotal]

    # Passing order details to pos for showing list of order
    @api.model
    def get_details(self, ref):
        result = []
        if ref == None or ref == u'':
            order = self.env['pos.order'].sudo().search(
                [('company_id', '=', self.env.user.company_id.id),
                 ('state', 'not in', ['cancel']), ('user_id', '=', self.env.user.id)], limit=10)
        else:
            order = self.env['pos.order'].sudo().search(
                [('name', 'like', '%' + ref + '%'), ('company_id', '=', self.env.user.company_id.id),
                 ('state', 'not in', ['cancel']), ('user_id', '=', self.env.user.id)], limit=1)

        if order:
            for line in order:
                vals = {
                    'id': line.id,
                    'name': line.name,
                    'pos_reference': line.pos_reference,
                    'partner_id': line.partner_id.name,
                    'date_order': line.date_order,
                    'account_move': line.account_move.id,
                    'amount_total': '{:0,.2f}'.format(line.amount_total),
                }
                result.append(vals)
        return result