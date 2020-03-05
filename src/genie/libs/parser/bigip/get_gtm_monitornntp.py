# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/nntp' resources
# =============================================


class GtmMonitorNntpSchema(MetaParser):

    schema = {}


class GtmMonitorNntp(GtmMonitorNntpSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/nntp
    """

    cli_command = "/mgmt/tm/gtm/monitor/nntp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
