from odoo import api, fields, models
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
