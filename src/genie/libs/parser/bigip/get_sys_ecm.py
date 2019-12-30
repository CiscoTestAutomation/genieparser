# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ecm' resources
# =============================================


class SysEcmSchema(MetaParser):

    schema = {}


class SysEcm(SysEcmSchema):
    """ To F5 resource for /mgmt/tm/sys/ecm
    """

    cli_command = "/mgmt/tm/sys/ecm"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
