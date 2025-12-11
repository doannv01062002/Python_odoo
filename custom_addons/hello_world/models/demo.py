from odoo import models, fields

class Demo(models.Model):
    _name = 'demo.hello'
    _description = 'Demo Model'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')