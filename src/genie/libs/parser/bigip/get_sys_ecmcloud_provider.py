# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ecm/cloud-provider' resources
# =============================================


class SysEcmCloudproviderSchema(MetaParser):

    schema = {}


class SysEcmCloudprovider(SysEcmCloudproviderSchema):
    """ To F5 resource for /mgmt/tm/sys/ecm/cloud-provider
    """

    cli_command = "/mgmt/tm/sys/ecm/cloud-provider"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
