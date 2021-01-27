odoo.define('pos_invoice_number.invoice_number', function (require) {
    var models = require('point_of_sale.models');
    var screens = require('point_of_sale.screens');
    var core = require('web.core');
    var qweb = core.qweb;
    var _t = core._t;


    models.load_models(
        {
            model:  'pos.config.invoice.sequence',
            fields: ['name', 'invoice_prefix','invoice_seq','seq_size', 'company_id', 'id'],
            domain: function(self){
                if (self.config.invoice_sequence_id) {
                    return [['id', '=', self.config.invoice_sequence_id[0]]];
                }
            },
            loaded: function(self, sequences){
                self.default_config_invoice_sequence = _.findWhere(sequences, {id: self.config.invoice_sequence_id[0]});
                self.config_invoice_sequences = sequences;
            }
        },
    );

    var _super_Order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function (attributes, options) {
         _super_Order.initialize.apply(this, arguments);

            //arya
            if (this.pos.config.show_invoice_number) {
                    this.show_invoice_number = true;
            }


//            this.invoice_prefix = this.pos.config.invoice_prefix;
//            this.invoice_seq = this.pos.config.invoice_seq++;
//            this.pos_invoice_number = _t(this.invoice_prefix) + this.invoice_seq;

            //arya
        },
        init_from_JSON: function (json) {
            var res = _super_Order.init_from_JSON.apply(this, arguments);

            //arya

            if (json.show_invoice_number) {
                this.show_invoice_number = json.show_invoice_number;
            }
            if (json.to_invoice) {
                this.to_invoice = json.to_invoice;
            }

            this.invoice_prefix = json.invoice_prefix;
            this.invoice_seq = json.invoice_seq;
            if (this.invoice_seq && this.pos.config.show_invoice_number)
                var invoice_seq_no = this.invoice_seq.toString().padStart(this.pos.default_config_invoice_sequence.seq_size, "0");
            else{
                var invoice_seq_no = " "
            }
            this.pos_invoice_number = _t(this.invoice_prefix) + invoice_seq_no;
            if (this.invoice_seq){
                if(this.pos.config.show_invoice_number){
                    this.pos.default_config_invoice_sequence.invoice_seq = Math.max(this.invoice_seq+1,this.pos.default_config_invoice_sequence.invoice_seq);
                }
            }


            return res;
            //arya
        },
        export_as_JSON: function() {
            var json = _super_Order.export_as_JSON.apply(this);
            if (this.show_invoice_number) {
                json.show_invoice_number = this.show_invoice_number;
            }
            if (this.invoice_prefix) {
                json.invoice_prefix = this.invoice_prefix;
            }
            if (this.invoice_seq) {
                json.invoice_seq = this.invoice_seq;
            }
            json.pos_invoice_number= this.get_pos_invoice_number();
            return json;
        },
        export_for_printing: function(){
            var receipt = _super_Order.export_for_printing.apply(this);
            receipt.pos_invoice_number= this.get_pos_invoice_number();
            return receipt;

        },
        get_pos_invoice_number: function() {
            return this.pos_invoice_number;
        },
    });

    screens.PaymentScreenWidget.include({
        finalize_validation: function() {

            var self = this;
            var order = this.pos.get_order();
             self.pos.config.pos_auto_invoice = 1;

            //arya
            if(this.pos.config.show_invoice_number){
                var invoice_prefix = this.pos.default_config_invoice_sequence.invoice_prefix;
                var invoice_seq = this.pos.default_config_invoice_sequence.invoice_seq++;
                var invoice_seq_no = invoice_seq.toString().padStart(this.pos.default_config_invoice_sequence.seq_size, "0");
                var pos_invoice_number = _t(invoice_prefix) + invoice_seq_no;
                order.invoice_prefix = invoice_prefix;
                order.invoice_seq = invoice_seq;
                order.pos_invoice_number =pos_invoice_number;
            }

            //arya
            this._super();
        },

    });

});
