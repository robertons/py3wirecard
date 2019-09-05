from py3wirecard.utils import util, constants
from py3wirecard.entities.payment import Payment

class Payment(Payment):

    def create(self, order_id:str):
        url = util._base_url() + constants.PAYMENT_ORDER_URL.format(ORDER_ID = order_id)
        self.__reponse__(**util._post(url=url, data=self.toJSON(encode=True, validate=True)))
        return self

    def get(self, id:str):
        url = util._base_url() + constants.PAYMENT_GET_URL.format(PAYMENT_ID = id)
        self.__reponse__(**util._get(url))
        return self

    def cancel(self, id:str):
        url = util._base_url() + constants.PAYMENT_CANCEL_URL.format(PAYMENT_ID = id)
        self.__reponse__(**util._post(url))
        return self
