from odoo import api, fields, models


class StockWarehouse(models.Model):
    _inherit = "stock.warehouse"

    register_payment = fields.Boolean(string="Register Payment on Confirm")
    default_journal_id = fields.Many2one(comodel_name='account.journal', string='Default Journal on Payments')

