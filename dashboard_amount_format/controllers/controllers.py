# -*- coding: utf-8 -*-
# from odoo import http


# class DashboardAmountFormat(http.Controller):
#     @http.route('/dashboard_amount_format/dashboard_amount_format/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dashboard_amount_format/dashboard_amount_format/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dashboard_amount_format.listing', {
#             'root': '/dashboard_amount_format/dashboard_amount_format',
#             'objects': http.request.env['dashboard_amount_format.dashboard_amount_format'].search([]),
#         })

#     @http.route('/dashboard_amount_format/dashboard_amount_format/objects/<model("dashboard_amount_format.dashboard_amount_format"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dashboard_amount_format.object', {
#             'object': obj
#         })
