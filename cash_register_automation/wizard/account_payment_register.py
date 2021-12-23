from odoo import api, fields, models
from datetime import date
import logging
_logger = logging.getLogger(__name__)

class AccountPaymentRegister(models.TransientModel):
    _inherit = "account.payment.register"

    create_cash_register_entry = fields.Boolean(string="Make Cash Register Entry")
    cash_register_id = fields.Many2one(comodel_name='account.bank.statement', string='Cash Register')
    
    def _create_payments(self):
        res = super(AccountPaymentRegister, self)._create_payments()
        for payment in res:
            payment.write({
                'create_cash_register_entry': self.create_cash_register_entry,
                'cash_register_id': self.cash_register_id
            })
        return res
    
    def action_create_payments(self):
        for wizard in self:
            wizard.cash_register_id.write({
                'line_ids': [(0,0,{
                    'date': wizard.payment_date,
                    'payment_ref': wizard.communication,
                    'partner_id': wizard.partner_id.id,
                    'amount': wizard.amount
                })]
            })
        return super(AccountPaymentRegister, self).action_create_payments()       
    
    @api.onchange('journal_id')
    def onchange_journal_id(self):
        for wizard in self:
            return {'domain': {'cash_register_id': [('state', '=', 'open'),('journal_id', '=', wizard.journal_id.id)]}}
        
    
    @api.depends('can_edit_wizard')
    def _compute_communication(self):
        for wizard in self:
            if wizard.can_edit_wizard:
                batches = self._get_batches()
                wizard.communication = wizard._get_batch_communication(batches[0])
            else:
                wizard.communication = False
            if self._context.get('communication', False):
                wizard.communication = self._context.get('communication', False)
    
    
    @api.depends('company_id', 'source_currency_id')
    def _compute_journal_id(self):
        for wizard in self:
            if self._context.get('journal_id', False):
                wizard.journal_id = self._context.get('journal_id', False)
                wizard.create_cash_register_entry = self.env['account.journal'].browse(self._context.get('journal_id', False)).type == 'cash'
                cash_register_id = self.env['account.bank.statement'].search([('state', '=', 'open'),('journal_id', '=', wizard.journal_id.id)], limit=1)
                if cash_register_id:
                    wizard.cash_register_id = cash_register_id
            else:
                domain = [
                    ('type', 'in', ('bank', 'cash')),
                    ('company_id', '=', wizard.company_id.id),
                ]
                journal = None
                if wizard.source_currency_id:
                    journal = self.env['account.journal'].search(domain + [('currency_id', '=', wizard.source_currency_id.id)], limit=1)
                if not journal:
                    journal = self.env['account.journal'].search(domain, limit=1)
                wizard.journal_id = journal

