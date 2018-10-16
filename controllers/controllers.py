# -*- coding: utf-8 -*-
from odoo import http

class DummyPipeline(http.Controller):
    @http.route('/dummy/pipeline/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/dummy/pipeline/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('dummy.pipeline.listing', {
            'root': '/dummy/pipeline',
            'objects': http.request.env['dummy.pipeline'].search([]),
        })

    @http.route('/dummy/pipeline/objects/<model("dummy.pipeline"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('dummy_pipeline.object', {
            'object': obj
        })