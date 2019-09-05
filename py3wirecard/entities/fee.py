#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Fee(WireEntity):

	@String()
	def type(self):pass

	@Int(max=12)
	def amount(self): pass
