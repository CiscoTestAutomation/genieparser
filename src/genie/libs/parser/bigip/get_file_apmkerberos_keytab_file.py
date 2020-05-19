# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/file/apm/aaa/kerberos-keytab-file' resources
# =============================================


class FileApmKerberoskeytabfileSchema(MetaParser):

    schema = {}


class FileApmKerberoskeytabfile(FileApmKerberoskeytabfileSchema):
    """ To F5 resource for /mgmt/tm/file/apm/aaa/kerberos-keytab-file
    """

    cli_command = "/mgmt/tm/file/apm/aaa/kerberos-keytab-file"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
