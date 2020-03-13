# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/file/ssl-crl' resources
# =============================================


class SysFileSslcrlSchema(MetaParser):

    schema = {}


class SysFileSslcrl(SysFileSslcrlSchema):
    """ To F5 resource for /mgmt/tm/sys/file/ssl-crl
    """

    cli_command = "/mgmt/tm/sys/file/ssl-crl"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
