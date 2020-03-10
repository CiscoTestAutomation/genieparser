# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/gateway-icmp' resources
# =============================================


class LtmMonitorGatewayicmpSchema(MetaParser):

    schema = {}


class LtmMonitorGatewayicmp(LtmMonitorGatewayicmpSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/gateway-icmp
    """

    cli_command = "/mgmt/tm/ltm/monitor/gateway-icmp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
