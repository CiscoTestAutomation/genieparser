# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/epsec/epsec-file-object' resources
# =============================================


class FileApmEpsecfileobjectSchema(MetaParser):

    schema = {}


class FileApmEpsecfileobject(FileApmEpsecfileobjectSchema):
    """ To F5 resource for /mgmt/tm/file/apm/epsec/epsec-file-object
    """

    cli_command = "/mgmt/tm/file/apm/epsec/epsec-file-object"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
