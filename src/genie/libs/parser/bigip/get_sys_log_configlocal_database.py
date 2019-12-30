# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/log-config/destination/local-database' resources
# =============================================


class SysLogconfigLocaldatabaseSchema(MetaParser):

    schema = {}


class SysLogconfigLocaldatabase(SysLogconfigLocaldatabaseSchema):
    """ To F5 resource for /mgmt/tm/sys/log-config/destination/local-database
    """

    cli_command = "/mgmt/tm/sys/log-config/destination/local-database"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
