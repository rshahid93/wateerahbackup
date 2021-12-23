from odoo import api, fields, models, _
from datetime import date

class AccountPayment(models.Model):
    _inherit = "account.payment"
    
    create_cash_register_entry = fields.Boolean(string="Make Cash Register Entry")
    cash_register_id = fields.Many2one(comodel_name='account.bank.statement', string='Cash Register')


