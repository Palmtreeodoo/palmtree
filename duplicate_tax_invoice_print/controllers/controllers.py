# -*- coding: utf-8 -*-
# from odoo import http


# class DuplicateTaxInvoicePrint(http.Controller):
#     @http.route('/duplicate_tax_invoice_print/duplicate_tax_invoice_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/duplicate_tax_invoice_print/duplicate_tax_invoice_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('duplicate_tax_invoice_print.listing', {
#             'root': '/duplicate_tax_invoice_print/duplicate_tax_invoice_print',
#             'objects': http.request.env['duplicate_tax_invoice_print.duplicate_tax_invoice_print'].search([]),
#         })

#     @http.route('/duplicate_tax_invoice_print/duplicate_tax_invoice_print/objects/<model("duplicate_tax_invoice_print.duplicate_tax_invoice_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('duplicate_tax_invoice_print.object', {
#             'object': obj
#         })
