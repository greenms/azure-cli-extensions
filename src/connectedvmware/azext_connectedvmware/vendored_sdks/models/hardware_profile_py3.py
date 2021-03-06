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


class HardwareProfile(Model):
    """Defines the resource properties.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :param memory_size_mb: Gets or sets memory size in MBs for the vm.
    :type memory_size_mb: int
    :param num_cp_us: Gets or sets the number of vCPUs for the vm.
    :type num_cp_us: int
    :param num_cores_per_socket: Gets or sets the number of cores per socket
     for the vm. Defaults to 1 if unspecified.
    :type num_cores_per_socket: int
    :ivar cpu_hot_add_enabled: Gets or sets a value indicating whether virtual
     processors can be added while this virtual machine is running.
    :vartype cpu_hot_add_enabled: bool
    :ivar cpu_hot_remove_enabled: Gets or sets a value indicating whether
     virtual processors can be removed while this virtual machine is running.
    :vartype cpu_hot_remove_enabled: bool
    :ivar memory_hot_add_enabled: Gets or sets a value indicating whether
     memory can be added while this virtual machine is running.
    :vartype memory_hot_add_enabled: bool
    """

    _validation = {
        'cpu_hot_add_enabled': {'readonly': True},
        'cpu_hot_remove_enabled': {'readonly': True},
        'memory_hot_add_enabled': {'readonly': True},
    }

    _attribute_map = {
        'memory_size_mb': {'key': 'memorySizeMB', 'type': 'int'},
        'num_cp_us': {'key': 'numCPUs', 'type': 'int'},
        'num_cores_per_socket': {'key': 'numCoresPerSocket', 'type': 'int'},
        'cpu_hot_add_enabled': {'key': 'cpuHotAddEnabled', 'type': 'bool'},
        'cpu_hot_remove_enabled': {'key': 'cpuHotRemoveEnabled', 'type': 'bool'},
        'memory_hot_add_enabled': {'key': 'memoryHotAddEnabled', 'type': 'bool'},
    }

    def __init__(self, *, memory_size_mb: int=None, num_cp_us: int=None, num_cores_per_socket: int=None, **kwargs) -> None:
        super(HardwareProfile, self).__init__(**kwargs)
        self.memory_size_mb = memory_size_mb
        self.num_cp_us = num_cp_us
        self.num_cores_per_socket = num_cores_per_socket
        self.cpu_hot_add_enabled = None
        self.cpu_hot_remove_enabled = None
        self.memory_hot_add_enabled = None
