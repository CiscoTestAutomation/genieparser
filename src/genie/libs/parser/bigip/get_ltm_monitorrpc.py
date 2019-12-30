# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/rpc' resources
# =============================================


class LtmMonitorRpcSchema(MetaParser):

    schema = {}


class LtmMonitorRpc(LtmMonitorRpcSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/rpc
    """

    cli_command = "/mgmt/tm/ltm/monitor/rpc"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
