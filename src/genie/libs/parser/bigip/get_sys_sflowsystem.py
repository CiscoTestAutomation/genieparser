# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/sflow/data-source/system' resources
# =============================================


class SysSflowSystemSchema(MetaParser):

    schema = {}


class SysSflowSystem(SysSflowSystemSchema):
    """ To F5 resource for /mgmt/tm/sys/sflow/data-source/system
    """

    cli_command = "/mgmt/tm/sys/sflow/data-source/system"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
