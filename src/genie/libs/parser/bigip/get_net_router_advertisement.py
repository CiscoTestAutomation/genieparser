# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/router-advertisement' resources
# =============================================


class NetRouteradvertisementSchema(MetaParser):

    schema = {}


class NetRouteradvertisement(NetRouteradvertisementSchema):
    """ To F5 resource for /mgmt/tm/net/router-advertisement
    """

    cli_command = "/mgmt/tm/net/router-advertisement"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
