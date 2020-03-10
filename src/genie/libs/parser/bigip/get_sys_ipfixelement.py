# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ipfix/element' resources
# =============================================


class SysIpfixElementSchema(MetaParser):

    schema = {}


class SysIpfixElement(SysIpfixElementSchema):
    """ To F5 resource for /mgmt/tm/sys/ipfix/element
    """

    cli_command = "/mgmt/tm/sys/ipfix/element"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
