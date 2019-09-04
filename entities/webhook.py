#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class WebHook(WireEntity):

	@String()
	def resourceId(self): pass

	@String()
	def event(self): pass

	@String()
	def url(self): pass

	@String()
	def status(self): pass

	@String()
	def id(self): pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def sentAt(self): pass
