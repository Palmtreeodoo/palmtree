odoo.define('pos_multi_barcodes.product_barcode', function (require) {
    "use strict";
    var models = require('point_of_sale.models');
    var core = require('web.core');
    var _t = core._t;

    //Load model product barcode and its fields
     models.load_models([
     {
            model: 'product.barcode',
            fields: ['product_tmpl_id', 'quantity', 'list_price', 'uom_id', 'barcode', 'product_id','product_mrp'],
            domain: function (self) {
                return []
            },
            context: {'pos': true},
            loaded: function (self, barcodes) {
                self.barcodes = barcodes;
                self.barcodes_by_barcode = {};
                for (var i = 0; i < barcodes.length; i++) {
                    if (!barcodes[i]['product_id']) {
                        continue
                    }
                    if (!self.barcodes_by_barcode[barcodes[i]['barcode']]) {
                        self.barcodes_by_barcode[barcodes[i]['barcode']] = [barcodes[i]];
                    } else {
                        self.barcodes_by_barcode[barcodes[i]['barcode']].push(barcodes[i]);
                    }
                }
            }
        }

     ]);

    var posodel_super = models.PosModel.prototype;
    models.PosModel = models.PosModel.extend({

        // scan product based on multiple barcode
        scan_product: function (parsed_code) {
            var self = this;
            var product = this.db.get_product_by_barcode(parsed_code.base_code);
            var barcodes = this.barcodes_by_barcode[parsed_code.base_code];
            var selectedOrder = this.get_order();
            if (!selectedOrder) {
                return posodel_super.scan_product.apply(this, arguments);
            }
            if (product && barcodes) {
                var list = [{
                    'label': product['display_name']  + '| MRP: ' + product['product_mrp'] + '| PRICE: ' + product['lst_price'] + ' | QTY: 1 ' + '| and Uoms: ' + product['uom_id'][1],
                    'item': product,
                }];
                for (var i = 0; i < barcodes.length; i++) {
                    var barcode = barcodes[i];
                    list.push({
                        'label': barcode['product_id'][1]  + '| MRP: ' + barcode['product_mrp'] + '| PRICE: ' + barcode['list_price'] + ' | QTY: ' + barcode['quantity'] + '| and Uoms: ' + barcode['uom_id'][1],
                        'item': barcode,
                    });
                }

                this.gui.show_popup('selection', {
                    title: _t('Select product'),
                    list: list,
                    confirm: function (item) {
                        var barcode;
                        var product;
                        if (item['product_id']) {
                            barcode = item;
                            product = self.db.product_by_id[barcode.product_id[0]]
                            selectedOrder.add_product(product, {
                                product_mrp: barcode['product_mrp'],
                                price: barcode['list_price'],
                                quantity: barcode['quantity'],
                                merge: false,
                                extras: {
                                    uom_id: barcode['uom_id']

                                }
                            });
                        } else {
                            product = item;
                            selectedOrder.add_product(product, {});
                        }
                    }
                });
                if (list.length > 0) {
                    return true;
                }
            } else if (!product && barcodes) {
                if (barcodes.length == 1) {
                    var barcode = barcodes[0]
                    var product = this.db.product_by_id[barcode['product_id'][0]];
                    if (product) {
                        selectedOrder.add_product(product, {
                            product_mrp: barcode['product_mrp'],
                            price: barcode['list_price'],
                            quantity: barcode['quantity'],
                            merge: false,
                            extras: {
                                uom_id: barcode['uom_id']

                            }
                        });
                        return true;
                    }
                } else if (barcodes.length > 1) {
                    // if multi items the same barcode, require cashier select
                    var list = [];
                    for (var i = 0; i < barcodes.length; i++) {
                        var barcode = barcodes[i];
                        list.push({
                            'label': barcode['product_id'][1] + '| MRP: ' + barcode['product_mrp'] + '| PRICE: ' + barcode['list_price'] + ' | QTY: ' + barcode['quantity'] + '| and Uoms: ' + barcode['uom_id'][1],
                            'item': barcode,
                        });
                    }
                    this.gui.show_popup('selection', {
                        title: _t('Select product'),
                        list: list,
                        confirm: function (barcode) {
                            var product = self.db.product_by_id[barcode['product_id'][0]];
                            if (product) {
                                selectedOrder.add_product(product, {

                                    price: barcode['list_price'],
                                    product_mrp: barcode['product_mrp'],
                                    quantity: barcode['quantity'],
                                    merge: false,
                                    extras: {
                                        uom_id: barcode['uom_id']

                                    }
                                });
                            }
                        }
                    });
                    if (list.length > 0) {
                        return true;
                    }
                }
            } else if (product && !barcodes) {
                return posodel_super.scan_product.apply(this, arguments);
            }
            else if (!product && !barcodes) {
                return posodel_super.scan_product.apply(this, arguments);
            }
        }
    });
});