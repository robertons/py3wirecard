from py3wirecard.utils import util
from py3wirecard.utils import constants
from py3wirecard.entities.refund import Refund

class Refund(Refund):

    def create(self, id:str, amount=None):
        url = util._base_url() + (constants.REFUND_PAYMENT_URL.format(PAYMENT_ID=id) if id.startswith("PAY") else constants.REFUND_ORDER_URL.format(ORDER_ID=id))
        self.__reponse__(**util._post(url=url, data={'amount':amount} if amount else {}))
        return self

    def get(self, id:str):
        url = util._base_url() + constants.REFUND_GET_URL.format(REFUND_ID = id)
        self.__reponse__(**util._get(url))
        return self
