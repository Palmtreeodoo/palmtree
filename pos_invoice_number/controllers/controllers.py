# -*- coding: utf-8 -*-
# from odoo import http


# class PosInvoiceNumber(http.Controller):
#     @http.route('/pos_invoice_number/pos_invoice_number/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_invoice_number/pos_invoice_number/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_invoice_number.listing', {
#             'root': '/pos_invoice_number/pos_invoice_number',
#             'objects': http.request.env['pos_invoice_number.pos_invoice_number'].search([]),
#         })

#     @http.route('/pos_invoice_number/pos_invoice_number/objects/<model("pos_invoice_number.pos_invoice_number"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_invoice_number.object', {
#             'object': obj
#         })
