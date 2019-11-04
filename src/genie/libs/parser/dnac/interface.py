"""
    interface.py
    DNAC parsers for the following show commands:

    * /dna/intent/api/v1/interface
"""

import os
import logging
import pprint
import re
import unittest
from genie import parsergen
from collections import defaultdict

from ats.log.utils import banner

from genie.metaparser import MetaParser
from genie.metaparser.util import merge_dict, keynames_convert
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use
# import parser utils
from genie.libs.parser.utils.common import Common

logger = logging.getLogger(__name__)

# ============================================
# Schema for '/dna/intent/api/v1/interface'
# ============================================
class InterfaceSchema(MetaParser):
    """schema for /dna/intent/api/v1/interface, /dna/intent/api/v1/interface/{interface}"""

    schema = {
               Any(): {
                   Any(): {
                           "adminStatus": str,
                           Optional("className"): str,
                           Optional("description"): str,
                           "deviceId": str,
                           Optional("duplex"): str,
                           Optional("id"): str,
                           "ifIndex": str,
                           "hostname": str,
                           Optional("instanceTenantId"): str,
                           Optional("instanceUuid"): str,
                           "interfaceType": str,
                           Optional("ipv4Address"): str,
                           Optional("ipv4Mask"): str,
                           "isisSupport": str,
                           "lastUpdated": str,
                           Optional("macAddress"): str,
                           Optional("mappedPhysicalInterfaceId"): str,
                           Optional("mappedPhysicalInterfaceName"): str,
                           Optional("mediaType"): str,
                           Optional("nativeVlanId"): str,
                           "ospfSupport": str,
                           "pid": str,
                           "portMode": str,
                           "portName": str,
                           Optional("portType"): str,
                           "serialNo": str,
                           "series": str,
                           Optional("speed"): str,
                           "status": str,
                           Optional("vlanId"): str,
                           Optional("voiceVlan"): str
                   }
               }
             }

# ============================================
# Parser for '/dna/intent/api/v1/interface'
# ============================================
class Interface(InterfaceSchema):
    """parser for /dna/intent/api/v1/interface, /dna/intent/api/v1/interface/{interface}"""

    cli_command = ['/dna/intent/api/v1/interface', '/dna/intent/api/v1/interface/{interface}']

    def cli(self,interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.get(cmd).json()['response']

        else:
            out = output

        # get device by id
        cmd = '/dna/intent/api/v1/network-device/{device_id}'

        result_dict={}
        id_to_hostname = {}
        for intf_dict in out:
            device_id = intf_dict['deviceId']
            if device_id not in id_to_hostname:
                device_id_cmd = cmd.format(device_id=device_id)
                device_id_response = self.device.get(device_id_cmd).json()['response']
                hostname = device_id_response['hostname']
                id_to_hostname[device_id] = hostname
            else:
                hostname = id_to_hostname[device_id]

            result_dict.setdefault(device_id, {})
            # remove None values
            result_dict[device_id][intf_dict['portName']] = {k: v for k, v in intf_dict.items() if v is not None}
            result_dict[device_id][intf_dict['portName']]['hostname'] = hostname

        return result_dict
