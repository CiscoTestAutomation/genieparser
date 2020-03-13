# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/pfman/consumer' resources
# =============================================


class SysPfmanConsumerSchema(MetaParser):

    schema = {}


class SysPfmanConsumer(SysPfmanConsumerSchema):
    """ To F5 resource for /mgmt/tm/sys/pfman/consumer
    """

    cli_command = "/mgmt/tm/sys/pfman/consumer"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
