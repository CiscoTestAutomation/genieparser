# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/none' resources
# =============================================


class LtmMonitorNoneSchema(MetaParser):

    schema = {}


class LtmMonitorNone(LtmMonitorNoneSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/none
    """

    cli_command = "/mgmt/tm/ltm/monitor/none"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
