from odoo import api, fields, models
from odoo.exceptions import UserError
from datetime import timedelta

class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer Model"

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
                record.property_id.state = "sold"
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
