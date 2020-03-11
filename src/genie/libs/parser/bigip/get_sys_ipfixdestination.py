# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ipfix/destination' resources
# =============================================


class SysIpfixDestinationSchema(MetaParser):

    schema = {}


class SysIpfixDestination(SysIpfixDestinationSchema):
    """ To F5 resource for /mgmt/tm/sys/ipfix/destination
    """

    cli_command = "/mgmt/tm/sys/ipfix/destination"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
