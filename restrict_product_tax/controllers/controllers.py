# -*- coding: utf-8 -*-
# from odoo import http


# class RestrictProductTax(http.Controller):
#     @http.route('/restrict_product_tax/restrict_product_tax/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/restrict_product_tax/restrict_product_tax/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('restrict_product_tax.listing', {
#             'root': '/restrict_product_tax/restrict_product_tax',
#             'objects': http.request.env['restrict_product_tax.restrict_product_tax'].search([]),
#         })

#     @http.route('/restrict_product_tax/restrict_product_tax/objects/<model("restrict_product_tax.restrict_product_tax"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('restrict_product_tax.object', {
#             'object': obj
#         })
