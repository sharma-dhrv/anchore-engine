# coding: utf-8

from __future__ import absolute_import
from anchore_engine.services.policy_engine.api.models.trigger_param_spec import TriggerParamSpec
from .base_model_ import Model
from datetime import date, datetime
from typing import List, Dict
from ..util import deserialize_model


class TriggerSpec(Model):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, name=None, description=None, is_deprecated=None, superceded_by=None, parameters=None):
        """
        TriggerSpec - a model defined in Swagger

        :param name: The name of this TriggerSpec.
        :type name: str
        :param description: The description of this TriggerSpec.
        :type description: str
        :param is_deprecated: The is_deprecated of this TriggerSpec.
        :type is_deprecated: str
        :param superceded_by: The superceded_by of this TriggerSpec.
        :type superceded_by: str
        :param parameters: The parameters of this TriggerSpec.
        :type parameters: List[TriggerParamSpec]
        """
        self.swagger_types = {
            'name': str,
            'description': str,
            'is_deprecated': bool,
            'superceded_by': str,
            'parameters': List[TriggerParamSpec]
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'is_deprecated': 'is_deprecated',
            'superceded_by': 'superceded_by',
            'parameters': 'parameters'
        }

        self._name = name
        self._description = description
        self._is_deprecated = is_deprecated
        self._superceded_by = superceded_by
        self._parameters = parameters

    @classmethod
    def from_dict(cls, dikt):
        """
        Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TriggerSpec of this TriggerSpec.
        :rtype: TriggerSpec
        """
        return deserialize_model(dikt, cls)

    @property
    def name(self):
        """
        Gets the name of this TriggerSpec.
        Name of the trigger as it would appear in a policy document

        :return: The name of this TriggerSpec.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this TriggerSpec.
        Name of the trigger as it would appear in a policy document

        :param name: The name of this TriggerSpec.
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """
        Gets the description of this TriggerSpec.
        Trigger description for what it tests and when it will fire during evaluation

        :return: The description of this TriggerSpec.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TriggerSpec.
        Trigger description for what it tests and when it will fire during evaluation

        :param description: The description of this TriggerSpec.
        :type description: str
        """

        self._description = description

    @property
    def is_deprecated(self):
        """
        Gets the is_deprecated of this TriggerSpec.
        True if this trigger is deprecated

        :return: The is_deprecated of this TriggerSpec.
        :rtype: bool
        """
        return self._is_deprecated

    @is_deprecated.setter
    def is_deprecated(self, is_deprecated):
        """
        Sets the is_deprecated of this TriggerSpec.
        True if this trigger is deprecated

        :param is_deprecated: The is_deprecated of this TriggerSpec.
        :type is_deprecated: bool
        """

        self._is_deprecated = is_deprecated

    @property
    def superceded_by(self):
        """
        Gets the superceded_by of this TriggerSpec.
        The name of another trigger that supercedes this on functionally if this is deprecated

        :return: The superceded_by of this TriggerSpec.
        :rtype: str
        """
        return self._superceded_by

    @superceded_by.setter
    def superceded_by(self, superceded_by):
        """
        Sets the superceded_by of this TriggerSpec.
        The name of another trigger that supercedes this on functionally if this is deprecated

        :param superceded_by: The superceded_by of this TriggerSpec.
        :type superceded_by: str
        """

        self._superceded_by = superceded_by

    @property
    def parameters(self):
        """
        Gets the parameters of this TriggerSpec.
        The list of parameters that are valid for this trigger

        :return: The parameters of this TriggerSpec.
        :rtype: List[TriggerParamSpec]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """
        Sets the parameters of this TriggerSpec.
        The list of parameters that are valid for this trigger

        :param parameters: The parameters of this TriggerSpec.
        :type parameters: List[TriggerParamSpec]
        """

        self._parameters = parameters

