odoo.define('palmtree_weightscale.models', function (require) {
    "use strict";

    var models = require('point_of_sale.models');

    var _super_PosModel = models.PosModel.prototype;

    models.PosModel = models.PosModel.extend({

        // identifies the type of the parsed code
        scan_product: function(parsed_code) {
            if (!(parsed_code.type === 'price_to_weight' || parsed_code.type === 'price_to_piece'))  {
                // Normal behaviour
                return _super_PosModel.scan_product.apply(this, [parsed_code]);
            }
//            if (! (parsed_code.type === 'price_to_piece')){
//                // Normal behaviour
//                return _super_PosModel.scan_product.apply(this, [parsed_code]);
//            }
            // Compute quantity, based on price and unit price
            var selectedOrder = this.get_order();
            var str = parsed_code.base_code;
            if (str.length > 11){
                var barcode = str.slice(2, 7);
            }
            else{
                var barcode = str.slice(1, 6);
            }

            var product = this.db.get_product_by_barcode(barcode);
            if(!product){
                return false;
            }
            var quantity = parseFloat(parsed_code.value) || 0;
            // var price = parseFloat(parsed_code.value) || 0;
            // if (price !== 0 && product.price !== 0){
            //     quantity = price / product.price;
            // }
            selectedOrder.add_product(product, {quantity:  quantity, merge: false});
            return true;
        },



    });
});
