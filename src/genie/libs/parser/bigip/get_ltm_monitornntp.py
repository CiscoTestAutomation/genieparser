# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/nntp' resources
# =============================================


class LtmMonitorNntpSchema(MetaParser):

    schema = {}


class LtmMonitorNntp(LtmMonitorNntpSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/nntp
    """

    cli_command = "/mgmt/tm/ltm/monitor/nntp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
