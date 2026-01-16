from odoo import models, fields

class Libro(models.Model):
    _name = 'biblioteca.libro'
    _description = 'Libro'

    name = fields.Char(string='Título', required=True)
    autor = fields.Char(string='Autor')
    fecha_publicacion = fields.Date(string='Fecha de Publicación')
    paginas = fields.Integer(string='Número de Páginas')
autor_id = fields.Many2one(
    'biblioteca.autor',
    string='Autor',
    ondelete='restrict'
)
