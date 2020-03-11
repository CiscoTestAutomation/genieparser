# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/dns/cache' resources
# =============================================


class LtmDnsCacheSchema(MetaParser):

    schema = {}


class LtmDnsCache(LtmDnsCacheSchema):
    """ To F5 resource for /mgmt/tm/ltm/dns/cache
    """

    cli_command = "/mgmt/tm/ltm/dns/cache"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
