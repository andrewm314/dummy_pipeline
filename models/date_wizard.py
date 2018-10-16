# -*- coding: utf-8 -*-

from odoo import models, fields, api

import logging
_logger = logging.getLogger(__name__)

PARAMS = [
    ("default_date_period", "dummy.date.period"),
    ("default_date_fiscal", "dummy.date.fiscal"),
]

class date_wizard(models.TransientModel):
    _name='dummy.date.wizard'
    _inherit='res.config.settings'
    
    default_date_period = fields.Date('Lock Date period')
    default_date_fiscal = fields.Date('Lock Date fiscal')


    @api.multi
    def set_values(self):
        self.ensure_one()

        for field_name, key_name in PARAMS:
            value = getattr(self, field_name, '').strip()
            self.env['ir.config_parameter'].set_param(key_name, value)
        
        return self.get_default_values(None, None, None)

    @api.model
    def get_default_values(self, cr, uid, fields, context=None):
        res = {}
        for field_name, key_name in PARAMS:
            res[field_name] = self.env['ir.config_parameter'].get_param(key_name, '').strip()
        return res