#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Address(WireEntity):

	@String(required=True)
	def street(self): pass

	@String(required=True)
	def streetNumber(self): pass

	@String(required=True)
	def complement(self): pass

	@String(max=45, required=True)
	def district(self): pass

	@String(required=True)
	def city(self): pass

	@String(max=2, required=True)
	def state(self): pass

	@String(max=3, required=True)
	def country(self): pass

	@Int(max=20, required=True)
	def zipCode(self): pass
