from odoo import api, fields, models,exceptions


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_confirm(self):
        res = super(SaleOrder,self).action_confirm()
        for order in self:
            warehouse = order.warehouse_id
            if warehouse.validate_invoice and warehouse.register_payment:
                return order.invoice_ids.with_context(
                    journal_id=warehouse.default_journal_id.id,
                    communication='%s (%s)' % (" ".join(order.invoice_ids.mapped('name')), order.name)
                ).action_register_payment()
        return res

