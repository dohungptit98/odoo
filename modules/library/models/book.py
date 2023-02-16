from odoo import api, fields, models

class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Library Book"

    name = fields.Char(string="Name", tracking=True)
    author = fields.Char(string="Author")
    describe = fields.Char(string="Describe")
    quantity = fields.Integer(string="Quantity")
    status = fields.Selection([('available', 'Available'), ('lock', 'Lock')], string="Status", tracking=True, default='available')