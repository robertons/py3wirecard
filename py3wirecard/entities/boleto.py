#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.boletoinstructionlines import BoletoInstructionLines

class Boleto(WireEntity):

	@String()
	def lineCode(self):pass

	@DateTime(format="%Y-%m-%d", required=True)
	def expirationDate(self): pass

	@String()
	def logoUri(self): pass

	@Object(type=BoletoInstructionLines)
	def instructionLines(self):pass
