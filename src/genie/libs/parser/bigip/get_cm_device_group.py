# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cm/device-group' resources
# =============================================


class CmDevicegroupSchema(MetaParser):

    schema = {}


class CmDevicegroup(CmDevicegroupSchema):
    """ To F5 resource for /mgmt/tm/cm/device-group
    """

    cli_command = "/mgmt/tm/cm/device-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
