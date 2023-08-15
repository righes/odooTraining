/** @odoo-module */

import { Component } from "@odoo/owl";

export class GalleryImage extends Component {}

GalleryImage.template = "awesome_gallery.GalleryImage";
GalleryImage.props = {
  image: { type: Object },
  className: { type: String },
  imageField: { type: String },
};
