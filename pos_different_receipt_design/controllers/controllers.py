# -*- coding: utf-8 -*-
# from odoo import http


# class PosDifferentReceiptDesign(http.Controller):
#     @http.route('/pos_different_receipt_design/pos_different_receipt_design/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_different_receipt_design/pos_different_receipt_design/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_different_receipt_design.listing', {
#             'root': '/pos_different_receipt_design/pos_different_receipt_design',
#             'objects': http.request.env['pos_different_receipt_design.pos_different_receipt_design'].search([]),
#         })

#     @http.route('/pos_different_receipt_design/pos_different_receipt_design/objects/<model("pos_different_receipt_design.pos_different_receipt_design"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_different_receipt_design.object', {
#             'object': obj
#         })
