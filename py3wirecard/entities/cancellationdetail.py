#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class CancellationDetail(WireEntity):

	@String()
	def cancelledBy(self):pass

	@Int()
	def code(self): pass

	@String()
	def description(self): pass
