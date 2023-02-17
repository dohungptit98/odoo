from odoo import api, fields, models

class LibraryStudent(models.Model):
    _name = "library.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Library Student"

    name = fields.Char(string="Name", tracking=True)
    date_of_birth = fields.Date(string="Date Of Birth")
    grade = fields.Char(string="Grade")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender", tracking=True, default='female')