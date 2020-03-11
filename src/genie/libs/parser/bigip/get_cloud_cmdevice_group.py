# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cloud/cm/device-group' resources
# =============================================


class CloudCmDevicegroupSchema(MetaParser):

    schema = {}


class CloudCmDevicegroup(CloudCmDevicegroupSchema):
    """ To F5 resource for /mgmt/tm/cloud/cm/device-group
    """

    cli_command = "/mgmt/tm/cloud/cm/device-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
