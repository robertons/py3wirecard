#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Subtotals(WireEntity):

	@Int(max=9)
	def shipping(self): pass

	@Int(max=9)
	def addition(self): pass

	@Int(max=9)
	def discount(self): pass

	@Int(max=12)
	def items(self): pass
