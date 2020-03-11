# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/management-ip' resources
# =============================================


class SysManagementipSchema(MetaParser):

    schema = {}


class SysManagementip(SysManagementipSchema):
    """ To F5 resource for /mgmt/tm/sys/management-ip
    """

    cli_command = "/mgmt/tm/sys/management-ip"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
