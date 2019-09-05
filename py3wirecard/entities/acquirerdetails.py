#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.taxdocument import TaxDocument

class AcquirerDetails(WireEntity):

	@String()
	def authorizationNumber(self): pass

	@Object(type=TaxDocument)
	def taxDocument(self):pass
