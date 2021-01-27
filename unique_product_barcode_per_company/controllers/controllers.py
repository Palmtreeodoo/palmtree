# -*- coding: utf-8 -*-
# from odoo import http


# class UniqueProductBarcodePerCompany(http.Controller):
#     @http.route('/unique_product_barcode_per_company/unique_product_barcode_per_company/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/unique_product_barcode_per_company/unique_product_barcode_per_company/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('unique_product_barcode_per_company.listing', {
#             'root': '/unique_product_barcode_per_company/unique_product_barcode_per_company',
#             'objects': http.request.env['unique_product_barcode_per_company.unique_product_barcode_per_company'].search([]),
#         })

#     @http.route('/unique_product_barcode_per_company/unique_product_barcode_per_company/objects/<model("unique_product_barcode_per_company.unique_product_barcode_per_company"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('unique_product_barcode_per_company.object', {
#             'object': obj
#         })
