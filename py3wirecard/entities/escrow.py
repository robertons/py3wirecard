#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Escrow(WireEntity):

	@String()
	def id(self): pass

	@String()
	def status(self): pass

	@String()
	def description(self): pass

	@Int()
	def amount(self): pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def createdAt(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def updatedAt(self):pass

	@Dict()
	def _links(self):pass
