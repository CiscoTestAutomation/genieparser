# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/icall/publisher' resources
# =============================================


class SysIcallPublisherSchema(MetaParser):

    schema = {}


class SysIcallPublisher(SysIcallPublisherSchema):
    """ To F5 resource for /mgmt/tm/sys/icall/publisher
    """

    cli_command = "/mgmt/tm/sys/icall/publisher"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
