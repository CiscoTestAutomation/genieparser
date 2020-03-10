# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/firepass' resources
# =============================================


class GtmMonitorFirepassSchema(MetaParser):

    schema = {}


class GtmMonitorFirepass(GtmMonitorFirepassSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/firepass
    """

    cli_command = "/mgmt/tm/gtm/monitor/firepass"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
