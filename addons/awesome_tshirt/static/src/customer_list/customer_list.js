/** @odoo-module */

import { Component, onWillStart, useState } from "@odoo/owl";
import { KeepLast } from "@web/core/utils/concurrency";
import { useService } from "@web/core/utils/hooks";
import { fuzzyLookup } from "@web/core/utils/search";

export class CustomerList extends Component {
  setup() {
    this.orm = useService("orm");
    this.partners = useState({ data: [] });
    this.keepLast = new KeepLast();
    this.state = useState({
      searchString: "",
      displayActiveCustomers: false,
    });
    onWillStart(async () => {
      this.partners.data = await this.loadCustomers();
    });
  }

  get displayedPartners() {
    return this.filterCustomers(this.state.searchString);
  }

  async onChangeActiveCustomers(ev) {
    this.state.displayActiveCustomers = ev.target.checked;
    this.partners.data = await this.keepLast.add(this.loadCustomers());
  }

  loadCustomers() {
    const domain = this.state.displayActiveCustomers ? [["has_active_order", "=", true]] : [];
    return this.orm.searchRead("res.partner", domain, ["display_name"]);
  }

  filterCustomers(name) {
    if (name) {
      return fuzzyLookup(name, this.partners.data, (partner) => partner.display_name);
    } else {
      return this.partners.data;
    }
  }
}

CustomerList.template = "awesome_tshirt.CustomerList";

CustomerList.props = {
  selectCustomer: {
    type: Function,
  },
};
