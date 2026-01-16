from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    nickname = fields.Char(
        string="Nickname"
    )

    puntos_acumulados = fields.Integer(
        string="Puntos acumulados",
        default=0
    )

    logros_desbloqueados = fields.Text(
        string="Logros desbloqueados"
    )

    avatar = fields.Binary(
        string="Avatar"
    )

    progreso_nivel = fields.Float(
        string="Progreso de nivel (%)",
        help="Porcentaje de progreso hacia el siguiente nivel"
    )
