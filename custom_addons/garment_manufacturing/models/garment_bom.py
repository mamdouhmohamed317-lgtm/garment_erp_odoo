from odoo import models, fields, api

class MrpBom(models.Model):
    _inherit = 'mrp.bom'

    cutting_cost = fields.Float(string='Cutting Cost per Unit', default=0.0)
    sewing_cost = fields.Float(string='Sewing Cost per Unit', default=0.0)
    finishing_cost = fields.Float(string='Finishing Cost per Unit', default=0.0)
    other_operation_cost = fields.Float(string='Other Operations Cost', default=0.0)
    
    total_operations_cost = fields.Float(
        string='Total Operations Cost',
        compute='_compute_total_garment_cost',
        store=True
    )
    raw_material_cost = fields.Float(
        string='Total Raw Material Cost',
        compute='_compute_total_garment_cost',
        store=True
    )
    total_garment_cost = fields.Float(
        string='Estimated Garment Unit Cost',
        compute='_compute_total_garment_cost',
        store=True
    )

    @api.depends('cutting_cost', 'sewing_cost', 'finishing_cost', 'other_operation_cost', 'bom_line_ids.product_id', 'bom_line_ids.product_qty')
    def _compute_total_garment_cost(self):
        for bom in self:
            material_total = sum(line.product_id.standard_price * line.product_qty for line in bom.bom_line_ids)
            ops_total = bom.cutting_cost + bom.sewing_cost + bom.finishing_cost + bom.other_operation_cost
            bom.raw_material_cost = material_total
            bom.total_operations_cost = ops_total
            bom.total_garment_cost = material_total + ops_total