# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/dns/cache/transparent' resources
# =============================================


class LtmDnsTransparentSchema(MetaParser):

    schema = {}


class LtmDnsTransparent(LtmDnsTransparentSchema):
    """ To F5 resource for /mgmt/tm/ltm/dns/cache/transparent
    """

    cli_command = "/mgmt/tm/ltm/dns/cache/transparent"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
