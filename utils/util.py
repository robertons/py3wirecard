import base64
import requests
import sys
from py3wirecard.utils import constants

TOKEN = {}

class RequestException(Exception):
    def __init__(self, msg, errors):
        Exception.__init__(self, msg)
        self.request_errors = errors

def WireCard(token, key, sandbox=False):
    global TOKEN
    TOKEN['TYPE'] = "Basic" if key else "Bearer"
    TOKEN['TOKEN'] = base64.b64encode('{}:{}'.format(token, key).encode('utf-8')).decode("utf-8") if key else token
    TOKEN['BASE'] = constants.BASE_URL_SANDBOX if sandbox else constants.BASE_URL_LIVE

def _base_url():
    try:
        return TOKEN['BASE']
    except  KeyError as key:
        raise Exception("wirecard module not initialized please see documentation")
    except Exception as e:
        raise e

def _headers():
    __headers = {
        'Content-Type': 'application/json',
        'Authorization': '{} {}'.format(TOKEN['TYPE'], TOKEN['TOKEN'])
    }
    return __headers

def _validate_response(response):
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    elif response.status_code != 204:
        status_code = response.status_code
        try:
            response_json = response.json()
        except Exception as e:
            response_json = {'errors': [{'description': 'WIRECARD RETURN ERROR: ' + str(e)}]}
        error_message = 'WIRECARD REQUEST ERROR: Status ' + str(status_code) + ' ' + \
                        'Request not sent. May contain errors as missing required parameters or transcription error. ' + \
                        str(response_json)
        raise RequestException(error_message, response_json)

def _get(url, data={}):
    return _validate_response(requests.get(url, params=data, headers=_headers()))

def _post(url, data):
    return _validate_response(requests.post(url, json=data, headers=_headers()))

def _put(url, data):
    return _validate_response(requests.put(url, json=data, headers=_headers()))

def _delete(url):
    return _validate_response(requests.delete(url, headers=_headers()))
