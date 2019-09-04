#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.installments import Installments
from py3wirecard.entities.redirecturls import RedirectUrls


class CheckoutPreferences(WireEntity):

	@Object(type=RedirectUrls, required=True)
	def redirectUrls(self):pass

	@Object(type=Installments, required=True)
	def installments(self):pass
