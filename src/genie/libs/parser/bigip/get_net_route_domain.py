# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/route-domain' resources
# =============================================


class NetRoutedomainSchema(MetaParser):

    schema = {}


class NetRoutedomain(NetRoutedomainSchema):
    """ To F5 resource for /mgmt/tm/net/route-domain
    """

    cli_command = "/mgmt/tm/net/route-domain"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
