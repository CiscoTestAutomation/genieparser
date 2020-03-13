# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/request-log' resources
# =============================================


class LtmProfileRequestlogSchema(MetaParser):

    schema = {}


class LtmProfileRequestlog(LtmProfileRequestlogSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/request-log
    """

    cli_command = "/mgmt/tm/ltm/profile/request-log"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
