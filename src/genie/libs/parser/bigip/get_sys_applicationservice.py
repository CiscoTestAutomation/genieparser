# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/application/service' resources
# =============================================


class SysApplicationServiceSchema(MetaParser):

    schema = {}


class SysApplicationService(SysApplicationServiceSchema):
    """ To F5 resource for /mgmt/tm/sys/application/service
    """

    cli_command = "/mgmt/tm/sys/application/service"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
