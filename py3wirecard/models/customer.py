from py3wirecard.utils import util
from py3wirecard.utils import constants
from py3wirecard.entities.customer import Customer

class Customer(Customer):

    def create(self):
        url = util._base_url() + constants.CUSTOMER_URL
        self.__reponse__(**util._post(url=url, data=self.toJSON(encode=True, validate=True)))
        return self

    def get(self, id:str):
        url = util._base_url() + constants.CUSTOMER_GET_URL.format(CUSTOMER_ID = id)
        self.__reponse__(**util._get(url))
        return self

    def list(self):
        url = util._base_url() + constants.CUSTOMER_URL
        _response = util._get(url)
        object_list = ListType(type=Customer)
        for item in _response:
            object_list.append(Customer(**item))
        return object_list
