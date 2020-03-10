# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/default-node-monitor' resources
# =============================================


class LtmDefaultnodemonitorSchema(MetaParser):

    schema = {}


class LtmDefaultnodemonitor(LtmDefaultnodemonitorSchema):
    """ To F5 resource for /mgmt/tm/ltm/default-node-monitor
    """

    cli_command = "/mgmt/tm/ltm/default-node-monitor"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
