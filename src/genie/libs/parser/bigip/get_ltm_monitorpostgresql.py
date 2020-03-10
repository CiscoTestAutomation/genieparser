# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/postgresql' resources
# =============================================


class LtmMonitorPostgresqlSchema(MetaParser):

    schema = {}


class LtmMonitorPostgresql(LtmMonitorPostgresqlSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/postgresql
    """

    cli_command = "/mgmt/tm/ltm/monitor/postgresql"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
