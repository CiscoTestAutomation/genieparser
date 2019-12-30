# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/smtp' resources
# =============================================


class LtmMonitorSmtpSchema(MetaParser):

    schema = {}


class LtmMonitorSmtp(LtmMonitorSmtpSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/smtp
    """

    cli_command = "/mgmt/tm/ltm/monitor/smtp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
