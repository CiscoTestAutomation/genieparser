# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/bigip-link' resources
# =============================================


class GtmMonitorBigiplinkSchema(MetaParser):

    schema = {}


class GtmMonitorBigiplink(GtmMonitorBigiplinkSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/bigip-link
    """

    cli_command = "/mgmt/tm/gtm/monitor/bigip-link"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
