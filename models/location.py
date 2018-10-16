# -*- coding: utf-8 -*-

from odoo import models, fields, api

class location(models.Model):
    _name = 'dummy.location'

    name = fields.Char()
    contents = fields.One2many('dummy.product',
                    'location',
                    string='Contents')