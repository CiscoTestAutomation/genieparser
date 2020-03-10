# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/ftp' resources
# =============================================


class LtmProfileFtpSchema(MetaParser):

    schema = {}


class LtmProfileFtp(LtmProfileFtpSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/ftp
    """

    cli_command = "/mgmt/tm/ltm/profile/ftp"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
