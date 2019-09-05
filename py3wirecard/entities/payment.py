#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.creditcard import CreditCard
from py3wirecard.entities.fundinginstrument import FundingInstrument
from py3wirecard.entities.fee import Fee
from py3wirecard.entities.cancellationdetail import CancellationDetail
from py3wirecard.entities.device import Device
from py3wirecard.entities.amount import Amount
from py3wirecard.entities.event import Event
from py3wirecard.entities.taxdocument import TaxDocument
from py3wirecard.entities.receiver import Receiver
from py3wirecard.entities.refund import Refund
from py3wirecard.entities.acquirerdetails import AcquirerDetails


class Payment(WireEntity):

	@String(max=16)
	def id(self):pass

	@String()
	def status(self):pass

	@Object(type=Amount)
	def amount(self):pass

	@Int()
	def installmentCount(self): pass

	@Boolean()
	def delayCapture(self):pass

	@String()
	def statementDescriptor(self):pass

	@Object(type=FundingInstrument, required = True)
	def fundingInstrument(self):pass

	@Object(type=AcquirerDetails)
	def acquirerDetails(self):pass

	@ObjectList(type=Fee)
	def fees(self):pass

	@ObjectList(type=Refund)
	def refunds(self):pass

	@ObjectList(type=Event)
	def events(self):pass

	@ObjectList(type=Receiver)
	def receivers(self):pass

	@Object(type=CancellationDetail)
	def cancellationDetails(self):pass

	@DateTime(format="%Y-%m-%d")
	def updatedAt(self):pass

	@DateTime(format="%Y-%m-%d")
	def createdAt(self):pass

	@Object(type=Device)
	def device(self):pass

	@Dict()
	def _links(self):pass
