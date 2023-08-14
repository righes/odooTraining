/** @odoo-module */

import { Component, onWillStart } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class CustomerList extends Component {
  setup() {
    this.orm = useService("orm");
    onWillStart(async () => {
      this.partners = await this.orm.searchRead("res.partner", [], ["display_name"]);
    });
  }
}

CustomerList.template = "awesome_tshirt.CustomerList";

CustomerList.props = {
  selectCustomer: {
    type: Function,
  },
};
