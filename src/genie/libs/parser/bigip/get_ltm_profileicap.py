# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/icap' resources
# =============================================


class LtmProfileIcapSchema(MetaParser):

    schema = {}


class LtmProfileIcap(LtmProfileIcapSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/icap
    """

    cli_command = "/mgmt/tm/ltm/profile/icap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
