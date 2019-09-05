#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.creditcard import CreditCard
from py3wirecard.entities.boleto import Boleto
from py3wirecard.entities.bankdebit import BankDebit

class FundingInstrument(WireEntity):

	@String(default="CREDIT_CARD", required=True)
	def method(self): pass

	@Object(type=CreditCard)
	def creditCard(self):pass

	@Object(type=Boleto)
	def boleto(self):pass

	@Object(type=BankDebit)
	def onlineBankDebit(self):pass
