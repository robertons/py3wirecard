#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Notification(WireEntity):

	@String(max=16)
	def id(self): pass

	@String()
	def target(self): pass

	@String()
	def media(self): pass

	@String()
	def token(self):pass

	@ObjectList(type=str)
	def events(self):pass
