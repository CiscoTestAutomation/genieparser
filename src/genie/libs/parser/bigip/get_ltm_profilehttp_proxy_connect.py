# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/http-proxy-connect' resources
# =============================================


class LtmProfileHttpproxyconnectSchema(MetaParser):

    schema = {}


class LtmProfileHttpproxyconnect(LtmProfileHttpproxyconnectSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/http-proxy-connect
    """

    cli_command = "/mgmt/tm/ltm/profile/http-proxy-connect"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
