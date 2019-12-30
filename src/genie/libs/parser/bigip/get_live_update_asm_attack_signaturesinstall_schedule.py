# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/asm-attack-signatures/install-schedule' resources
# =============================================


class Live_updateAsmattacksignaturesInstallscheduleSchema(MetaParser):

    schema = {}


class Live_updateAsmattacksignaturesInstallschedule(
    Live_updateAsmattacksignaturesInstallscheduleSchema
):
    """ To F5 resource for /mgmt/tm/live-update/asm-attack-signatures/install-schedule
    """

    cli_command = "/mgmt/tm/live-update/asm-attack-signatures/install-schedule"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
