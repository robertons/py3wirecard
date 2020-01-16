# -*- coding: utf-8 -*-

import decimal
import datetime


class ValidateValue:

    def __init__(self, required=False, max=None, type=None, format=None, default=None):
        self.required = required
        self.max = max
        self.type = type
        self.format = format
        self.default = ListType(self.type) if self.__class__.__name__ == "ObjectList" else default

    def __call__(self, obj, **kw):
        self.func = obj
        self.field_name = obj.__name__[1:] if obj.__name__.startswith("_") else obj.__name__
        return self

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class String(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if not isinstance(data, str):
                try:
                    data = str(data)
                except ValueError as e:
                    raise Exception("%s requires string" % self.field_name)
            if self.max and len(data) > self.max:
                raise Exception("Value too large. The default limit for %s field is %s" %(self.field_name, self.max))
        super().__setattr__(attr, data)


class Int(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if self.max and len(str(data))> self.max:
                raise Exception("Value too large. The default limit for %s field is %s" %(self.field_name, self.max))
            if not isinstance(data, int):
                try:
                    data = int(data)
                except ValueError as e:
                    raise Exception("%s requires int" % self.field_name)
        super().__setattr__(attr, data)


class DateTime(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if not isinstance(data, datetime.datetime):
                try:
                    data = datetime.datetime.strptime(data, self.format)
                except ValueError as e:
                    if "unconverted data remain" not in str(e):
                        raise Exception("%s requires datetime" % self.field_name)
                    pass
        super().__setattr__(attr, data)


class Decimal(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if not isinstance(data, decimal.Decimal):
                try:
                    data = decimal.Decimal(data)
                except ValueError as e:
                    raise Exception("%s requires Decimal" % self.field_name)
        super().__setattr__(attr, data)

class Float(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if not isinstance(data, float):
                try:
                    data = float(data)
                except ValueError as e:
                    raise Exception("%s requires Float" % self.field_name)
        super().__setattr__(attr, data)

class Boolean(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if not isinstance(data, bool):
                try:
                    data = bool(data)
                except ValueError as e:
                    raise Exception("%s requires Boolean" % self.field_name)
        super().__setattr__(attr, data)

class Dict(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if not isinstance(data, dict):
                raise Exception("%s requires Dict" % self.field_name)
        super().__setattr__(attr, data)

class Object(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            if data.__class__.__name__ != self.type.__name__:
                    raise Exception("%s requires %s object" % (self.field_name, self.type.__name__))
        super().__setattr__(attr, data)


class ListType(list):

    def __init__(self, type):
        try:
            self._type = type
            super(ListType, self).__init__()
        except Exception as e:
            raise e

    def append(self, item):
        try:
            if item.__class__.__name__ != self._type.__name__:
                raise Exception('Item type not is %s' %self._type.__name__)
            super(ListType, self).append(item)
        except Exception as e:
            raise e

    def toJSON(self, encode=False, validate=False):
        try:
            return [item.toJSON(encode, validate) if hasattr(item, "toJSON") else item for item in self]
        except Exception as e:
            raise e

class ObjectList(ValidateValue):

    def __init__(self, **attrs):
        super().__init__(**attrs)

    def __setattr__(self, attr, data):
        if attr == "value" and data is not None:
            raise Exception("method not allowed, please use `%s.append(Object)`" %self.field_name)
        super().__setattr__(attr, data)
