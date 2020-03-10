# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/udp' resources
# =============================================


class GtmMonitorUdpSchema(MetaParser):

    schema = {}


class GtmMonitorUdp(GtmMonitorUdpSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/udp
    """

    cli_command = "/mgmt/tm/gtm/monitor/udp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
