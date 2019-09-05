#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.taxdocument import TaxDocument
from py3wirecard.entities.phone import Phone
from py3wirecard.entities.address import Address

class Holder(WireEntity):

	@Boolean()
	def store(self): pass

	@String(max = 90, required=True)
	def fullname(self): pass

	@DateTime(format="%Y-%m-%d", required=True)
	def birthdate(self): pass

	@DateTime(format="%Y-%m-%d")
	def birthDate(self): pass

	@Object(type=TaxDocument, required=True)
	def taxDocument(self):pass

	@Object(type=Phone)
	def phone(self):pass

	@Object(type=Address)
	def billingAddress(self):pass
