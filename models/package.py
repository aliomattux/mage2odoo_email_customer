from openerp.osv import osv, fields

class OmnishipProcessor(osv.osv_memory):

    _inherit = 'omniship.processor'

    def generate_shipping_label(self, cr, uid, carrier, package):
	res = super(OmnishipProcessor, self).generate_shipping_label(cr, uid, carrier, package)
	stock_obj = self.pool.get('stock.picking')
	stock_obj.send_one_tracking_email(cr, uid, [package.picking.id])

	return res
