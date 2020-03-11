# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/tmm-traffic' resources
# =============================================


class SysTmmtrafficSchema(MetaParser):

    schema = {}


class SysTmmtraffic(SysTmmtrafficSchema):
    """ To F5 resource for /mgmt/tm/sys/tmm-traffic
    """

    cli_command = "/mgmt/tm/sys/tmm-traffic"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
