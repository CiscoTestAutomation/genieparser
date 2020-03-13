# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/oracle' resources
# =============================================


class GtmMonitorOracleSchema(MetaParser):

    schema = {}


class GtmMonitorOracle(GtmMonitorOracleSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/oracle
    """

    cli_command = "/mgmt/tm/gtm/monitor/oracle"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
