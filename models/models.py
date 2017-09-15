# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
_logger = logging.getLogger(__name__)

class make_to_order(models.Model):
    _inherit = 'product.template'

    @api.multi
    def _all_make_to_order1(self):
        recs = self.search([])
        for rec in recs:
            rec.route_ids=[(6, 0, [1,5])]
            _logger.info("Product route id: %s" %rec.route_ids)
        return True