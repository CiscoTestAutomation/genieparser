# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/external' resources
# =============================================


class LtmMonitorExternalSchema(MetaParser):

    schema = {}


class LtmMonitorExternal(LtmMonitorExternalSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/external
    """

    cli_command = "/mgmt/tm/ltm/monitor/external"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
