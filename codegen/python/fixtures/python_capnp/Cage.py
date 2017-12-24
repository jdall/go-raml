"""
Auto-generated class for Cage
"""
import capnp
import os
from .Animal import Animal
from six import string_types

from . import client_support

dir = os.path.dirname(os.path.realpath(__file__))


class Cage(object):
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def create(**kwargs):
        """
        :type colours: str
        :type owner: Animal
        :rtype: Cage
        """

        return Cage(**kwargs)

    def __init__(self, json=None, **kwargs):
        if json is None and not kwargs:
            raise ValueError('No data or kwargs present')

        class_name = 'Cage'
        data = json or kwargs

        # set attributes
        data_types = [string_types]
        self.colours = client_support.set_property('colours', data, data_types, False, [], False, True, class_name)
        data_types = [Animal]
        self.owner = client_support.set_property('owner', data, data_types, False, [], False, True, class_name)

    def __str__(self):
        return self.as_json(indent=4)

    def as_json(self, indent=0):
        return client_support.to_json(self, indent=indent)

    def as_dict(self):
        return client_support.to_dict(self)

    def to_capnp(self):
        """
        Load the class in capnp schema Cage.capnp
        :rtype bytes
        """
        template = capnp.load('%s/Cage.capnp' % dir)
        return template.Cage.new_message(**self.as_dict()).to_bytes()


class CageCollection:
    """
    auto-generated. don't touch.
    """

    @staticmethod
    def new(binary=None):
        """
        Load the binary of Cage.capnp into class Cage
        :type binary: bytes. If none creates an empty capnp object.
        rtype: Cage
        """
        template = capnp.load('%s/Cage.capnp' % dir)
        struct = template.Cage.from_bytes(binary) if binary else template.Cage.new_message()
        return Cage(**struct.to_dict(verbose=True))
