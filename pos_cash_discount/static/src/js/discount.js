odoo.define('pos_cash_discount.pos_cash_discount', function (require) {
"use strict";

var core = require('web.core');
var screens = require('point_of_sale.screens');
var models = require('point_of_sale.models');
var field_utils = require('web.field_utils');

var _t = core._t;

var existing_models = models.PosModel.prototype.models;
var product_index = _.findIndex(existing_models, function (model) {
    return model.model === "product.product";
});
var product_model = existing_models[product_index];


models.load_models([{
  model:  product_model.model,
  fields: product_model.fields,
  order:  product_model.order,
  domain: function(self) {return [['id', '=', self.config.cash_discount_product_id[0]]];},
  context: product_model.context,
  loaded: product_model.loaded,
}]);


var CashDiscountButton = screens.ActionButtonWidget.extend({
    template: 'CashDiscountButton',
    button_click: function(){
        var self = this;
        this.gui.show_popup('number',{
            'title': _t('Discount Amount'),
            'value': this.pos.config.discount_amt,
            'confirm': function(val) {
//                val = Math.round(Math.max(0,Math.min(100,field_utils.parse.float(val))));
                val = Math.max(0,Math.min(2000,field_utils.parse.float(val)));
                self.apply_discount(val);
            },
        });
    },
    apply_discount: function(amt) {
        var order    = this.pos.get_order();
        var lines    = order.get_orderlines();
        var product  = this.pos.db.get_product_by_id(this.pos.config.cash_discount_product_id[0]);
        if (product === undefined) {
            this.gui.show_popup('error', {
                title : _t("No discount product found"),
                body  : _t("The discount product seems misconfigured. Make sure it is flagged as 'Can be Sold' and 'Available in Point of Sale'."),
            });
            return;
        }

        // Remove existing discounts
        var i = 0;
        while ( i < lines.length ) {
            if (lines[i].get_product() === product) {
                order.remove_orderline(lines[i]);
            } else {
                i++;
            }
        }

        // Add discount
        // We add the price as manually set to avoid recomputation when changing customer.
        var discount = - amt ;

        if( discount < 0 ){
            order.add_product(product, {
                price: discount,
                lst_price: discount,
                extras: {
                    price_manually_set: true,
                },
            });
        }
    },
});

screens.define_action_button({
    'name': 'cash_discount',
    'widget': CashDiscountButton,
    'condition': function(){
        return this.pos.config.module_pos_cash_discount && this.pos.config.cash_discount_product_id;
    },
});

return {
    CashDiscountButton: CashDiscountButton,
}

});
