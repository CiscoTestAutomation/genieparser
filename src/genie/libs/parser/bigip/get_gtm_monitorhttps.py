# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/https' resources
# =============================================


class GtmMonitorHttpsSchema(MetaParser):

    schema = {}


class GtmMonitorHttps(GtmMonitorHttpsSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/https
    """

    cli_command = "/mgmt/tm/gtm/monitor/https"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
