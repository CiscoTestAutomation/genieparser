# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/software/block-device-hotfix' resources
# =============================================


class SysSoftwareBlockdevicehotfixSchema(MetaParser):

    schema = {}


class SysSoftwareBlockdevicehotfix(SysSoftwareBlockdevicehotfixSchema):
    """ To F5 resource for /mgmt/tm/sys/software/block-device-hotfix
    """

    cli_command = "/mgmt/tm/sys/software/block-device-hotfix"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
