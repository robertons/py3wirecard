#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class MoipAccount(WireEntity):

	@String(max=256)
	def login(self): pass

	@String(max=256)
	def fullname(self): pass

	@String(max=16)
	def id(self): pass
