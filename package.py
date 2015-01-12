from openerp.osv import osv, fields
from pprint import pprint as pp

class MageIntegrator(osv.osv_memory):

    _inherit = 'mage.integrator'

    def send_one_package(self, cr, uid, job, incrementid, package, track_only):
	res = super(MageIntegrator, self).send_one_package(cr, uid, job, incrementid, package, track_only)
	if res:
	    stock_obj = self.pool.get('stock.picking')
	    stock_obj.send_one_tracking_email(cr, uid, [package.picking.id])

	return res
