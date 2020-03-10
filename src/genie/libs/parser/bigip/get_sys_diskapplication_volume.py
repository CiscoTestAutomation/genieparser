# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/disk/application-volume' resources
# =============================================


class SysDiskApplicationvolumeSchema(MetaParser):

    schema = {}


class SysDiskApplicationvolume(SysDiskApplicationvolumeSchema):
    """ To F5 resource for /mgmt/tm/sys/disk/application-volume
    """

    cli_command = "/mgmt/tm/sys/disk/application-volume"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
