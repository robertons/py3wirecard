from py3wirecard.utils import util
from py3wirecard.utils import constants
from py3wirecard.entities.notification import Notification
from py3wirecard.entities.lib.datatype import ListType

class Notification(Notification):

    def create(self):
        url = util._base_url() + constants.NOTIFICATION_URL
        self.__reponse__(**util._post(url=url, data=self.toJSON(encode=True, validate=True)))
        return self

    def get(self, id:str):
        url = util._base_url() + constants.NOTIFICATION_GET_URL.format(NOTIFICATION_ID = id)
        self.__reponse__(**util._get(url))
        return self

    def list(self):
        url = util._base_url() + constants.NOTIFICATION_URL
        _response = util._get(url)
        object_list = ListType(type=Notification)
        for item in _response:
            object_list.append(Notification(**item))
        return object_list

    def delete(self, id:str):
        url = util._base_url() + constants.NOTIFICATION_GET_URL.format(NOTIFICATION_ID = id)
        return util._delete(url)
