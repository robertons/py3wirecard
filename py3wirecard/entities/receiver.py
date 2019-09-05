#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.amount import Amount
from py3wirecard.entities.moipaccount import MoipAccount


class Receiver(WireEntity):

	@String()
	def type(self): pass

	@Boolean()
	def feePayor(self):pass

	@Object(type=MoipAccount)
	def moipAccount(self):pass

	@Object(type=Amount)
	def amount(self):pass
