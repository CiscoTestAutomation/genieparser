# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/software/image' resources
# =============================================


class SysSoftwareImageSchema(MetaParser):

    schema = {}


class SysSoftwareImage(SysSoftwareImageSchema):
    """ To F5 resource for /mgmt/tm/sys/software/image
    """

    cli_command = "/mgmt/tm/sys/software/image"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
