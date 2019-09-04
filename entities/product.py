#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Product(WireEntity):

	@String(max=250, required=True)
	def product(self): pass

	@String(max=256, default="DIGITAL_SERVICES")
	def category(self): pass

	@Int(max=5, required=True)
	def quantity(self): pass

	@String(max=250)
	def detail(self): pass

	@Int(max=8, required=True)
	def price(self): pass
