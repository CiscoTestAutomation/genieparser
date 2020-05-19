# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/management-route' resources
# =============================================


class SysManagementrouteSchema(MetaParser):

    schema = {}


class SysManagementroute(SysManagementrouteSchema):
    """ To F5 resource for /mgmt/tm/sys/management-route
    """

    cli_command = "/mgmt/tm/sys/management-route"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
