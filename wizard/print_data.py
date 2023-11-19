from odoo import api, fields, models

class printData(models.TransientModel):
    _name = "lib.print.wizard"
    _description = "Print data wizard"

    from_date = fields.Datetime('begin_date')
    to_date = fields.Datetime('end_date')

    # date = fields.Many2one('lib.library','create_date')"""

    def print_required_data(self):
        return self.env.ref('library.report_print_data').report_action(self)
        """
        if context is None:
            context = {}

        data = {}
        data['ids'] = context.get('active_ids', [])
        data['model'] = context.get('active_model', 'ir.ui.menu')
        return self.pool['report'].get_action(cr, uid, [], 'library.print_required_data', data=data, context=context)

    """