# -*- coding: utf-8 -*-
# from odoo import http


# class PosReprintTicket(http.Controller):
#     @http.route('/pos_reprint_ticket/pos_reprint_ticket/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_reprint_ticket/pos_reprint_ticket/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_reprint_ticket.listing', {
#             'root': '/pos_reprint_ticket/pos_reprint_ticket',
#             'objects': http.request.env['pos_reprint_ticket.pos_reprint_ticket'].search([]),
#         })

#     @http.route('/pos_reprint_ticket/pos_reprint_ticket/objects/<model("pos_reprint_ticket.pos_reprint_ticket"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_reprint_ticket.object', {
#             'object': obj
#         })
