# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/wap' resources
# =============================================


class GtmMonitorWapSchema(MetaParser):

    schema = {}


class GtmMonitorWap(GtmMonitorWapSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/wap
    """

    cli_command = "/mgmt/tm/gtm/monitor/wap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
