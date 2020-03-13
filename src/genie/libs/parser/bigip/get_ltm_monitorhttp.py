# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/http' resources
# =============================================


class LtmMonitorHttpSchema(MetaParser):

    schema = {}


class LtmMonitorHttp(LtmMonitorHttpSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/http
    """

    cli_command = "/mgmt/tm/ltm/monitor/http"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
