# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/file/system-ssl-cert' resources
# =============================================


class SysFileSystemsslcertSchema(MetaParser):

    schema = {}


class SysFileSystemsslcert(SysFileSystemsslcertSchema):
    """ To F5 resource for /mgmt/tm/sys/file/system-ssl-cert
    """

    cli_command = "/mgmt/tm/sys/file/system-ssl-cert"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
