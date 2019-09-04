#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.boletoinstructionlines import BoletoInstructionLines

class BankDebit(WireEntity):

	@String()
	def bankNumber(self): pass

	@String()
	def bankName(self): pass

	@DateTime(format="%Y-%m-%d", required=True)
	def expirationDate(self): pass

	@String()
	def returnUri(self):pass
