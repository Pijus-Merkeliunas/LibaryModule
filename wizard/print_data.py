from odoo import api, fields, models

class printData(models.TransientModel):
    _name = "lib.print.wizard"
    _description = "Print data wizard"

    from_date = fields.Datetime('begin_date')
    to_date = fields.Datetime('end_date')

    # date = fields.Many2one('lib.library','create_date')"""

    @api.model
    def print_required_data(self, cr, uid, ids, context=None):
        #return self.env.ref('library.report_print_data').report_action(self)

        if ids:
            if not isinstance(ids, list):
                ids = [ids]
            context = dict(context or {}, active_ids=ids, active_model=self._name)

        data = {}
        data['ids'] = context.get('name', [])
        data['model'] = context.get('lib.library', 'ir.ui.menu')

        return self.pool['report'].get_action(cr, uid, [], 'library.report_print_data', data=data, context=context)