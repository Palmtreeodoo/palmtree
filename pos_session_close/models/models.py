# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class pos_session(models.Model):
    _inherit = 'pos.session'


    def action_pos_session_closing_control(self):
        # The government does not want PS orders that have not been
        # finalized into an NS before we close a session
        regular_orders = self.env['pos.order'].search([('session_id', '=', self.id),('state', '!=', 'invoiced')])

        # we can link pro forma orders to regular orders using their pos_reference
        regular_orders = {order.pos_reference for order in regular_orders}
        non_finalized_orders = regular_orders

        if non_finalized_orders:
            raise UserError(_("Your session still contains Paid orders (%s).") % ', '.join(non_finalized_orders))

        return super(pos_session, self).action_pos_session_closing_control()
