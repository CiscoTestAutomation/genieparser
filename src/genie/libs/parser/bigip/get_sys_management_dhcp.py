# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/management-dhcp' resources
# =============================================


class SysManagementdhcpSchema(MetaParser):

    schema = {}


class SysManagementdhcp(SysManagementdhcpSchema):
    """ To F5 resource for /mgmt/tm/sys/management-dhcp
    """

    cli_command = "/mgmt/tm/sys/management-dhcp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
