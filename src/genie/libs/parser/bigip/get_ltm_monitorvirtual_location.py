# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/virtual-location' resources
# =============================================


class LtmMonitorVirtuallocationSchema(MetaParser):

    schema = {}


class LtmMonitorVirtuallocation(LtmMonitorVirtuallocationSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/virtual-location
    """

    cli_command = "/mgmt/tm/ltm/monitor/virtual-location"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
