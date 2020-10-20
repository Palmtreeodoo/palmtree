# -*- coding: utf-8 -*-
# from odoo import http


# class PosAutoInvoiceCheck(http.Controller):
#     @http.route('/pos_auto_invoice_check/pos_auto_invoice_check/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_auto_invoice_check/pos_auto_invoice_check/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_auto_invoice_check.listing', {
#             'root': '/pos_auto_invoice_check/pos_auto_invoice_check',
#             'objects': http.request.env['pos_auto_invoice_check.pos_auto_invoice_check'].search([]),
#         })

#     @http.route('/pos_auto_invoice_check/pos_auto_invoice_check/objects/<model("pos_auto_invoice_check.pos_auto_invoice_check"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_auto_invoice_check.object', {
#             'object': obj
#         })
