# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/https' resources
# =============================================


class LtmMonitorHttpsSchema(MetaParser):

    schema = {}


class LtmMonitorHttps(LtmMonitorHttpsSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/https
    """

    cli_command = "/mgmt/tm/ltm/monitor/https"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
