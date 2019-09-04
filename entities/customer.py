#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.taxdocument import TaxDocument
from py3wirecard.entities.phone import Phone
from py3wirecard.entities.address import Address
from py3wirecard.entities.fundinginstrument import FundingInstrument
from py3wirecard.entities.moipaccount import MoipAccount

class Customer(WireEntity):

	@String(max = 65, required=True)
	def ownId(self): pass

	@String(max = 90, required=True)
	def fullname(self): pass

	@String(max = 90, required=True)
	def email(self): pass

	@DateTime(format="%Y-%m-%d")
	def birthDate(self): pass

	@Object(type=TaxDocument)
	def taxDocument(self):pass

	@Object(type=Phone)
	def phone(self):pass

	@Object(type=Address)
	def shippingAddress(self):pass

	@Object(type=FundingInstrument)
	def fundingInstrument(self):pass

	# Reponse Fields

	@String(max = 65)
	def id(self): pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def createdAt(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def updatedAt(self):pass

	@Object(type=MoipAccount)
	def moipAccount(self):pass

	@ObjectList(type=FundingInstrument)
	def fundingInstruments(self):pass

	@Dict()
	def _links(self):pass
