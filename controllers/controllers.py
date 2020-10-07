# -*- coding: utf-8 -*-
from odoo import http

# class Hellowolrd(http.Controller):
#     @http.route('/hellowolrd/hellowolrd/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hellowolrd/hellowolrd/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hellowolrd.listing', {
#             'root': '/hellowolrd/hellowolrd',
#             'objects': http.request.env['hellowolrd.hellowolrd'].search([]),
#         })

#     @http.route('/hellowolrd/hellowolrd/objects/<model("hellowolrd.hellowolrd"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hellowolrd.object', {
#             'object': obj
#         })