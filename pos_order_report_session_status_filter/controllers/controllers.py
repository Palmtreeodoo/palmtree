# -*- coding: utf-8 -*-
# from odoo import http


# class PosOrderReportSessionStatusFilter(http.Controller):
#     @http.route('/pos_order_report_session_status_filter/pos_order_report_session_status_filter/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_order_report_session_status_filter/pos_order_report_session_status_filter/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_order_report_session_status_filter.listing', {
#             'root': '/pos_order_report_session_status_filter/pos_order_report_session_status_filter',
#             'objects': http.request.env['pos_order_report_session_status_filter.pos_order_report_session_status_filter'].search([]),
#         })

#     @http.route('/pos_order_report_session_status_filter/pos_order_report_session_status_filter/objects/<model("pos_order_report_session_status_filter.pos_order_report_session_status_filter"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_order_report_session_status_filter.object', {
#             'object': obj
#         })
