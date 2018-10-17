# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date
import logging

_logger = logging.getLogger(__name__)

class product(models.Model):
    _name = 'dummy.product'

    name = fields.Char(required=True)
    quantity = fields.Integer(required=True)
    price_per_unit = fields.Integer(required=True)
    total_cost = fields.Integer(compute="_get_total_cost", store=True)

    state = fields.Selection([('ordered', 'Ordered'),
                    ('out', 'Out for delivery'),
                    ('delivered', 'Delivered')])

    location = fields.Many2one('dummy.location')

    @api.constrains("name")
    def _check_date(self):
        _logger.info(self.env['ir.config_parameter'].get_param("dummy.date.period", '').strip())
        constrain_date = self.env['ir.config_parameter'].get_param("dummy.date.period", '').strip()
        today = str(date.today())
        if constrain_date > today:
            raise ValidationError("It's too early to do this, locked until: %s" % constrain_date)


    @api.depends("quantity", "price_per_unit")  
    def _get_total_cost(self):
        self.total_cost = self.quantity * self.price_per_unit
