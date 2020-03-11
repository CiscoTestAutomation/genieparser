# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/wom/profile/isession' resources
# =============================================


class WomProfileIsessionSchema(MetaParser):

    schema = {}


class WomProfileIsession(WomProfileIsessionSchema):
    """ To F5 resource for /mgmt/tm/wom/profile/isession
    """

    cli_command = "/mgmt/tm/wom/profile/isession"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
