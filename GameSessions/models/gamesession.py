from odoo import models, fields

class GameSession(models.Model):
    _name = 'game.session'
    _description = 'Game Session'
    _order = 'fecha desc'

    jugador_id = fields.Many2one(
        'res.partner',
        string="Jugador",
        required=True
    )

    juego = fields.Selection(
        [
            ('snake', 'Snake'),
            ('pong', 'Pong'),
            ('tetris', 'Tetris'),
        ],
        string="Juego",
        required=True
    )

    fecha = fields.Datetime(
        string="Fecha",
        default=fields.Datetime.now
    )

    duracion = fields.Integer(
        string="Duración (segundos)"
    )

    score = fields.Integer(
        string="Resultado (Score)"
    )

    estado = fields.Selection(
        [
            ('finalizada', 'Finalizada'),
            ('abandonada', 'Abandonada'),
        ],
        string="Estado",
        default='finalizada'
    )
