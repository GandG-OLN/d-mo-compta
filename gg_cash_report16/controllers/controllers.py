# -*- coding: utf-8 -*-
# from odoo import http


# class GgCashReport16(http.Controller):
#     @http.route('/gg_cash_report16/gg_cash_report16', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gg_cash_report16/gg_cash_report16/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gg_cash_report16.listing', {
#             'root': '/gg_cash_report16/gg_cash_report16',
#             'objects': http.request.env['gg_cash_report16.gg_cash_report16'].search([]),
#         })

#     @http.route('/gg_cash_report16/gg_cash_report16/objects/<model("gg_cash_report16.gg_cash_report16"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gg_cash_report16.object', {
#             'object': obj
#         })
