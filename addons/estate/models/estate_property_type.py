from odoo import api, fields, models

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"
    _order = "sequence, name"

    name = fields.Char("Name", required = True)
    sequence = fields.Integer("Sequence", default = 1, help = "Used to order stages. Lower is better.")
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Offers")
    offer_count = fields.Integer("Number of Offers", compute='_compute_offers') 

    _sql_constraints = [
        ("check_name", "UNIQUE(name)", "The name must be unique!"),
    ]

    @api.depends("offer_ids")
    def _compute_offers(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    def action_view_offers(self):
        res = self.env.ref("estate.property_offer_action").read()[0]
        res["domain"] = [("id", "in", self.offer_ids.ids)]
        return res
