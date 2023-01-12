# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class gg_cash_report16(models.Model):
#     _name = 'gg_cash_report16.gg_cash_report16'
#     _description = 'gg_cash_report16.gg_cash_report16'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
