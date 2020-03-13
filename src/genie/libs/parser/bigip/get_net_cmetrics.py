# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/cmetrics' resources
# =============================================


class NetCmetricsSchema(MetaParser):

    schema = {}


class NetCmetrics(NetCmetricsSchema):
    """ To F5 resource for /mgmt/tm/net/cmetrics
    """

    cli_command = "/mgmt/tm/net/cmetrics"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
