#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.amount import Amount
from py3wirecard.entities.moipaccount import MoipAccount


class ReceiverDebited(WireEntity):

	@String()
	def type(self): pass

	@Boolean()
	def feePayor(self):pass

	@String()
	def moipAccount(self):pass

	@Int()
	def amount(self):pass
