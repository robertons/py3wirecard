from py3wirecard.utils import util
from py3wirecard.utils import constants
from py3wirecard.entities.order import Order

class Order(Order):

    def create(self):
        url = util._base_url() + constants.ORDER_URL
        self.__reponse__(**util._post(url=url, data=self.toJSON(encode=True, validate=True)))
        return self

    def get(self, id:str):
        url = util._base_url() + constants.ORDER_GET_URL.format(ORDER_ID = id)
        self.__reponse__(**util._get(url))
        return self
