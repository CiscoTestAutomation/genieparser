# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/management-proxy-config' resources
# =============================================


class SysManagementproxyconfigSchema(MetaParser):

    schema = {}


class SysManagementproxyconfig(SysManagementproxyconfigSchema):
    """ To F5 resource for /mgmt/tm/sys/management-proxy-config
    """

    cli_command = "/mgmt/tm/sys/management-proxy-config"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
