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


class OAuth2(Model):
    """OAuth2.

    :param odatatype: Microsoft.DirectoryServices.OAuth2PermissionGrant
    :type odatatype: str
    :param client_id: The objectId of the Service Principal associated with
     the app
    :type client_id: str
    :param consent_type: Typically set to AllPrincipals
    :type consent_type: str
    :param principal_id: Set to null if AllPrincipals is set
    :type principal_id: object
    :param resource_id: Service Principal Id of the resource you want to grant
    :type resource_id: str
    :param scope: Typically set to user_impersonation
    :type scope: str
    :param start_time: Start time for TTL
    :type start_time: str
    :param expiry_time: Expiry time for TTL
    :type expiry_time: str
    """

    _attribute_map = {
        'odatatype': {'key': 'odata\\.type', 'type': 'str'},
        'client_id': {'key': 'clientId', 'type': 'str'},
        'consent_type': {'key': 'consentType', 'type': 'str'},
        'principal_id': {'key': 'principalId', 'type': 'object'},
        'resource_id': {'key': 'resourceId', 'type': 'str'},
        'scope': {'key': 'scope', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'str'},
        'expiry_time': {'key': 'expiryTime', 'type': 'str'},
    }

    def __init__(self, odatatype=None, client_id=None, consent_type=None, principal_id=None, resource_id=None, scope=None, start_time=None, expiry_time=None):
        super(OAuth2, self).__init__()
        self.odatatype = odatatype
        self.client_id = client_id
        self.consent_type = consent_type
        self.principal_id = principal_id
        self.resource_id = resource_id
        self.scope = scope
        self.start_time = start_time
        self.expiry_time = expiry_time
