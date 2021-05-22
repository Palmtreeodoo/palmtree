# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Stockpicking(models.Model):
    _inherit = 'stock.picking'


    @api.onchange('location_dest_id')
    def _onchange_default_location_dest_id(self):
        for stock in self:
            if stock.location_dest_id:
                for i in stock.move_line_ids_without_package:
                    i.write(
                    {
                        'location_dest_id':stock.location_dest_id.id,
                    }
                )

