odoo.define('dashboard_amount_format.utils', function (require) {
"use strict";
var utils = require('web.utils');

var core = require('web.core');
var _t = core._t;
var QWeb = core.qweb;
var id = -1;

    function human_number(number, decimals, minDigits, formatterCallback) {


//     new_human_number: function (number, decimals, minDigits, formatterCallback) {
//        this._super.apply(this, arguments);
        number = Math.round(number);
        decimals = decimals | 0;
        minDigits = minDigits || 1;
//        formatterCallback = formatterCallback || utils.insert_thousand_seps;
        formatterCallback =  utils.insert_thousand_seps;

        var d2 = Math.pow(10, decimals);
        var val = _t('kMGTPE');
        var symbol = '';
        var numberMagnitude = number.toExponential().split('e')[1];
        // the case numberMagnitude >= 21 corresponds to a number
        // better expressed in the scientific format.
        if (numberMagnitude >= 21) {
            // we do not use number.toExponential(decimals) because we want to
            // avoid the possible useless O decimals: 1e.+24 preferred to 1.0e+24
            number = Math.round(number * Math.pow(10, decimals - numberMagnitude)) / d2;
            // formatterCallback seems useless here.
            return number + 'e' + numberMagnitude;
        }
        var sign = Math.sign(number);
        number = Math.abs(number);
        for (var i = val.length; i > 0 ; i--) {
            var s = Math.pow(10, i-- * 3);
            if (s <= number / Math.pow(10, minDigits - 1)) {
                number = Math.round(number * d2 / s) / d2;
                symbol = val[i - 1];
                break;
            }
        }
        number = sign * number;
        return formatterCallback('' + number) + symbol;
    }
    utils.human_number = human_number;
//    field_utils.format.float = MyCustomformatFloat;
});





