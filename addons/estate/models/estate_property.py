from odoo import api, fields, models
from dateutil.relativedelta import relativedelta

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    name = fields.Char("Name", required = True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availability = fields.Date("Available From", default = lambda self: fields.Datetime.now()+relativedelta(months=3), copy = False)
    expected_price = fields.Float("Expected Price", required = True)
    selling_price = fields.Float("Selling Price", readonly = True, copy = False)
    bedrooms = fields.Integer("Bedrooms", default = 2)
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(
        string = 'Garden Orientation',
        selection = [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West'),
        ],
    )
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(
        string = 'Status',
        selection = [
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled'),
        ],
        default = 'new',
        required=True,
        copy=False,
    )
    property_type_id = fields.Many2one("estate.property.type", string="Property Type")
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")
    offer_ids = fields.One2many("estate.property.offer", "property_id", string="Offers")
    seller_id = fields.Many2one('res.users', string="Salesman", default=lambda self: self.env.user)
    buyer_id = fields.Many2one('res.partner', string="Buyer", copy=False)

    total_area = fields.Float("Total Area (sqm)", compute = "_compute_total_area")

    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = self.living_area + self.garden_area

    best_price = fields.Float("Best Offer", compute = "_compute_best_price")

    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            record.best_price = max(self.offer_ids.mapped("price"), default = 0)

    @api.onchange("garden")
    def _onchange_partner_id(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = "north"
        else:
            self.garden_area = 0
            self.garden_orientation = False
