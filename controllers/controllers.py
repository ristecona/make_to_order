# -*- coding: utf-8 -*-
from odoo import http

# class MakeToOrder(http.Controller):
#     @http.route('/make_to_order/make_to_order/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/make_to_order/make_to_order/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('make_to_order.listing', {
#             'root': '/make_to_order/make_to_order',
#             'objects': http.request.env['make_to_order.make_to_order'].search([]),
#         })

#     @http.route('/make_to_order/make_to_order/objects/<model("make_to_order.make_to_order"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('make_to_order.object', {
#             'object': obj
#         })