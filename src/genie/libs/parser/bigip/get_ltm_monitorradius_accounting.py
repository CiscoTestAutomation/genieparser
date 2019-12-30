# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/radius-accounting' resources
# =============================================


class LtmMonitorRadiusaccountingSchema(MetaParser):

    schema = {}


class LtmMonitorRadiusaccounting(LtmMonitorRadiusaccountingSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/radius-accounting
    """

    cli_command = "/mgmt/tm/ltm/monitor/radius-accounting"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
