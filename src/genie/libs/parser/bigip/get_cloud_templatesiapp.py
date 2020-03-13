# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cloud/templates/iapp' resources
# =============================================


class CloudTemplatesIappSchema(MetaParser):

    schema = {}


class CloudTemplatesIapp(CloudTemplatesIappSchema):
    """ To F5 resource for /mgmt/tm/cloud/templates/iapp
    """

    cli_command = "/mgmt/tm/cloud/templates/iapp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
