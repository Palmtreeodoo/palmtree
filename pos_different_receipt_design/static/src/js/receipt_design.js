odoo.define('pos_different_receipt_design.receipt_design', function (require) {
"use strict";
    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var PosDB = require("point_of_sale.DB");
    var core = require('web.core');
    var config = require('web.config');
    var QWeb = core.qweb;
    var SuperPosModel = models.PosModel.prototype;

    models.load_models([{
        model: 'pos.receipt.design',
        loaded: function(self, designs) {
            self.db.all_designs = designs;
            self.db.receipt_by_id = {};
            designs.forEach(function(design){
                self.db.receipt_by_id[design.id] = design;
            });
        },
    }]);

    PosDB.include({
        init: function(options){
            var self = this;
            this._super(options);
            this.receipt_design = null;
        },
    });

    screens.ReceiptScreenWidget.include({
        render_receipt: function() {
            var self = this;
            if(!self.pos.config.use_custom_receipt){
                this._super();
            }
            else{
                var receipt_design_id = self.pos.config.pos_receipt_design_id[0]
                var receipt_design = self.pos.db.receipt_by_id[receipt_design_id].receipt_design
                var order = self.pos.get_order();

                var data = {
                    widget: this,
                    pos: order.pos,
                    order: order,
                    receipt: order.export_for_printing(),
                    orderlines: order.get_orderlines(),
                    paymentlines: order.get_paymentlines(),
                };

                var parser = new DOMParser();
                var xmlDoc = parser.parseFromString(receipt_design,"text/xml");

                var s = new XMLSerializer();
                var newXmlStr = s.serializeToString(xmlDoc);

		//Works using the DOMParser
                var qweb = new QWeb2.Engine();
                qweb.add_template('<templates><t t-name="receipt_design">'+newXmlStr+'</t></templates>');


		// Also works without using the DOMParser
                // var qweb = new QWeb2.Engine();
                // qweb.add_template('<templates><t t-name="receipt_design">'+receipt_design+'</t></templates>');

                var receipt = qweb.render('receipt_design',data) ;
                this.$('.pos-receipt-container').html(receipt);
            }
        },
    });

    var _super_order = models.Order.prototype;

    models.Order = models.Order.extend({
        get_tax_details_for_receipt: function(){
            var details = {};
            var taxwithout={};
            var fulldetails = [];
            this.orderlines.each(function(line){
                var ldetails = line.get_tax_details();
                var tax_without = line.get_price_without_tax();
                for(var id in ldetails){
                    if(ldetails.hasOwnProperty(id)){
                        details[id] = (details[id] || 0) + ldetails[id];
                        taxwithout[id] = parseFloat((taxwithout[id] || 0) + tax_without).toFixed(2);
                    }
                }
            });
            for(var id in details){
                if(details.hasOwnProperty(id)){
                    fulldetails.push(
                        {
                            amount: details[id],
                            tax: this.pos.taxes_by_id[id],
                            taxable: taxwithout[id] ,
                            name: this.pos.taxes_by_id[id].name,
                            kfc : this.pos.taxes_by_id[id].name.toLowerCase().includes("kfc"),
                            cess : this.pos.taxes_by_id[id].name.toLowerCase().includes("cess"),
                        });
                }
            }
//            console.log(fulldetails);
            return fulldetails;
        },
    });

    //Tax details for print line wise as we are using group of tax 2 tax appears on print
    var _super_order_line = models.Orderline.prototype;
    models.Orderline = models.Orderline.extend({
        get_orderline_tax: function() {
            var self = this;
            var taxname = []
            var product =  this.get_product();
            var taxes_ids = product.taxes_id;
            var taxes =  this.pos.taxes;
    //        var taxdetail = {};
            var product_taxes = [];

            _(taxes_ids).each(function(el){
                product_taxes.push(_.detect(taxes, function(t){
                    return t.id === el;
                }));
            });
            _(product_taxes).each(function(tax) {
                if (self.order.fiscal_position){
                    tax = self._map_tax_fiscal_position(tax);
                }
                if (!tax){
                    return;
                }
                var taxdetail = {
                            name: tax.name,
                        };
                taxname.push(taxdetail);
            });
            return taxname
        },
    });
});