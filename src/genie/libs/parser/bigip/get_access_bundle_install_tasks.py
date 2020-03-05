# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/access/bundle-install-tasks' resources
# =============================================


class AccessBundleinstalltasksSchema(MetaParser):

    schema = {}


class AccessBundleinstalltasks(AccessBundleinstalltasksSchema):
    """ To F5 resource for /mgmt/tm/access/bundle-install-tasks
    """

    cli_command = "/mgmt/tm/access/bundle-install-tasks"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
