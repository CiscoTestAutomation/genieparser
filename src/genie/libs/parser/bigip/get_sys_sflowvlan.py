# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/sflow/global-settings/vlan' resources
# =============================================


class SysSflowVlanSchema(MetaParser):

    schema = {}


class SysSflowVlan(SysSflowVlanSchema):
    """ To F5 resource for /mgmt/tm/sys/sflow/global-settings/vlan
    """

    cli_command = "/mgmt/tm/sys/sflow/global-settings/vlan"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
