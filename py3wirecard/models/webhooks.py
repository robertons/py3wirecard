from py3wirecard.utils import util
from py3wirecard.utils import constants
from py3wirecard.entities.webhooks import WebHooks
from py3wirecard.entities.lib.datatype import ListType
from py3wirecard.entities.webhook import WebHook

class WebHooks(WebHooks):

    def get(self, id=None):
        url = util._base_url() + (constants.WEBHOOK_GET_URL.format(RESOURCE_ID = id) if id else constants.WEBHOOK_URL)
        self.__reponse__(**util._get(url))
        return self

    def resend(self, resource_id:str, event:str):
        url = util._base_url() + constants.WEBHOOK_URL
        return WebHook(**util._post(url=url, data={"resourceId": resource_id, "event": event }))
