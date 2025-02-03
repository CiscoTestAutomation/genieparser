# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common
from genie.libs.parser.iosxe.rv2.show_lisp_super import *

class ShowLispV4PublicationPrefix(ShowLispPublicationPrefixSuperParser):

    """
    Parser for
    *show lisp instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp eid-table {eid_table} ipv4 publication {eid_prefix}
    *show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication {eid_prefix}
    *show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}
    *show lisp instance-id {instance_id} ipv4 publication detail
    *show lisp {lisp_id} instance-id {instance_id} ipv4 publication detail
    *show lisp eid-table {eid_table} ipv4 publication detail
    *show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication detail
    *show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication detail
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication detail
    """
    cli_command = ['show lisp instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp eid-table {eid_table} ipv4 publication {eid_prefix}',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication {eid_prefix}',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication {eid_prefix}',
                   'show lisp instance-id {instance_id} ipv4 publication detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 publication detail',
                   'show lisp eid-table {eid_table} ipv4 publication detail',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv4 publication detail',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication detail',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv4 publication detail']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, eid_prefix=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and vrf and eid_prefix:
                output = self.device.execute(self.cli_command[3].format(lisp_id=lisp_id, vrf=vrf, eid_prefix=eid_prefix))
            elif vrf and instance_id and eid_prefix:
                if vrf == "default":
                    output = self.device.execute(self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
                else:
                    output = self.device.execute(self.cli_command[5].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif eid_table and eid_prefix:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table, eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[7].format(lisp_id=lisp_id, instance_id=instance_id))
            elif lisp_id and vrf:
                output = self.device.execute(self.cli_command[9].format(lisp_id=lisp_id, vrf=vrf))
            elif vrf and instance_id:
                if vrf == "default":
                    output = self.device.execute(self.cli_command[10].format(vrf=vrf, instance_id=instance_id))
                else:
                    output = self.device.execute(self.cli_command[11].format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[6].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[8].format(eid_table=eid_table))
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, eid_prefix=eid_prefix, vrf=vrf, output=output)
