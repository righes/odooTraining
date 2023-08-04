from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"
    _order = "price desc"

    price = fields.Float("Price")
    status = fields.Selection(
        string = 'Status',
        selection = [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ],
        copy = False,
    )
    partner_id = fields.Many2one("res.partner", string="Partner", required = True)
    property_id = fields.Many2one("estate.property", string="Property", required = True)
    property_type_id = fields.Many2one("estate.property.type", related = "property_id.property_type_id", string = "Property Type", store=True)

    validity = fields.Integer("Validity (days)", default = 7)

    date_deadline = fields.Date("Deadline", compute="_compute_date_deadline", inverse="_inverse_date_deadline")

    @api.depends("validity")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = (record.create_date or fields.Datetime.now()).date() + timedelta(days = record.validity)

    def _inverse_date_deadline(self):
        for record in self:
            record.validity = (record.date_deadline - (record.create_date or fields.Datetime.now()).date()).days

    def accept_offer(self):
        for record in self:
            if record.status != False:
                raise UserError("This offer has already been handled.")
            else:
                for offer in self.property_id.offer_ids:
                    if offer.status == "accepted":
                        raise UserError("Another offer have been accepted!")
                record.status = "accepted"
                record.property_id.state = "offer_accepted"
                record.property_id.buyer_id = record.partner_id
                record.property_id.selling_price = record.price
        return True

    def refuse_offer(self):
        for record in self:
            if record.status != False:
                raise UserError("This offer has already been handled.")
            else:
                record.status = "refused"
        return True

    @api.model
    def create(self, vals):
        current_property = self.env['estate.property'].browse(vals['property_id'])
        if vals['price'] < current_property.best_price:
            raise ValidationError("Price can't be lower then the best offer!")
        current_property.state = "offer_received"
        return super().create(vals)

    _sql_constraints = [
        ("check_price", "check(price > 0)", "The price must be positive"),
    ]
