#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.creditcard import CreditCard
from py3wirecard.entities.amount import Amount
from py3wirecard.entities.fundinginstrument import FundingInstrument

class Entrie(WireEntity):

	@String()
	def id(self):pass

	@String()
	def event(self):pass

	@String()
	def status(self):pass

	@String()
	def operation(self):pass

	@String()
	def description(self):pass

	@Int()
	def installmentCount(self): pass

	@String()
	def statementDescriptor(self):pass

	@Boolean()
	def delayCapture(self):pass

	@Object(type=FundingInstrument)
	def fundingInstrument(self):pass

	@Object(type=Amount)
	def amount(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def scheduledFor(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def settledAt(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def updatedAt(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def createdAt(self):pass

	@String()
	def title(self):pass

	@Dict()
	def _links(self):pass

	@Dict()
	def occurrence(self):pass
