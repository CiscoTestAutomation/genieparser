# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/pop3' resources
# =============================================


class GtmMonitorPop3Schema(MetaParser):

    schema = {}


class GtmMonitorPop3(GtmMonitorPop3Schema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/pop3
    """

    cli_command = "/mgmt/tm/gtm/monitor/pop3"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
