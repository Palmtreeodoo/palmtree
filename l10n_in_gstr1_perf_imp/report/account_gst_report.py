# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models

class L10nInReportAccount(models.AbstractModel):
    _description = "GST Report"
    _inherit = "l10n.in.report.account"

    def get_gst_section_model_domain(self, gst_return_type, gst_section):
        res = super().get_gst_section_model_domain(gst_return_type, gst_section)
        if res and res.get('model') == 'l10n_in.account.invoice.report':
            res['model'] = 'l10n_in.account.invoice.report.temp'
        return res