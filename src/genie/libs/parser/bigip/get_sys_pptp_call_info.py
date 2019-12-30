# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/pptp-call-info' resources
# =============================================


class SysPptpcallinfoSchema(MetaParser):

    schema = {}


class SysPptpcallinfo(SysPptpcallinfoSchema):
    """ To F5 resource for /mgmt/tm/sys/pptp-call-info
    """

    cli_command = "/mgmt/tm/sys/pptp-call-info"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
