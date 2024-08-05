from odoo import fields, models
from odoo.tools import date_utils


class RealEstateProperty(models.Model):
    _name = 'real.estate.property'
    _description = "Real Estate Property"

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    image = fields.Image(string="Image")
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        string="State",
        selection=[
            ('new', "New"),
            ('offer_received', "Offer Received"),
            ('under_option', "Under Option"),
            ('sold', "Sold"),
        ],
        required=True,
        default='new',
    )
    type_id = fields.Many2one(
        string="Type", comodel_name='real.estate.property.type', ondelete='restrict', required=True
    )
    selling_price = fields.Float(
        string="Selling Price", help="The selling price excluding taxes.", required=True
    )
    availability_date = fields.Date(
        string="Availability Date", default=date_utils.add(fields.Date.today(), months=2)
    )
    floor_area = fields.Integer(
        string="Floor Area", help="The floor area in square meters excluding the garden."
    )
    bedrooms = fields.Integer(string="Number of Bedrooms", default=2)
    has_garden = fields.Boolean(string="Garden")
    has_garage = fields.Boolean(string="Garage")
    seller_id = fields.Many2one(string="Seller", comodel_name='res.partner', required=True)
    salesperson_id = fields.Many2one(string="Salesperson", comodel_name='res.users')
    offer_ids = fields.One2many(
        string="Offers", comodel_name='real.estate.offer', inverse_name='property_id'
    )