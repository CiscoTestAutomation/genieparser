"""show_lisp_ipv4.py

    * show lisp all service ipv4
    * show lisp all instance-id <instance_id> ipv4
    * show lisp all instance-id <instance_id> ipv4 map-cache
    * show lisp all instance-id <instance_id> ipv4 server rloc members
    * show lisp all instance-id <instance_id> ipv4 smr
    * show lisp all instance-id <instance_id> ipv4 database
    * show lisp all instance-id <instance_id> ipv4 server summary
    * show lisp all instance-id <instance_id> ipv4 server detail internal
    * show lisp all instance-id <instance_id> ipv4 statistics
    * show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber
    * show lisp instance-id {instance_id} ipv4 subscriber
    * show lisp eid-table {eid_table} ipv4 subscriber
    * show lisp eid-table vrf {vrf} ipv4 subscriber
    * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
    * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
    * show lisp instance-id {instance_id} ipv4 publisher
    * show lisp eid-table {eid_table} ipv4 publisher
    * show lisp eid-table vrf {vrf} ipv4 publisher
    * show lisp instance-id {instance_id} ipv4 away
    * show lisp instance-id {instance_id} ipv4 away {eid}
    * show lisp instance-id {instance_id} ipv4 away {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} ipv4 away
    * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}
    * show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}
    * show lisp eid-table {eid_table} ipv4 away
    * show lisp eid-table {eid_table} ipv4 away {eid}
    * show lisp eid-table {eid_table} ipv4 away {eid_prefix}
    * show lisp eid-table vrf {eid_table} ipv4 away
    * show lisp eid-table vrf {eid_table} ipv4 away {eid}
    * show lisp eid-table vrf {eid_table} ipv4 away {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
    * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
    * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
    * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
    * show lisp eid-table vrf ipv4 publisher {publisher_id}
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

class ShowLispIpv4ServerSHD(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ipv4 server silent-host-detection
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server silent-host-detection
        * show lisp eid-table {eid_table} ipv4 server silent-host-detection
        * show lisp eid-table vrf {vrf} ipv4 server silent-host-detection
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server silent-host-detection
    """

    cli_command = ['show lisp instance-id {instance_id} ipv4 server silent-host-detection',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server silent-host-detection',
                   'show lisp eid-table {eid_table} ipv4 server silent-host-detection',
                   'show lisp eid-table vrf {vrf} ipv4 server silent-host-detection',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server silent-host-detection']

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

class ShowLispIpv4ServerExtranetPolicy(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ipv4 server extranet-policy
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy
        * show lisp eid-table {eid_table} ipv4 server extranet-policy
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy
    """

    cli_command = ['show lisp instance-id {instance_id} ipv4 server extranet-policy',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy',
                   'show lisp eid-table {eid_table} ipv4 server extranet-policy',
                   'show lisp eid-table vrf {vrf} ipv4 server extranet-policy',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy']

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


class ShowLispInstanceIdIpv4Server(ShowLispSiteSuperParser):

    """ Parser for
        * show lisp instance-id {instance_id} ipv4 server
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server
        * show lisp eid-table vrf {vrf} ipv4 server
        * show lisp eid-table {eid_table} ipv4 server
    """

    cli_command = ['show lisp instance-id {instance_id} ipv4 server',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server',
                   'show lisp eid-table vrf {vrf} ipv4 server',
                   'show lisp eid-table {eid_table} ipv4 server']

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
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, output=output)


# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ipv4 publication'
#  * 'show lisp {lisp_id} instance-id {instance_id} ipv4 publication'
#  * 'show lisp eid-table {eid-table} ipv4 publication'
#  * 'show lisp eid-table vrf {vrf} ipv4 publication'
#  * 'show lisp locator-table {vrf} instance-id {instance-id} ipv4 publication'
# ==========================================
class ShowLispIpv4Publication(ShowLispIpv4PublicationSchema):
    """Parser for show lisp ipv4 publication"""
    cli_command = ['show lisp instance-id {instance_id} ipv4 publication',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 publication',
                   'show lisp eid-table {eid_table} ipv4 publication',
                   'show lisp eid-table vrf {vrf} ipv4 publication',
                   'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publication']

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

        # 44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
        # 44:44:44:44::   1d21h       192.168.1.71/32          11.11.11.11     -
        # 13.13.13.13     00:00:54    192.168.0.0/16           -       -
        p3 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                        r"(?P<last_published>\S+)\s+(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})\s+"
                        r"(?P<rloc>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+)|-)\s+(?P<encap_iid>\S+)$")

        # New format (Locators are no longer displayed in the output)

        # 192.168.1.71/32     1d21h   44.44.44.44   -
        p4 = re.compile(r"^(?P<eid_prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})\s+"
                        r"(?P<last_published>\S+)\s+(?P<publisher_ip>(\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<encap_iid>\S+)$")

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

            # 44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11
            # 44:44:44:44::   1d21h       192.168.1.71/32          11.11.11.11     -
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

            # 192.168.1.71/32     1d21h   44.44.44.44   -
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


class ShowLispIpv4RouteImportMapCache(ShowLispRouteImportMapCacheSuperParser,ShowLispRouteImportMapCacheSchema):
      '''route Import map-cache cli variations'''
      cli_command = [
        'show lisp instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid}',
        'show lisp eid-table vrf {vrf} ipv4 route-import map-cache {eid_prefix}',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid}',
        'show lisp eid-table {eid_table} ipv4 route-import map-cache {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 route-import map-cache {eid_prefix}'
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


class ShowLispIpv4Away(ShowLispEidAwaySuperParser, ShowLispEidAwaySchema):
    ''' Show Command Ipv4 Away
        show lisp instance-id {instance_id} ipv4 away
        show lisp instance-id {instance_id} ipv4 away {eid}
        show lisp instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp {lisp_id} instance-id {instance_id} ipv4 away
        show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}
        show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}
        show lisp eid-table {eid_table} ipv4 away
        show lisp eid-table {eid_table} ipv4 away {eid}
        show lisp eid-table {eid_table} ipv4 away {eid_prefix}
        show lisp eid-table vrf {eid_table} ipv4 away
        show lisp eid-table vrf {eid_table} ipv4 away {eid}
        show lisp eid-table vrf {eid_table} ipv4 away {eid_prefix}
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ipv4 away',
        'show lisp instance-id {instance_id} ipv4 away {eid}',
        'show lisp instance-id {instance_id} ipv4 away {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 away',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid}',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 away {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 away {eid_prefix}',
        'show lisp eid-table {eid_table} ipv4 away',
        'show lisp eid-table {eid_table} ipv4 away {eid}',
        'show lisp eid-table {eid_table} ipv4 away {eid_prefix}',
        'show lisp eid-table vrf {vrf} ipv4 away',
        'show lisp eid-table vrf {vrf} ipv4 away {eid}',
        'show lisp eid-table vrf {vrf} ipv4 away {eid_prefix}'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[4].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[5].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                                format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id and eid:
                output = self.device.execute(self.cli_command[1].\
                                                format(instance_id=instance_id, eid= eid))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].\
                                                format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[7].\
                                                format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[8].\
                                                format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[6].\
                                                format(locator_table=locator_table, instance_id=instance_id))
            elif eid_table and eid:
                output = self.device.execute(self.cli_command[10].\
                                                format(eid_table=eid_table, eid=eid))
            elif eid_table and eid_prefix:
                output = self.device.execute(self.cli_command[11].\
                                                format(eid_table=eid_table, eid_prefix=eid_prefix))
            elif eid_table:
                output = self.device.execute(self.cli_command[9].\
                                                format(eid_table=eid_table))
            elif vrf and eid:
                output = self.device.execute(self.cli_command[13].\
                                                format(vrf=vrf, eid=eid))
            elif vrf and eid_prefix:
                output = self.device.execute(self.cli_command[14].\
                                                format(vrf=vrf, eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[12].\
                                                format(vrf=vrf))
        else:
            output = output

        return super().cli(output=output)


class ShowLispIpv4Publisher(ShowLispPublisherSuperParser, ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher
        * show lisp instance-id {instance_id} ipv4 publisher
        * show lisp eid-table {eid_table} ipv4 publisher
        * show lisp eid-table vrf {vrf} ipv4 publisher
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv4 publisher',
        'show lisp locator-table {vrf} instance-id {instance_id} ipv4 publisher',
        'show lisp instance-id {instance_id} ipv4 publisher',
        'show lisp eid-table {eid_table} ipv4 publisher',
        'show lisp eid-table vrf {vrf} ipv4 publisher',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, eid_table=None):

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


class ShowLispIpv4Subscriber(ShowLispSubscriberSuperParser, ShowLispSubscriberSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber
        * show lisp instance-id {instance_id} ipv4 subscriber
        * show lisp eid-table {eid_table} ipv4 subscriber
        * show lisp eid-table vrf {vrf} ipv4 subscriber
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv4 subscriber',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscriber',
        'show lisp instance-id {instance_id} ipv4 subscriber',
        'show lisp eid-table {eid_table} ipv4 subscriber',
        'show lisp eid-table vrf {vrf} ipv4 subscriber'
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


class ShowLispIpv4Subscription(ShowLispSubscriptionSuperParser, ShowLispSubscriptionSchema):
    ''' Show Command Ipv4 Subscription
        show lisp instance-id {instance_id} ipv4 subscription
        show lisp {lisp_id} instance-id {instance_id} ipv4 subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscription
        show lisp eid-table {eid_table} ipv4 subscription
        show lisp eid-table vrf {eid_table} ipv4 subscription
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ipv4 subscription',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 subscription',
        'show lisp eid-table {eid_table} ipv4 subscription',
        'show lisp eid-table vrf {vrf} ipv4 subscription'
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


class ShowLispIpv4PublisherRloc(ShowLispIpv4v6PublisherRloc):

    ''' Parser for
     * show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp instance-id {instance_id} ipv4 publisher {publisher_id}
     * show lisp eid-table {eid_table} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}
     * show lisp eid-table vrf ipv4 publisher {publisher_id}
    '''

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ipv4 publisher {publisher_id}',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 publisher {publisher_id}',
        'show lisp instance-id {instance_id} ipv4 publisher {publisher_id}',
        'show lisp eid-table {eid_table} ipv4 publisher {publisher_id}',
        'show lisp eid-table vrf {vrf} ipv4 publisher {publisher_id}',
        'show lisp eid-table vrf ipv4 publisher {publisher_id}',
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


class ShowLispSMRSchema(MetaParser):

    ''' Schema for
        * show lisp instance-id {instance_id} ipv4 smr
        * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
        * show lisp eid-table {eid_table} ipv4 smr
        * show lisp eid-table vrf {vrf} ipv4 smr
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        Optional('eid_table'): str,
                        'entries': int,
                        'prefix': {
                            str: { # EID prefix
                                'producer': list
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispV4SMRParser(ShowLispSMRSchema):
    """
    Parser for
    * show lisp instance-id {instance_id} ipv4 smr
    * show lisp {lisp_id} instance-id {instance_id} ipv4 smr
    * show lisp eid-table {eid_table} ipv4 smr
    * show lisp eid-table vrf {vrf} ipv4 smr
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr
    """
    cli_command = ['show lisp instance-id {instance_id} ipv4 smr',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 smr',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 smr'
                   #'show lisp eid-table {eid_table} ipv4 smr',
                   #'show lisp eid-table vrf {vrf} ipv4 smr',
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
        lisp_v4_smr = {}
        count = 0

        #Output for router lisp 0 instance-id 4100
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        #LISP SMR Table for router lisp 0 (red) IID 4100
        p2 = re.compile(r"^LISP\s+SMR\s+Table\s+for\s+router\s+lisp\s+"
                        r"\d+\s+\((?P<eid_table>\S+)\)\s+IID\s+\d+")

        #Entries: 3
        p3 = re.compile(r"^Entries:\s+(?P<entries>\d+)")

        #192.168.1.0/24                          away table
        p4 = re.compile(r"^(?P<prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
                        r"\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3})\s+"
                        r"(?P<producer>\w+\s\w+\,\s\w+\s\w+|\w+\s\w+|\w+)")

        #  Instance ID:                              4100
        p5 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\S+)")

        for line in output.splitlines():
            line = line.strip()
            count += 1
            #Output for router lisp 0 instance-id 4100
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = lisp_v4_smr.setdefault('lisp_id',{})\
                                          .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                              .setdefault(instance_id,{})
                continue
            if not m and count < 2 and lisp_id != "all" and line != "":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = lisp_v4_smr.setdefault('lisp_id',{})\
                                              .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                   .setdefault(instance_id,{})
                    count += 1
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = lisp_v4_smr.setdefault('lisp_id',{})\
                                              .setdefault(lisp_id,{})
                    if instance_id != "*":
                        instance_id = int(instance_id)
                        instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                       .setdefault(instance_id,{})
                    count += 1
                    continue

            #LISP SMR Table for router lisp 0 (red) IID 4100
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                eid_table = groups['eid_table']
                instance_id_dict.update({'eid_table':eid_table})
                continue

            #Entries: 3
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['entries'])
                instance_id_dict.update({'entries':entries})
                continue

            #192.168.1.0/24                          away table
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                prefix = groups['prefix']
                producer = groups['producer']
                prefix_dict = instance_id_dict.setdefault('prefix',{})\
                                          .setdefault(prefix,{})
                producer_list = prefix_dict.setdefault('producer',[])
                producer_list.append(producer)
                producer_list = producer_list[0].split(',')
                prefix_dict.update({'producer':producer_list})
        return lisp_v4_smr


class ShowLispInstanceIdIpv4ForwardingEID(ShowLispInstanceIdForwardingEidRemoteSchema):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 forwarding eid remote
    '''
    cli_command = 'show lisp instance-id {instance_id} ipv4 forwarding eid remote'

    def cli(self, instance_id, output=None):
        if output is None:
            if instance_id:
                output = self.device.execute(self.cli_command.format(instance_id=instance_id))
        ret_dict = {}

        # 0.0.0.0/0              signal      0x00000000            N/A
        p1 = re.compile(r"^(?P<prefix>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})\s+"
                        r"(?P<fwd_action>\S+)\s+(?P<locator_status_bits>\S+)\s+(?P<encap_iid>\S+)$")

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


class ShowLispIpv4MapCachePrefix(ShowLispIpMapCachePrefixSuperParser):

    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}
        * show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv4 map-cache {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache {prefix}',
                   'show lisp eid-table vrf {eid_table} ipv4 map-cache {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache {prefix}']

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


class ShowLispIpv4ServerDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 server detail
        * show lisp instance-id {instance_id} ipv4 server name {site_name}
        * show lisp instance-id {instance_id} ipv4 server {eid}
        * show lisp instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server detail
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server etr-address {etr_address}
        * show lisp eid-table {eid_table} ipv4 server detail
        * show lisp eid-table {eid_table} ipv4 server name {site_name}
        * show lisp eid-table {eid_table} ipv4 server {eid}
        * show lisp eid-table {eid_table} ipv4 server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ipv4 server detail
        * show lisp eid-table vrf {vrf} ipv4 server name {site_name}
        * show lisp eid-table vrf {vrf} ipv4 server {eid}
        * show lisp eid-table vrf {vrf} ipv4 server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server etr-address {etr_address}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv4 server detail',
                   'show lisp instance-id {instance_id} ipv4 server name {site_name}',
                   'show lisp instance-id {instance_id} ipv4 server {eid}',
                   'show lisp instance-id {instance_id} ipv4 server etr-address {etr_address}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server detail',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server name {site_name}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server etr-address {etr_address}',
                   'show lisp eid-table vrf {vrf} ipv4 server detail',
                   'show lisp eid-table vrf {vrf} ipv4 server name {site_name}',
                   'show lisp eid-table vrf {vrf} ipv4 server {eid}',
                   'show lisp eid-table vrf {vrf} ipv4 server etr-address {etr_address}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server name {site_name}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server etr-address {etr_address}',
                   'show lisp eid-table {eid_table} ipv4 server detail',
                   'show lisp eid-table {eid_table} ipv4 server name {site_name}',
                   'show lisp eid-table {eid_table} ipv4 server {eid}',
                   'show lisp eid-table {eid_table} ipv4 server etr-address {etr_address}']

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


class ShowLispIpv4ServerExtranetPolicyEid(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy {prefix}
        * show lisp eid-table {eid_table} ipv4 server extranet-policy {prefix}
        * show lisp eid-table vrf {vrf} ipv4 server extranet-policy {prefix}
        * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy {prefix}
    '''
    cli_command = ['show lisp instance-id {instance_id} ipv4 server extranet-policy {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server extranet-policy {prefix}',
                   'show lisp eid-table {eid_table} ipv4 server extranet-policy {prefix}',
                   'show lisp eid-table vrf {vrf} ipv4 server extranet-policy {prefix}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server extranet-policy {prefix}']

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


class ShowLispInstanceIdIpv4MapCache(ShowLispMapCacheSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv4 map-cache
    * show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache
    * show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache
    * show lisp eid-table vrf {vrf} ipv4 map-cache
    * show lisp eid-table {eid_table} ipv4 map-caches"""

    cli_command = ['show lisp instance-id {instance_id} ipv4 map-cache',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 map-cache',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 map-cache',
                   'show lisp eid-table vrf {vrf} ipv4 map-cache',
                   'show lisp eid-table {eid_table} ipv4 map-cache']

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


class ShowLispV4ServerConfigPropagation(ShowLispSiteSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv4 server config-propagation
    * show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation
    """
    cli_command = ['show lisp instance-id {instance_id} ipv4 server config-propagation',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation']

    def cli(self, lisp_id=None, instance_id=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(
                    lisp_id=lisp_id, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(
                    instance_id=instance_id))
        return super().cli(output=output,lisp_id=lisp_id, instance_id=instance_id)


class ShowLispServerConfigPropV4Parser(ShowLispSiteSuperParser):

    """ Parser for
        * show lisp instance-id {instance_id} ipv4 server config-propagation
        * show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation
    """

    cli_command = ['show lisp instance-id {instance_id} ipv4 server config-propagation',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 server config-propagation']

    def cli(self, instance_id, lisp_id=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id)
            else:
                cmd = self.cli_command[0].format(instance_id=instance_id)
            output = self.device.execute(cmd)
        return super().cli(output=output, instance_id=instance_id)


class ShowLispIpv4ServerSubscription(ShowLispServerSubscriptionSuperParser, ShowLispServerSubscriptionSchema):
    ''' Show Command Ipv4 Subscription
        show lisp instance-id {instance_id} ipv4 server subscription
        show lisp {lisp_id} instance-id {instance_id} ipv4 server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server subscription
        show lisp eid-table {eid_table} ipv4 server subscription
        show lisp eid-table vrf {vrf} ipv4 server subscription
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ipv4 server subscription',
        'show lisp {lisp_id} instance-id {instance_id} ipv4 server subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} ipv4 server subscription',
        'show lisp eid-table {eid_table} ipv4 server subscription',
        'show lisp eid-table vrf {vrf} ipv4 server subscription'
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


class ShowLispPublicationConfigPropV4Parser(ShowLispPublicationConfigPropSuperParser):

    ''' Parser for
    * show lisp {lisp_id} instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
    * show lisp instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
    * show lisp instance-id {instance_id} ipv4 publication config-propagation detail',
    * show lisp all instance-id * ipv4 publication config-propagation
    '''

    cli_command = ['show lisp {lisp_id} instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
                   'show lisp instance-id {instance_id} ipv4 publication config-propagation {eid_prefix}',
                   'show lisp instance-id {instance_id} ipv4 publication config-propagation detail',
                   'show lisp all instance-id * ipv4 publication config-propagation']

    def cli(self, instance_id, output=None, lisp_id=None, eid_prefix=None):

        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(instance_id=instance_id, eid_prefix=eid_prefix))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[3])
        return super().cli(instance_id=instance_id,output=output)


class ShowLispDatabaseConfigPropV4Parser(ShowLispDatabaseConfigPropSuperParser):

    """
    Parser for
    * show lisp instance-id {instance_id} ipv4 database config-propagation
    * show lisp {lisp_id} instance-id {instance_id} ipv4 database config-propagation'
    * show lisp instance-id {instance_id} ipv4 database config-propagation {eid_prefix}
    """

    cli_command = ['show lisp instance-id {instance_id} ipv4 database config-propagation',
                   'show lisp {lisp_id} instance-id {instance_id} ipv4 database config-propagation',
                   'show lisp instance-id {instance_id} ipv4 database config-propagation {eid_prefix}']

    def cli(self, instance_id, output=None, lisp_id=None, eid_prefix=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id))
            elif instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id, eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
        return super().cli(instance_id=instance_id, output=output)