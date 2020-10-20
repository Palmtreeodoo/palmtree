odoo.define('pos_reprint_ticket.pos', function (require) {
"use strict";

var rpc = require('web.rpc');
var screens = require('point_of_sale.screens');
var gui = require('point_of_sale.gui');
var models = require('point_of_sale.models');
var core = require('web.core');
var QWeb = core.qweb;
var SuperPosModel = models.PosModel.prototype;

    //Loading pos order and pos order line to POS
    models.load_models({
        model: 'pos.order',
        fields: ['id','name','date_order','partner_id','lines','pos_reference','account_move'],
        domain: function(self){
            var domain_list = [];
            domain_list = [['session_id', '=', self.pos_session.name], ['state','not in',['draft','cancel']]]
            return domain_list;
        },
        loaded: function(self,wk_order){
            self.db.pos_all_orders = wk_order;
			self.db.order_by_id = {};
			wk_order.forEach(function(order){
				var order_date = new Date(order['date_order']);
          		var utc = order_date.getTime() - (order_date.getTimezoneOffset() * 60000);
				order['date_order'] = new Date(utc).toLocaleString();
				self.db.order_by_id[order.id] = order;
			});
        },
    });
    models.load_models({
        model: 'pos.order.line',
        fields: ['product_id', 'order_id', 'qty','discount','price_unit','price_subtotal_incl','price_subtotal'],
        domain: function(self){
            var order_lines = []
			var orders = self.db.pos_all_orders;
			for (var i = 0; i < orders.length; i++) {
				order_lines = order_lines.concat(orders[i]['lines']);
			}
			return [
				['id', 'in', order_lines]
			];
        },
        loaded: function(self, wk_order_lines) {
			self.db.pos_all_order_lines = wk_order_lines;
			self.db.line_by_id = {};
			wk_order_lines.forEach(function(line){
				self.db.line_by_id[line.id] = line;
			});
		},
    });

    models.PosModel = models.PosModel.extend({
        _save_to_server: function (orders, options) {
			var self = this;
			return SuperPosModel._save_to_server.call(this,orders,options).then(function(return_dict){
				if(return_dict.orders != null){
					return_dict.orders.forEach(function(order){
						if(order.existing)
						{
							self.db.pos_all_orders.forEach(function(order_from_list){
								if(order_from_list.id == order.original_order_id)
									order_from_list.return_status = order.return_status
							});
						}
						else{
							var order_date = new Date(order['date_order'])
							var utc = order_date.getTime() - (order_date.getTimezoneOffset() * 60000);
							order['date_order'] = new Date(utc).toLocaleString()
							self.db.pos_all_orders.unshift(order);
							self.db.order_by_id[order.id] = order;
						}
					});
					return_dict.orderlines.forEach(function(orderline){
						if(orderline.existing){
							var target_line = self.db.line_by_id[orderline.id];
							target_line.line_qty_returned = orderline.line_qty_returned;
						}
						else{
							self.db.pos_all_order_lines.unshift(orderline);
							self.db.line_by_id[orderline.id] = orderline;
						}
					});
					if(self.db.all_statements)
						return_dict.statements.forEach(function(statement) {
							self.db.all_statements.unshift(statement);
							self.db.statement_by_id[statement.id] = statement;
					});

				}
				return return_dict;

			});
		},
    });

    //Order screen widget -shows list of orders
    var OrdersScreenWidget = screens.ScreenWidget.extend({
		template: 'OrdersScreenWidget',
		init: function(parent, options) {
			this._super(parent, options);
		},
		get_customer: function(customer_id){
			var self = this;
			if(self.gui)
				return self.gui.get_current_screen_param('customer_id');
			else
				return undefined;
		},
		render_list: function(order, input_txt) {
			var self = this;
			var customer_id = this.get_customer();
			var contents = this.$el[0].querySelector('.wk-order-list-contents');
			var order = [];
			contents.innerHTML = "";
			//calling pos.order function get_details to get details od orders to display on order screen widget
			rpc.query({
                model: 'pos.order',
                method: 'get_details',
                args: [input_txt]
            }).then(function (data) {
                console.log(data);
                contents.innerHTML = "";
                order = [];
                order = data;
                var wk_orders = order;
                for (var i = 0;i < wk_orders.length; i++) {
			        var wk_order = wk_orders[i];
				    var order_date = new Date(wk_orders[i]['date_order']);
          	        var utc = order_date.getTime() - (order_date.getTimezoneOffset() * 60000);
				    wk_orders[i]['date_order'] = new Date(utc).toLocaleString();
				    var orderline_html = QWeb.render('WkOrderLine', {
				        widget: this,
					    order: wk_orders[i],
					    customer_id:wk_orders[i].partner_id[0],
				    });
				    var orderline = document.createElement('tbody');
				    orderline.innerHTML = orderline_html;
				    orderline = orderline.childNodes[1];
				    contents.appendChild(orderline);
                }

            });

            this.$('.searchbox .search-clear').click(function(){
	            $('.searchbox input').val("");
	            $('.searchbox input').focus();
	            self.render_list(this.value);
	        });
		},
		show: function() {
		    var self = this;
		    var contents = this.$el[0].querySelector('.wk-order-list-contents');
			this._super();
			var orders = self.pos.db.pos_all_orders;
			for(var i = 0, len = Math.min(orders.length,1000); i < len; i++) {
                if (orders[i]) {
                    var order = orders[i];
                    // self.order_string += i + ':' + order.pos_reference + '\n';
            	    }
        	}
        	this.render_list(orders, undefined);
			this.$('.searchbox input').keyup(function() {
				self.render_list(orders, this.value);
			});
			this.$('.back').on('click',function() {
				console.log('fgf');
				self.gui.show_screen('products');
			});
			//Code for print button in order screen widget
			this.$('.wk-order-list-contents').delegate('.print-button', 'click', function(event){
                var order_id = $(this).data('id');
                var lines = [];
            	var payments = [];
            	var discount = 0;
            	var subtotal = 0;
            	var order_new = null;
            	var receipt ={};
            	var tax =[];
            	var con_line=[];
            	for(var i = 0, len = Math.min(orders.length,1000); i < len; i++) {
                	if (orders[i] && orders[i].id == order_id) {
                    	order_new = orders[i];
                	}
            	}
            	// getting order details from pos_order model by calling get_orderlines() function
            	if(order_id){
                    rpc.query({
                        model: 'pos.order',
                        method: 'get_orderlines',
                        args: [order_id]
                    }).then(function (result) {
                        lines = result[0];
                		payments = result[2];
                		discount = result[1];
                		order = result[4];
                		tax = result[5];
                		subtotal=result[6];
                		var cashier = self.pos.cashier || self.pos.user;
                        var company = self.pos.company;
                		receipt['header'] = self.pos.config.receipt_header || '';
                        receipt['footer'] = self.pos.config.receipt_footer || '';
                        receipt['curr_user'] = cashier ? cashier.name : null
                        receipt['shop'] = self.pos.shop;
                        receipt['company'] = {
                            email: company.email,
                            website: company.website,
                            company_registry: company.company_registry,
                            contact_address: company.partner_id[1],
                            vat: company.vat,
                            name: company.name,
                            phone: company.phone,
                            logo: self.pos.company_logo_base64,
                        };
                        // rendering data to template
                        $('.pos-receipt-container').html(QWeb.render('PosTicket3', {
                            widget:self,
                    		order: order,
                    		change: result[3],
                    		receipt:receipt,
                    		orderlines: lines,
                    		discount_total: discount,
                    		paymentlines: payments,
                    		taxlines:tax,
                    		pos:self.pos,
                    		subtotal:subtotal,
                    		a2 : window.location.origin + '/web/image?model=pos.config&field=image&id='+self.pos.config.id,


                        }));
                        self.gui.show_screen("reprint_ticket");
                    });
                }
            	contents.innerHTML = "";
                $('.searchbox input').val("");
			});
		},
		close: function() {
			this._super();
			this.$('.wk-order-list-contents').undelegate();
		},
	});
	gui.define_screen({name: 'wk_order',widget:OrdersScreenWidget});

    //Reprint ticket screen widget
	var ReprintTicketScreenWidget = screens.ScreenWidget.extend({
        template: 'ReprintTicketScreenWidget',
        show: function() {
            var self = this;
            self._super();
            $('.button.back.wk_reprint_back').on("click", function() {
                self.gui.show_screen('wk_order');
            });
            $('.button.next.wk_reprint_home').on("click", function() {
                self.gui.show_screen('products');
            });
            $('.button.print').click(function() {
                var test = self.chrome.screens.receipt;
                setTimeout(function() {
                    self.chrome.screens.receipt.lock_screen(false);
                }, 1000);
                if (!test['_locked']) {
                    self.chrome.screens.receipt.print_web();
                    self.chrome.screens.receipt.lock_screen(true);
                }
            });
        }
    });
    gui.define_screen({ name: 'reprint_ticket', widget: ReprintTicketScreenWidget });

    //reprint action button widget
    var TicketReprintButton = screens.ActionButtonWidget.extend({
        template: 'TicketReprintButton',
        show: function(){
            this._super();
            var self = this;
            this.product_categories_widget.reset_category();
		    this.numpad.state.reset();
        },
        button_click: function() {
            var self = this;
            this._super();
    	    self.gui.show_screen('wk_order',{});
        },
    });

    screens.define_action_button({
        'name': 'ticket_receiptbutton',
        'widget': TicketReprintButton,
    });
    return {
        OrdersScreenWidget: OrdersScreenWidget,
        ReprintTicketScreenWidget:ReprintTicketScreenWidget,
    };

});