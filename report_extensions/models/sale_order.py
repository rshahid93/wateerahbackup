# -*- coding: utf-8 -*-

from odoo import api, fields, models
import qrcode
import base64
import io

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.model
    def get_qr_code(self):

        def get_qr_encoding(tag, field):
            company_name_byte_array = field.encode('UTF-8')
            company_name_tag_encoding = tag.to_bytes(length=1, byteorder='big')
            company_name_length_encoding = len(company_name_byte_array).to_bytes(length=1, byteorder='big')
            return company_name_tag_encoding + company_name_length_encoding + company_name_byte_array

        qr_code_str = ''
        seller_name_enc = get_qr_encoding(1, self.company_id.display_name)
        company_vat_enc = get_qr_encoding(2, self.company_id.vat or '')
        time_sa = fields.Datetime.context_timestamp(self.with_context(tz='Asia/Riyadh'), self.date_order or self.create_date)
        timestamp_enc = get_qr_encoding(3, time_sa.isoformat())
        invoice_total_enc = get_qr_encoding(4, str(self.amount_total))
        total_vat_enc = get_qr_encoding(5, str(self.currency_id.round(self.amount_total - self.amount_untaxed)))

        str_to_encode = seller_name_enc + company_vat_enc + timestamp_enc + invoice_total_enc + total_vat_enc
        qr_code_str = base64.b64encode(str_to_encode).decode('UTF-8')
        print("TESTTTTTTTTTTTTTTTTTTTTTTTT",qr_code_str)
        return qr_code_str


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    line_no = fields.Char('No.')
