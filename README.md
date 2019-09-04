# Python3 Wirecard API v2 Wrapper

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

```bash
import py3wirecard

WireCard("API TOKEN", "API KEY",sandbox=True)
```
## Cliente

**Cadastro**

```bash
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

```bash
cliente = Customer().get("CUS-PCVTIJ37EWBZ")
```
