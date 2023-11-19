from odoo import api, fields, models

class printData(models.TransientModel):
    _name = "lib.print.wizard"
    _description = "Print data wizard"

    from_date = fields.Datetime('begin_date')
    to_date = fields.Datetime('end_date')

    # date = fields.Many2one('lib.library','create_date')
