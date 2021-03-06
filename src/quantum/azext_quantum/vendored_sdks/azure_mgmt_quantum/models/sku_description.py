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


class SkuDescription(Model):
    """Information about a specific sku.

    :param id: Unique sku id.
    :type id: str
    :param name: Display name of this sku.
    :type name: str
    :param version: Display name of this sku.
    :type version: str
    :param description: Description about this sku.
    :type description: str
    :param restricted_access_uri: Uri to subscribe to the restricted access
     sku.
    :type restricted_access_uri: str
    :param targets: The list of targets available for this sku.
    :type targets: list[str]
    :param quota_dimensions: The list of quota dimensions for this sku.
    :type quota_dimensions: list[~azure.quantum.models.QuotaDimension]
    :param pricing_details: The list of pricing details for the sku.
    :type pricing_details: list[~azure.quantum.models.PricingDetail]
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'version': {'key': 'version', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'restricted_access_uri': {'key': 'restrictedAccessUri', 'type': 'str'},
        'targets': {'key': 'targets', 'type': '[str]'},
        'quota_dimensions': {'key': 'quotaDimensions', 'type': '[QuotaDimension]'},
        'pricing_details': {'key': 'pricingDetails', 'type': '[PricingDetail]'},
    }

    def __init__(self, **kwargs):
        super(SkuDescription, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.version = kwargs.get('version', None)
        self.description = kwargs.get('description', None)
        self.restricted_access_uri = kwargs.get('restricted_access_uri', None)
        self.targets = kwargs.get('targets', None)
        self.quota_dimensions = kwargs.get('quota_dimensions', None)
        self.pricing_details = kwargs.get('pricing_details', None)
