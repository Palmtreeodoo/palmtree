# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


import logging
_logger = logging.getLogger(__name__)


class PosSession(models.Model):
    _inherit = 'pos.session'

    def action_pos_session_close(self):
        res = super(PosSession, self).action_pos_session_close()
        # Code to send sms to responsible about session.
        sms_template_objs = self.env["sms.notification.template"].sudo().search(
            [('condition', '=', 'session_closed'), ('globally_access', '=', False)])
        for sms_template_obj in sms_template_objs:
            # mobile = sms_template_obj._get_partner_mobile(self.user_id)
            if sms_template_obj.to:
                mobile = [sms_template_obj.to]
                for element in mobile:
                    for mobi_no in element.split(','):
                        mobile = mobi_no
                        if mobile:
                            sms_template_obj.send_sms_using_template(
                                mobile, sms_template_obj, obj=self)
            else:
                mobile = self.user_id.mobile
                if mobile:
                    sms_template_obj.send_sms_using_template(
                        mobile, sms_template_obj, obj=self)
        return res
