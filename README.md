
# Wirecard API v2 Wrapper - Python3

Integração com a API v2 de pagamentos e notificações da  Wirecard utilizando requests.

Consulte a documentação oficial e as [referências API v2 Wirecard](https://dev.wirecard.com.br/reference)


# Instalação
Instalação utilizando Pip
```bash
pip install py3wirecard
```
Git/Clone
```
git clone https://github.com/robertons/py3wirecard
cd py3wirecard
pip install -r requirements.txt
python setup.py install
```

## Configuração

```python
from py3wirecard import *

WireCard("API TOKEN", "API KEY",sandbox=True)
```
## Cliente

**Cadastro**

```python
cliente = Customer()
cliente.ownId = "1201"
cliente.fullname = "Fulando da Silva"
cliente.email = "fulano@email.com"
cliente.birthDate = datetime(1980,1,1)
cliente.taxDocument = TaxDocument(type="CPF", number = "000000000")
cliente.shippingAddress = Address(street= "Nome da Rua", streetNumber="01", complement="SN", district="Bairro", city="Cidade", state="UF", zipCode=00000000, country="BRA")
cliente.phone = Phone(countryCode=55, areaCode=11, number=999999999)
cliente.create()
```
**Consulta**

```python
cliente = Customer().get("CUS-PCVTIJ37EWBZ")
```
**Lista**

```python
clientes = Customer().list()
```
**Atualização**

Para atualizar um cliente basta criar um novo pedido com os dados do cliente existente informando seu id ou ownId.

## Pedido

**Cadastro**

```python
compra = Order()
compra.ownId = "1234"
compra.amount = Amount()
compra.items.append(Product(product="Nome Produto", detail="Descrição Produto", quantity=1, price=23999))
compra.customer = Customer()
compra.customer.ownId = "1201"
compra.customer.fullname = "Fulando da Silva"
compra.customer.email = "fulano@email.com"
compra.customer.birthDate = datetime(1980,1,1)
compra.customer.taxDocument = TaxDocument(type="CPF", number = "000000000")
compra.customer.shippingAddress = Address(street= "Nome da Rua", streetNumber="01", complement="SN", district="Bairro", city="Cidade", state="UF", zipCode=00000000, country="BRA")
compra.customer.phone = Phone(countryCode=55, areaCode=11, number=999999999)
compra.shippingAddress = Address(street= "Nome da Rua", streetNumber="01", complement="SN", district="Bairro", city="Cidade", state="UF", zipCode=00000000, country="BRA")
compra.receivers.append(Receiver(type = 'SECONDARY', feePayor = False, moipAccount = MoipAccount(id='IDCONTA'), amount = Amount(fixed = 10000)))
compra.create()
```

**Consulta**

```python
compra = Order().get("ORD-01KHBJSQ9QB0")
```

## Pagamento

```python
pagamento = Payment()
pagamento.fundingInstrument = FundingInstrument(method = "CREDIT_CARD")
```
Cartão de Crédito **(hash)**
```python
pagamento.fundingInstrument.creditCard = CreditCard(hash = "HASH...", holder = Holder(fullname = "Fulando da Silva", TaxDocument(type="CPF", number = "000000000"), phone =  Phone(countryCode=55, areaCode=11, number=999999999), birthdate =  datetime(1980,1,1)))
```

Cartão de Crédito  **(dados)** *(Necessário certificação PCI)*
```python
pagamento.fundingInstrument.creditCard = CreditCard(number="5555666677778884", expirationMonth="06", expirationYear="2022", cvc="123", holder = Holder(fullname = "Fulando da Silva", TaxDocument(type="CPF", number = "000000000"), phone =  Phone(countryCode=55, areaCode=11, number=999999999), birthdate =  datetime(1980,1,1)))
```
Envio do Pagamento
```python
pagamento.create(order_id="ORD-01F0UADQ9QB0")
```
**Consulta**

```python
pagamento = Payment().get("PAY-1A24BB9K8DX4")
```
## Reembolso
**Completo de Pagamento**
```python
reembolso = Refund().create("PAY-1W24IB9J0DX4")
```
**Parcial de Pagamento**
```python
reembolso = Refund().create("PAY-U67EYCMPR8C4", amount=1000)
```
**Completo de Compra**
```python
reembolso = Refund().create("ORD-01F8CQ9QB0")
```
**Parcial de Compra**
```python
reembolso = Refund().create("ORD-01F8CQ9QB0", amount=1000)
```
**Consulta**
```python
reembolso = Refund().get("REF-VRK1K0N6GOXA")
```
## Notificações

**Cadastro de Preferências de Notificações**
```python
notificacoes.events = [
            "ORDER.*",
            "PAYMENT.AUTHORIZED",
            "PAYMENT.CANCELLED"
            ]
notificacoes.target = "https://myapi.com/notifications"
notificacoes.media = "WEBHOOK"
notificacoes.create()
```
**Consulta**
```python
notificacao = Notification().get("NPR-S1VEAS06KBAXA")
```
**Lista Preferências de Notificações**
```python
notificacoes = Notification().list()
```
**Excluir Preferências de Notificações**
```python
Notification().delete("NPR-U18BA1ME2MTB")
```
## Webhooks
**Consultar Webhooks enviados com Código Identificador do Evento**
```python
webhooks = WebHooks().get("ORD-01F0UJSQ9QB0")
```
**Consultar Todos Webhooks enviados**
```python
webhooks = WebHooks().get()
```
**Reenviar Webhook**
```python
webhook = WebHooks().resend(resource_id="PAY-U67EYHGCR8C4", event="PAYMENT.AUTHORIZED")
```
