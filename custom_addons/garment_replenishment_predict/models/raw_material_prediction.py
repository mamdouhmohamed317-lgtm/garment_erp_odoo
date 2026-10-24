from odoo import models, fields, api
from datetime import timedelta

class GarmentMaterialPrediction(models.Model):
    _name = 'garment.material.prediction'
    _description = 'Garment Fabric & Material Demand Prediction'

    product_id = fields.Many2one('product.product', string='Raw Material (Fabric/Trims)', required=True)
    current_qty = fields.Float(string='Current Stock In Factory')
    predicted_demand_30days = fields.Float(string='Predicted Demand (Next 30 Days)')
    shortage_qty = fields.Float(string='Estimated Shortage')
    recommended_purchase_qty = fields.Float(string='Recommended Order Qty')
    state = fields.Selection([
        ('normal', 'Stock Sufficient'),
        ('warning', 'Low Stock Warning'),
        ('critical', 'Critical Shortage')
    ], string='Alert Level', compute='_compute_alert_level', store=True)

    @api.depends('shortage_qty')
    def _compute_alert_level(self):
        for rec in self:
            if rec.shortage_qty <= 0:
                rec.state = 'normal'
            elif rec.shortage_qty < 50:
                rec.state = 'warning'
            else:
                rec.state = 'critical'

    @api.model
    def generate_predictions(self):
        self.search([]).unlink()
        date_30_days_ago = fields.Datetime.now() - timedelta(days=30)
        pos_lines = self.env['pos.order.line'].search([
            ('create_date', '>=', date_30_days_ago)
        ])
        
        material_demand = {}
        for line in pos_lines:
            bom = self.env['mrp.bom'].search([('product_tmpl_id', '=', line.product_id.product_tmpl_id.id)], limit=1)
            if bom:
                for bom_line in bom.bom_line_ids:
                    mat = bom_line.product_id
                    qty_needed = bom_line.product_qty * line.qty
                    material_demand[mat] = material_demand.get(mat, 0.0) + qty_needed
        
        for material, demand in material_demand.items():
            current_stock = material.qty_available
            shortage = demand - current_stock
            rec_qty = max(0.0, shortage * 1.2)
            
            self.create({
                'product_id': material.id,
                'current_qty': current_stock,
                'predicted_demand_30days': demand,
                'shortage_qty': max(0.0, shortage),
                'recommended_purchase_qty': rec_qty,
            })