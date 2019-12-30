# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/provision' resources
# =============================================


class SysProvisionSchema(MetaParser):

    schema = {}


class SysProvision(SysProvisionSchema):
    """ To F5 resource for /mgmt/tm/sys/provision
    """

    cli_command = "/mgmt/tm/sys/provision"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
