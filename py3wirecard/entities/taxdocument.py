#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class TaxDocument(WireEntity):

	@String(max = 4, required=True)
	def type(self): pass

	@String(max = 14, required=True)
	def number(self): pass
