# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/httpd' resources
# =============================================


class SysHttpdSchema(MetaParser):

    schema = {}


class SysHttpd(SysHttpdSchema):
    """ To F5 resource for /mgmt/tm/sys/httpd
    """

    cli_command = "/mgmt/tm/sys/httpd"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
