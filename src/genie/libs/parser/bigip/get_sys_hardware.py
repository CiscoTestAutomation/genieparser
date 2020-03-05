# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/hardware' resources
# =============================================


class SysHardwareSchema(MetaParser):

    schema = {}


class SysHardware(SysHardwareSchema):
    """ To F5 resource for /mgmt/tm/sys/hardware
    """

    cli_command = "/mgmt/tm/sys/hardware"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
