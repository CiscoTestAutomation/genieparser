# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/mqtt' resources
# =============================================


class LtmMonitorMqttSchema(MetaParser):

    schema = {}


class LtmMonitorMqtt(LtmMonitorMqttSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/mqtt
    """

    cli_command = "/mgmt/tm/ltm/monitor/mqtt"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
