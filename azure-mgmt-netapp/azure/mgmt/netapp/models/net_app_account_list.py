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

from msrest.serialization import Model


class NetAppAccountList(Model):
    """List of NetApp account resources.

    :param value: Multiple NetApp accounts
    :type value: list[~azure.mgmt.netapp.models.NetAppAccount]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[NetAppAccount]'},
    }

    def __init__(self, **kwargs):
        super(NetAppAccountList, self).__init__(**kwargs)
        self.value = kwargs.get('value', None)
