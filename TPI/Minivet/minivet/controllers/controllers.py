# -*- coding: utf-8 -*-
# from odoo import http


# class Minivet(http.Controller):
#     @http.route('/minivet/minivet/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/minivet/minivet/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('minivet.listing', {
#             'root': '/minivet/minivet',
#             'objects': http.request.env['minivet.minivet'].search([]),
#         })

#     @http.route('/minivet/minivet/objects/<model("minivet.minivet"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('minivet.object', {
#             'object': obj
#         })
