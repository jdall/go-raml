"""
Auto-generated class for PlainObject
"""

from . import client_support


class PlainObject(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type obj: dict
        :rtype: PlainObject
        """

        return PlainObject(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'PlainObject'
        data = json or kwargs

        # set attributes
        data_types = [dict]
        self.obj = client_support.set_property('obj', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)
