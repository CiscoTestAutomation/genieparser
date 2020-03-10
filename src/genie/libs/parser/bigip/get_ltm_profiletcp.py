# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/tcp' resources
# =============================================


class LtmProfileTcpSchema(MetaParser):

    schema = {}


class LtmProfileTcp(LtmProfileTcpSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/tcp
    """

    cli_command = "/mgmt/tm/ltm/profile/tcp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
