/** @odoo-module */

import { Component } from "@odoo/owl";
import { useCommand } from "@web/core/commands/command_hook";
import { registry } from "@web/core/registry";
import { CharField } from "@web/views/fields/char/char_field";

class ImagePreviewField extends Component {
  setup() {
    useCommand("Open image in a new tab", () => {
      window.open(this.props.value, "_blank");
    });
  }
}

ImagePreviewField.template = "awesome_tshirt.ImagePreviewField";
ImagePreviewField.components = { CharField };
ImagePreviewField.supportedTypes = ["char"];

registry.category("fields").add("image_preview", ImagePreviewField);
