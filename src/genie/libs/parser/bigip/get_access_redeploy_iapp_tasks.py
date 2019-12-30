# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/access/redeploy-iapp-tasks' resources
# =============================================


class AccessRedeployiapptasksSchema(MetaParser):

    schema = {}


class AccessRedeployiapptasks(AccessRedeployiapptasksSchema):
    """ To F5 resource for /mgmt/tm/access/redeploy-iapp-tasks
    """

    cli_command = "/mgmt/tm/access/redeploy-iapp-tasks"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
