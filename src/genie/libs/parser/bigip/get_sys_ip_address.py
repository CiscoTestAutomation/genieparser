# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ip-address' resources
# =============================================


class SysIpaddressSchema(MetaParser):

    schema = {}


class SysIpaddress(SysIpaddressSchema):
    """ To F5 resource for /mgmt/tm/sys/ip-address
    """

    cli_command = "/mgmt/tm/sys/ip-address"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
