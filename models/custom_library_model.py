from odoo import models, fields, api

class LibraryModel(models.Model):
    _name = 'lib.library'
    _description = 'Library Model description.'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    company = fields.Many2one('res.company', string="Company")