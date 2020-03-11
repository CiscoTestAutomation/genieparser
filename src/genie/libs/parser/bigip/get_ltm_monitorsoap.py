# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/soap' resources
# =============================================


class LtmMonitorSoapSchema(MetaParser):

    schema = {}


class LtmMonitorSoap(LtmMonitorSoapSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/soap
    """

    cli_command = "/mgmt/tm/ltm/monitor/soap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
