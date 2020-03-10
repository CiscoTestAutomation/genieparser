# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/ipfix/irules' resources
# =============================================


class SysIpfixIrulesSchema(MetaParser):

    schema = {}


class SysIpfixIrules(SysIpfixIrulesSchema):
    """ To F5 resource for /mgmt/tm/sys/ipfix/irules
    """

    cli_command = "/mgmt/tm/sys/ipfix/irules"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
