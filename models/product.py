# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

class product(models.Model):
    _name = 'dummy.product'

    name = fields.Char(required=True)
    quantity = fields.Integer(required=True)
    price_per_unit = fields.Integer(required=True)
    total_cost = fields.Integer(compute="_get_total_cost", store=True)

    description = fields.Text(compute="_get_dates", store=True)

    state = fields.Selection([('ordered', 'Ordered'),
                    ('out', 'Out for delivery'),
                    ('delivered', 'Delivered')])

    location = fields.Many2one('dummy.location')

    @api.depends("name")  
    def _get_dates(self):
        _logger.debug(self.env['ir.config_parameter'].get_param("dummy.date.period", '').strip())
        self.description = self.env['ir.config_parameter'].get_param("dummy.date.period", '').strip()


    @api.depends("quantity", "price_per_unit")  
    def _get_total_cost(self):
        self.total_cost = self.quantity * self.price_per_unit