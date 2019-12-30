# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/wmi' resources
# =============================================


class LtmMonitorWmiSchema(MetaParser):

    schema = {}


class LtmMonitorWmi(LtmMonitorWmiSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/wmi
    """

    cli_command = "/mgmt/tm/ltm/monitor/wmi"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
