# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/tcp-echo' resources
# =============================================


class LtmMonitorTcpechoSchema(MetaParser):

    schema = {}


class LtmMonitorTcpecho(LtmMonitorTcpechoSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/tcp-echo
    """

    cli_command = "/mgmt/tm/ltm/monitor/tcp-echo"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
