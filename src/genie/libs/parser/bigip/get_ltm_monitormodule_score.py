# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/module-score' resources
# =============================================


class LtmMonitorModulescoreSchema(MetaParser):

    schema = {}


class LtmMonitorModulescore(LtmMonitorModulescoreSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/module-score
    """

    cli_command = "/mgmt/tm/ltm/monitor/module-score"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
