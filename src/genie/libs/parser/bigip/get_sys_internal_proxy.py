# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/internal-proxy' resources
# =============================================


class SysInternalproxySchema(MetaParser):

    schema = {}


class SysInternalproxy(SysInternalproxySchema):
    """ To F5 resource for /mgmt/tm/sys/internal-proxy
    """

    cli_command = "/mgmt/tm/sys/internal-proxy"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
