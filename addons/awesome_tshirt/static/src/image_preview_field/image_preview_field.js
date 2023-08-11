/** @odoo-module */

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { CharField } from "@web/views/fields/char/char_field";

class ImagePreviewField extends Component {}

ImagePreviewField.template = "awesome_tshirt.ImagePreviewField";
ImagePreviewField.components = { CharField };
ImagePreviewField.supportedTypes = ["char"];

registry.category("fields").add("image_preview", ImagePreviewField);
