#-*- coding: utf-8 -*-
from py3wirecard.entities.lib.datatype import *

__private_methods__ = ["toJSON", "create", "get", "cancel", "list", "delete", "resend"]

def CustomEncoder(item, datatype, encode=False, validate=False):
	try:
		if hasattr(item, "toJSON"):
			return item.toJSON(encode, validate)
		if isinstance(item, decimal.Decimal):
			return float(item)
		if isinstance(item, datetime.datetime):
			return item.strftime(datatype.format)
		if isinstance(item, bytes):
			return item.decode('utf-8')
		return item
	except Exception as e:
		raise e

class WireEntity(object):

	def __init__(self, **kw):
		try:
			for item in self.__dir__():
				if not item.startswith("__") and item not in __private_methods__:
					self.__dict__["__%s"%item] = self.__getattribute__(item)
					self.__dict__[item] = self.__dict__["__%s"%item].default
					if hasattr(self.__dict__[item], "clear"):
						self.__dict__["__%s"%item].default.clear()
						self.__dict__[item].clear()
			for _item, value in kw.items():
				self.__setattr__(_item, value)
		except Exception as e:
			raise e

	def __reponse__(self, **kw):
		try:
			for _item, value in kw.items():
				try:
					self.__setattr__(_item, value)
				except Exception as e:
					print("Error: {} : {} | {}".format(_item, value, e))
		except Exception as e:
			raise e
		return self

	def __setattr__(self, item, value):
		try:
			if not item.startswith("__"):
				if hasattr(self, "__%s"%item):
					field = self.__getattribute__("__%s"%item)
					if field.type and field.__class__.__name__ is "ObjectList" and isinstance(value, list):
						for item_list in value:
							self.__dict__[item].append(field.type(**item_list) if isinstance(item_list, dict) else field.type(item_list))
					else:
						if field.type and isinstance(value, dict):
							field.value = field.type(**value)
						else:
							field.value = value
						self.__dict__[item] = field.value
				else:
					raise Exception("%s field does not exist"%item)
			else:
				super().__setattr__(item, value)
		except Exception as e:
			raise e

	def toJSON(self, encode=False, validate=False):
		try:
			fields = {k: CustomEncoder(v, self.__getattribute__("__%s"%k), encode, validate) if encode else v for k, v in self.__dict__.items() if not k.startswith("__") and v is not None }
			if validate:
				required = [item.replace("__","") for item, value in self.__dict__.items() if item.startswith("__") and value.required and item.replace("__","") not in fields]
				if len(required)>0:
					raise Exception("the following fields for %s are required and must be completed: %s"% (self.__class__.__name__, ", ".join(required)))
			return fields
		except Exception as e:
			raise e
