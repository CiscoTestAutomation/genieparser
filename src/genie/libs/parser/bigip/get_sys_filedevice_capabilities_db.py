# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/file/device-capabilities-db' resources
# =============================================


class SysFileDevicecapabilitiesdbSchema(MetaParser):

    schema = {}


class SysFileDevicecapabilitiesdb(SysFileDevicecapabilitiesdbSchema):
    """ To F5 resource for /mgmt/tm/sys/file/device-capabilities-db
    """

    cli_command = "/mgmt/tm/sys/file/device-capabilities-db"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
