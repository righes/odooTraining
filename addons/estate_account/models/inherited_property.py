from odoo import models

class InheritedProperty(models.Model):
	_inherit = "estate.property"

	def finish_sale(self):
		self._create_invoice()
		return super().finish_sale()

	def _create_invoice(self):
		journal = self.env["account.journal"].search([("type", "=", "sale")], limit = 1)
		for record in self:
			self.env["account.move"].create({
				"partner_id": record.buyer_id.id,
				"move_type": "out_invoice",
				"journal_id": journal.id,
				"invoice_line_ids": [
					(
						0,
						0,
						{
							"name": record.name,
							"quantity": 1.0,
							"price_unit": record.selling_price * 6.0 / 100.0,
						},
					), (
						0,
						0,
						{
							"name": "Administrative fees",
							"quantity": 1.0,
							"price_unit": 100.0,
						},
					),
				],
			})
		return True
