#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import sys
import os
import re
from datetime import datetime

sys.path.append('/Users/roberto/projects/py3wirecard')

from py3wirecard import *

def main(arg):

    WireCard("0INPI8X1E06VRHDVBF4LSPNPTXRG7JQJ", "VHZLZFBJSNDIC0JJZKLOQC7WGOWMCLDZHNSP54BF", sandbox=True)

    #Criar Cliente
    # cliente = Customer()
    # cliente.ownId = "1234"
    # cliente.fullname = "Fulando da Silva"
    # cliente.email = "fulano@email.com"
    # cliente.birthDate = datetime(1980,1,1)
    # cliente.taxDocument = TaxDocument(type="CPF", number = "09292800752")
    # cliente.shippingAddress = Address(street= "Nome da Rua", streetNumber="01", complement="SN", district="Bairro", city="Cidade", state="UF", zipCode=00000000, country="BRA")
    # cliente.phone = Phone(countryCode=55, areaCode=11, number=999999999)
    # cliente.create()

    # Consultar Cliente
    # cliente = Customer()
    # cliente.get("CUS-WCVTIJ37EWBZ")

    # Criar Compra
    # compra = Order()
    # compra.ownId = "123"
    # compra.amount = Amount()
    # compra.items.append(Product(product="Anuncio Mensal", detail="Anuncio teste", quantity=1, price=23999))
    # compra.customer = Customer()
    # compra.customer.ownId = "1200"
    # compra.customer.fullname = "Roberto Neves da Silva"
    # compra.customer.email = "robertonsilva@gmail.com"
    # compra.customer.birthDate = datetime(1982,2,25)
    # compra.customer.taxDocument = TaxDocument(type="CPF", number = "09292800752")
    # compra.customer.shippingAddress = Address(street= "Des. Euripedes Queiroz do Valle", streetNumber="301", complement="802", district="Jardim Camburi", city="Vitória", state="ES", zipCode=29090090, country="BRA")
    # compra.customer.phone = Phone(countryCode=55, areaCode=27, number=999191566)
    # compra.shippingAddress = Address(street= "Des. Euripedes Queiroz do Valle", streetNumber="301", complement="802", district="Jardim Camburi", city="Vitória", state="ES", zipCode=29090090, country="BRA")
    # compra.create()

    # Consultar Compra
    # compra = Order()
    # compra.get("ORD-01F0UJSQ9QB0")

    # Criar Pagamento
    # pagamento = Payment()
    # pagamento.fundingInstrument = FundingInstrument()
    # pagamento.fundingInstrument.method = "CREDIT_CARD"
    # # Cartão Via Hash
    # # pagamento.fundingInstrument.creditCard = CreditCard(hash="HhL0kbhfid+jwgj5l6Kt9EPdetDxQN8s7uKUHDYxDC/XoULjzik44rSda3EcWuOcL17Eb8JjWc1JI7gsuwg9P0rJv1mJQx+d3Dv1puQYz1iRjEWWhnB1bw0gTvnnC/05KbWN5M8oTiugmhVK02Rt2gpbcTtpS7VWyacfgesBJFavYYMljYg8p2YGHXkXrMuQiOCeemKLk420d0OTMBba27jDVVJ663HZDrObnjFXJH/4B5irkj+HO5genV+V4PYoLcOESG4nrI3oFAsMGsLLcdJo0NNvkEmJpn0e9GzureKKFYisYU+BEd9EMr/odS0VMvOYRV65HbPTspIkjl2+3Q==")
    # # Cartão Via PCI Compilance
    # pagamento.fundingInstrument.creditCard = CreditCard(number="5555666677778884", expirationMonth="06", expirationYear="2022", cvc="123")
    # pagamento.fundingInstrument.creditCard.holder = Holder(fullname = "Roberto Neves da Silva", taxDocument = TaxDocument(type="CPF", number = "09292800752"), phone = Phone(countryCode=55, areaCode=27, number=999191566), birthdate = datetime(1982,2,25))
    # pagamento.create(order_id="ORD-01F0UJSQ9QB0")

    # Consultar Pagamento
    # pagamento = Payment().get("PAY-1W24IB9J0DX4")

    # Criar Reembolso Completo de Pagamento
    # reembolso = Refund().create("PAY-1W24IB9J0DX4")

    # Criar Reembolso Completo de Compra
    # reembolso = Refund().create("ORD-01F0UJSQ9QB0")

    # Criar Reembolso Parcial de Pagamento
    # reembolso = Refund().create("PAY-U67EYCMPR8C4", 1000)

    # Criar Reembolso Parcial de Compra
    # reembolso = Refund().create("ORD-01F0UJSQ9QB0", amount=1000)

    # Consultar Reembolso
    # reembolso = Refund().get("REF-VRK0R4N6GAXA")

    # Criar Preferência de Notificações
    # notificacoes = Notification()
    # notificacoes.events = [
    #         "ORDER.*",
    #         "PAYMENT.AUTHORIZED",
    #         "PAYMENT.CANCELLED"
    #         ]
    # notificacoes.target = "https://api.ilhadoprazer.com.br/webhook/notifications"
    # notificacoes.media = "WEBHOOK"
    # notificacoes.create()

    # Consultar Preferência de Notificações
    # notificacoes = Notification().get("NPR-S5AETS06KUXA")

    # Consultar Lista de Notificacoes
    # notificacoes = Notification().list()

    # Excluir Preferências de Notificacoes
    # Notification().delete("NPR-U18MX1ME2MTB")

    # Consultar Webhooks Enviados com Código Identificador do Evento
    # webhooks = WebHooks().get("ORD-01F0UJSQ9QB0")

    # Consultar Todos Webhooks Enviados
    # webhooks = WebHooks().get()

    # Reenviar Webhook
    # webhook = WebHooks().resend(resource_id="PAY-U67EYCMPR8C4", event="PAYMENT.AUTHORIZED")
    # print(webhook.toJSON())

if __name__ == "__main__":
    main(sys.argv)
