from odoo import api, fields, models, _
from datetime import date

class AccountMove(models.Model):
    _inherit = "account.move"

    def action_register_payment(self):
        context = {
            'active_model' : 'account.move',
            'active_ids' : self.ids
        }
        if self._context.get('journal_id', False):
            context['journal_id'] = self._context.get('journal_id', False)
        elif self.invoice_user_id.property_warehouse_id and self.invoice_user_id.property_warehouse_id.default_journal_id:
            context['journal_id'] = self.invoice_user_id.property_warehouse_id.default_journal_id.id
        if self._context.get('communication', False):
            context['communication'] = self._context.get('communication', False)
        return {
            'name': _('Register Payment'),
            'res_model': 'account.payment.register',
            'view_mode': 'form',
            'context': context,
            'target': 'new',
            'type': 'ir.actions.act_window',
        }

