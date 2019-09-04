#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Geolocation(WireEntity):

	@Float()
	def latitude(self): pass

	@Float()
	def longitude(self): pass
