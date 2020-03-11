# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/pfman/device' resources
# =============================================


class SysPfmanDeviceSchema(MetaParser):

    schema = {}


class SysPfmanDevice(SysPfmanDeviceSchema):
    """ To F5 resource for /mgmt/tm/sys/pfman/device
    """

    cli_command = "/mgmt/tm/sys/pfman/device"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
