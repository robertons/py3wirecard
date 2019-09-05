#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.wireentity import *
from py3wirecard.entities.amount import Amount
from py3wirecard.entities.product import Product
from py3wirecard.entities.checkoutpreferences import CheckoutPreferences
from py3wirecard.entities.receiver import Receiver
from py3wirecard.entities.customer import Customer
from py3wirecard.entities.address import Address
from py3wirecard.entities.redirecthref import RedirectHref
from py3wirecard.entities.payment import Payment
from py3wirecard.entities.entrie import Entrie
from py3wirecard.entities.refund import Refund
from py3wirecard.entities.event import Event
from py3wirecard.entities.escrow import Escrow

class Order(WireEntity):

	@String(max = 45, required=True)
	def ownId(self): pass

	@Object(type=Amount)
	def amount(self):pass

	@ObjectList(type=Product, required=True)
	def items(self):pass

	@Object(type=CheckoutPreferences)
	def checkoutPreferences(self):pass

	@Object(type=Address)
	def shippingAddress(self):pass

	@Object(type=Customer, required=True)
	def customer(self):pass

	@ObjectList(type=Receiver)
	def receivers(self):pass

	# Response Fields
	@String(max = 16)
	def platform(self):pass

	@String(max = 16)
	def id(self):pass

	@String()
	def status(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def createdAt(self):pass

	@ObjectList(type=Payment)
	def payments(self):pass

	@ObjectList(type=Refund)
	def refunds(self):pass

	@ObjectList(type=Entrie)
	def entries(self):pass

	@ObjectList(type=Event)
	def events(self):pass

	@ObjectList(type=Escrow)
	def escrows(self):pass

	@DateTime(format="%Y-%m-%dT%H:%M:%S.%f")
	def updatedAt(self):pass

	@Dict()
	def _links(self):pass

	@Object(type=RedirectHref)
	def payCheckout(self):pass

	@Object(type=RedirectHref)
	def payCreditCard(self):pass

	@Object(type=RedirectHref)
	def payBoleto(self):pass

	@Object(type=RedirectHref)
	def payOnlineBankDebitItau(self):pass
