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
    _description = "Grade Model"
    
    name = fields.Char(string="Libelle")
    code = fields.Char(string="Code")
    
    
class gestion_hopital_specialite(models.Model):
    _name = "gestion_hopital.specialite"
    _description = "Specialite Model"
    
    name = fields.Char(string="Libelle")
    code = fields.Char(string="Code")
    
    
class gestion_hopital_salle(models.Model):
    _name = "gestion_hopital.salle"
    _description = "Salle Model"
    
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (numero)',  'You can not have two rooms with the same number !')
    ]
    
    name = fields.Char(string="Salle")
    numero = fields.Char(string="Numero")
    nb_patient = fields.Integer(string="Nombre Patient")
    
    
class gestion_hopital_internat(models.Model):
    _name = 'gestion_hopital.internat'
    _description = "Internat Model"
    
    name = fields.Char(readonly=True, required=True, copy=False,default='New')
    salle_id = fields.Many2one('gestion_hopital.salle', string='Salle')
    patient_id = fields.Many2one('gestion_hopital.patient', string='Patient')
    in_date = fields.Date(string='Date Entrée')
    out_date = fields.Date(string='Date Entrée')
    note = fields.Text(string='Note')
    
    
    @api.model
    def create(self, vals):
       if vals.get('name', 'New') == 'New':
           patient = self.env['gestion_hopital.patient'].search([('id', '=', vals.get('patient_id'))])
           vals['name'] = 'Hospitalisation '+ patient.name or 'New'
       result = super(gestion_hopital_internat, self).create(vals)
       return result
    
    

    