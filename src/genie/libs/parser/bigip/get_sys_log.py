# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/log' resources
# =============================================


class SysLogSchema(MetaParser):

    schema = {}


class SysLog(SysLogSchema):
    """ To F5 resource for /mgmt/tm/sys/log
    """

    cli_command = "/mgmt/tm/sys/log"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
