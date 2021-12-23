from odoo import api, fields, models
from datetime import date

class AccountJournal(models.Model):
    _inherit = "account.journal"

    create_cash_register = fields.Boolean(string="Auto Create Cash Register Daily")
    
    @api.model
    def _create_cash_register(self):
        for journal in self.search([('type', '=', 'cash'),('create_cash_register', '=', True)]):
            self.env['account.bank.statement'].create({
                'name': '%s %s' % (date.today().strftime("%Y/%m/%d"), journal.code),
                'journal_id': journal.id
            })

