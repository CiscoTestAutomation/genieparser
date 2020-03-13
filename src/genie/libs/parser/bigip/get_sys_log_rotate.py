# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/log-rotate' resources
# =============================================


class SysLogrotateSchema(MetaParser):

    schema = {}


class SysLogrotate(SysLogrotateSchema):
    """ To F5 resource for /mgmt/tm/sys/log-rotate
    """

    cli_command = "/mgmt/tm/sys/log-rotate"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
