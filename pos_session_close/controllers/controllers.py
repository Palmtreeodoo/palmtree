# -*- coding: utf-8 -*-
# from odoo import http


# class PosSessionClose(http.Controller):
#     @http.route('/pos_session_close/pos_session_close/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_session_close/pos_session_close/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_session_close.listing', {
#             'root': '/pos_session_close/pos_session_close',
#             'objects': http.request.env['pos_session_close.pos_session_close'].search([]),
#         })

#     @http.route('/pos_session_close/pos_session_close/objects/<model("pos_session_close.pos_session_close"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_session_close.object', {
#             'object': obj
#         })
