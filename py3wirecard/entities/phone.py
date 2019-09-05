#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Phone(WireEntity):

	@Int(max=2, required=True)
	def countryCode(self): pass

	@Int(max=2, required=True)
	def areaCode(self): pass

	@Int(max=16, required=True)
	def number(self): pass
