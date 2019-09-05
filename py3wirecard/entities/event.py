#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Event(WireEntity):

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def createdAt(self):pass

	@String()
	def type(self): pass

	@String(max=65)
	def description(self): pass
