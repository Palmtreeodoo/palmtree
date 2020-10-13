# -*- coding: utf-8 -*-
# from odoo import http


# class PalmtreeWeightscale(http.Controller):
#     @http.route('/palmtree_weightscale/palmtree_weightscale/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/palmtree_weightscale/palmtree_weightscale/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('palmtree_weightscale.listing', {
#             'root': '/palmtree_weightscale/palmtree_weightscale',
#             'objects': http.request.env['palmtree_weightscale.palmtree_weightscale'].search([]),
#         })

#     @http.route('/palmtree_weightscale/palmtree_weightscale/objects/<model("palmtree_weightscale.palmtree_weightscale"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('palmtree_weightscale.object', {
#             'object': obj
#         })
