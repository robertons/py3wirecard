#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.amount import Amount
from py3wirecard.entities.event import Event
from py3wirecard.entities.receiver import Receiver
from py3wirecard.entities.receiverdebited import ReceiverDebited
from py3wirecard.entities.creditcard import CreditCard
from py3wirecard.entities.fundinginstrument import FundingInstrument

class Refund(WireEntity):

	@String(max=16)
	def id(self): pass

	@String()
	def status(self): pass

	@Object(type=Amount)
	def amount(self): pass

	@String()
	def type(self): pass

	@Int()
	def installmentCount(self): pass

	@String()
	def statementDescriptor(self):pass

	@Boolean()
	def delayCapture(self):pass

	@Object(type=FundingInstrument)
	def fundingInstrument(self):pass

	@Object(type=FundingInstrument)
	def refundingInstrument(self):pass

	@ObjectList(type=Event)
	def events(self):pass

	@ObjectList(type=ReceiverDebited)
	def receiversDebited(self):pass

	@DateTime(format="%Y-%m-%d")
	def createdAt(self):pass

	@Dict()
	def _links(self):pass
