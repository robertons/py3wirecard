#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.webhook import WebHook

class WebHooks(WireEntity):

	@ObjectList(type=WebHook)
	def webhooks(self):pass
