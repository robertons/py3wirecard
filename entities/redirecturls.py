#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *

class RedirectUrls(WireEntity):

	@String()
	def urlSuccess(self): pass

	@String()
	def urlFailure(self):pass
