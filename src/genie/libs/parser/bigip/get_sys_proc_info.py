# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/proc-info' resources
# =============================================


class SysProcinfoSchema(MetaParser):

    schema = {}


class SysProcinfo(SysProcinfoSchema):
    """ To F5 resource for /mgmt/tm/sys/proc-info
    """

    cli_command = "/mgmt/tm/sys/proc-info"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
