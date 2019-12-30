# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/connector' resources
# =============================================


class LtmProfileConnectorSchema(MetaParser):

    schema = {}


class LtmProfileConnector(LtmProfileConnectorSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/connector
    """

    cli_command = "/mgmt/tm/ltm/profile/connector"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
