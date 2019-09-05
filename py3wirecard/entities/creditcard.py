#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.holder import Holder

class CreditCard(WireEntity):

	@String(max = 16)
	def id(self): pass

	@String(max = 16)
	def brand(self): pass

	@Int(max = 6)
	def first6(self): pass

	@Int(max = 4)
	def last4(self): pass

	@String()
	def hash(self): pass

	@Boolean()
	def store(self): pass

	@String(max = 18)
	def number(self): pass

	@String(max = 2)
	def expirationMonth(self): pass

	@String(max = 4)
	def expirationYear(self): pass

	@String()
	def cvc(self): pass

	@Object(type=Holder, required=True)
	def holder(self):pass
