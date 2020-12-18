# -*- coding: utf-8 -*-
# from odoo import http


# class TaxInvoicePrint(http.Controller):
#     @http.route('/tax_invoice_print/tax_invoice_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tax_invoice_print/tax_invoice_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tax_invoice_print.listing', {
#             'root': '/tax_invoice_print/tax_invoice_print',
#             'objects': http.request.env['tax_invoice_print.tax_invoice_print'].search([]),
#         })

#     @http.route('/tax_invoice_print/tax_invoice_print/objects/<model("tax_invoice_print.tax_invoice_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tax_invoice_print.object', {
#             'object': obj
#         })
