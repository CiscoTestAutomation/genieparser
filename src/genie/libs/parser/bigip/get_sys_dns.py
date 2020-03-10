# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/dns' resources
# =============================================


class SysDnsSchema(MetaParser):

    schema = {}


class SysDns(SysDnsSchema):
    """ To F5 resource for /mgmt/tm/sys/dns
    """

    cli_command = "/mgmt/tm/sys/dns"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
