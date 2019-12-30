# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/inband' resources
# =============================================


class LtmMonitorInbandSchema(MetaParser):

    schema = {}


class LtmMonitorInband(LtmMonitorInbandSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/inband
    """

    cli_command = "/mgmt/tm/ltm/monitor/inband"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
