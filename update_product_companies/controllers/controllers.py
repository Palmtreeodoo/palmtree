# -*- coding: utf-8 -*-
# from odoo import http


# class UpdateProductCompanies(http.Controller):
#     @http.route('/update_product_companies/update_product_companies/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/update_product_companies/update_product_companies/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('update_product_companies.listing', {
#             'root': '/update_product_companies/update_product_companies',
#             'objects': http.request.env['update_product_companies.update_product_companies'].search([]),
#         })

#     @http.route('/update_product_companies/update_product_companies/objects/<model("update_product_companies.update_product_companies"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('update_product_companies.object', {
#             'object': obj
#         })
