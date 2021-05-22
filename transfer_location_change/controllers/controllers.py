# -*- coding: utf-8 -*-
# from odoo import http


# class TransferLocationChange(http.Controller):
#     @http.route('/transfer_location_change/transfer_location_change/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/transfer_location_change/transfer_location_change/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('transfer_location_change.listing', {
#             'root': '/transfer_location_change/transfer_location_change',
#             'objects': http.request.env['transfer_location_change.transfer_location_change'].search([]),
#         })

#     @http.route('/transfer_location_change/transfer_location_change/objects/<model("transfer_location_change.transfer_location_change"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('transfer_location_change.object', {
#             'object': obj
#         })
