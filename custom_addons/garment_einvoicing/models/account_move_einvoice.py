import base64
import qrcode
from io import BytesIO
from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    qr_code_image = fields.Binary(string='E-Invoice QR Code', compute='_generate_qr_code', store=True)

    @api.depends('name', 'amount_total', 'amount_tax', 'invoice_date')
    def _generate_qr_code(self):
        for move in self:
            if move.move_type in ['out_invoice', 'out_refund'] and move.name:
                qr_data = f"Seller: Garment Factory | Date: {move.invoice_date} | Total: {move.amount_total} | Tax: {move.amount_tax}"
                qr = qrcode.QRCode(version=1, box_size=4, border=1)
                qr.add_data(qr_data)
                qr.make(fit=True)
                img = qr.make_image(fill_color="black", back_color="white")
                buffer = BytesIO()
                img.save(buffer, format="PNG")
                move.qr_code_image = base64.b64encode(buffer.getvalue())
            else:
                move.qr_code_image = False