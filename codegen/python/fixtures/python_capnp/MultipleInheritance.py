"""
Auto-generated class for MultipleInheritance
"""
import capnp
import os
from .EnumCity import EnumCity
from six import string_types

from . import client_support

dir = os.path.dirname(os.path.realpath(__file__))


class MultipleInheritance(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type cities: list[EnumCity]
        :type color: str
        :type colours: list[str]
        :type kind: str
        :type name: str
        :rtype: MultipleInheritance
        """

        return MultipleInheritance(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'MultipleInheritance'
        data = json or kwargs

        # set attributes
        data_types = [EnumCity]
        self.cities = client_support.set_property('cities', data, data_types, False, [], True, True, class_name)
        data_types = [string_types]
        self.color = client_support.set_property('color', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.colours = client_support.set_property('colours', data, data_types, False, [], True, True, class_name)
        data_types = [string_types]
        self.kind = client_support.set_property('kind', data, data_types, False, [], False, True, class_name)
        data_types = [string_types]
        self.name = client_support.set_property('name', data, data_types, False, [], False, False, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

    def to_capnp(self):
        """
        Load the class in capnp schema MultipleInheritance.capnp
        :rtype bytes
        """
        template = capnp.load('%s/MultipleInheritance.capnp' % dir)
        return template.MultipleInheritance.new_message(**self.as_dict()).to_bytes()


class MultipleInheritanceCollection:
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def new(binary=None):
        """
        Load the binary of MultipleInheritance.capnp into class MultipleInheritance
        :type binary: bytes. If none creates an empty capnp object.
        rtype: MultipleInheritance
        """
        template = capnp.load('%s/MultipleInheritance.capnp' % dir)
        struct = template.MultipleInheritance.from_bytes(binary) if binary else template.MultipleInheritance.new_message()
        return MultipleInheritance(**struct.to_dict(verbose=True))
