# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icontrol-soap' resources
# =============================================


class SysIcontrolsoapSchema(MetaParser):

    schema = {}


class SysIcontrolsoap(SysIcontrolsoapSchema):
    """ To F5 resource for /mgmt/tm/sys/icontrol-soap
    """

    cli_command = "/mgmt/tm/sys/icontrol-soap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
