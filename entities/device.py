#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.geolocation import Geolocation

class Device(WireEntity):

	@String()
	def ip(self): pass

	@String()
	def userAgent(self): pass

	@Object(type=Geolocation, required=True)
	def geolocation(self):pass

	@String()
	def fingerprint(self):pass
