# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.tools.translate import _


class BarcodeSettings(models.Model):
    _name = 'item.barcode'

    barcode_x1 = fields.Char(string='barcode_x1', default='25')
    barcode_x2 = fields.Char(string='barcode_x2', default='225')
    barcode_y = fields.Char(string='barcode_y', default='33')

    itemname_x1 = fields.Char(string='item name_x1', default='10')
    itemname_x2 = fields.Char(string='item name_x2', default='210')
    itemname_y = fields.Char(string='item name_y', default='12')

    itemcode_x1 = fields.Char(string='item code_x1', default='25')
    itemcode_x2 = fields.Char(string='item code_x2', default='225')
    itemcode_y = fields.Char(string='item code_y', default='70')

    mrp_x1 = fields.Char(string='mrp_x1', default='25')
    mrp_x2 = fields.Char(string='mrp_x2', default='225')
    mrp_y = fields.Char(string='mrp_y', default='23')

    sellprice_x1 = fields.Char(string='sell price_x1', default='75')
    sellprice_x2 = fields.Char(string='sell price_x2', default='275')
    sellprice_y = fields.Char(string='sell price_y', default='70')

    customer_x1 = fields.Char(string='customer_x1', default='40')
    customer_x2 = fields.Char(string='customer_x2', default='240')
    customer_y = fields.Char(string='customer_y', default='0')

    barcount = fields.Char(string='barcount', default='2')
    mrpstatus = fields.Char(string='mrp status', default='0')
    datestatus = fields.Char(string='date status', default='0')

    datex1 = fields.Char(string='date x1', default='25')
    datex2 = fields.Char(string='date x2', default='225')
    datey = fields.Char(string='date y', default='85')

    dateexpx1 = fields.Char(string='date exp x1', default='25')
    dateexpy = fields.Char(string='date exp y', default='225')
    dateexpx2 = fields.Char(string='date exp x2', default='95')

    fnt8 = fields.Char(string='fnt8', default='8')
    fnt9 = fields.Char(string='fnt9', default='9')
    fnt10 = fields.Char(string='fnt10', default='10')
    fnt12 = fields.Char(string='fnt12', default='12')

    bcode_height = fields.Char(string='barcode height', default='20')
    bcode_width = fields.Char(string='barcode width', default='142')

    net = fields.Char(string='Net')
    net_x1 = fields.Char(string='Net X1')
    net_x2 = fields.Char(string='Net X2')
    net_y = fields.Char(string='Net Y')

    incl = fields.Char(string='Incl')
    incl_x1 = fields.Char(string='Incl X1')
    incl_x2 = fields.Char(string='Incl X2')
    incl_y = fields.Char(string='Incl Y')


class BarcodeSettingstwo(models.Model):
    _name = 'item.barcodetwo'

    barcode_x1 = fields.Char(string='barcode_x1', default='25')
    barcode_x2 = fields.Char(string='barcode_x2', default='225')
    barcode_x3 = fields.Char(string='barcode_x3', default='325')
    barcode_y = fields.Char(string='barcode_y', default='33')

    itemname_x1 = fields.Char(string='item name_x1', default='10')
    itemname_x2 = fields.Char(string='item name_x2', default='210')
    itemname_x3 = fields.Char(string='item name_x3', default='310')
    itemname_y = fields.Char(string='item name_y', default='12')

    itemcode_x1 = fields.Char(string='item code_x1', default='25')
    itemcode_x2 = fields.Char(string='item code_x2', default='225')
    itemcode_x3 = fields.Char(string='item code_x3', default='325')

    itemcode_y = fields.Char(string='item code_y', default='70')

    mrp_x1 = fields.Char(string='mrp_x1', default='25')
    mrp_x2 = fields.Char(string='mrp_x2', default='225')
    mrp_x3 = fields.Char(string='mrp_x3', default='325')
    mrp_y = fields.Char(string='mrp_y', default='23')

    sellprice_x1 = fields.Char(string='sell price_x1', default='75')
    sellprice_x2 = fields.Char(string='sell price_x2', default='275')
    sellprice_x3 = fields.Char(string='sell price_x3', default='375')
    sellprice_y = fields.Char(string='sell price_y', default='70')

    customer_x1 = fields.Char(string='customer_x1', default='40')
    customer_x2 = fields.Char(string='customer_x2', default='240')
    customer_x3 = fields.Char(string='customer_x3', default='340')
    customer_y = fields.Char(string='customer_y', default='0')

    barcount = fields.Char(string='barcount', default='2')
    mrpstatus = fields.Char(string='mrp status', default='0')
    datestatus = fields.Char(string='date status', default='0')

    datex1 = fields.Char(string='date x1', default='25')
    datex2 = fields.Char(string='date x2', default='225')
    datex3 = fields.Char(string='date x3', default='325')
    datey = fields.Char(string='date y', default='85')

    dateexpx1 = fields.Char(string='date exp x1', default='25')
    dateexpx2 = fields.Char(string='date exp x2', default='225')
    dateexpx3 = fields.Char(string='date exp x3', default='325')
    dateexpy = fields.Char(string='date exp y', default='95')

    fnt8 = fields.Char(string='fnt8', default='8')
    fnt9 = fields.Char(string='fnt9', default='9')
    fnt10 = fields.Char(string='fnt10', default='10')
    fnt12 = fields.Char(string='fnt12', default='12')

    bcode_height = fields.Char(string='barcode height', default='20')
    bcode_width = fields.Char(string='barcode width', default='142')

    net = fields.Char(string='Net')
    net_x1 = fields.Char(string='Net X1')
    net_x2 = fields.Char(string='Net X2')
    net_y = fields.Char(string='Net Y')

    incl = fields.Char(string='Incl')
    incl_x1 = fields.Char(string='Incl X1')
    incl_x2 = fields.Char(string='Incl X2')
    incl_y = fields.Char(string='Incl Y')



