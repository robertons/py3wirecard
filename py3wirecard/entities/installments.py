#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class Installments(WireEntity):

	@ObjectList(type=int, required=True)
	def quantity(self):pass

	@Int(max=9)
	def discount(self):pass

	@Int(max=9)
	def addition(self):pass
