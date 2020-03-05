# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/dns/zone' resources
# =============================================


class LtmDnsZoneSchema(MetaParser):

    schema = {}


class LtmDnsZone(LtmDnsZoneSchema):
    """ To F5 resource for /mgmt/tm/ltm/dns/zone
    """

    cli_command = "/mgmt/tm/ltm/dns/zone"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
