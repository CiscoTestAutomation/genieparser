# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/wmi' resources
# =============================================


class GtmMonitorWmiSchema(MetaParser):

    schema = {}


class GtmMonitorWmi(GtmMonitorWmiSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/wmi
    """

    cli_command = "/mgmt/tm/gtm/monitor/wmi"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
