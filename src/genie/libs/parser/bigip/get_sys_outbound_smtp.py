# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/outbound-smtp' resources
# =============================================


class SysOutboundsmtpSchema(MetaParser):

    schema = {}


class SysOutboundsmtp(SysOutboundsmtpSchema):
    """ To F5 resource for /mgmt/tm/sys/outbound-smtp
    """

    cli_command = "/mgmt/tm/sys/outbound-smtp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
