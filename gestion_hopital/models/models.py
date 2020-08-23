# -*- coding: utf-8 -*-

from odoo import models, fields, api

class gestion_hopital_patient(models.Model):
    _name = 'gestion_hopital.patient'
    _inherit = 'res.partner'

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
    numero = fields.Char(string="Numero",readonly=True, required=True, copy=False, default='New')
    date_naissance = fields.Date("Date de naissance")
    lieu_naissance = fields.Char(string="Lieu de Naissance")
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ], 'Sexe')
    numero_securite_sociale = fields.Char(string="Numero securité social")
    medecin_ids = fields.Many2many('gestion_hopital.medecin', 'medecin_patient_rel', 'patient_id', 'medecin_id', string="Medecin")
    
    
    @api.model
    def create(self, vals):
       if vals.get('numero', 'New') == 'New':
           vals['numero'] = self.env['ir.sequence'].next_by_code(
               'gestion_hopital.patient') or 'New'
       result = super(gestion_hopital_patient, self).create(vals)
       return result
    
    
class gestion_hopital_medecin(models.Model):
    _name = 'gestion_hopital.medecin'
    _inherit = 'res.partner'
    
    grade_id = fields.Many2one('gestion_hopital.grade', 'Grade')
    specialite_id = fields.Many2one('gestion_hopital.specialite', 'Specialité')
    sexe = fields.Selection([
        ('homme', 'Homme'),
        ('femme', 'Femme'),
    ], 'Sexe')
    code = fields.Char(string="Code Medecin")
    
    
class gestion_hopital_grade(models.Model):
    _name = "gestion_hopital.grade"
    
    nom = fields.Char(string="Libelle")
    code = fields.Char(string="Code")
    
    
class gestion_hopital_specialite(models.Model):
    _name = "gestion_hopital.specialite"
    
    nom = fields.Char(string="Libelle")
    code = fields.Char(string="Code")
    
    