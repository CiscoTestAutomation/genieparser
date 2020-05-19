# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor' resources
# =============================================


class LtmMonitorSchema(MetaParser):

    schema = {}


class LtmMonitor(LtmMonitorSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor
    """

    cli_command = "/mgmt/tm/ltm/monitor"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
