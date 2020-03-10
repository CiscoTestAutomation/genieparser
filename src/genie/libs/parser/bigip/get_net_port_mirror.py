# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/port-mirror' resources
# =============================================


class NetPortmirrorSchema(MetaParser):

    schema = {}


class NetPortmirror(NetPortmirrorSchema):
    """ To F5 resource for /mgmt/tm/net/port-mirror
    """

    cli_command = "/mgmt/tm/net/port-mirror"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
