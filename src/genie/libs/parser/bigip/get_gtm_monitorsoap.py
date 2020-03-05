# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/soap' resources
# =============================================


class GtmMonitorSoapSchema(MetaParser):

    schema = {}


class GtmMonitorSoap(GtmMonitorSoapSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/soap
    """

    cli_command = "/mgmt/tm/gtm/monitor/soap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
