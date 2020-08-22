# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gestion_hopital(models.Model):
    _name = 'gestion_hopital.patient'
    _inherit = 'res.users'

    groupe = fields.Selection([
        ('O-', 'O-'),
        ('O+', 'O+'),
        ('B-', 'B-'),
        ('B+', 'B+'),
        ('A-', 'A-'),
        ('A+', 'A+'),
        ('AB-', 'AB-'),
        ('AB+', 'AB+'),
    ])
    numero = fields.Char(string="year", store=True)
    