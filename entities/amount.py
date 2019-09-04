#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.subtotals import Subtotals

class Amount(WireEntity):

	@String(max=3, default="BRL", required=True)
	def currency(self): pass

	@String(max=9)
	def fixed(self): pass

	@String(max=4)
	def percentual(self):pass

	@Int(max=12)
	def paid(self):pass

	@Int(max=12)
	def refunds(self):pass

	@Int(max=12)
	def fees(self):pass

	@Int(max=12)
	def fee(self):pass

	@Int(max=12)
	def total(self):pass

	@Int(max=12)
	def gross(self):pass

	@Int(max=12)
	def liquid(self):pass

	@Int(max=12)
	def otherReceivers(self):pass

	@Object(type=Subtotals)
	def subtotals(self):pass
