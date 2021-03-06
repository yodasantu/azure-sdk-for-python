# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .safety_check_py3 import SafetyCheck


class SeedNodeSafetyCheck(SafetyCheck):
    """Represents a safety check for the seed nodes being performed by service
    fabric before continuing with node level operations.

    All required parameters must be populated in order to send to Azure.

    :param kind: Required. Constant filled by server.
    :type kind: str
    """

    _validation = {
        'kind': {'required': True},
    }

    _attribute_map = {
        'kind': {'key': 'Kind', 'type': 'str'},
    }

    def __init__(self, **kwargs) -> None:
        super(SeedNodeSafetyCheck, self).__init__(**kwargs)
        self.kind = 'EnsureSeedNodeQuorum'
