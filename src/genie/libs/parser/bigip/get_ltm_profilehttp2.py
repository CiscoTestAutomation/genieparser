# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/http2' resources
# =============================================


class LtmProfileHttp2Schema(MetaParser):

    schema = {}


class LtmProfileHttp2(LtmProfileHttp2Schema):
    """ To F5 resource for /mgmt/tm/ltm/profile/http2
    """

    cli_command = "/mgmt/tm/ltm/profile/http2"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
