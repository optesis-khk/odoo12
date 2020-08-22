# -*- coding: utf-8 -*-
from odoo import http

# class GestionHopital(http.Controller):
#     @http.route('/gestion_hopital/gestion_hopital/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion_hopital/gestion_hopital/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion_hopital.listing', {
#             'root': '/gestion_hopital/gestion_hopital',
#             'objects': http.request.env['gestion_hopital.gestion_hopital'].search([]),
#         })

#     @http.route('/gestion_hopital/gestion_hopital/objects/<model("gestion_hopital.gestion_hopital"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion_hopital.object', {
#             'object': obj
#         })