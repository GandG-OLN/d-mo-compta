# -*- coding: utf-8 -*-

from odoo import models, fields, api
from num2words import num2words


class gg_cash_report16(models.Model):
   
    _inherit = 'account.bank.statement.line'
    _description = 'Bank Statement Line'
    
    amount_text = fields.Char('Montant en lettres', compute='get_amount_text')
    
    
    
#    @api.depends('amount')
#    def get_amount_text(self):
#        for rec in self:
#            number_in_word = num2words(abs(rec.amount), lang='fr')
#            rec.amount_text = number_in_word and number_in_word.capitalize()
            
            
    @api.depends('amount')
    def get_amount_text(self):
        for record in self:
            record.amount_text = num2words.num2words(record.amount, lang='fr')
#            number_in_word = num2words(abs(record.amount), lang='fr')
#            record.amount_text = number_in_word and number_in_word.capitalize()
                   
            
            
  

