# -*- coding: utf-8 -*-
# from odoo import http


# class PosCashDiscount(http.Controller):
#     @http.route('/pos_cash_discount/pos_cash_discount/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_cash_discount/pos_cash_discount/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_cash_discount.listing', {
#             'root': '/pos_cash_discount/pos_cash_discount',
#             'objects': http.request.env['pos_cash_discount.pos_cash_discount'].search([]),
#         })

#     @http.route('/pos_cash_discount/pos_cash_discount/objects/<model("pos_cash_discount.pos_cash_discount"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_cash_discount.object', {
#             'object': obj
#         })
