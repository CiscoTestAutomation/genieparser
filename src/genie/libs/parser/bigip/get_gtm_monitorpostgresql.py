# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/postgresql' resources
# =============================================


class GtmMonitorPostgresqlSchema(MetaParser):

    schema = {}


class GtmMonitorPostgresql(GtmMonitorPostgresqlSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/postgresql
    """

    cli_command = "/mgmt/tm/gtm/monitor/postgresql"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
