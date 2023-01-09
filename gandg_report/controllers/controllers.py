# -*- coding: utf-8 -*-
# from odoo import http


# class GandgReport(http.Controller):
#     @http.route('/gandg_report/gandg_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gandg_report/gandg_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gandg_report.listing', {
#             'root': '/gandg_report/gandg_report',
#             'objects': http.request.env['gandg_report.gandg_report'].search([]),
#         })

#     @http.route('/gandg_report/gandg_report/objects/<model("gandg_report.gandg_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gandg_report.object', {
#             'object': obj
#         })
