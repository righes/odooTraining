/** @odoo-module */

import { Component } from "@odoo/owl";
import { GalleryImage } from "./gallery_image/gallery_image";

export class GalleryRenderer extends Component {}

GalleryRenderer.components = { GalleryImage };
GalleryRenderer.template = "awesome_gallery.Renderer";
