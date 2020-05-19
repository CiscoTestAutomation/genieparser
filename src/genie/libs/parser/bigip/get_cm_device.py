# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cm/device' resources
# =============================================


class CmDeviceSchema(MetaParser):

    schema = {}


class CmDevice(CmDeviceSchema):
    """ To F5 resource for /mgmt/tm/cm/device
    """

    cli_command = "/mgmt/tm/cm/device"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
