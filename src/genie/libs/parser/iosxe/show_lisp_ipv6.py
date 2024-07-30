"""show_lisp_ipv6.py

    * show lisp all service ipv6
    * show lisp all instance-id <instance_id> ipv6
    * show lisp all instance-id <instance_id> ipv6 map-cache
    * show lisp all instance-id <instance_id> ipv6 server rloc members
    * show lisp all instance-id <instance_id> ipv6 smr
    * show lisp all instance-id <instance_id> ipv6 database
    * show lisp all instance-id <instance_id> ipv6 server summary
    * show lisp all instance-id <instance_id> ipv6 server detail internal
    * show lisp all instance-id <instance_id> ipv6 statistics
    * show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber
    * show lisp instance-id {instance_id} ipv6 subscriber
    * show lisp eid-table {eid_table} ipv6 subscriber
    * show lisp eid-table vrf {vrf} ipv6 subscriber
    * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
    * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
    * show lisp instance-id {instance_id} ipv6 publisher
    * show lisp eid-table {eid_table} ipv6 publisher
    * show lisp eid-table vrf {vrf} ipv6 publisher
"""


# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common

from genie.libs.parser.iosxe.show_lisp_super import *
from genie.libs.parser.iosxe.show_lisp_ipv4 import *


class ShowLispPublicationConfigPropV6Parser(ShowLispPublicationConfigPropSuperParser):

    ''' Parser for
    * show lisp {lisp_id} instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
    * show lisp instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
    * show lisp instance-id {instance_id} ipv6 publication config-propagation detail',
    * show lisp all instance-id * ipv6 publication config-propagation
    '''

    cli_command = ['show lisp instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 publication config-propagation {eid_prefix}',
                   'show lisp instance-id {instance_id} ipv6 publication config-propagation detail',
                   'show lisp all instance-id * ipv6 publication config-propagation']

    def cli(self, instance_id, output=None, lisp_id=None, eid_prefix=None):

        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[3])
        return super().cli(instance_id=instance_id, output=output)


class ShowLispDatabaseConfigPropV6Parser(ShowLispDatabaseConfigPropSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv6 database config-propagation
    * show lisp {lisp_id} instance-id {instance_id} ipv6 database config-propagation'
    * show lisp instance-id {instance_id} ipv6 database config-propagation {eid_prefix}
    """

    cli_command = ['show lisp instance-id {instance_id} ipv6 database config-propagation',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 database config-propagation',
                   'show lisp instance-id {instance_id} ipv6 database config-propagation {eid_prefix}']

    def cli(self, instance_id, output=None, lisp_id=None, eid_prefix=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id, eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
        return super().cli(instance_id=instance_id,output=output)


class ShowLispIpv6ServerSHD(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ipv6 server silent-host-detection
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server silent-host-detection
        * show lisp eid-table {eid_table} ipv6 server silent-host-detection
        * show lisp eid-table vrf {vrf} ipv6 server silent-host-detection
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server silent-host-detection
    """

    cli_command = ['show lisp instance-id {instance_id} ipv6 server silent-host-detection',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server silent-host-detection',
                   'show lisp eid-table {eid_table} ipv6 server silent-host-detection',
                   'show lisp eid-table vrf {vrf} ipv6 server silent-host-detection',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server silent-host-detection']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispIpv6ServerExtranetPolicy(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ipv6 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy
        * show lisp eid-table {eid_table} ipv6 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy
    """

    cli_command = ['show lisp instance-id {instance_id} ipv6 server extranet-policy',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy',
                   'show lisp eid-table {eid_table} ipv6 server extranet-policy',
                   'show lisp eid-table vrf {vrf} ipv6 server extranet-policy',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispInstanceIdIpv6Server(ShowLispSiteSuperParser):

    """ Parser for
        * show lisp instance-id {instance_id} ipv6 server
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server
        * show lisp eid-table vrf {vrf} ipv6 server
        * show lisp eid-table {eid_table} ipv6 server
    """

    cli_command = ['show lisp instance-id {instance_id} ipv6 server',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server',
                   'show lisp eid-table vrf {vrf} ipv6 server',
                   'show lisp eid-table {eid_table} ipv6 server']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, locator_table=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(lisp_id=lisp_id, instance_id=instance_id,output=output)


# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ipv6 publication'
#  * 'show lisp {lisp_id} instance-id {instance_id} ipv6 publication'
#  * 'show lisp eid-table {eid-table} ipv6 publication'
#  * 'show lisp eid-table vrf {vrf} ipv6 publication'
#  * 'show lisp locator-table {vrf} instance-id {instance-id} ipv6 publication'
# ==========================================
class ShowLispIpv6Publication(ShowLispIpv4PublicationSchema):
    """Parser for show lisp ipv4 publication"""
    cli_command = ['show lisp instance-id {instance_id} ipv6 publication',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 publication',
                   'show lisp eid-table {eid_table} ipv6 publication',
                   'show lisp eid-table vrf {vrf} ipv6 publication',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication']

    def cli(self, lisp_id=None, instance_id=None, vrf=None, eid_table=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id)
            elif vrf and instance_id:
                cmd = self.cli_command[4].format(vrf=vrf, instance_id=instance_id)
            elif instance_id:
                cmd = self.cli_command[0].format(instance_id=instance_id)
            elif eid_table:
                cmd = self.cli_command[2].format(eid_table=eid_table)
            else:
                cmd = self.cli_command[3].format(vrf=vrf)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Publication Information for LISP 0 EID-table vrf red (IID 4100)
        p1 = re.compile(r"^Publication\s+Information\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+vrf\s+\S+\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\)$")

        # Entries total 2
        p2 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)")

        # 100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
        # 13.13.13.13     00:00:54    192.168.0.0/16           -       -
        p3 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                        r"(?P<last_published>\S+)\s+(?P<eid_prefix>[a-fA-F\d\:]+\/\d{1,3})\s+"
                        r"(?P<rloc>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+)|-)\s+(?P<encap_iid>\S+)$")

        # New format (Locators are no longer displayed in the output)

        # 2001:192:168:1::2/128   01:11:02   100.14.14.14   -
        p4 = re.compile(r"^(?P<eid_prefix>[a-fA-F\d\:]+\/\d{1,3})\s+(?P<last_published>\S+)\s+"
                        r"(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<encap_iid>\S+)$")

        for line in output.splitlines():

            # Publication Information for LISP 0 EID-table vrf red (IID 4100)
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                    .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                    .setdefault(instance_id,{})
                continue

            # Entries total 2
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                instance_id_dict.update({'total_entries':entries})
                continue

            # 100.14.14.14    01:11:02    2001:192:168:1::2/128    100.11.11.11    -
            # 13.13.13.13     00:00:54    192.168.0.0/16           -       -
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publisher_ip = groups['publisher_ip']
                last_published = groups['last_published']
                rloc = groups['rloc']
                encap_iid = groups['encap_iid']
                eid_prefix = instance_id_dict.setdefault('eid_prefix',{})\
                    .setdefault(publications,{})
                eid_prefix.update({'publisher_ip':publisher_ip})
                eid_prefix.update({'last_published':last_published})
                eid_prefix.update({'rloc':rloc})
                eid_prefix.update({'encap_iid':encap_iid})
                continue

            # New format (Locators are no longer displayed in the output)

            # 2001:192:168:1::2/128   01:11:02   100.14.14.14   -
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                publications = groups['eid_prefix']
                publisher_ip = groups['publisher_ip']
                last_published = groups['last_published']
                encap_iid = groups['encap_iid']
                eid_prefix = instance_id_dict.setdefault('eid_prefix',{})\
                    .setdefault(publications,{})
                eid_prefix.update({'publisher_ip':publisher_ip})
                eid_prefix.update({'last_published':last_published})
                eid_prefix.update({'encap_iid':encap_iid})
                continue
        return ret_dict


class ShowLispIpv6RouteImportMapCache(ShowLispRouteImportMapCacheSuperParser,ShowLispRouteImportMapCacheSchema):
      '''route Import map-cache cli variations'''
      cli_command = [
        'show lisp instance-id {instance_id} ipv6 route-import map-cache',
        'show lisp instance-id {instance_id} ipv6 route-import map-cache {eid}',
        'show lisp instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv6 route-import map-cache',
        'show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid}',
        'show lisp eid-table vrf {vrf} ipv6 route-import map-cache {eid_prefix}',
        'show lisp eid-table {eid_table} ipv6 route-import map-cache',
        'show lisp eid-table {eid_table} ipv6 route-import map-cache {eid}',
        'show lisp eid-table {eid_table} ipv6 route-import map-cache {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 route-import map-cache {eid_prefix}'
      ]

      def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None,
            eid_table=None, eid=None, vrf=None, eid_prefix=None):

          if output is None:
             if lisp_id and instance_id and eid:
                 output = self.device.execute(self.cli_command[4].\
                                             format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
             elif lisp_id and instance_id and eid_prefix :
                 output = self.device.execute(self.cli_command[5].\
                                             format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
             elif lisp_id and instance_id:
                 output = self.device.execute(self.cli_command[3].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
             elif instance_id and eid:
                 output = self.device.execute(self.cli_command[1].\
                                             format(instance_id=instance_id, eid=eid))
             elif instance_id and eid_prefix:
                 output = self.device.execute(self.cli_command[2].\
                                             format(instance_id=instance_id, eid_prefix=eid_prefix))
             elif instance_id:
                 output = self.device.execute(self.cli_command[0].\
                                             format(instance_id=instance_id))
             elif vrf and eid:
                 output = self.device.execute(self.cli_command[7].\
                                             format(vrf=vrf, eid=eid))
             elif vrf and eid_prefix:
                 output = self.device.execute(self.cli_command[8].\
                                             format(vrf=vrf, eid_prefix=eid_prefix))
             elif vrf:
                 output = self.device.execute(self.cli_command[6].\
                                             format(vrf=vrf))
             elif eid_table and eid:
                 output = self.device.execute(self.cli_command[10].\
                                             format(eid_table=eid_table, eid=eid))
             elif eid_table and eid_prefix:
                 output = self.device.execute(self.cli_command[11].\
                                             format(eid_table=eid_table, eid_prefix=eid_prefix))
             elif eid_table:
                 output = self.device.execute(self.cli_command[9].\
                                             format(eid_table=eid_table))
             elif locator_table and instance_id and eid_prefix:
                 output = self.device.execute(self.cli_command[14].\
                                             format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix))
             elif locator_table and instance_id and eid:
                 output = self.device.execute(self.cli_command[13].\
                                             format(locator_table=locator_table, instance_id=instance_id, eid=eid))
             else:
                 output = self.device.execute(self.cli_command[12].\
                                             format(locator_table=locator_table, instance_id=instance_id))
          else:
              output = output
          return super().cli(output=output)

class ShowLispIpv6Away(ShowLispEidAwaySuperParser, ShowLispEidAwaySchema):
    ''' Show Command Ipv6 Away
        show lisp instance-id {instance_id} ipv6 away
        show lisp instance-id {instance_id} ipv6 away {eid}
        show lisp instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp {lisp_id} instance-id {instance_id} ipv6 away
        show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid}
        show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid_prefix}
        show lisp eid-table {eid_table} ipv6 away
        show lisp eid-table {eid_table} ipv6 away {eid}
        show lisp eid-table {eid_table} ipv6 away {eid_prefix}
        show lisp eid-table vrf {eid_table} ipv6 away
        show lisp eid-table vrf {eid_table} ipv6 away {eid}
        show lisp eid-table vrf {eid_table} ipv6 away {eid_prefix}
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ipv6 away',
        'show lisp instance-id {instance_id} ipv6 away {eid}',
        'show lisp instance-id {instance_id} ipv6 away {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 away',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 away {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 away {eid_prefix}',
        'show lisp eid-table {eid_table} ipv6 away',
        'show lisp eid-table {eid_table} ipv6 away {eid}',
        'show lisp eid-table {eid_table} ipv6 away {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv6 away',
        'show lisp eid-table vrf {vrf} ipv6 away {eid}',
        'show lisp eid-table vrf {vrf} ipv6 away {eid_prefix}'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[4].\
                                                format(lisp_id=lisp_id, \
                                                   instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[5].\
                                                format(lisp_id=lisp_id, \
                                                   instance_id=instance_id, \
                                                   eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                                format(lisp_id=lisp_id, \
                                                   instance_id=instance_id))
            elif instance_id and eid:
                output = self.device.execute(self.cli_command[1].\
                                                format(instance_id=instance_id, \
                                                   eid= eid))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].\
                                                format(instance_id=instance_id,\
                                                   eid_prefix=eid_prefix))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[7].\
                                                format(locator_table=locator_table, \
                                                   instance_id=instance_id, \
                                                   eid=eid))
            elif locator_table and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[8].\
                                                format(locator_table=locator_table, \
                                                   instance_id=instance_id, \
                                                   eid_prefix=eid_prefix))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[6].\
                                                format(locator_table=locator_table, \
                                                   instance_id=instance_id))
            elif eid_table and eid:
                output = self.device.execute(self.cli_command[10].\
                                                format(eid_table=eid_table, eid=eid))
            elif eid_table and eid_prefix:
                output = self.device.execute(self.cli_command[11].\
                                                format(eid_table=eid_table, \
                                                   eid_prefix=eid_prefix))
            elif eid_table:
                output = self.device.execute(self.cli_command[9].\
                                                format(eid_table=eid_table))
            elif vrf and eid:
                output = self.device.execute(self.cli_command[13].\
                                                format(vrf=vrf, eid=eid))
            elif vrf and eid_prefix:
                output = self.device.execute(self.cli_command[14].\
                                                format(vrf=vrf, \
                                                   eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[12].\
                                                format(vrf=vrf))

        return super().cli(output=output)


class ShowLispIpv6Publisher(ShowLispPublisherSuperParser, ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher
        * show lisp instance-id {instance_id} ipv6 publisher
        * show lisp eid-table {eid_table} ipv6 publisher
        * show lisp eid-table vrf {vrf} ipv6 publisher
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv6 publisher',
        'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publisher',
        'show lisp instance-id {instance_id} ipv6 publisher',
        'show lisp eid-table {eid_table} ipv6 publisher',
        'show lisp eid-table vrf {vrf} ipv6 publisher',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, eid_table=None):

        # Initialize dictionary
        ret_dict = {}

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif vrf and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(vrf=vrf, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispV6PublicationPrefix(ShowLispPublicationPrefixSuperParser):

    """
    Parser for
    *show lisp instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp {lisp_id} instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp eid-table {eid_table} ipv6 publication {eid_prefix}
    *show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication {eid_prefix}
    *show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}
    *show lisp instance-id {instance_id} ipv6 publication detail
    *show lisp {lisp_id} instance-id {instance_id} ipv6 publication detail
    *show lisp eid-table {eid_table} ipv6 publication detail
    *show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication detail
    *show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication detail
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication detail
    """
    cli_command = ['show lisp instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lis locator-table {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lispp eid-table {eid_table} ipv6 publication {eid_prefix}',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication {eid_prefix}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication {eid_prefix}',
                   'show lisp instance-id {instance_id} ipv6 publication detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 publication detail',
                   'show lisp eid-table {eid_table} ipv6 publication detail',
                   'show lisp {lisp_id} eid-table vrf {vrf} ipv6 publication detail',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv6 publication detail',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ipv6 publication detail']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, eid_prefix=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and vrf and eid_prefix:
                output = self.device.execute(self.cli_command[3].format(lisp_id=lisp_id, vrf=vrf, eid_prefix=eid_prefix))
            elif vrf and instance_id and eid_prefix:
                if "vrf" in self.cli_command:
                    output = self.device.execute(self.cli_command[5].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
                else:
                    output = self.device.execute(self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
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


class ShowLispIpv6Subscriber(ShowLispSubscriberSuperParser, ShowLispSubscriberSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber
        * show lisp instance-id {instance_id} ipv6 subscriber
        * show lisp eid-table {eid_table} ipv6 subscriber
        * show lisp eid-table vrf {vrf} ipv6 subscriber
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv6 subscriber',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscriber',
        'show lisp instance-id {instance_id} ipv6 subscriber',
        'show lisp eid-table {eid_table} ipv6 subscriber',
        'show lisp eid-table vrf {vrf} ipv6 subscriber',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None, eid_table=None,
            vrf=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].format(vrf=vrf))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispIpv6Subscription(ShowLispSubscriptionSuperParser, ShowLispSubscriptionSchema):
    ''' Show Command Ipv6 subscription
        show lisp instance-id {instance_id} ipv6 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv6 subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscription
        show lisp eid-table {eid_table} ipv6 subscription
        show lisp eid-table vrf {eid_table} ipv6 subscription
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ipv6 subscription',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 subscription',
        'show lisp eid-table {eid_table} ipv6 subscription',
        'show lisp eid-table vrf {vrf} ipv6 subscription'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                                format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                                format(locator_table=locator_table, instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].\
                                                format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].\
                                                format(vrf=vrf))

        return super().cli(output=output)


class ShowLispIpv6PublisherRloc(ShowLispIpv4v6PublisherRloc):

    ''' Parser for
     * show lisp {lisp_id} instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv6 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv6 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv6 publisher {publisher_id}
     * show lisp eid-table vrf ipv6 publisher {publisher_id}
    '''

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv6 publisher {publisher_id}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 publisher {publisher_id}',
        'show lisp instance-id {instance_id} ipv6 publisher {publisher_id}',
        'show lisp eid-table {eid_table} ipv6 publisher {publisher_id}',
        'show lisp eid-table vrf {vrf} ipv6 publisher {publisher_id}',
        'show lisp eid-table vrf ipv6 publisher {publisher_id}',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, publisher_id=None, locator_table=None,
            eid_table=None, vrf=None):

        if output is None:
            if lisp_id and instance_id and publisher_id:
                cmd = self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id,\
                                                 publisher_id=publisher_id)

            elif locator_table and instance_id and publisher_id:
                cmd = self.cli_command[1].format(locator_table=locator_table, instance_id=instance_id,\
                                                 publisher_id=publisher_id)
            elif instance_id and publisher_id:
                cmd = self.cli_command[2].format(instance_id=instance_id, publisher_id=publisher_id)

            elif eid_table and publisher_id:
                cmd = self.cli_command[3].format(eid_table=eid_table, publisher_id=publisher_id)

            elif vrf and publisher_id:
                cmd = self.cli_command[4].format(vrf=vrf, publisher_id=publisher_id)

            else:
                cmd = self.cli_command[5].format(publisher_id=publisher_id)

            output = self.device.execute(cmd)
        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispV6SMRParser(ShowLispV4SMRParser):
    """
    Parser for
    * show lisp instance-id {instance_id} ipv6 smr
    * show lisp {lisp_id} instance-id {instance_id} ipv6 smr
    * show lisp eid-table {eid_table} ipv6 smr
    * show lisp eid-table vrf {vrf} ipv6 smr
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 smr
    """
    cli_command = ['show lisp instance-id {instance_id} ipv6 smr',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 smr',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 smr'
                   #'show lisp eid-table {eid_table} ipv6 smr',
                   #'show lisp eid-table vrf {vrf} ipv6 smr'
                   ]

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, locator_table=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
            """elif vrf:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf))
            else:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table))"""
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, vrf=vrf, locator_table=locator_table, output=output)


class ShowLispInstanceIdIpv6ForwardingEID(ShowLispInstanceIdForwardingEidRemoteSchema):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 forwarding eid remote
    '''
    cli_command = 'show lisp instance-id {instance_id} ipv6 forwarding eid remote'

    def cli(self, instance_id, output=None):
        if output is None:
            if instance_id:
                output = self.device.execute(self.cli_command.format(instance_id=instance_id))
        ret_dict = {}

        # ::/0           signal      0x00000000            N/A
        p1 = re.compile(r"^(?P<prefix>[a-fA-F\d\:]+\/\d{1,3})\s+(?P<fwd_action>\S+)"
                        r"\s+(?P<locator_status_bits>\S+)\s+(?P<encap_iid>\S+)$")

        #   packets/bytes       0/0
        p2 = re.compile(r"^packets\/bytes\s+(?P<packets>\d+)\/(?P<bytes>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # 0.0.0.0/0              signal      0x00000000            N/A
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = 0
                instance_id = int(instance_id)
                prefix = groups['prefix']
                fwd_action = groups['fwd_action']
                locator_status_bits = groups['locator_status_bits']
                encap_iid = groups['encap_iid']
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                prefix_dict = instance_id_dict.setdefault('prefix',{}).setdefault(prefix,{})
                prefix_dict.update({'fwd_action':fwd_action,
                                    'locator_status_bits':locator_status_bits,
                                    'encap_iid':encap_iid})

            #   packets/bytes       0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                packets = int(groups['packets'])
                bytes = int(groups['bytes'])
                prefix_dict.update({'packets':packets,
                                    'bytes':bytes})
        return ret_dict


class ShowLispIpv6MapCachePrefix(ShowLispIpMapCachePrefixSuperParser):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv6 map-cache {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache {prefix}',
                   'show lisp eid-table vrf {eid_table} ipv6 map-cache {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache {prefix}']

    def cli(self, prefix, output=None, lisp_id=None, instance_id=None, eid_table=None, locator_table=None):
        if output is None:
            if locator_table and instance_id and prefix:
                output = self.device.execute(self.cli_command[3].format(locator_table=locator_table,instance_id=instance_id,prefix=prefix))
            elif lisp_id and instance_id and prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,instance_id=instance_id,prefix=prefix))
            elif instance_id and prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id,prefix=prefix))
            else:
                output = self.device.execute(self.cli_command[2].format(eid_table=eid_table,prefix=prefix))
        return super().cli(prefix, output=output, lisp_id=lisp_id, instance_id=instance_id, eid_table=eid_table, locator_table=locator_table)


class ShowLispIpv6ServerDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 server detail
        * show lisp instance-id {instance_id} ipv6 server name {site_name}
        * show lisp instance-id {instance_id} ipv6 server {eid}
        * show lisp instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv6 server detail
        * show lisp eid-table {eid_table} ipv6 server name {site_name}
        * show lisp eid-table {eid_table} ipv6 server {eid}
        * show lisp eid-table {eid_table} ipv6 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv6 server detail
        * show lisp eid-table vrf {vrf} ipv6 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv6 server {eid}
        * show lisp eid-table vrf {vrf} ipv6 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server etr-address {etr_address}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv6 server detail',
                   'show lisp instance-id {instance_id} ipv6 server name {site_name}',
                   'show lisp instance-id {instance_id} ipv6 server {eid}',
                   'show lisp instance-id {instance_id} ipv6 server etr-address {etr_address}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server name {site_name}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server etr-address {etr_address}',
                   'show lisp eid-table vrf {vrf} ipv6 server detail',
                   'show lisp eid-table vrf {vrf} ipv6 server name {site_name}',
                   'show lisp eid-table vrf {vrf} ipv6 server {eid}',
                   'show lisp eid-table vrf {vrf} ipv6 server etr-address {etr_address}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server name {site_name}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server etr-address {etr_address}',
                   'show lisp eid-table {eid_table} ipv6 server detail',
                   'show lisp eid-table {eid_table} ipv6 server name {site_name}',
                   'show lisp eid-table {eid_table} ipv6 server {eid}',
                   'show lisp eid-table {eid_table} ipv6 server etr-address {etr_address}']

    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None, eid_table=None,
            vrf=None, locator_table=None, site_name=None, etr_address=None):

        if output is None:
            if locator_table and instance_id and site_name:
                output = self.device.execute(self.cli_command[13].\
                                            format(locator_table=locator_table, instance_id=instance_id, site_name=site_name))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[14].\
                                            format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and instance_id and etr_address:
                output = self.device.execute(self.cli_command[15].\
                                            format(locator_table=locator_table, instance_id=instance_id, etr_address=etr_address))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[12].\
                                            format(locator_table=locator_table, instance_id=instance_id))
            elif lisp_id and instance_id and site_name:
                output = self.device.execute(self.cli_command[5].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, site_name=site_name))
            elif lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[6].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and etr_address:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, etr_address=etr_address))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[4].\
                                            format(lisp_id=lisp_id, instance_id=instance_id))
            elif etr_address and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(etr_address=etr_address, instance_id=instance_id))
            elif eid and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid=eid, instance_id=instance_id))
            elif site_name and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(site_name=site_name, instance_id=instance_id))
            elif etr_address and vrf:
                output = self.device.execute(self.cli_command[11].\
                                            format(etr_address=etr_address, vrf=vrf))
            elif eid and vrf:
                output = self.device.execute(self.cli_command[10].\
                                            format(eid=eid, vrf=vrf))
            elif site_name and vrf:
                output = self.device.execute(self.cli_command[9].\
                                            format(site_name=site_name, vrf=vrf))
            elif vrf:
                output = self.device.execute(self.cli_command[8].\
                                            format(vrf=vrf))
            elif eid_table and site_name:
                output = self.device.execute(self.cli_command[17].\
                                            format(eid_table=eid_table, site_name=site_name))
            elif eid_table and eid:
                output = self.device.execute(self.cli_command[18].\
                                            format(eid_table=eid_table, eid=eid))
            elif eid_table and etr_address:
                output = self.device.execute(self.cli_command[19].\
                                            format(eid_table=eid_table, etr_address=etr_address))
            elif eid_table:
                output = self.device.execute(self.cli_command[16].\
                                            format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispIpv6ServerExtranetPolicyEid(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv6 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv6 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv6 server extranet-policy {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server extranet-policy {prefix}',
                   'show lisp eid-table {eid_table} ipv6 server extranet-policy {prefix}',
                   'show lisp eid-table vrf {vrf} ipv6 server extranet-policy {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server extranet-policy {prefix}']

    def cli(self, output=None, lisp_id=None, instance_id=None, eid_table=None, prefix=None, vrf=None, locator_table=None):

        if output is None:
            if locator_table and instance_id and prefix:
                output = self.device.execute(self.cli_command[4].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id,
                                                   prefix=prefix))
            elif lisp_id and instance_id and prefix:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id,
                                                   prefix=prefix))
            elif instance_id and prefix:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id,
                                                   prefix=prefix))
            elif vrf and prefix:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf,
                                                   prefix=prefix))
            else:
                output = self.device.execute(self.cli_command[2].\
                                            format(eid_table=eid_table,
                                                   prefix=prefix))
        return super().cli(output=output)


class ShowLispInstanceIdIpv6MapCache(ShowLispMapCacheSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv6 map-cache
    * show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache
    * show lisp eid-table vrf {vrf} ipv6 map-cache
    * show lisp eid-table {eid_table} ipv6 map-caches"""

    cli_command = ['show lisp instance-id {instance_id} ipv6 map-cache',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 map-cache',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 map-cache',
                   'show lisp eid-table vrf {vrf} ipv6 map-cache',
                   'show lisp eid-table {eid_table} ipv6 map-cache']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):
        if output is None:
            if locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].format(vrf=vrf),timeout=300)
            elif eid_table:
                output = self.device.execute(self.cli_command[4].format(eid_table=eid_table))
            else:
                raise TypeError("No arguments provided to parser")
        return super().cli(output=output)


class ShowLispV6ServerConfigPropagation(ShowLispSiteSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv6 server config-propagation
    * show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation
    """
    cli_command = ['show lisp instance-id {instance_id} ipv6 server config-propagation',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation']

    def cli(self, lisp_id=None, instance_id=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(
                    lisp_id=lisp_id, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(
                    instance_id=instance_id))
        return super().cli(output=output,lisp_id=lisp_id, instance_id=instance_id)


class ShowLispServerConfigPropV6Parser(ShowLispServerConfigPropV4Parser):

    """ Parser for
        * show lisp instance-id {instance_id} ipv6 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation
    """

    cli_command = ['show lisp instance-id {instance_id} ipv6 server config-propagation',
                   'show lisp {lisp_id} instance-id {instance_id} ipv6 server config-propagation']

    pass


class ShowLispIpv6ServerSubscription(ShowLispServerSubscriptionSuperParser, ShowLispServerSubscriptionSchema):
    ''' Show Command Ipv6 subscription
        show lisp instance-id {instance_id} ipv6 server subscription
        show lisp {lisp_id} instance-id {instance_id} ipv6 server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server subscription
        show lisp eid-table {eid_table} ipv6 server subscription
        show lisp eid-table vrf {vrf} ipv6 server subscription
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ipv6 server subscription',
        'show lisp {lisp_id} instance-id {instance_id} ipv6 server subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv6 server subscription',
        'show lisp eid-table {eid_table} ipv6 server subscription',
        'show lisp eid-table vrf {vrf} ipv6 server subscription'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                                format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                                format(locator_table=locator_table, instance_id=instance_id))
            elif eid_table:
                output = self.device.execute(self.cli_command[3].\
                                                format(eid_table=eid_table))
            else:
                output = self.device.execute(self.cli_command[4].\
                                                format(vrf=vrf))

        return super().cli(output=output)

