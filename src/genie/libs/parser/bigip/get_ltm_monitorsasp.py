# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/sasp' resources
# =============================================


class LtmMonitorSaspSchema(MetaParser):

    schema = {}


class LtmMonitorSasp(LtmMonitorSaspSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/sasp
    """

    cli_command = "/mgmt/tm/ltm/monitor/sasp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
