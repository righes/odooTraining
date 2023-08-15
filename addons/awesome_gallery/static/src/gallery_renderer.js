/** @odoo-module */

import { Component } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { GalleryImage } from "./gallery_image/gallery_image";

export class GalleryRenderer extends Component {
  setup() {
    this.action = useService("action");
  }

  onImageClick(resId) {
    this.action.switchView("form", { resId });
  }
}

GalleryRenderer.components = { GalleryImage };
GalleryRenderer.template = "awesome_gallery.Renderer";
