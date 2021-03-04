# -*- coding: utf-8 -*-
# from odoo import http


# class PosSessionAvoidDifference(http.Controller):
#     @http.route('/pos_session_avoid_difference/pos_session_avoid_difference/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_session_avoid_difference/pos_session_avoid_difference/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_session_avoid_difference.listing', {
#             'root': '/pos_session_avoid_difference/pos_session_avoid_difference',
#             'objects': http.request.env['pos_session_avoid_difference.pos_session_avoid_difference'].search([]),
#         })

#     @http.route('/pos_session_avoid_difference/pos_session_avoid_difference/objects/<model("pos_session_avoid_difference.pos_session_avoid_difference"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_session_avoid_difference.object', {
#             'object': obj
#         })
