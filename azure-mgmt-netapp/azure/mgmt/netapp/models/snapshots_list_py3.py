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


class SnapshotsList(Model):
    """List of Snapshots.

    :param value: A list of Snapshots
    :type value: list[~azure.mgmt.netapp.models.Snapshot]
    """

    _attribute_map = {
        'value': {'key': 'value', 'type': '[Snapshot]'},
    }

    def __init__(self, *, value=None, **kwargs) -> None:
        super(SnapshotsList, self).__init__(**kwargs)
        self.value = value
