# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/monitor/smtp' resources
# =============================================


class GtmMonitorSmtpSchema(MetaParser):

    schema = {}


class GtmMonitorSmtp(GtmMonitorSmtpSchema):
    """ To F5 resource for /mgmt/tm/gtm/monitor/smtp
    """

    cli_command = "/mgmt/tm/gtm/monitor/smtp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
