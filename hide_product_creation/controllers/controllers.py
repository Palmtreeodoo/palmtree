# -*- coding: utf-8 -*-
# from odoo import http


# class HideProductCreation(http.Controller):
#     @http.route('/hide_product_creation/hide_product_creation/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hide_product_creation/hide_product_creation/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hide_product_creation.listing', {
#             'root': '/hide_product_creation/hide_product_creation',
#             'objects': http.request.env['hide_product_creation.hide_product_creation'].search([]),
#         })

#     @http.route('/hide_product_creation/hide_product_creation/objects/<model("hide_product_creation.hide_product_creation"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hide_product_creation.object', {
#             'object': obj
#         })
