# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/snmp-dca' resources
# =============================================


class LtmMonitorSnmpdcaSchema(MetaParser):

    schema = {}


class LtmMonitorSnmpdca(LtmMonitorSnmpdcaSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/snmp-dca
    """

    cli_command = "/mgmt/tm/ltm/monitor/snmp-dca"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
