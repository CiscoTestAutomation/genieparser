# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/dns/cache/validating-resolver' resources
# =============================================


class LtmDnsValidatingresolverSchema(MetaParser):

    schema = {}


class LtmDnsValidatingresolver(LtmDnsValidatingresolverSchema):
    """ To F5 resource for /mgmt/tm/ltm/dns/cache/validating-resolver
    """

    cli_command = "/mgmt/tm/ltm/dns/cache/validating-resolver"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
