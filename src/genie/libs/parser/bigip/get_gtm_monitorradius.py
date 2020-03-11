# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/radius' resources
# =============================================


class GtmMonitorRadiusSchema(MetaParser):

    schema = {}


class GtmMonitorRadius(GtmMonitorRadiusSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/radius
    """

    cli_command = "/mgmt/tm/gtm/monitor/radius"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
