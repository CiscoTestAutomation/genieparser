# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/sflow/receiver' resources
# =============================================


class SysSflowReceiverSchema(MetaParser):

    schema = {}


class SysSflowReceiver(SysSflowReceiverSchema):
    """ To F5 resource for /mgmt/tm/sys/sflow/receiver
    """

    cli_command = "/mgmt/tm/sys/sflow/receiver"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
