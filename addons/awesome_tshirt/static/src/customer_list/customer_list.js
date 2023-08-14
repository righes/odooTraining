/** @odoo-module */

import { Component } from "@odoo/owl";

export class CustomerList extends Component {}

CustomerList.template = "awesome_tshirt.CustomerList";

CustomerList.props = {
  selectCustomer: {
    type: Function,
  },
};
