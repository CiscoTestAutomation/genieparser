# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/ldns' resources
# =============================================


class GtmLdnsSchema(MetaParser):

    schema = {}


class GtmLdns(GtmLdnsSchema):
    """ To F5 resource for /mgmt/tm/gtm/ldns
    """

    cli_command = "/mgmt/tm/gtm/ldns"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
