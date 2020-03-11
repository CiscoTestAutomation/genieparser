# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/mac-address' resources
# =============================================


class SysMacaddressSchema(MetaParser):

    schema = {}


class SysMacaddress(SysMacaddressSchema):
    """ To F5 resource for /mgmt/tm/sys/mac-address
    """

    cli_command = "/mgmt/tm/sys/mac-address"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
