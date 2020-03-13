# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cloud/services/iapp' resources
# =============================================


class CloudServicesIappSchema(MetaParser):

    schema = {}


class CloudServicesIapp(CloudServicesIappSchema):
    """ To F5 resource for /mgmt/tm/cloud/services/iapp
    """

    cli_command = "/mgmt/tm/cloud/services/iapp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
