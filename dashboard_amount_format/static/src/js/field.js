odoo.define('dashboard_amount_format.field', function (require) {
"use strict";
var utils = require('web.utils');
var field_utils = require('web.field_utils');

var core = require('web.core');
var _t = core._t;
var QWeb = core.qweb;
var id = -1;

    function formatFloat(value, field, options) {
    options = options || {};
    if (value === false) {
        return "";
    }
//    if (options.humanReadable && options.humanReadable(value)) {
//        return utils.human_number(value, options.decimals, options.minDigits, options.formatterCallback);
//    }
    var l10n = core._t.database.parameters;
    var precision;
    if (options.digits) {
        precision = options.digits[1];
    } else if (field && field.digits) {
        precision = field.digits[1];
    } else {
        precision = 2;
    }
    var formatted = _.str.sprintf('%.' + precision + 'f', value || 0).split('.');
    formatted[0] = utils.insert_thousand_seps(formatted[0]);
    return formatted.join(l10n.decimal_point);
}
    field_utils.format.float = formatFloat;
});





