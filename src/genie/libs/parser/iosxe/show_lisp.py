''' show_lisp.py

IOSXE parsers for the following show commands:
    * show lisp all extranet <extranet> instance-id <instance_id>
    * show lisp all service ethernet
    * show lisp all instance-id <instance_id> ethernet
    * show lisp all instance-id <instance_id> ethernet map-cache
    * show lisp all instance-id <instance_id> ethernet server rloc members
    * show lisp all instance-id <instance_id> ethernet smr
    * show lisp service {service} summary
    * show lisp {lisp_id} service {service} summary
    * show lisp locator-table {locator_table} service {service} summary
    * show lisp locator-table vrf {vrf} service {service} summary
    * show lisp all instance-id <instance_id> ethernet database
    * show lisp all instance-id <instance_id> ethernet server summary
    * show lisp all instance-id <instance_id> ethernet server detail internal
    * show lisp all instance-id <instance_id> ethernet statistics
    * show lisp {lisp_id} instance-id {instance_id} ethernet subscriber
    * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber
    * show lisp instance-id {instance_id} ethernet subscriber
    * show lisp eid-table vlan {vlan} ethernet subscriber
    * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
    * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
    * show lisp instance-id {instance_id} ethernet publisher
    * show lisp eid-table vlan {vlan} ethernet publisher
    * show lisp instance-id {instance-id} {address-family} database {prefix}
    * show lisp {lisp_id} instance-id {instance-id} {address-family} database {prefix}
    * show lisp locator-table {vrf} instance-id {instance-id} {address-family} database {prefix}
    * show lisp locator-table vrf {vrf} instance-id {instance-id} {address-family} database {prefix}
    * show lisp eid-table {vrf} {address-family} {prefix}
    * show lisp eid-table vrf {vrf} {address-family} database {prefix}
    * show lisp eid-table vlan {vlan_id} ethernet database {prefix}
    * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
    * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
    * show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}
    * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    * show lisp {lisp_id} redundancy
    * show lisp redundancy
    * show lisp locator-table {locator_table} redundancy
    * show lisp {lisp_id} instance-id {instance_id} {address_family} eid-watch
    * show lisp instance-id {instance_id} {address_family} eid-watch
    * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} eid-watch
    * show lisp eid-table {eid_table} {address_family} eid-watch
    * show lisp eid-table vlan {vlan_id} ethernet eid-watch
    * show lisp {lisp_id} instance-id {instance_id} dn statistics
    * show lisp remote-locator-set {remote_locator_type}
    * show lisp remote-locator-set name {remote_locator_name}
    * show lisp {lisp_id} remote-locator-set {remote_locator_type}
    * show lisp {lisp_id} remote-locator-set name {remote_locator_name}
    * show lisp vrf {vrf}
'''

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


# ========================================================================
# Schema for 'show lisp <lisp_id> extranet <extranet_name> instance-id <instance_id>'
# ========================================================================
class ShowLispExtranetSchema(MetaParser):

    ''' Schema for
        * show lisp extranet {extranet_name} instance-id {instance_id}
        * show lisp {lisp_id} extranet {extranet_name} instance-id {instance_id}
    '''
    schema = {
        'lisp_id': {
            int: {
                'home_instance': int,
                'total': int,
                Optional('eid_prefix'): {
                    str:{
                        'type': str,
                        'source': str,
                        'iid': int,
                        'eid': str,
                        'mask': int
                        }
                    }
                }
            }
        }


# ========================================================================
# Parser for 'show lisp <lisp_id> extranet <extranet_name> instance-id <instance_id>'
# ========================================================================
class ShowLispExtranet(ShowLispExtranetSchema):

    ''' Parser for
        * show lisp extranet {extranet_name} instance-id {instance_id}
        * show lisp {lisp_id} extranet {extranet_name} instance-id {instance_id}
    '''
    cli_command = ['show lisp extranet {extranet_name} instance-id {instance_id}',
                   'show lisp {lisp_id} extranet {extranet_name} instance-id {instance_id}']

    def cli(self, extranet_name, instance_id, output=None, lisp_id=None):

        if output is None:
            if lisp_id and extranet_name and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, extranet_name=extranet_name, instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[0].format(extranet_name=extranet_name, instance_id=instance_id))
        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>(\d+))$")

        # Home Instance ID: 101
        p2 = re.compile(r"^Home\s+Instance\s+ID:\s+(?P<home_instance>(\d+))$")

        # Provider    Dynamic     103        88.88.88.0/24
        # Provider    Config      103        88.88.88.0/24
        # Provider    Config      103        2001:200:200:200::/64
        p3 = re.compile(r'^(?P<type>Provider|Subscriber)\s+(?P<source>Dynamic|Config)'
                        r'\s+(?P<iid>\d+)\s+(?P<eid>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'
                        r'[a-fA-F\d\:]+)\/(?P<mask>\d{1,2})$')

        # Total entries: 5
        p4 = re.compile(r"^Total\s+entries:\s+(?P<total>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                continue

            # Home Instance ID: 101
            m = p2.match(line)
            if m:
                if lisp_id != "all":
                    lisp_id = int(lisp_id) if lisp_id else 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                groups = m.groupdict()
                home_instance = int(groups['home_instance'])
                lisp_id_dict.update({'home_instance':home_instance})
                lisp_id_dict.setdefault('total')
                continue

            # Provider    Dynamic     103        88.88.88.0/24
            # Provider    Config      103        2001:200:200:200::/64
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                type = groups['type']
                source = groups['source']
                iid = int(groups['iid'])
                eid = groups['eid']
                mask = int(groups['mask'])
                eid_prefix = "{}/{}".format(eid,mask)
                eid_dict = lisp_id_dict.setdefault('eid_prefix',{})\
                                       .setdefault(eid_prefix,{})
                eid_dict.update({'type':type,
                                 'source':source,
                                 'iid':iid,
                                 'eid':eid,
                                 'mask':mask})
                continue

            # Total entries: 5
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                total = int(groups['total'])
                lisp_id_dict.update({'total':total})
                continue
        return ret_dict


# ===================
# Parser for:
#  * 'show lisp site'
# ===================
class ShowLispSite(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp site
        * show lisp {lisp_id} site
        * show lisp site instance-id {instance_id}
        * show lisp {lisp_id} site instance-id {instance_id}
        * show lisp site eid-table {eid_table}
        * show lisp {lisp_id} site eid-table {eid_table}
        * show lisp site eid-table vrf {vrf}
        * show lisp {lisp_id} site eid-table vrf {vrf}
    """

    cli_command = ['show lisp site',
                   'show lisp {lisp_id} site',
                   'show lisp site instance-id {instance_id}',
                   'show lisp {lisp_id} site instance-id {instance_id}',
                   'show lisp site eid-table {eid_table}',
                   'show lisp {lisp_id} site eid-table {eid_table}',
                   'show lisp site eid-table vrf {vrf}',
                   'show lisp {lisp_id} site eid-table vrf {vrf}']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vrf=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif lisp_id and eid_table:
                output = self.device.execute(self.cli_command[5].\
                                            format(lisp_id=lisp_id,
                                                   eid_table=eid_table))
            elif lisp_id and vrf:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id,
                                                   vrf=vrf))
            elif vrf:
                output = self.device.execute(self.cli_command[6].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid_table=eid_table))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(instance_id=instance_id))
            elif lisp_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])
        return super().cli(output=output)


# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ethernet server'
# ==========================================
class ShowLispInstanceIdEthernetServer(ShowLispSiteSuperParser):

    """ Parser for show lisp site
        * show lisp instance-id {instance_id} ethernet server
        * show lisp {lisp_id} instance-id {instance_id} ethernet server
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server
        * show lisp eid-table vlan {vlan} ethernet server
    """

    cli_command = ['show lisp instance-id {instance_id} ethernet server',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server',
                   'show lisp eid-table vlan {vlan} ethernet server']

    def cli(self, lisp_id=None, instance_id=None, locator_table=None, vlan=None, output=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id,
                                                   instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(locator_table=locator_table,
                                                   instance_id=instance_id))
            elif vlan:
                output = self.device.execute(self.cli_command[3].\
                                            format(vlan=vlan))
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(lisp_id=lisp_id, instance_id=instance_id, output=output)


class ShowLispPrefixListSchema(MetaParser):

    """
    Schema for show lisp prefix-list <name>
    """
    schema = {
        'lisp_id': {
            int: {
                'prefix_list_name': {
                    str:{
                        'number_of_entries': int,
                        Optional('users'):
                            ListOf({
                                Optional(str): str
                            }),
                        Optional('prefix_list_users'): {
                            'instance_id': {
                                int: {
                                    'address_family': {
                                        str: {
                                            'users': {
                                                str: {
                                                    Optional('address'): ListOf(str)
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        Optional('entries'):{
                            str:{
                                'sources': str,
                                'first_added': str,
                                'last_verified_by':  str,
                                'last_verified': str,
                                 Optional('source_list'): ListOf(str),
                                 Optional('number_of_rib_sources'): int,
                                 Optional('number_of_publication_sources'): int,
                                 Optional('number_of_site_registration_sources'): int
                            }
                        }
                    }
                }
            }
        }
    }


'''Parser for "show lisp prefix-list"'''
class ShowLispPrefixList(ShowLispPrefixListSchema):

    '''Parser for "show lisp prefix-list"'''
    cli_command = ['show lisp prefix-list',
                   'show lisp prefix-list {prefix_list_name}',
                   'show lisp {lisp_id} prefix-list',
                   'show lisp {lisp_id} prefix-list {prefix_list_name}']

    def cli(self, lisp_id=None, instance_id=None, prefix_list_name=None, output=None):
        if output is None:
            if lisp_id and prefix_list_name:
                cmd = self.cli_command[3].format(lisp_id=lisp_id, prefix_list_name=prefix_list_name)
            elif prefix_list_name:
                cmd = self.cli_command[1].format(prefix_list_name=prefix_list_name)
            elif lisp_id:
                cmd = self.cli_command[2].format(lisp_id=lisp_id)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)
        lisp_prefix_dict = {}

        #LISP Prefix List information for router lisp 0
        p1 = re.compile(r"^LISP Prefix List information for router lisp\s+(?P<lisp_prefix_id>\d+)$")

        #Prefix List: site1
        p2 = re.compile(r"^Prefix\s+List:\s+(?P<prefix_list_name>\S+)$")

        #Number of entries: 2
        p3 = re.compile(r"^\s+Number\s+of\s+entries:\s+(?P<no_entries>\d+)")

        #ITR Map Resolver    100.100.100.100|2001:192:168:1::
        #IID 5000     IPv6  ITR Map Resolver    3130:3130:3130:3130:3130:3130:3130:3130
        p4 = re.compile(r"^\s+(IID\s+)?(?P<iid>\d+)?\s*(?P<afi>\w+)?\s*ITR\s+Map\s+Resolver\s+(?P<itr_map_resolver_ip>[0-9a-fA-F\d:]+|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$")

        #ETR Map Server      44.44.44.44|2001:192:168:1::
        #IID 5000     IPv6  ETR Map Server      3130:3130:3130:3130:3130:3130:3130:3130
        p5 = re.compile(r"^\s+(IID\s+)?(?P<iid>\d+)?\s*(?P<afi>\w+)?\s*ETR\s+Map\s+Server\s+(?P<etr_map_server_ip>[0-9a-fA-F\d:]+|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$")

        #Import Publication
        #IID 5000     IPv6  Import Publication
        p6 = re.compile(r"^\s+(IID\s+)?(?P<iid>\d+)?\s*(?P<afi>\w+)?\s*Import\s+Publication(?P<import_publication>\s)")

        #Route Import
        #IID 5000     IPv6  Route Import
        p7 = re.compile(r"^\s+(IID\s+)?(?P<iid>\d+)?\s*(?P<afi>\w+)?\s*Route\s+Import(?P<route_import>\s)")

        #Import
        #IID 5000     IPv6  Import
        p8 = re.compile(r"^\s+(IID\s+)?(?P<iid>\d+)?\s*(?P<afi>\w+)?\s*Import(?P<import>\s)")

        #192.168.1.0/24|2001:192:168:1::/64
        p9 = re.compile(r"^\s+(?P<eid_prefix>[0-9a-fA-F\d:]+\/\d+|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})$")

        #Sources: static
        #Sources: static, publication
        p10 = re.compile(r"^\s+Sources:\s+(?P<prefix_source>.+)$")

        #First added: 00:09:20
        p11 = re.compile(r"^\s+First added:\s+(?P<first_added>\S+),")

        #last verified: by static
        p12 = re.compile(r"^\s+First added:\s+\S+\s+last verified:\s+(?P<last_verified_by>\S+\s+\S+),")

        #00:09:20
        p13 = re.compile(r"^\s+First added:\s+\S+\s+last verified:\s\S+\s+\S+,\s+(?P<last_verified>\S+)")

        #Number of publications sourcing this entry: 2
        p14 = re.compile(r"^\s+Number of publications sourcing this entry: (?P<pub_source_count>\d+)")

        #Number of route imports sourcing this entry: 2
        p15 = re.compile(r"^\s+Number of route imports sourcing this entry: (?P<rib_source_count>\d+)")

        #Number of site registrations sourcing this entry: 2
        p16 = re.compile(r"^\s+Number of site registrations sourcing this entry: (?P<site_reg_source_count>\d+)")

        for line in output.splitlines():
            #LISP Prefix List information for router lisp 0
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                prefix_id = int(groups['lisp_prefix_id'])
                lisp_id_dict = lisp_prefix_dict.setdefault('lisp_id',{})\
                    .setdefault(prefix_id,{})
                continue

            #Prefix List: site1
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                prefix_list_name = groups['prefix_list_name']
                prefix_dict = lisp_id_dict.setdefault('prefix_list_name',{})\
                    .setdefault(prefix_list_name,{})
                continue

            #Number of entries: 2
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                no_entries = int(groups['no_entries'])
                prefix_dict.update({'number_of_entries':no_entries})
                continue

            #ITR Map Resolver    100.100.100.100|2001:192:168:1::
            #IID 5000     IPv6  ITR Map Resolver    3130:3130:3130:3130:3130:3130:3130:3130
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                itr_ip = groups['itr_map_resolver_ip']
                user_list = prefix_dict.setdefault('users',[])
                user_list.append({'itr_map_resolver' : itr_ip})

                if groups['iid'] is None or groups['afi'] is None:
                    continue

                plu_iid = int(groups['iid'])
                plu_afi = groups['afi']
                plu_dict = prefix_dict.setdefault('prefix_list_users', {})

                plu_instance_dict = \
                    plu_dict.setdefault('instance_id', {}) \
                            .setdefault(plu_iid, {})

                plu_afi_dict = \
                    plu_instance_dict.setdefault('address_family', {}) \
                                     .setdefault(plu_afi, {})

                plu_user_imr_address_list = \
                    plu_afi_dict.setdefault('users', {}) \
                                .setdefault('itr_map_resolver', {}) \
                                .setdefault('address', [])

                plu_user_imr_address_list.append(itr_ip)
                continue

            #ETR Map Server      44.44.44.44|2001:192:168:1::
            #IID 5000     IPv6  ETR Map Server      3130:3130:3130:3130:3130:3130:3130:3130
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                etr_ip = groups['etr_map_server_ip']
                user_list = prefix_dict.setdefault('users',[])
                user_list.append({'etr_map_server' : etr_ip})

                if groups['iid'] is None or groups['afi'] is None:
                    continue

                plu_iid = int(groups['iid'])
                plu_afi = groups['afi']
                plu_dict = prefix_dict.setdefault('prefix_list_users', {})

                plu_instance_dict = \
                    plu_dict.setdefault('instance_id', {}) \
                            .setdefault(plu_iid, {})

                plu_afi_dict = \
                    plu_instance_dict.setdefault('address_family', {}) \
                                     .setdefault(plu_afi, {})

                plu_user_ems_address_list = \
                    plu_afi_dict.setdefault('users', {}) \
                                .setdefault('etr_map_server', {}) \
                                .setdefault('address', [])

                plu_user_ems_address_list.append(etr_ip)
                continue

            #Import Publication
            #IID 5000     IPv6  Import Publication
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                import_user = groups['import_publication']
                user_list = prefix_dict.setdefault('users',[])
                user_list.append({'import_publication' : import_user})

                if groups['iid'] is None or groups['afi'] is None:
                    continue

                plu_iid = int(groups['iid'])
                plu_afi = groups['afi']
                plu_dict = prefix_dict.setdefault('prefix_list_users', {})

                plu_instance_dict = \
                    plu_dict.setdefault('instance_id', {}) \
                            .setdefault(plu_iid, {})

                plu_afi_dict = \
                    plu_instance_dict.setdefault('address_family', {}) \
                                     .setdefault(plu_afi, {})

                plu_afi_dict.setdefault('users', {}) \
                            .setdefault('import_publication', {})
                continue

            #Route Import
            #IID 5000     IPv6  Route Import
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                route_import = groups['route_import']
                user_list = prefix_dict.setdefault('users',[])
                user_list.append({'route_import' : route_import})

                if groups['iid'] is None or groups['afi'] is None:
                    continue

                plu_iid = int(groups['iid'])
                plu_afi = groups['afi']
                plu_dict = prefix_dict.setdefault('prefix_list_users', {})

                plu_instance_dict = \
                    plu_dict.setdefault('instance_id', {}) \
                            .setdefault(plu_iid, {})

                plu_afi_dict = \
                    plu_instance_dict.setdefault('address_family', {}) \
                                     .setdefault(plu_afi, {})

                plu_afi_dict.setdefault('users', {}) \
                            .setdefault('route_import', {})
                continue

            #Import
            #IID 5000     IPv6  Import
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                import_publication = groups['import']
                user_list = prefix_dict.setdefault('users',[])
                user_list.append({'import' : import_publication})

                if groups['iid'] is None or groups['afi'] is None:
                    continue

                plu_iid = int(groups['iid'])
                plu_afi = groups['afi']
                plu_dict = prefix_dict.setdefault('prefix_list_users', {})

                plu_instance_dict = \
                    plu_dict.setdefault('instance_id', {}) \
                            .setdefault(plu_iid, {})

                plu_afi_dict = \
                    plu_instance_dict.setdefault('address_family', {}) \
                                     .setdefault(plu_afi, {})

                plu_afi_dict.setdefault('users', {}) \
                            .setdefault('import_site_registration', {})
                continue

            #192.168.1.0/24|2001:192:168:1::/64
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                resolver_ip = groups['eid_prefix']
                prefix_list_entry_dict = \
                    prefix_dict.setdefault('entries', {})\
                                    .setdefault(resolver_ip, {})
                continue

            #Sources: static
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                source = groups['prefix_source']
                prefix_list_entry_dict.update({'sources' : source})

                prefix_list_entry_source_list = \
                    prefix_list_entry_dict.setdefault('source_list', [])
                source_list = source.split(',')
                for source_elm in source_list:
                    prefix_list_entry_source_list.append(source_elm.strip())
                continue

            #First added: 00:09:20
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                first_add = groups['first_added']
                prefix_list_entry_dict.update({'first_added' : first_add})

                m=p12.match(line)
                if m:
                    groups = m.groupdict()
                    last_verified_by = groups['last_verified_by']
                    prefix_list_entry_dict.update({'last_verified_by' : last_verified_by})

                #00:09:20
                m=p13.match(line)
                if m:
                    groups = m.groupdict()
                    last_Verified = groups['last_verified']
                    prefix_list_entry_dict.update({'last_verified' : last_Verified})

            #Number of publications sourcing this entry: 2
            m=p14.match(line)
            if m:
                groups = m.groupdict()
                pub_source_count = int(groups['pub_source_count'])
                prefix_list_entry_dict.update({'number_of_publication_sources' : pub_source_count})
                continue

            #Number of route imports sourcing this entry: 2
            m=p15.match(line)
            if m:
                groups = m.groupdict()
                rib_source_count = int(groups['rib_source_count'])
                prefix_list_entry_dict.update({'number_of_rib_sources' : rib_source_count})
                continue

            #Number of site registrations sourcing this entry: 2
            m=p16.match(line)
            if m:
                groups = m.groupdict()
                site_reg_source_count = int(groups['site_reg_source_count'])
                prefix_list_entry_dict.update({'number_of_site_registration_sources' : site_reg_source_count})
                continue

        return lisp_prefix_dict


class ShowLispARSchema(MetaParser):

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        Optional('entries'): {
                            str: {
                                'mac_address': str,
                                'inst_id': str
                            },
                        }
                    }
                }
            }
        }
    }


# ==========================================
# Parser for:
#   'Parser for show lisp instance-id <id> ethernet server address-resolution'
# ==========================================
class ShowLispAR(ShowLispARSchema):
    cli_command = ["show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution",
                   "show lisp instance-id {instance_id} ethernet server address-resolution"]

    def cli(self, lisp_id=None, instance_id=None, output=None):

        if not output:
            if lisp_id and instance_id:
                out = self.device.execute(self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id))
            else:
                out = self.device.execute(self.cli_command[1].format(instance_id=instance_id))
        else:
            out = output

        lisp_ar_dict = {}

        # Address-resolution data for router lisp 0 instance-id 1
        p1 = re.compile(
            r"^Address-resolution\s+data\s+for\s+router\s+lisp\s+"
            r"(?P<lisp_id>\d+)\s+instance-id\s+(?P<instance_id>\d+)$")

        # 0    192.168.1.1/32       aabb.cc00.ca00
        # 4100 2001:192:168:1::71/128 aabb.cc00.c901
        p2 = re.compile(
            r"^(?P<l2_inst_id>\d+)\s+(?P<eid_address>[0-9.]+\d+\/\d+"
            r"|[0-9a-fA-F.:]+\d+\/\d+|[0-9a-fA-F.:]+\/\d+)\s+(?P<mac_addr>[0-9a-fA-F.]+)$")

        for line in out.splitlines():
            line = line.strip()
            # Address-resolution data for router lisp 0 instance-id 1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = lisp_ar_dict.setdefault('lisp_id', {}) \
                    .setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}) \
                    .setdefault(instance_id, {})
                continue

            # 0    192.168.1.1/32       aabb.cc00.ca00
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                eid_address = groups['eid_address']
                mac_address = groups['mac_addr']
                inst_id = groups['l2_inst_id']
                entries_dict = instance_id_dict.setdefault('entries', {}) \
                    .setdefault(eid_address, {})
                entries_dict.update({'mac_address': mac_address})
                entries_dict.update({'inst_id': inst_id})
        return lisp_ar_dict


class ShowLispEthernetPublisher(ShowLispPublisherSuperParser, ShowLispPublisherSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ethernet publisher
        * show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher
        * show lisp instance-id {instance_id} ethernet publisher
        * show lisp eid-table vlan {vlan} ethernet publisher
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ethernet publisher',
        'show lisp locator-table {vrf} instance-id {instance_id} ethernet publisher',
        'show lisp instance-id {instance_id} ethernet publisher',
        'show lisp eid-table vlan {vlan} ethernet publisher',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, vlan=None):

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
            else:
                output = self.device.execute(self.cli_command[3].format(vlan=vlan))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispEthernetSubscriber(ShowLispSubscriberSuperParser, ShowLispSubscriberSchema):
    """ Parser for:
        * show lisp {lisp_id} instance-id {instance_id} ethernet subscriber
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber
        * show lisp instance-id {instance_id} ethernet subscriber
        * show lisp eid-table vlan {vlan} ethernet subscriber
    """

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ethernet subscriber',
        'show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscriber',
        'show lisp instance-id {instance_id} ethernet subscriber',
        'show lisp eid-table vlan {vlan} ethernet subscriber',
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, locator_table=None, vlan=None):

        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[0].\
                                             format(lisp_id=lisp_id, instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                             format(locator_table=locator_table, instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id))
            else:
                output = self.device.execute(self.cli_command[3].format(vlan=vlan))

        return super().cli(output=output, lisp_id=lisp_id, instance_id=instance_id)


class ShowLispEthernetSubscription(ShowLispSubscriptionSuperParser, ShowLispSubscriptionSchema):
    ''' Show Command ethernet subscription
        show lisp instance-id {instance_id} ethernet subscription
        show lisp {lisp_id} instance-id {instance_id} ethernet subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscription
        show lisp eid-table vlan {eid_table} ethernet subscription
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ethernet subscription',
        'show lisp {lisp_id} instance-id {instance_id} ethernet subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} ethernet subscription',
        'show lisp eid-table vlan {vlan} ethernet subscription'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vlan=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].\
                                                format(lisp_id=lisp_id, \
                                                   instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id))
            elif locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].\
                                                format(locator_table=locator_table, \
                                                   instance_id=instance_id))
            elif vlan:
                output = self.device.execute(self.cli_command[3].\
                                                format(vlan=vlan))

        return super().cli(output=output)



class ShowLispAFSubscriptionPrefix(ShowLispSubscriptionPrefixSuperParser, ShowLispSubscriptionPrefixSchema):
    ''' Show Command Ipv4 Subscription
        show lisp instance-id {instance_id} {address_family} subscription {prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} {address_family} subscription {prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} {address_family} subscription {prefix}/detail
        show lisp eid-table {eid_table} {address_family} subscription {prefix}/detail
        show lisp eid-table vrf {eid_table} {address_family} subscription {prefix}/detail
    '''

    cli_command = [
        'show lisp instance-id {instance_id} {address_family} subscription {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} {address_family} subscription {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} subscription {eid_prefix}',
        'show lisp eid-table {eid_table} {address_family} subscription {eid_prefix}',
        'show lisp eid-table vrf {vrf} {address_family} subscription {eid_prefix}',
        'show lisp instance-id {instance_id} {address_family} subscription detail',
        'show lisp {lisp_id} instance-id {instance_id} {address_family} subscription detail',
        'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} subscription detail',
        'show lisp eid-table {eid_table} {address_family} subscription detail',
        'show lisp eid-table vrf {vrf} {address_family} subscription detail'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, address_family='ipv4', eid=None, eid_prefix=None):
        if output is None:
            if lisp_id and instance_id and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[1].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix, address_family= address_family))
            elif instance_id and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id, eid_prefix=eid_prefix, address_family= address_family))
            elif locator_table and instance_id and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[2].\
                                                format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix, address_family=address_family))
            elif eid_table and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[3].\
                                                format(eid_table=eid_table, eid_prefix=eid_prefix, address_family=address_family))
            elif vrf and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[4].\
                                                format(vrf=vrf, eid_prefix=eid_prefix, address_family=address_family))
            elif lisp_id and instance_id and address_family:
                output = self.device.execute(self.cli_command[6].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family))
            elif instance_id and address_family:
                output = self.device.execute(self.cli_command[5].\
                                                format(instance_id=instance_id, address_family=address_family))
            elif locator_table and instance_id and address_family:
                output = self.device.execute(self.cli_command[7].\
                                                format(locator_table=locator_table, instance_id=instance_id, address_family=address_family))
            elif eid_table and address_family:
                output = self.device.execute(self.cli_command[8].\
                                                format(eid_table=eid_table, address_family=address_family))
            else:
                output = self.device.execute(self.cli_command[9].\
                                                format(vrf=vrf, address_family=address_family))

        return super().cli(output=output)


# ==========================================
# Parser for:
#  * 'show lisp instance-id {instance_id} ethernet publication'
#  * 'show lisp {lisp_id} instance-id {instance_id} ethernet publication'
#  * 'show lisp locator-table {vrf} instance-id {instance-id} ethernet publication'
# ==========================================
class ShowLispEthernetPublication(ShowLispIpv4PublicationSchema):
    """Parser for show lisp ethernet publication"""
    cli_command = ['show lisp instance-id {instance_id} ethernet publication',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet publication',
                   'show lisp locator-table {vrf} instance-id {instance_id} ethernet publication']

    def cli(self, lisp_id=None, instance_id=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id)
            elif vrf and instance_id:
                cmd = self.cli_command[2].format(vrf=vrf, instance_id=instance_id)
            else:
                cmd = self.cli_command[0].format(instance_id=instance_id)
            output = self.device.execute(cmd)
        ret_dict = {}
        # Output for router lisp 0 instance-id 101
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)\s+"
                        r"instance-id\s+(?P<instance_id>\d+)$")

        # Entries total 2
        p2 = re.compile(r"^Entries\s+total\s+(?P<total_entries>\d+)$")

        # 100.100.100.100 15:52:51    aabb.cc00.c901/48        11.11.11.11     -
        # 100:100:100:100:: 15:52:51    aabb.cc00.c901/48        11:11:11:11::   -
        p3 = re.compile(r"^(?P<publisher_ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                        r"(?P<last_published>\S+)\s+(?P<eid_prefix>([a-fA-F\d]{4}\.){2}"
                        r"[a-fA-F\d]{4}\/\d{1,3})\s+(?P<rloc>(\d{1,3}\.\d{1,3}\.\d{1,3}\."
                        r"\d{1,3})|([a-fA-F\d\:]+))\s+(?P<encap_iid>\S+)$")

        # New format (Locators are no longer displayed in the output)

        # aabb.cc00.c901/48   15:52:51   100.100.100.100   -
        p4 = re.compile(r"^(?P<eid_prefix>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,3})\s+"
                        r"(?P<last_published>\S+)\s+(?P<publisher_ip>(\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<encap_iid>\S+)$")
        count = 0

        for line in output.splitlines():
            line = line.strip()
            count += 1
            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                    .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                    .setdefault(instance_id,{})
            if not m and count < 2 and lisp_id != "all":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue

            # Entries total 2
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                entries = int(groups['total_entries'])
                instance_id_dict.update({'total_entries':entries})
                continue

            # 44.44.44.44     1d21h       192.168.1.71/32          11.11.11.11     -
            # 100:100:100:100:: 15:52:51    aabb.cc00.c901/48        11.11.11.11     -
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

            # aabb.cc00.c901/48   15:52:51   100.100.100.100   -
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


class ShowLispEthernetPublicationPrefix(ShowLispPublicationPrefixSchema):
    """
    Parser for
    *show lisp instance-id {instance_id} ethernet publication {eid_prefix}
    *show lisp {lisp_id} instance-id {instance_id} ethernet publication {eid_prefix}
    *show lisp eid-table vlan {vlan} ethernet publication {eid_prefix}
    *show lisp locator-table {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
    *show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet publication {eid_prefix}
    """
    cli_command = ['show lisp instance-id {instance_id} ethernet publication {eid_prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet publication {eid_prefix}',
                   #'show lisp eid-table vlan {vlan} ethernet publication {eid_prefix}',
                   'show lisp locator-table {vrf} instance-id {instance_id} ethernet publication {eid_prefix}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet publication {eid_prefix}']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, vlan=None, eid_prefix=None, vrf=None, output=None):
        ret_dict = {}
        if output is None:
            if lisp_id and instance_id and eid_prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix))
            elif vrf and instance_id and eid_prefix:
                if "vrf" in self.cli_command:
                    output = self.device.execute(self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
                else:
                    output = self.device.execute(self.cli_command[3].format(vrf=vrf, instance_id=instance_id, eid_prefix=eid_prefix))
            else:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, eid_prefix=eid_prefix))
            #else:
            #    output = self.device.execute(self.cli_command[2].format(vlan=vlan,eid_prefix=eid_prefix))
        else:
            output = output
        #Output for router lisp 0 instance-id 4100
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        #EID-prefix: aabb.cc00.c901/48
        p2 = re.compile(r"^EID-prefix:\s+(?P<eid_prefixes>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,3})$")

        #First published:      03:05:56
        p3 = re.compile(r"^First\s+published:\s+(?P<first_published>\S+)$")

        #Last published:      03:05:56
        p4 = re.compile(r"^Last\s+published:\s+(?P<last_published>\S+)$")

        #State:                complete
        p5 = re.compile(r"^State:\s+(?P<state>\S+)$")

        #Exported to:          map-cache
        p6 = re.compile(r"^Exported\s+to:\s+(?P<exported_to>\S+)$")

        #Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
        #Publisher 100:100:100:100::.4342, last published 16:02:47, TTL never
        p7 = re.compile(r"^Publisher\s+(?P<publishers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(:|\.)"
                        r"(?P<port>\d+),\s+last\s+published\s+(?P<last_published>\S+),\s+"
                        r"TTL\s+(?P<ttl>\S+)")

        #publisher epoch 1, entry epoch 1
        p8 = re.compile(r"^publisher\s+epoch\s+(?P<publisher_epoch>\d+),"
                        r"\s+entry\s+epoch\s+(?P<entry_epoch>\d+)")

        #entry-state complete
        p9 = re.compile(r"^entry-state\s+(?P<entry_state>\S+)")

        #routing table tag 101
        p10 = re.compile(r"^routing\s+table\s+tag\s+(?P<routing_tag>\d+)")

        #xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
        p11 = re.compile(r"^xTR-ID\s+(?P<xtr_id>\S+)")

        #site-ID unspecified
        p12 = re.compile(r"^site-ID\s+(?P<site_id>\S+)")

        #Domain-ID unset
        p13 = re.compile(r"^Domain-ID\s+(?P<domain_id>\S+)")

        #Multihoming-ID unspecified
        p14 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)")

        #11.11.11.11   10/10   up        -                   1/1       44
        #11:11:11:11:: 10/10   up        -                   1/1       44
        p15 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)"
                         r"|\s+(?P<domain_id>\d+)\/(?P<multihoming_id>\d+)\s+(?P<metric>\d+)")

        #  Instance ID:                              4100
        p16 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\d+)")
        count = 0

        #Publisher 100.100.100.100:4342
        #Publisher 100:100:100:100::.4342
        p17 = re.compile(r"^Publisher\s+(?P<publishers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|"
                         r"([a-fA-F\d\:]+))(:|\.)(?P<port>\d+)")

        #  last published 16:02:47, TTL never
        p18 = re.compile(r"^last\s+published\s+(?P<last_published>\S+),\s+"
                        r"TTL\s+(?P<ttl>\S+)")

        for line in output.splitlines():
            line = line.strip()
            count += 1
            #Output for router lisp 0 instance-id 4100
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                prefix_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                                 .setdefault(lisp_id,{})
                instance_id_dict = ret_dict.setdefault('instance_id',{})\
                                                     .setdefault(prefix_id,{})
                continue
            if not m and count < 2 and lisp_id != "all":
                if lisp_id and instance_id:
                    lisp_id = int(lisp_id)
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue
                if not lisp_id and instance_id:
                    lisp_id = 0
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                        .setdefault(lisp_id,{})
                    instance_id = int(instance_id)
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                        .setdefault(instance_id,{})
                    count += 1
                    continue

            #EID-prefix: 192.168.1.71/3
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                eid_prefixes = groups['eid_prefixes']
                eid_prefix = instance_id_dict.setdefault('eid_prefixes',{})\
                    .setdefault(eid_prefixes,{})
                continue

            #First published:      03:05:56
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                first_published = groups['first_published']
                eid_prefix.update({'first_published':first_published})
                continue

            #Last published:      03:05:56
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                eid_prefix.update({'last_published':last_published})
                continue

            #State:                complete
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                eid_prefix.update({'state':state})
                continue

            #Exported to:          map-cache
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                exported_to = groups['exported_to']
                exported_list = eid_prefix.setdefault('exported_to',[])
                exported_list.append(exported_to)
                eid_prefix.update({'exported_to':exported_list})
                continue

            #Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
            #Publisher 100:100:100:100::.4342, last published 16:02:47, TTL never
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                last_published = groups['last_published']
                ttl = groups['ttl']
                publishers = "{}:{}".format(publishers,port)
                publish_dict = eid_prefix.setdefault('publishers',{})\
                    .setdefault(publishers,{})
                publish_dict.update({'port':port})
                publish_dict.update({'last_published':last_published})
                publish_dict.update({'ttl':ttl})
                continue

            #publisher epoch 0,entry epoch 0
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                publisher_epoch = int(groups['publisher_epoch'])
                entry_epoch = int(groups['entry_epoch'])
                publish_dict.update({'publisher_epoch':publisher_epoch})
                publish_dict.update({'entry_epoch':entry_epoch})
                continue

            #entry-state complete
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                entry_state = groups['entry_state']
                publish_dict.update({'entry_state':entry_state})
                continue

            #routing table tag 101
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                routing_tag = int(groups['routing_tag'])
                publish_dict.update({'routing_tag':routing_tag})
                continue

            #xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                publish_dict.update({'xtr_id':xtr_id})
                continue

            #site-ID unspecified
            m=p12.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                publish_dict.update({'site_id':site_id})
                continue

            #Domain-ID unset
            m=p13.match(line)
            if m:
                groups = m.groupdict()
                domain_id = (groups['domain_id'])
                publish_dict.update({'domain_id':domain_id})
                continue

            #Multihoming-ID unspecified
            m=p14.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = (groups['multihoming_id'])
                publish_dict.update({'multihoming_id':multihoming_id})
                continue

            #22.22.22.22   10/10   up        -                   1/1       44
            #11:11:11:11:: 10/10   up        -                   1/1       44
            m=p15.match(line)
            if m:
                groups = m.groupdict()
                locators = (groups['locators'])
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                state = groups['state']
                encap_iid = groups['encap_iid']
                locator_dict =  publish_dict.setdefault('locators',{})\
                                            .setdefault(locators,{})
                locator_dict.update({'priority':priority})
                locator_dict.update({'weight':weight})
                locator_dict.update({'state':state})
                locator_dict.update({'encap_iid':encap_iid})
                if groups['metric'] != None:
                    metric = int(groups['metric'])
                    locator_dict.update({'metric':metric})
                if groups['domain_id'] != None:
                    domain_id = int(groups['domain_id'])
                    locator_dict.update({'domain_id':domain_id})
                if groups['multihoming_id'] != None:
                    multihoming_id = int(groups['multihoming_id'])
                    locator_dict.update({'multihoming_id':multihoming_id})
                continue

            #Publisher 100.100.100.100:4342
            #Publisher 100:100:100:100::.4342
            m=p17.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])

                if publishers.count('.') > 1:
                    publishers = "{}:{}".format(publishers, port)
                else:
                    publishers = "{}.{}".format(publishers, port)

                publish_dict = eid_prefix.setdefault('publishers',{})\
                    .setdefault(publishers,{})
                publish_dict.update({'port':port})
                continue

            # last published 16:02:47, TTL never
            m=p18.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                ttl = groups['ttl']
                publish_dict.update({'last_published':last_published})
                publish_dict.update({'ttl':ttl})
                continue

        return ret_dict


class ShowLispARDetailSchema(MetaParser):

    schema = {
        'lisp_id': {
        int: {
            'instance_id': {
                int: {
                    'site': str,
                    'host_address': {
                        str: { # ipv4 or ipv6
                            'hardware_address': str, # MAC address
                            'first_registered': str,
                            'last_registered': str,
                            'registration_errors': {
                                'authentication_failures': int
                            },
                            'etr': {
                                str: {
                                    'port': int,
                                    'last_registered': str,
                                    'ttl': str,
                                    'xtr_id': str,
                                    'site_id': str,
                                    'registered_addr': str,
                                    'l3_instance_id': int
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


'''Parser for show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {prefix | detail}'''
class ShowLispARDetailParser(ShowLispARDetailSchema):
    """ Parser for:
        * show lisp instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp eid-table vlan {vlan} ethernet server address-resolution {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution {eid}
        * show lisp instance-id {instance_id} ethernet server address-resolution detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp eid-table vlan {vlan} ethernet server address-resolution detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution detail
        * show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution detail"""

    cli_command = ['show lisp instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp eid-table vlan {vlan} ethernet server address-resolution {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server address-resolution detail',
                   'show lisp eid-table vlan {vlan} ethernet server address-resolution detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server address-resolution detail',
                   'show lisp locator-table vrf {vrf} instance-id {instance_id} ethernet server address-resolution detail']

    def cli(self, lisp_id=None, instance_id=None, vlan=None, vrf=None, eid=None, locator_table=None, output=None):

        ret_dict = {}
        if output is None:
            if locator_table and instance_id and eid:
                cmd = self.cli_command[3].format(locator_table=locator_table, instance_id=instance_id, eid=eid)
            elif vrf and instance_id and eid:
                cmd = self.cli_command[4].format(vrf=vrf, instance_id=instance_id, eid=eid)
            elif lisp_id and instance_id and eid:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, eid=eid)
            elif instance_id and eid:
                cmd = self.cli_command[0].format(instance_id=instance_id, eid=eid)
            elif vlan and eid:
                cmd = self.cli_command[2].format(vlan=vlan, eid=eid)
            elif lisp_id and instance_id:
                cmd = self.cli_command[5].format(instance_id=instance_id, lisp_id=lisp_id)
            elif locator_table and instance_id:
                cmd = self.cli_command[7].format(instance_id=instance_id, locator_table=locator_table)
            elif vrf and instance_id:
                cmd = self.cli_command[8].format(instance_id=instance_id, vrf=vrf)
            else:
                cmd = self.cli_command[6].format(vlan=vlan)
            output = self.device.execute(cmd)

        #Address-resolution data for router lisp 0 instance-id 101
        p1 = re.compile(r"^Address-resolution\s+data\s+for\s+router\s+"
                        r"lisp\s+(?P<lisp_id>\d+)\s+instance-id\s+(?P<instance_id>\d+)$")

        #Site name: Shire
        p2 = re.compile(r"^Site\s+name:\s+(?P<site>\S+)$")

        #Host Address:         192.168.1.71/32
        p3 = re.compile(r"^Host\s+Address:\s+(?P<host_address>\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}|[a-fA-F\d\:]+\/\d{1,3})$")

        #Hardware Address:     aabb.cc00.c901
        p4 = re.compile(r"^Hardware\s+Address:\s+(?P<hardware_address>"
                        r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$")

        #First registered:     1w0d
        p5 = re.compile(r"^First\s+registered:\s+(?P<first_registered>\S+)$")

        #Last registered:      1w0d
        p6 = re.compile(r"^Last\s+registered:\s+(?P<last_registered>\S+)$")

        #Authentication failures:   0
        p7 = re.compile(r"^\s+Authentication\s+failures:\s+(?P<authentication_failures>\d+)$")

        #ETR 11.11.11.11:28966
        #ETR 11:11:11:11::.28966
        p8 = re.compile(r"^\s+ETR\s+(?P<etr>((\d{1,3}\.\d{1,3}\."
                        r"\d{1,3}\.\d{1,3}:)|([a-fA-F\d\:]+\.))(?P<port>\d+))$")

        #Last registered:      1w0d
        p9 = re.compile(r"^\s+Last\s+registered:\s+(?P<etr_last_registered>\S+)$")

        #TTL:                   1d00h
        p10 = re.compile(r"^\s+TTL:\s+(?P<ttl>\S+)$")

        #xTR-ID:                0xC25C9262-0xC9865A33-0x008E8A37-0x9206AC33
        p11 = re.compile(r"^\s+xTR-ID:\s+(?P<xtr_id>\S+)$")

        #Site-ID:               unspecified
        p12 = re.compile(r"^\s+Site-ID:\s+(?P<site_id>\S+)$")

        #Registered addr:       aabb.cc00.c901
        p13 = re.compile(r"^\s+Registered\s+addr:\s+(?P<registered_addr>"
                         r"([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})$")

        #L3 Instance ID:        4100
        p14 = re.compile(r"^\s+L3\s+Instance\s+ID:\s+(?P<l3_instance_id>\d+)$")

        for line in output.splitlines():
            #Address-resolution data for router lisp 0 instance-id 101
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                prefix_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(prefix_id,{})
                continue

            #Site name: Shire
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                site = groups['site']
                instance_id_dict.update({'site':site})
                continue

            #Site name: Shire
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                site = groups['site']
                instance_id_dict.update({'site':site})
                continue

            #Host Address:         192.168.1.71/32
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                host_address = groups['host_address']
                host_address_dict = instance_id_dict.setdefault('host_address',{})\
                                                    .setdefault(host_address,{})
                continue

            #Hardware Address:     aabb.cc00.c901
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                hardware_address = groups['hardware_address']
                host_address_dict.update({'hardware_address':hardware_address})
                continue

            #First registered:     1w0d
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                first_registered = groups['first_registered']
                host_address_dict.update({'first_registered':first_registered})
                continue

            #Last registered:      1w0d
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                last_registered = groups['last_registered']
                host_address_dict.update({'last_registered':last_registered})
                continue

            #Authentication failures:   0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                authentication_failures = int(groups['authentication_failures'])
                authentication_dict = host_address_dict.setdefault('registration_errors',{})\
                                                       .setdefault('authentication_failures',authentication_failures)
                continue

            #ETR 11.11.11.11:28966
            #ETR 11:11:11:11::.28966
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                etr = groups['etr']
                port = int(groups['port'])
                etr_dict = host_address_dict.setdefault('etr',{})\
                                            .setdefault(etr,{})
                etr_dict.update({'port':port})
                continue
            #Last registered:      1w0d
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                etr_last_registered = groups['etr_last_registered']
                etr_dict.update({'last_registered':etr_last_registered})
                continue

            #TTL:                   1d00h
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                ttl = groups['ttl']
                etr_dict.update({'ttl':ttl})
                continue

            #xTR-ID:                0xC25C9262-0xC9865A33-0x008E8A37-0x9206AC33
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                etr_dict.update({'xtr_id':xtr_id})
                continue

            #Site-ID:               unspecified
            m=p12.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                etr_dict.update({'site_id':site_id})
                continue

            #Registered addr:       aabb.cc00.c901
            m=p13.match(line)
            if m:
                groups = m.groupdict()
                registered_addr = groups['registered_addr']
                etr_dict.update({'registered_addr':registered_addr})
                continue

            #L3 Instance ID:        4100
            m=p14.match(line)
            if m:
                groups = m.groupdict()
                l3_instance_id = int(groups['l3_instance_id'])
                etr_dict.update({'l3_instance_id':l3_instance_id})
        return ret_dict




# ==========================================
# Parser for: show lisp {lisp_id} instance-id
# {id} {address-family} database {prefix}
# ==========================================
class ShowLispDatabaseEidSchema(MetaParser):
    schema = {
        'lisp_id': {
            int: { # lisp id
                'instance_id': {
                    int: { # instance id
                        'address_family': str,
                        'eid_table': str,
                        'lsb': str,
                        'entries_total': int,
                        'no_route_entries': int,
                        'inactive_entries': int,
                        Optional('do_not_register_entries'): int,
                        'all_no_route': bool,
                        'eid_prefix': str,
                        'eid_info': str,
                        Optional('route_map'): str,
                        'domain_id': str,
                        Optional('metric'): str,
                        Optional('srvc_ins_type'): str,
                        Optional('srvc_ins_id'): int,
                        Optional('extranet_iid'): int,
                        Optional('sgt'): int,
                        Optional('locators'): {
                            str: { # locator address
                                Optional('priority'): int,
                                Optional('weight'): int,
                                Optional('source'): str,
                                Optional('state'): str,
                                'config_missing': bool,
                                Optional('affinity_id_x'): int,
                                Optional('affinity_id_y'): int
                            }
                        },
                        Optional('map_servers'): {
                            str: { # map-server address
                                'uptime': str,
                                'ack': str,
                                'domain_id': str
                            }
                        }
                    }
                }
            }
        }
    }


class ShowLispDatabaseEid(ShowLispDatabaseEidSchema):
    cli_command = ['show lisp instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp locator-table {rloc_vrf} instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp locator-table vrf {rloc_vrf} instance-id {instance_id} {address_family} database {prefix}',
                   'show lisp eid-table {eid_vrf} {address_family} database {prefix}',
                   'show lisp eid-table vrf {eid_vrf} {address_family} database {prefix}',
                   'show lisp eid-table vlan {vlan_id} ethernet database {prefix}']

    def cli(self, lisp_id=None, instance_id=None, address_family=None, prefix=None, rloc_vrf=None, eid_vrf=None, vlan_id=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                cmd = self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family, prefix=prefix)
            elif rloc_vrf and instance_id:
                cmd = self.cli_command[2].format(rloc_vrf=rloc_vrf, instance_id=instance_id, address_family=address_family, prefix=prefix)
            elif eid_vrf:
                cmd = self.cli_command[4].format(eid_vrf=eid_vrf, address_family=address_family, prefix=prefix)
            elif vlan_id:
                cmd = self.cli_command[6].format(vlan_id=vlan_id, prefix=prefix)
            else:
                cmd = self.cli_command[0].format(instance_id=instance_id, address_family=address_family, prefix=prefix)
            output = self.device.execute(cmd)

        lisp_id_dict = {}

        #LISP ETR IPv4 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x0
        #LISP ETR MAC Mapping Database for EID-table Vlan 111 (IID 102), LSBs: 0x1
        #LISP ETR IPv4 Mapping Database for LISP 1 EID-table vrf red (IID 101), LSBs: 0x0
        #LISP ETR MAC Mapping Database for LISP 1 EID-table Vlan 111 (IID 102), LSBs: 0x1
        #LISP ETR IPv4 Mapping Database for LISP 0 EID-table default (IID 4098), LSBs: 0x1
        p1 = re.compile(r"^LISP\sETR\s(?P<address_family>[A-Za-z0-9]+)\sMapping\sDatabase\sfor"
                        r"(\sLISP\s)?(?P<lisp_id>\d)?\sEID-table\s(?P<eid_table>\S+"
                        r"|(vrf\s\w+)|(Vlan\s\d+))\s\(IID\s(?P<instance_id>\d+)\),\sLSBs:\s"
                        r"(?P<lsb>0x[a-fA-F\d]+)$")

        #Entries total 2, no-route 2, inactive 0, do-not-register 0
        # Entries total 1, no-route 0, inactive 0
        p2 = re.compile(r"^Entries total\s(?P<entries_total>\d+),\sno-route\s(?P<no_route_entries>\d+),\sinactive\s(?P<inactive_entries>\d+)(,\sdo-not-register\s(?P<do_not_register_entries>\d+))?$")

        #*** ALL ACTIVE LOCAL EID PREFIXES HAVE NO ROUTE ***
        #***    REPORTING LOCAL RLOCS AS UNREACHABLE     ***
        p3 = re.compile(r"^(?P<all_no_route>\*\*\* ALL ACTIVE LOCAL EID PREFIXES HAVE NO ROUTE \*\*\*)")

        #192.168.1.0/24, locator-set RLOC *** NO ROUTE TO EID PREFIX ***
        #00aa.00bb.00cc/48, locator-set RLOC
        p4 = re.compile(r"^(?P<eid_prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})|([a-fA-F\d\:]+\/\d{1,3})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2})),\s(?P<eid_info>.+)$")

        #  Uptime: 00:00:56, Last-change: 00:00:56
        # Line not parsed, not interesting data for now

        #  Route-map: match-metric
        p5 = re.compile(r"^Route-map:\s(?P<route_map>.+)$")

        #  Domain-ID: unset
        p6 = re.compile(r"^Domain-ID:\s(?P<domain_id>.+)$")

        #  Metric: -
        p7 = re.compile(r"^Metric:\s(?P<metric>.+)$")

        #  Service-Insertion: N/A (0)
        p8 = re.compile(r"^Service-Insertion:\s(?P<srvc_ins_type>[^\s]+)\s\((?P<srvc_ins_id>\d+)\)$")

        #  Extranet-IID: 4100
        p9 = re.compile(r"^Extranet-IID:\s(?P<extranet_iid>\d+)$")

        # SGT: 10
        p10 = re.compile(r"^SGT:\s(?P<sgt>\d+)$")

        #  Locator       Pri/Wgt  Source     State
        #  100.31.31.31    1/1    cfg-addr   site-self, unreachable
        #  100.44.44.44 *** missing in configuration ***
        p11 = re.compile(r"^(?P<locator>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<source>[\w-]+)\s+(?P<state>.+)$")
        p12 = re.compile(r"^(?P<locator>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s(?P<config_missing>\*\*\* missing in configuration \*\*\*)$")

        # Affinity-id: 20 , 20
        p12_1 = re.compile(r'^Affinity-id:\s+(?P<affinity_id_x>\d+)(\s+,\s+(?P<affinity_id_y>\d+))?$')

        #  Map-server       Uptime         ACK  Domain-ID
        #  100.31.31.31     00:00:21       No   0
        #  100.31.31.31     never          No   0
        p13 = re.compile(r"^(?P<map_server>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<uptime>\S+)\s+(?P<ack>Yes|No)\s+(?P<domain_id>\w+)")

        for line in output.splitlines():
            line = line.strip()

            #LISP ETR IPv4 Mapping Database for EID-table vrf red (IID 101), LSBs: 0x0
            #LISP ETR MAC Mapping Database for EID-table Vlan 111 (IID 102), LSBs: 0x1
            #LISP ETR IPv4 Mapping Database for LISP 1 EID-table vrf red (IID 101), LSBs: 0x0
            #LISP ETR MAC Mapping Database for LISP 1 EID-table Vlan 111 (IID 102), LSBs: 0x1
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                if 'lisp_id' in groups and groups['lisp_id'] is not None:
                    lisp_id = int(groups['lisp_id'])
                else:
                    lisp_id = 0

                instance_id = int(groups['instance_id'])
                instance_id_dict = lisp_id_dict.setdefault('lisp_id', {}) \
                                                .setdefault(lisp_id, {}) \
                                                .setdefault('instance_id', {}) \
                                                .setdefault(instance_id, {})

                instance_id_dict['address_family'] = groups['address_family']
                instance_id_dict['eid_table'] = groups['eid_table']
                instance_id_dict['lsb'] = groups['lsb']
                instance_id_dict['all_no_route'] = False # default value
                continue

            #Entries total 2, no-route 2, inactive 0, do-not-register 0
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['entries_total'] = int(groups['entries_total'])
                instance_id_dict['no_route_entries'] = int(groups['no_route_entries'])
                instance_id_dict['inactive_entries'] = int(groups['inactive_entries'])
                if groups['do_not_register_entries']:
                    instance_id_dict['do_not_register_entries'] = int(groups['do_not_register_entries'])
                continue

            #*** ALL ACTIVE LOCAL EID PREFIXES HAVE NO ROUTE ***
            #***    REPORTING LOCAL RLOCS AS UNREACHABLE     ***
            m=p3.match(line)
            if m:
                instance_id_dict['all_no_route'] = True
                continue

            #192.168.1.0/24, locator-set RLOC *** NO ROUTE TO EID PREFIX ***
            #00aa.00bb.00cc/48, locator-set RLOC
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['eid_prefix'] = groups['eid_prefix']
                instance_id_dict['eid_info'] = groups['eid_info']
                continue

            #  Route-map: match-metric
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['route_map'] = groups['route_map']
                continue

            #  Domain-ID: unset
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['domain_id'] = groups['domain_id']
                continue

            #  Metric: -
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['metric'] = groups['metric']
                continue

            #  Service-Insertion: N/A (0)
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['srvc_ins_type'] = groups['srvc_ins_type']
                instance_id_dict['srvc_ins_id'] = int(groups['srvc_ins_id'])
                continue

            #  Extranet-IID: 4100
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['extranet_iid'] = int(groups['extranet_iid'])
                continue

            # SGT: 10
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict['sgt'] = int(groups['sgt'])
                continue

            #  Locator       Pri/Wgt  Source     State
            #  100.31.31.31    1/1    cfg-addr   site-self, unreachable
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                locator = groups['locator']
                locator_dict = instance_id_dict.setdefault('locators', {}) \
                                               .setdefault(locator, {})

                locator_dict['priority'] = int(groups['priority'])
                locator_dict['weight'] = int(groups['weight'])
                locator_dict['source'] = groups['source']
                locator_dict['state'] = groups['state']
                locator_dict['config_missing'] = False
                continue

            #  100.44.44.44 *** missing in configuration ***
            m=p12.match(line)
            if m:
                groups = m.groupdict()
                locator = groups['locator']
                locator_dict = instance_id_dict.setdefault('locators', {}) \
                                               .setdefault(locator, {})
                locator_dict['config_missing'] = True
                continue

            # Affinity-id: 20 , 20
            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                if group['affinity_id_y']:
                    locator_dict.update({'affinity_id_y':int(group['affinity_id_y'])})
                locator_dict.update({'affinity_id_x':int(group['affinity_id_x'])})
                continue

            #  Map-server       Uptime         ACK  Domain-ID
            #  100.31.31.31     00:00:21       No   0
            #  100.31.31.31     never          No   0
            m=p13.match(line)
            if m:
                groups = m.groupdict()
                map_server = groups['map_server']
                map_server_dict = instance_id_dict.setdefault('map_servers', {}) \
                                                  .setdefault(map_server, {})

                map_server_dict['uptime'] = groups['uptime']
                map_server_dict['ack'] = groups['ack']
                map_server_dict['domain_id'] = groups['domain_id']
                continue

        return lisp_id_dict


class ShowLispEthernetMapCachePrefixSchema(MetaParser):

    ''' Schema for
      * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
      * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
      * show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}
      * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    '''

    Schema = {
        "lisp_id": {
            int: {
                "instance_id": {
                    int: {
                        "eid_table": str,
                        "entries": int,
                        "eid_prefix": {
                            "str": {
                                "uptime": str,
                                "expiry_time": str,
                                "via": str,
                                "map_reply_state": str,
                                Optional("prefix_location"): str,
                                "source_type": str,
                                "last_modified": str,
                                "source_ip": str,
                                "prefix_state": str,
                                "encap": str,
                                "rloc_set": {
                                    "str": {
                                        "uptime": str,
                                        "rloc_state": str,
                                        "priority": int,
                                        "weight": int,
                                        "encap_iid": str,
                                        "last_state_change": {
                                            "time": str,
                                            "count": int
                                        },
                                        "last_route_reach_change": {
                                            "time": str,
                                            "count": int,
                                        },
                                        "last_pri_weight_change": {
                                            "priority": str,
                                            "weight": str,
                                        },
                                        "rloc_probe_sent": {
                                            "time": str,
                                            "rtt": int,
                                            "rtt_unit": str,
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowLispEthernetMapCachePrefix(ShowLispEthernetMapCachePrefixSchema):
    ''' Parser for
        * show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}
        * show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}
        * show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}
    '''

    cli_command = [
        'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache {eid_prefix}',
        'show lisp instance-id {instance_id} ethernet map-cache {eid_prefix}',
        'show lisp eid-table vlan {vlan_id} ethernet map-cache {eid_prefix}',
        'show lisp locator-table {locator_table} ethernet map-cache {eid_prefix}'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, eid_prefix=None, vlan_id=None,
            locator_table=None):

        if output is None:
            if lisp_id and instance_id and eid_prefix:
                cmd = self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id,\
                                                 eid_prefix=eid_prefix)
            elif instance_id and eid_prefix:
                cmd = self.cli_command[1].format(instance_id=instance_id, eid_prefix=eid_prefix)
            elif vlan_id and eid_prefix:
                cmd = self.cli_command[2].format(vlan_id=vlan_id, eid_prefix=eid_prefix)
            else:
                cmd = self.cli_command[3].format(locator_table=locator_table, eid_prefix=eid_prefix)

            output = self.device.execute(cmd)


        # Initialize dictionary
        ret_dict = {}

        # To handle lisp_id
        if not lisp_id or isinstance(lisp_id, str):
            lisp_id = 0
        elif lisp_id.isdigit():
            lisp_id = int(lisp_id)

        # To get instance_id from device
        if not instance_id:
            self.device.sendline('sh lisp eid-table vrf red ipv4 | i Instance')
            out = self.device.expect(
                [r'Instance ID:\s+\S+'],
                timeout=2).match_output
            p0 = re.compile('^Instance ID:\s+(?P<instance_id>\d+)$')
            group = p0.match(out)
            instance_id = int(group['instance_id'])
        else:
            if instance_id.isdigit():
                instance_id = int(instance_id)

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 193
        # Output for router lisp 2 instance-id 101
        p1 = re.compile(r'^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>(\d+))'
                        r'(?: +instance-id +(?P<instance_id>(\d+)))?$')

        # LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
        # LISP MAC Mapping Cache for LISP 0 EID-table Vlan 101 (IID 1031), 1 entries
        p2 = re.compile(r'^LISP\sMAC\sMapping\sCache\sfor\s(LISP\s+\d+\s+)?EID-table\s'
                        r'(?P<eid_table>.*)\s\(IID\s(?P<instance_id>\d+)\),'
                        r'\s(?P<entries>\d+)\sentries$')

        # 0017.0100.0001/48, uptime: 01:09:06, expires: 22:50:53, via map-reply, complete, local-to-site
	# aabb.cc00.ca00/48, uptime: 00:00:08, expires: 23:59:51, via map-reply, complete
        p3 = re.compile(r'^(?P<eid_prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})|([a-fA-F\d\:]+\/\d{1,3})|'
                        r'(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2})),\suptime:\s(?P<uptime>\S+),\sexpires:\s(?P<expiry_time>\S+),'
                        r'\s+via\s(?P<via>\S+),\s(?P<map_reply_state>\S+)(,\s(?P<prefix_location>\S+))?$')

        # Sources: map-reply
        p4 = re.compile(r'^Sources:\s(?P<source_type>\S+)$')

        # State: complete, last modified: 01:09:06, map-source: 1.1.1.10
        p5 = re.compile(r'^State:\s(?P<state>\S+),\slast\smodified:\s(?P<last_modified>\S+)\smap-source:\s(?P<source_ip>.+)$')

        # Active, Packets out: 139(0 bytes), counters are not accurate (~ 00:00:01 ago)
        p6 = re.compile(r'^(?P<prefix_state>\S+),\sPackets out:\s(?P<packets_out>\d+).+$')

        # Encapsulating dynamic-EID traffic
        p7 = re.compile(r'^Encapsulating\s(?P<encap>.+)$')

        # 1.1.1.10  01:09:06  up      10/10        -
        # 1:1:1:10::  01:09:06  up      10/10        -
        p8 = re.compile(r'^(?P<rloc_set>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+(?P<uptime>\S+)\s+(?P<rloc_state>\S+)\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<encap_iid>\S+)$')

        # Last up-down state change:         01:09:06, state change count: 1
        p9 = re.compile(r'^Last\sup-down\sstate\schange:\s+(?P<time>\S+),\s+state change count:\s+(?P<count>\d+)$')

        # Last route reachability change:    01:09:06, state change count: 1
        p10 = re.compile(r'^Last\sroute\sreachability\schange:\s+(?P<time>\S+),\s+state change count:\s+(?P<count>\d+)$')

        # Last priority / weight change:     never/never
        p11 = re.compile(r'^Last\spriority\s\/\sweight\schange:\s+(?P<priority>\S+)\/(?P<weight>\S+)$')

        # Last RLOC-probe sent:            01:09:06 (rtt 1ms)
        p12 = re.compile(r'^Last\sRLOC-probe\ssent:\s+(?P<time>\S+)\s\(rtt (?P<rtt>\d+)(?P<rtt_unit>\S+)\)$')

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            # Output for router lisp 0 instance-id 193
            # Output for router lisp 2 instance-id 101
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                if group['instance_id']:
                    instance_id = int(group['instance_id'])
                continue

            # LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['instance_id']:
                    instance_id = int(group['instance_id'])
                lisp_id_dict = \
                    ret_dict.setdefault('lisp_id', {})\
                        .setdefault(lisp_id, {})\
                        .setdefault('instance_id', {})\
                        .setdefault(instance_id, {})
                lisp_id_dict.update({
                    'eid_table': group['eid_table'],
                    'entries': int(group['entries'])
                })
                continue

            # 0017.0100.0001/48, uptime: 01:09:06, expires: 22:50:53, via map-reply, complete, local-to-site
            m = p3.match(line)
            if m:
                group = m.groupdict()
                eid_prefix = group.pop('eid_prefix')
                eid_prefix_dict = lisp_id_dict.setdefault('eid_prefix', {})\
                                              .setdefault(eid_prefix, {})
                eid_prefix_dict.update(
                    {k:v for k, v in group.items() if v is not None}
                )
                continue

            # Sources: map-reply
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'source_type': group['source_type']})
                continue

            # State: complete, last modified: 01:09:06, map-source: 1.1.1.10
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({
                    'last_modified': group['last_modified'],
                    'source_ip': group['source_ip']
                })
                continue

            # Active, Packets out: 139(0 bytes), counters are not accurate (~ 00:00:01 ago)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'prefix_state': group['prefix_state']})
                continue

            # Encapsulating dynamic-EID traffic
            m = p7.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_dict.update({'encap': group['encap']})
                continue

            # 1.1.1.10  01:09:06  up      10/10        -
            # 1:1:1:10::  01:09:06  up      10/10        -
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rloc_set = group.pop('rloc_set')
                rloc_set_dict = eid_prefix_dict.setdefault('rloc_set', {})\
                                               .setdefault(rloc_set, {})
                rloc_set_dict.update({
                    'uptime': group['uptime'],
                    'rloc_state': group['rloc_state'],
                    'priority': int(group['priority']),
                    'weight': int(group['weight']),
                    'encap_iid': group['encap_iid']
                })
                continue

            # Last up-down state change:         01:09:06, state change count: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                last_state_change_dict = rloc_set_dict.setdefault('last_state_change', {})
                last_state_change_dict.update({
                    'time': group['time'],
                    'count': int(group['count'])
                })
                continue

            # Last route reachability change:    01:09:06, state change count: 1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                last_route_reach_change_dict = rloc_set_dict.setdefault('last_route_reach_change', {})
                last_route_reach_change_dict.update({
                    'time': group['time'],
                    'count': int(group['count'])
                })
                continue

            # Last priority / weight change:     never/never
            m = p11.match(line)
            if m:
                group = m.groupdict()
                last_pri_weight_change_dict = rloc_set_dict.setdefault('last_pri_weight_change', {})
                last_pri_weight_change_dict.update({
                    'priority': group['priority'],
                    'weight': group['weight']
                })
                continue

            # Last RLOC-probe sent:            01:09:06 (rtt 1ms)
            m = p12.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_sent_dict = rloc_set_dict.setdefault('rloc_probe_sent', {})
                rloc_probe_sent_dict.update({
                    'time': group['time'],
                    'rtt': int(group['rtt']),
                    'rtt_unit': group['rtt_unit']
                })
                continue

        return ret_dict



# ==========================================
# Parser for: show lisp {lisp_id} redundancy
# ==========================================
class ShowLispRedundancySchema(MetaParser):
    schema = {
        'lisp_id': {
            int: { # LISP ID
                'rp': str,
                'sso': str,
                'checkpoint_connection': str,
                'peer_redundancy_state': str,
                'number_of_bulk_sync_started': int,
                'last_bulk_sync_started': str,
                'last_bulk_sync_finished': str,
                'last_sync_lost': str,
                'queued_checkpoint_requests': int,
                'unack_checkpoint_requests': int,
                'max_checkpoint_requests': int,
            }
        }
    }


class ShowLispRedundancy(ShowLispRedundancySchema):
    cli_command = ['show lisp {lisp_id} redundancy',
                   'show lisp redundancy',
                   'show lisp locator-table {locator_table} redundancy']

    def cli(self, lisp_id=None, locator_table=None, output=None):
        if output is None:
            if lisp_id:
                cmd = self.cli_command[0].format(lisp_id=lisp_id)
            elif locator_table:
                cmd = self.cli_command[2].format(locator_table=locator_table)
            else:
                cmd = self.cli_command[1]
            output = self.device.execute(cmd)

        lisp_dict = {}

        #Redundancy for LISP 0
        p1 = re.compile(r"^Redundancy\s+for\s+LISP\s+(?P<lisp_id>\d+)$")

        #  Active RP
        #  Standby RP
        p2 = re.compile(r"^(?P<rp>Active|Standby)\s+RP$")

        #  SSO enabled
        #  SSO disabled
        p3 = re.compile(r"^SSO\s+(?P<sso>enabled|disabled)$")

        #  Checkpoint connection open
        #  Checkpoint connection closed
        p4 = re.compile(r"^Checkpoint\s+connection\s+(?P<checkpoint_connection>open|closed)$")

        #  Peer redundancy state: synchronized
        #  Peer redundancy state: unsynchronized
        p5 = re.compile(r"^Peer\s+redundancy\s+state:\s+(?P<peer_redundancy_state>synchronized|unsynchronized)$")

        #  Number of Bulk Syncs started: 1
        p6 = re.compile(r"^Number\s+of\s+Bulk\s+Syncs\s+started:\s+(?P<number_of_bulk_sync_started>\d+)$")

        #  Last Bulk Sync started: never
        #  Last Bulk Sync started: Jan 23 15:55:26.712 PST
        p7 = re.compile(r"^Last\s+Bulk\s+Sync\s+started:\s+(?P<last_bulk_sync_started>[\w:\s+\.]+)$")

        #  Last Bulk Sync finished: never
        #  Last Bulk Sync finished: Jan 23 15:55:26.712 PST
        p8 = re.compile(r"^Last\s+Bulk\s+Sync\s+finished:\s+(?P<last_bulk_sync_finished>[\w:\s+\.]+)$")

        #  Last time synchronization was lost: never
        #  Last time synchronization was lost: Jan 23 15:55:26.712 PST
        p9 = re.compile(r"^Last\s+time\s+synchronization\s+was\s+lost:\s+(?P<last_sync_lost>[\w\s+\d:\.]+)$")

        #  Queued/max checkpoint requests: 0/17
        p10 = re.compile(r"^Queued\/max\s+checkpoint\s+requests:\s+(?P<queued_checkpoint_requests>\d+)\/(?P<max_checkpoint_requests>\d+)$")

        #  Unacknowledged/max checkpoint requests: 0/17
        p11 = re.compile(r"^Unacknowledged\/max\s+checkpoint\s+requests:\s+(?P<unack_checkpoint_requests>\d+)\/\d+$")

        for line in output.splitlines():
            line = line.strip()

            #Redundancy for LISP 0
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])

                lisp_id_dict = lisp_dict.setdefault('lisp_id', {}) \
                                        .setdefault(lisp_id, {})
                continue

            #  Active RP
            #  Standby RP
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['rp'] = groups['rp']
                continue

            #  SSO enabled
            #  SSO disabled
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['sso'] = groups['sso']
                continue

            #  Checkpoint connection open
            #  Checkpoint connection closed
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['checkpoint_connection'] = groups['checkpoint_connection']
                continue

            #  Peer redundancy state: synchronized
            #  Peer redundancy state: unsynchronized
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['peer_redundancy_state'] = groups['peer_redundancy_state']
                continue

            #  Number of Bulk Syncs started: 1
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['number_of_bulk_sync_started'] = int(groups['number_of_bulk_sync_started'])
                continue

            #  Last Bulk Sync started: never
            #  Last Bulk Sync started: Jan 23 15:55:26.712 PST
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['last_bulk_sync_started'] = groups['last_bulk_sync_started']
                continue

            #  Last Bulk Sync finished: never
            #  Last Bulk Sync finished: Jan 23 15:55:26.712 PST
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['last_bulk_sync_finished'] = groups['last_bulk_sync_finished']
                continue

            #  Last time synchronization was lost: never
            #  Last time synchronization was lost: Jan 23 15:55:26.712 PST
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['last_sync_lost'] = groups['last_sync_lost']
                continue

            #  Queued/max checkpoint requests: 0/17
            m=p10.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['queued_checkpoint_requests'] = int(groups['queued_checkpoint_requests'])
                lisp_id_dict['max_checkpoint_requests'] = int(groups['max_checkpoint_requests'])
                continue

            #  Unacknowledged/max checkpoint requests: 0/17
            m=p11.match(line)
            if m:
                groups = m.groupdict()
                lisp_id_dict['unack_checkpoint_requests'] = int(groups['unack_checkpoint_requests'])
                continue

        return lisp_dict


class ShowLispEthernetMapCacheSchema(MetaParser):

    ''' Schema for
        * 'show lisp instance-id <instance_id> ethernet map-cache'
        * 'show lisp <lisp_id> instance-id <instance_id> ethernet map-cache'
        * 'show lisp eid-table vlan <vlan> ethernet map-cache'
        * 'show lisp locator-table <vrf> ethernet map-cache'''
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_table': str,
                        'entries': int,
                        'eid_prefix': {
                            str: {
                                'uptime': str,
                                'expiry_time': str,
                                'via': str,
                                'map_reply_state': str,
                                Optional('site'): str,
                                Optional('locators'): {
                                    str: {
                                        'uptime': str,
                                        'rloc_state': str,
                                        'priority': int,
                                        'weight': int,
                                        'encap_iid': str
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispEthernetMapCache(ShowLispEthernetMapCacheSchema):
    """Parser for
    * 'show lisp instance-id <instance_id> ethernet map-cache'
    * 'show lisp <lisp_id> instance-id <instance_id> ethernet map-cache'
    * 'show lisp eid-table vlan <vlan> ethernet map-cache'
    * 'show lisp locator-table <vrf> ethernet map-cache'"""
    cli_command = ['show lisp locator-table {vrf} instance-id {instance_id} ethernet map-cache',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache',
                   'show lisp instance-id {instance_id} ethernet map-cache'
                   #'show lisp eid-table vlan {vlan} ethernet map-cache',
                   ]

    def cli(self, lisp_id=None, instance_id=None, vlan=None, vrf=None, output=None):
        if output is None:
            if lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[2].format(instance_id=instance_id),timeout=300)
            elif vrf:
                output = self.device.execute(self.cli_command[0].format(vrf=vrf,instance_id=instance_id))
            #else:
            #    output = self.device.execute(self.cli_command[3].format(vlan=vlan))
        ret_dict = {}

        #Output for router lisp 0 instance-id 8188
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        #LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
        # LISP MAC Mapping Cache for LISP 0 EID-table Vlan 101 (IID 1023), 2 entries
        p2 = re.compile(r"^LISP\s+MAC\s+Mapping\s+Cache\s+for(\s+LISP\s+\d+)?\s+EID-table\s+"
                        r"(?P<eid_table>Vlan\s+\d+)\s+\(IID\s+\d+\),\s+(?P<entries>\d+)\s+entries$")

        #0017.0100.0001/48, uptime: 18:33:39, expires: 05:26:20, via map-reply, complete, local-to-site
        # aabb.cc00.cb00/48, uptime: 00:00:03, expires: never, via pub-sub, complete, local-to-site
        p3 = re.compile(r"^(?P<eid_prefix>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2}),"
                        r"\s+uptime:\s+(?P<uptime>\S+),\s+expires:\s+"
                        r"(?P<expiry_time>\d{1,2}:\d{1,2}:\d{1,2}|\S+),\s+via\s+(?P<via>\w+\-+\w+),\s+"
                        r"(?P<map_reply_state>\w+),\s+(?P<site>\S+)$")

        # 0000.58bb.6f48/48, uptime: 1d05h, expires: 5d18h, via map-reply, complete
        p3_1 = re.compile(r"(?P<eid_prefix>([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2}),"
                          r"\s+uptime:\s+(?P<uptime>\S+),\s+expires:\s+"
                          r"(?P<expiry_time>\d{1,2}:\d{1,2}:\d{1,2}|\S+),\s+via\s+"
                          r"(?P<via>(\w+\-+\w+)|\S+\s+\w+\-+\w+),\s+(?P<map_reply_state>\w+)$")

        #  1.1.1.10  18:33:39  up      10/10        -
        #  1:1:1:10::  18:33:39  up      10/10        -
        p4 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                        r"(?P<uptime>\S+)\s+(?P<rloc_state>\S+)"
                        r"\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<encap_iid>\S+)$")
        for line in output.splitlines():
            line = line.strip()
            #Output for router lisp 0 instance-id 8188
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                instance_id = int(groups['instance_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                instance_id_dict = ret_dict.setdefault('instance_id',{})\
                                           .setdefault(instance_id,{})
                continue

            #LISP MAC Mapping Cache for EID-table Vlan 210 (IID 8188), 1 entries
            m = p2.match(line)
            if m:
                if "lisp_id" and "instance_id" not in ret_dict:
                    if lisp_id and instance_id:
                        lisp_id = int(lisp_id)
                        lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                               .setdefault(lisp_id,{})
                        instance_id = int(instance_id)
                        instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                       .setdefault(instance_id,{})
                    elif not lisp_id and instance_id:
                        lisp_id = 0
                        lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                               .setdefault(lisp_id,{})
                        instance_id = int(instance_id)
                        instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                                       .setdefault(instance_id,{})
                groups = m.groupdict()
                eid_table = groups['eid_table']
                entries = int(groups['entries'])
                instance_id_dict.update({'eid_table':eid_table,'entries':entries})

            #0017.0100.0001/48, uptime: 18:33:39, expires: 05:26:20, via map-reply, complete, local-to-site
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                eid_prefix = groups['eid_prefix']
                uptime = groups['uptime']
                expiry_time = groups['expiry_time']
                via = groups['via']
                map_reply_state = groups['map_reply_state']
                site = groups['site']
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                  .setdefault(eid_prefix,{})
                eid_prefix_dict.update({
                    'uptime':uptime,
                    'expiry_time':expiry_time,
                    'via':via,
                    'map_reply_state':map_reply_state,
                    'site':site
                })

            # 0000.58bb.6f48/48, uptime: 1d05h, expires: 5d18h, via map-reply, complete
            m = p3_1.match(line)
            if m:
                groups = m.groupdict()
                eid_prefix = groups['eid_prefix']
                uptime = groups['uptime']
                expiry_time = groups['expiry_time']
                via = groups['via']
                map_reply_state = groups['map_reply_state']
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefix',{})\
                                                  .setdefault(eid_prefix,{})
                eid_prefix_dict.update({
                    'uptime':uptime,
                    'expiry_time':expiry_time,
                    'via':via,
                    'map_reply_state':map_reply_state
                    })

            #  1.1.1.10  18:33:39  up      10/10        -
            #  1:1:1:10::  18:33:39  up      10/10        -
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                locators = groups['locators']
                uptime = groups['uptime']
                rloc_state = groups['rloc_state']
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                encap_iid = groups['encap_iid']
                rloc_set_dict = eid_prefix_dict.setdefault('locators',{})\
                                               .setdefault(locators,{})
                rloc_set_dict.update({
                    'uptime':uptime,
                    'rloc_state':rloc_state,
                    'priority':priority,
                    'weight':weight,
                    'encap_iid':encap_iid
                })
        return ret_dict

# ==========================================
# Parser for: show lisp {lisp_id} instance-id
# {instance_id} {address_family} eid-watch
# ==========================================
class ShowLispEidWatchSchema(MetaParser):
    schema = {
        'lisp_id': {
            int: { # lisp id
                Optional('instance_id'): {
                    Optional(int): { # instance id
                        'client_name': str,
                        'process_id': int,
                        'connection_to_control_process': str,
                        'ipc_endpoint': int,
                        'client_notifications': str,
                        'address_family': str,
                        'eid_table': str,
                        'entry_count': int,
                        'prefix': str,
                        'watched_entries': ListOf(str)
                    }
                }
            }
        }
    }


class ShowLispEidWatch(ShowLispEidWatchSchema):
    cli_command = ['show lisp {lisp_id} instance-id {instance_id} {address_family} eid-watch',
                   'show lisp instance-id {instance_id} {address_family} eid-watch',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} eid-watch',
                   'show lisp eid-table {eid_table} {address_family} eid-watch',
                   'show lisp eid-table vlan {vlan_id} ethernet eid-watch',
                   'show lisp instance-id {instance_id} {address_family} eid-watch address-resolution']

    def cli(self, lisp_id=None, instance_id=None, address_family=None, locator_table=None, eid_table=None, vlan_id=None, output=None):
        if output is None:
            if lisp_id and instance_id and address_family:
                cmd = self.cli_command[0].format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family)
            elif locator_table and instance_id:
                cmd = self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id, address_family=address_family)
            elif eid_table:
                cmd = self.cli_command[3].format(eid_table=eid_table, address_family=address_family)
            elif vlan_id:
                cmd = self.cli_command[4].format(vlan_id=vlan_id)
            else:
                if "address-resolution" in self.cli_command:
                    cmd = self.cli_command[5].format(instance_id=instance_id, address_family=address_family)
                else:
                    cmd = self.cli_command[1].format(instance_id=instance_id, address_family=address_family)
            output = self.device.execute(cmd)

        lisp_dict = {}

        #LISP EID watch information for router 0
        p1 = re.compile(r"^LISP\sEID\swatch\sinformation\sfor\srouter\s+(?P<lisp_id>\d+)$")

        #Client : Test 0
        p2 = re.compile(r"^Client\s+:\s+(?P<client_name>.+)$")

        #Process ID : 87
        p3 = re.compile(r"^Process\sID\s+:\s+(?P<process_id>\d+)$")

        #Connection to LISP control process : ENABLED
        p4 = re.compile(r"^Connection\sto\sLISP\scontrol\sprocess\s+:\s+(?P<connection_to_control_process>.+)$")

        #IPC end point : 1
        p5 = re.compile(r"^IPC\send\spoint\s+:\s+(?P<ipc_endpoint>\d+)$")

        #Client notifications : Delivered
        p6 = re.compile(r"^Client\snotifications\s+:\s+(?P<client_notifications>.+)$")

        #LISP IPv4 EID Watches for Table (RLOC mapping in vrf default IPv4) IID (101), 1 watch entries
        #LISP invalid EID Watches for Table (AR mapping in Vlan 100) IID (103), 1 watch entries
        p7 = re.compile(r"^LISP\s+(?P<address_family>[A-Za-z0-9]+)\sEID\sWatches\sfor\sTable\s+\((RLOC|AR)\smapping\sin\s+(?P<eid_table>(vrf\s+\w+)|(Vlan\s+\d+))(\s+)?(IPv4|IPv6)?\)\sIID\s+\((?P<instance_id>\d+)\),\s+(?P<entry_count>\d+)\swatch\sentries$")

        #  Watch entries for prefix 0.0.0.0/0
        #  Watch entries for prefix ::/0
        #  Watch entries for prefix 0000.0000.0000/0
        p8 = re.compile(r"^Watch\sentries\sfor\sprefix\s+(?P<prefix>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2})|([a-fA-F\d\:]+\/\d{1,3})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4}\/\d{1,2}))$")

        #   1.1.1.1
        #   E80::AEDE:48FF:FE00:1111
        #   f100.a551.0501
        p9 = re.compile(r"^(?P<watched_entry>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|(([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})|([a-fA-F\d\:]+))")

        for line in output.splitlines():
            line = line.strip()
           #LISP EID watch information for router 0
            m=p1.match(line)
            if m:
                groups = m.groupdict()
                if groups['lisp_id']:
                    lisp_id = int(groups['lisp_id'])
                else:
                    lisp_id = 0

                instance_id_container = lisp_dict.setdefault('lisp_id', {}) \
                                                 .setdefault(lisp_id, {})
                instance_id_dict = instance_id_container.setdefault('instance_id', {})

                # At this point we don't know instance_id yet
                dummy_instance_id_dict = instance_id_dict.setdefault('dummy_instance_id', {})
                continue

            #Client : Test 0
            m=p2.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['client_name'] = groups['client_name']
                continue

            #Process ID : 87
            m=p3.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['process_id'] = int(groups['process_id'])
                continue

            #Connection to LISP control process : ENABLED
            m=p4.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['connection_to_control_process'] = groups['connection_to_control_process']
                continue

            #IPC end point : 1
            m=p5.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['ipc_endpoint'] = int(groups['ipc_endpoint'])
                continue

            #Client notifications : Delivered
            m=p6.match(line)
            if m:
                groups = m.groupdict()
                dummy_instance_id_dict['client_notifications'] = groups['client_notifications']
                continue

            #LISP IPv4 EID Watches for Table (RLOC mapping in vrf default IPv4) IID (101), 1 watch entries
            #LISP invalid EID Watches for Table (AR mapping in Vlan 100) IID (103), 1 watch entries
            m=p7.match(line)
            if m:
                groups = m.groupdict()
                instance_id = int(groups['instance_id'])

                instance_id_dict[instance_id] = instance_id_dict.pop('dummy_instance_id')
                instance_id_dict[instance_id]['address_family'] = groups['address_family']
                instance_id_dict[instance_id]['eid_table'] = groups['eid_table']
                instance_id_dict[instance_id]['entry_count'] = int(groups['entry_count'])
                continue

            #  Watch entries for prefix 0.0.0.0/0
            #  Watch entries for prefix ::/0
            #  Watch entries for prefix 0000.0000.0000/0
            m=p8.match(line)
            if m:
                groups = m.groupdict()
                instance_id_dict[instance_id]['prefix'] = groups['prefix']
                continue

            #   1.1.1.1
            #   E80::AEDE:48FF:FE00:1111
            #   f100.a551.0501
            m=p9.match(line)
            if m:
                groups = m.groupdict()
                watched_entries = instance_id_dict[instance_id].setdefault('watched_entries', [])
                watched_entries.append(groups['watched_entry'])
                continue

        # Post processing in case the output does not have instance id
        if lisp_dict == {}:
            return {}

        lisp_ids_to_delete = []
        for lisp_id, lisp_id_dict in lisp_dict['lisp_id'].items():
            for instance_id, instance_id_dict in lisp_id_dict['instance_id'].items():
                if instance_id == 'dummy_instance_id':
                    lisp_ids_to_delete.append(lisp_id)
                    break

        for id in lisp_ids_to_delete:
            del lisp_dict['lisp_id'][id]['instance_id']['dummy_instance_id']

        return lisp_dict


class ShowLispInstanceIdForwardingStateSchema(MetaParser):

    ''' Schema for
        * show ip lisp instance-id {instance_id} forwarding state
        * show ipv6 lisp instance-id {instance_id} forwarding state
        * show lisp instance-id {instance_id} {service} forwarding state
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'lisp_virtual_intf': str,
                        'user': str,
                        'eid_vrf': {
                            str: {
                                'address_family': { # IPv4|IPv6|L2
                                    str: {
                                        Optional('configured_roles'): ListOf(str),
                                        Optional('eid_table'): str,
                                        Optional('alt_table'): str,
                                        Optional('locator_status_bit'): str,
                                        Optional('nonce'): str,
                                        Optional('ttl_propagation'): str,
                                        Optional('table_supression'): str,
                                        Optional('sgt_policy_fwd'): str,
                                        Optional('l2_domain_id'): int,
                                        Optional('ipv4_unnum_if'): str,
                                        Optional('ipv6_unnum_if'): str
                                        }
                                    },
                                'rloc_transport': {
                                    'vrf': str,
                                    'ipv4_rloc_table': str,
                                    'ipv6_rloc_table': str,
                                    'ipv4_path_mtu_discovery': {
                                        'min': int,
                                        'max': int
                                        },
                                    'ipv6_path_mtu_discovery': {
                                        'min': int,
                                        'max': int
                                        },
                                    'ipv4_rloc_fltr_handle': str,
                                    'ipv6_rloc_fltr_handle': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispInstanceIdForwardingState(ShowLispInstanceIdForwardingStateSchema):
    ''' Parser for
        * show ip lisp instance-id {instance_id} forwarding state
        * show ipv6 lisp instance-id {instance_id} forwarding state
        * show lisp instance-id {instance_id} {service} forwarding state

    '''
    cli_command = ['show ip lisp instance-id {instance_id} forwarding state',
                   'show ipv6 lisp instance-id {instance_id} forwarding state',
                   'show lisp instance-id {instance_id} {service} forwarding state']

    def cli(self, instance_id, output=None, service=None):
        if output is None:
            if instance_id and service:
                output = self.device.execute(self.cli_command[2].format(instance_id = instance_id,service = service))
            if instance_id:
                if "ipv6" in self.cli_command:
                    output = self.device.execute(self.cli_command[1].format(instance_id = instance_id))
                else:
                    output = self.device.execute(self.cli_command[0].format(instance_id = instance_id))
        ret_dict = {}

        # EID VRF                      red (0x2)
        p1 = re.compile(r"^EID\s+VRF\s+(?P<eid_vrf>\S+\s+\S+)$")

        # IPv4
        p2 = re.compile(r"^(?P<address_family>IPv4|IPv6|L2)$")

        # Configured roles         ETR|PITR
        p3 = re.compile(r"^Configured\s+roles\s+(?P<configured_roles>\S+)$")

        # EID table                IPv4:red
        p4 = re.compile(r"^EID\s+table\s+(?P<eid_table>\S+)$")

        # ALT table                <null>
        p5 = re.compile(r"^ALT\s+table\s+(?P<alt_table>\S+)$")

        # Locator status bits      Disabled
        p6 = re.compile(r"^Locator\s+status\s+bits\s+(?P<locator_status_bit>Disabled|Enabled)$")

        # Nonce                    N/A
        p7 = re.compile(r"^Nonce\s+(?P<nonce>\S+)$")

        # TTL Propagation          Enabled
        p8 = re.compile(r"^TTL\s+Propagation\s+(?P<ttl_propagation>Disabled|Enabled)$")

        # Table Suppression        Disabled
        p9 = re.compile(r"^Table\s+Suppression\s+(?P<table_supression>Disabled|Enabled)$")

        # SGT Policy Fwd           Disabled
        p10 = re.compile(r"^SGT\s+Policy\s+Fwd\s+(?P<sgt_policy_fwd>Disabled|Enabled)$")

        # L2 Domain ID             0
        p11 = re.compile(r"^L2\s+Domain\s+ID\s+(?P<l2_domain_id>\d+)$")

        # IPv4 Unnum I/F           N/A
        p12 = re.compile(r"^IPv4\s+Unnum\s+I\/F\s+(?P<ipv4_unnum_if>\S+)$")

        # IPv6 Unnum I/F           N/A
        p13 = re.compile(r"^IPv6\s+Unnum\s+I\/F\s+(?P<ipv6_unnum_if>\S+)$")

        # RLOC transport VRF         Default
        p14  = re.compile(r"^RLOC\s+transport\s+VRF\s+(?P<vrf>\S+)")

        # IPv4 RLOC table          IPv4:Default
        p15 = re.compile(r"^IPv4\s+RLOC\s+table\s+(?P<ipv4_rloc_table>\S+)")

        # IPv6 RLOC table          IPv6:Default
        p16 = re.compile(r"^IPv6\s+RLOC\s+table\s+(?P<ipv6_rloc_table>\S+)")

        # IPv4 path MTU discovery  min  576 max 65535
        # IPv6 path MTU discovery  min  1280 max 65535
        p17 = re.compile(r"^IPv(?P<ip_version>\d)\s+path\s+MTU\s+discovery\s+"
                         r"min\s+(?P<min>\d+)\s+max\s+(?P<max>\d+)$")

        # IPv4 RLOC fltr handle    0x0
        # IPv6 RLOC fltr handle    0x0
        p18 = re.compile(r"^IPv(?P<ip_version>\d)\s+RLOC\s+fltr\s+handle\s+"
                         r"(?P<rloc_fltr_handle>\S+)$")

        # LISP router ID             0
        p19 = re.compile(r"^LISP\s+router\s+ID\s+(?P<lisp_id>\d+)$")

        # LISP virtual interface     LISP0.4100
        p20 = re.compile(r"^LISP\s+virtual\s+interface\s+"
                         r"(?P<lisp_virtual_intf>\S+)$")

        # User                       LISP
        p21 = re.compile(r"^User\s+(?P<user>\S+)$")

        for line in output.splitlines():
            line = line.strip()

            # EID VRF                      red (0x2)
            m = p1.match(line)
            if m:
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(None,{})
                instance_id = int(instance_id)
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                groups = m.groupdict()
                eid_vrf = groups['eid_vrf']
                instance_id_dict.setdefault('lisp_virtual_intf')
                instance_id_dict.setdefault('user')
                eid_dict = instance_id_dict.setdefault('eid_vrf', {}).setdefault(eid_vrf, {})
                continue

            # IPv4
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                address_family = groups['address_family']
                af_dict = eid_dict.setdefault('address_family', {}).setdefault(address_family, {})
                continue

            # Configured roles         ETR|PITR
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                configured_role = groups['configured_roles']
                configured_roles = configured_role.split("|")
                af_dict.update({'configured_roles':configured_roles})
                continue

            # EID table                IPv4:red
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                eid_table = groups['eid_table']
                af_dict.update({'eid_table':eid_table})
                continue

            # ALT table                <null>
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                alt_table = groups['alt_table']
                af_dict.update({'alt_table':alt_table})
                continue

            # Locator status bits      Disabled
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                locator_status_bit = groups['locator_status_bit']
                af_dict.update({'locator_status_bit':locator_status_bit})
                continue

            # Nonce                    N/A
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                nonce = groups['nonce']
                af_dict.update({'nonce':nonce})
                continue

            # TTL Propagation          Enabled
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                ttl_propagation = groups['ttl_propagation']
                af_dict.update({'ttl_propagation':ttl_propagation})
                continue

            # Table Suppression        Disabled
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                table_supression = groups['table_supression']
                af_dict.update({'table_supression':table_supression})
                continue

            # SGT Policy Fwd           Disabled
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                sgt_policy_fwd = groups['sgt_policy_fwd']
                af_dict.update({'sgt_policy_fwd':sgt_policy_fwd})
                continue

            # L2 Domain ID             0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                l2_domain_id = int(groups['l2_domain_id'])
                af_dict.update({'l2_domain_id':l2_domain_id})
                continue

            # IPv4 Unnum I/F           N/A
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                ipv4_unnum_if = groups['ipv4_unnum_if']
                af_dict.update({'ipv4_unnum_if':ipv4_unnum_if})
                continue

            # IPv6 Unnum I/F           N/A
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                ipv6_unnum_if = groups['ipv6_unnum_if']
                af_dict.update({'ipv6_unnum_if':ipv6_unnum_if})
                continue

            # RLOC transport VRF         Default
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                vrf = groups['vrf']
                rloc_dict = eid_dict.setdefault('rloc_transport', {})
                rloc_dict.update({'vrf':vrf})
                continue

            # IPv4 RLOC table          IPv4:Default
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ipv4_rloc_table = groups['ipv4_rloc_table']
                rloc_dict.update({'ipv4_rloc_table':ipv4_rloc_table})
                continue

            # IPv6 RLOC table          IPv6:Default
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                ipv6_rloc_table = groups['ipv6_rloc_table']
                rloc_dict.update({'ipv6_rloc_table':ipv6_rloc_table})
                continue

            # IPv4 path MTU discovery  min  576 max 65535
            # IPv6 path MTU discovery  min  1280 max 65535
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                ip_version = int(groups['ip_version'])
                min = int(groups['min'])
                max = int(groups['max'])
                if ip_version == 4:
                    v4_mtu_dict = rloc_dict.setdefault('ipv4_path_mtu_discovery',{})
                    v4_mtu_dict.update({'min':min,'max':max})
                else:
                    v6_mtu_dict = rloc_dict.setdefault('ipv6_path_mtu_discovery',{})
                    v6_mtu_dict.update({'min':min,'max':max})
                continue

            # IPv4 RLOC fltr handle    0x0
            # IPv6 RLOC fltr handle    0x0
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                rloc_fltr_handle = groups['rloc_fltr_handle']
                ip_version = groups['ip_version']
                rloc_dict.update({f'ipv{ip_version}_rloc_fltr_handle': rloc_fltr_handle})
                continue

            # LISP router ID             0
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                ret_dict['lisp_id'][lisp_id] = ret_dict['lisp_id'].pop(None)
                continue

            # LISP virtual interface     LISP0.4100
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                lisp_virtual_intf = groups['lisp_virtual_intf']
                instance_id_dict.update({'lisp_virtual_intf':lisp_virtual_intf})
                continue

            # User                       LISP
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                user = groups['user']
                instance_id_dict.update({'user':user})
                continue
        return ret_dict


class ShowLispIAFServerSchema(MetaParser):

    ''' Schema for
        * show lisp instance-id {instance_id} {address_family} server summary
        * show lisp {lisp_id} instance-id {instance_id} {address_family} server summary
        * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'site': {
                            str: {
                                'configured': int,
                                'registered': int,
                                'incons': int
                                }
                            },
                        'site_reg_limit': int,
                        'site_reg_count': int,
                        'configured_sites': int,
                        'registered_sites': int,
                        'sites_inconsistent_registrations': int,
                        'af': {
                            str: { # IPv4|IPv6|MAC
                                'configured_eid_prefixes': int,
                                'registered_eid_prefixes': int,
                                'instance_service_site_reg_limit': int,
                                'registration_history_size': int,
                                'registration_history_limit': int
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispIAFServer(ShowLispIAFServerSchema):
    ''' Parser for
        * show lisp instance-id {instance_id} {address_family} server summary
        * show lisp {lisp_id} instance-id {instance_id} {address_family} server summary
        * show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary
    '''
    cli_command = ['show lisp instance-id {instance_id} {address_family} server summary',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server summary',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server summary'
                   ]

    def cli(self, output=None, lisp_id=None, instance_id=None, address_family=None, locator_table=None):
        if output is None:
            if lisp_id and instance_id and address_family:
                output = self.device.execute(self.cli_command[1].format(
                        lisp_id=lisp_id,
                        instance_id=instance_id,
                        address_family=address_family))
            elif locator_table and instance_id and address_family:
                output = self.device.execute(self.cli_command[2].format(
                        locator_table=locator_table,
                        instance_id=instance_id,
                        address_family=address_family))
            else:
                output = self.device.execute(self.cli_command[0].format(
                        instance_id=instance_id,
                        address_family=address_family))
        ret_dict = {}

        # Output for router lisp 0 instance-id 4100
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)"
                        r"\s+instance-id\s+(?P<instance_id>\d+)$")

        # Shire                         1          0      0
        p2 = re.compile(r"^(?P<site>\S+)\s+(?P<configured>\d+)\s+"
                        r"(?P<registered>\d+)\s+(?P<incons>\d+)$")

        # Site-registration limit for router lisp 0:              0
        p3 = re.compile(r"^Site-registration\s+limit\s+for\s+"
                        r"router\s+lisp\s+\d+:\s+(?P<site_reg_limit>\d+)")

        # Site-registration count for router lisp 0:              6
        p4 = re.compile(r"^Site-registration\s+count\s+for\s+router\s+"
                        r"lisp\s+\d+:\s+(?P<site_reg_count>\d+)")

        # Number of configured sites:                             1
        p5 = re.compile(r"^Number\s+of\s+configured\s+sites:\s+(?P<configured_sites>\d+)")

        # Number of registered sites:                             0
        p6 = re.compile(r"^Number\s+of\s+registered\s+sites:\s+(?P<registered_sites>\d+)")

        # Sites with inconsistent registrations:                  0
        p7 = re.compile(r"^Sites\s+with\s+inconsistent\s+registrations:\s+"
                        r"(?P<sites_inconsistent_registrations>\d+)")

        # IPv4|IPv6|MAC
        p8 = re.compile(r"^(?P<af>IPv4|IPv6|MAC)$")

        # Number of configured EID prefixes:                    1
        p9 = re.compile(r"^Number\s+of\s+configured\s+EID\s+prefixes:\s+"
                        r"(?P<configured_eid_prefixes>\d+)$")

        # Number of registered EID prefixes:                    0
        p10 = re.compile(r"^Number\s+of\s+registered\s+EID\s+prefixes:\s+"
                         r"(?P<registered_eid_prefixes>\d+)$")

        # Instance-Service site-registration limit:             0
        p11 = re.compile(r"^Instance-Service\s+site-registration\s+limit:\s+"
                         r"(?P<instance_service_site_reg_limit>\d+)$")

        # Registration-history size/limit:                      0/1000
        p12 = re.compile(r"^Registration-history\s+size\/limit:\s+"
                         r"(?P<registration_history_size>\d+)\/(?P<registration_history_limit>\d+)$")

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0 instance-id 4100
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

            # Shire                         1          0      0
            m = p2.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id = int(instance_id)
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                groups = m.groupdict()
                site = groups['site']
                configured = int(groups['configured'])
                registered = int(groups['registered'])
                incons = int(groups['incons'])
                site_dict = instance_id_dict.setdefault('site',{})\
                                            .setdefault(site,{})
                site_dict.update({'configured':configured,'registered':registered,
                                  'incons':incons})

            # Site-registration limit for router lisp 0:              0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                site_reg_limit = int(groups['site_reg_limit'])
                instance_id_dict.update({'site_reg_limit':site_reg_limit})

            # Site-registration count for router lisp 0:              6
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                site_reg_count = int(groups['site_reg_count'])
                instance_id_dict.update({'site_reg_count':site_reg_count})

            # Number of configured sites:                             1
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                configured_sites = int(groups['configured_sites'])
                instance_id_dict.update({'configured_sites':configured_sites})

            # Number of registered sites:                             0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                registered_sites = int(groups['registered_sites'])
                instance_id_dict.update({'registered_sites':registered_sites})

            # Sites with inconsistent registrations:                  0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                sites_inconsistent_registrations = int(groups['sites_inconsistent_registrations'])
                instance_id_dict.update({'sites_inconsistent_registrations':sites_inconsistent_registrations})

            # IPv4|IPv6|MAC
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                af = groups['af']
                af_dict = instance_id_dict.setdefault('af',{})\
                                          .setdefault(af,{})

            # Number of configured EID prefixes:                    1
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                configured_eid_prefixes = int(groups['configured_eid_prefixes'])
                af_dict.update({'configured_eid_prefixes':configured_eid_prefixes})

            # Number of registered EID prefixes:                    0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                registered_eid_prefixes = int(groups['registered_eid_prefixes'])
                af_dict.update({'registered_eid_prefixes':registered_eid_prefixes})

            # Instance-Service site-registration limit:             0
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                instance_service_site_reg_limit = int(groups['instance_service_site_reg_limit'])
                af_dict.update({'instance_service_site_reg_limit':instance_service_site_reg_limit})

            # Registration-history size/limit:                      0/1000
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                registration_history_size = int(groups['registration_history_size'])
                registration_history_limit = int(groups['registration_history_limit'])
                af_dict.update({'registration_history_size':registration_history_size,
                                'registration_history_limit':registration_history_limit})
        return ret_dict


class ShowLispInstanceIdDNStatisticsSchema(MetaParser):

    ''' Schema for
        * show lisp {lisp_id} instance-id 16777214 dn statistics
        * show lisp {lisp_id} instance-id {instance_id} dn statistics
        * show lisp instance-id 16777214 dn statistics
    '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: { # Value other than 16777214 is not accepted
                        'iaf_count': int,
                        'loca_eid_map_count': int,
                        'etr_ems_link_count': int,
                        'udp_map_register': {
                            'sent': int,
                            'received': int
                            },
                        'tcp_map_register': {
                            'sent': int,
                            'received': int
                            },
                        'udp_map_notify': {
                            'sent': int,
                            'received': int
                            },
                        'tcp_map_notify': {
                            'sent': int,
                            'received': int
                            }
                        }
                    }
                }
            }
        }


class ShowLispInstanceIdDNStatistics(ShowLispInstanceIdDNStatisticsSchema):

    ''' Parser for
        * show lisp instance-id 16777214 dn statistics
        * show lisp {lisp_id} instance-id 16777214 dn statistics
        * show lisp {lisp_id} instance-id {instance_id} dn statistics
    '''
    cli_command = ['show lisp instance-id 16777214 dn statistics',
                   'show lisp {lisp_id} instance-id {instance_id} dn statistics']

    def cli(self, output=None, lisp_id=None, instance_id=None):
        if output is None:
            if lisp_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id,
                    instance_id=instance_id if instance_id else '16777214'))
            else:
                output = self.device.execute(self.cli_command[0])
        ret_dict = {}

        # Output for router lisp 0
        p1 = re.compile(r"^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$")

        # LISP EID Statistics for instance ID 16777214
        p2 = re.compile(r"^LISP\s+EID\s+Statistics\s+for\s+instance\s+ID\s+(?P<instance_id>\d+)$")

        # Active DN IAF count:                              1
        p3 = re.compile(r"^Active\s+DN\s+IAF\s+count:\s+(?P<iaf_count>\d+)$")

        # Active DN local eid map count:                    1
        p4 = re.compile(r"^Active\s+DN\s+local\s+eid\s+map\s+"
                        r"count:\s+(?P<loca_eid_map_count>\d+)$")

        # Active DN etr ems registration link count:        2
        p5 = re.compile(r"^Active\s+DN\s+etr\s+ems\s+registration\s+"
                        r"link\s+count:\s+(?P<etr_ems_link_count>\d+)$")

        # UDP Map-Register (send/recv):                     1/0
        p6 = re.compile(r"^UDP\s+Map-Register\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")

        # TCP Map-Register (send/recv):                     1/0
        p7 = re.compile(r"^TCP\s+Map-Register\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")

        # UDP Map-Notify (send/recv):                       0/2
        p8 = re.compile(r"^UDP\s+Map-Notify\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")

        # TCP Map-Notify (send/recv):                       0/5
        p9 = re.compile(r"^TCP\s+Map-Notify\s+\(send\/recv\):\s+"
                        r"(?P<sent>\d)\/(?P<received>\d)")
        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                continue

            # LISP EID Statistics for instance ID 16777214
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                instance_id = int(groups['instance_id'])
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_id_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                instance_id_dict = lisp_id_dict.setdefault('instance_id', {}).setdefault(instance_id, {})
                continue

            # Active DN IAF count:                              1
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                iaf_count = int(groups['iaf_count'])
                instance_id_dict.update({'iaf_count':iaf_count})
                continue

            #  Active DN local eid map count:                    1
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                loca_eid_map_count = int(groups['loca_eid_map_count'])
                instance_id_dict.update({'loca_eid_map_count':loca_eid_map_count})
                continue

            # Active DN etr ems registration link count:        2
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                etr_ems_link_count = int(groups['etr_ems_link_count'])
                instance_id_dict.update({'etr_ems_link_count':etr_ems_link_count})
                continue

            # UDP Map-Register (send/recv):                     1/0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                udp_map_dict = instance_id_dict.setdefault('udp_map_register', {})
                udp_map_dict.update({'sent':sent,
                                     'received':received})
                continue

            # TCP Map-Register (send/recv):                     1/0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                tcp_map_dict = instance_id_dict.setdefault('tcp_map_register', {})
                tcp_map_dict.update({'sent':sent,
                                     'received':received})
                continue

            # UDP Map-Notify (send/recv):                       0/2
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                udp_map_dict = instance_id_dict.setdefault('udp_map_notify', {})
                udp_map_dict.update({'sent':sent,
                                     'received':received})
                continue

            # TCP Map-Notify (send/recv):                       0/5
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                sent = int(groups['sent'])
                received = int(groups['received'])
                tcp_map_dict = instance_id_dict.setdefault('tcp_map_notify', {})
                tcp_map_dict.update({'sent':sent,
                                     'received':received})
                continue
        return ret_dict


class ShowLispExtranetSummarySchema(MetaParser):

    ''' Schema for "show lisp extranet summary" '''

    schema = {
          'lisp_id': {
              int: {
                    'total_extranets': int,
                    'max_allowed_ipv4_prefix' : int,
                    'total_ipv4_prefix':int,
                    'max_allowed_ipv6_prefix' : int,
                    'total_ipv6_prefix':int,
                    'extranet_name': {
                        str: {
                            'provider_iid': int,
                            'provider_ipv4_prefix_count': int,
                            'provider_ipv6_prefix_count': int,
                            'provider_total_prefix_count': int,
                            'subscriber_inst_count': int,
                            'subscriber_ipv4_prefix_count': int,
                            'subscriber_ipv6_prefix_count': int,
                            'subscriber_total_prefix_count': int,
                            'total_ipv4_prefix_count': int,
                            'total_ipv6_prefix_count': int,
                            'total_prefix_count': int,
                            },
                        },
                    },
                },
             }

# ==============================
# Parser for 'show lisp extranet summary'
# ==============================
class ShowLispExtranetSummary(ShowLispExtranetSummarySchema):

    ''' Parser for "show lisp extranet summary" '''

    cli_command = ["show lisp extranet summary",
                   "show lisp {lisp_id} extranet summary"]

    def cli(self, lisp_id=None, output=None):
        if not output:
            if lisp_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])

        parsed_dict = {}

        # Total extranets: 1
        p1 = re.compile(r"^Total\sextranets:\s+(?P<total_ext>\d+)")

        # Max allowed Extranet IPV4 EID prefixes: 4294967295
        p2 = re.compile(r"^Max\sallowed\sExtranet\sIPV4\sEID\sprefixes:\s+(?P<MAX_ALLOWED_IPV4_PREFIX>\d+)")

        # Total Extranet IPV4 EID prefixes      : 4
        p3 = re.compile(r"^Total\sExtranet\sIPV4\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV4_PREFIX>\d+)")

        # Max allowed Extranet IPV6 EID prefixes: 4294967295
        p4 = re.compile(r"^Max\sallowed\sExtranet\sIPV6\sEID\sprefixes:\s+(?P<MAX_ALLOWED_IPV6_PREFIX>\d+)")

        # Total Extranet IPV6 EID prefixes      : 0
        p5 = re.compile(r"^Total\sExtranet\sIPV6\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV6_PREFIX>\d+)")

        # Extranet name: ext1
        p6 = re.compile(r"^\s*Extranet\sname:\s+(?P<EXTRANET_NAME>\S+)")

        # Provider Instance ID : 111
        p7 = re.compile(r"^Provider\sInstance ID\s+:\s+(?P<PROVIDER_IID>\d+)")

        # Total Provider IPV4 EID prefixes : 0
        p8 = re.compile(r"^Total\sProvider\sIPV4\sEID\sprefixes\s+:\s+(?P<PROVIDER_IPV4_PREFIX_COUNT>\d+)")

        # Total Provider IPV6 EID prefixes : 0
        p9 = re.compile(r"^Total\sProvider\sIPV6\sEID\sprefixes\s+:\s+(?P<PROVIDER_IPV6_PREFIX_COUNT>\d+)")

        # Total Provider EID prefixes : 0
        p10 = re.compile(r"^Total\sProvider\sEID\sprefixes\s+:\s+(?P<PROVIDER_TOTAL_PREFIX_COUNT>\d+)")

        # Total Subscriber Instances : 1
        p11 = re.compile(r"^Total\sSubscriber\sInstances\s+:\s+(?P<SUBSCRIBER_INST_COUNT>\d+)")

        # Total Subscriber IPV4 EID prefixes  : 4
        p12 = re.compile(r"^Total\sSubscriber\sIPV4\sEID\sprefixes\s+:\s+(?P<SUBSCRIBER_IPV4_PREFIX_COUNT>\d+)")

        # Total Subscriber IPV6 EID prefixes  : 0
        p13 = re.compile(r"^Total\sSubscriber\sIPV6\sEID\sprefixes\s+:\s+(?P<SUBSCRIBER_IPV6_PREFIX_COUNT>\d+)")

        # Total Subscriber EID prefixes : 4
        p14 = re.compile(r"^Total\sSubscriber\sEID\sprefixes\s+:\s+(?P<SUBSCRIBER_TOTAL_PREFIX_COUNT>\d+)")

        # Total IPV4 EID prefixes  : 4
        p15 = re.compile(r"^Total\sIPV4\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV4_PREFIX_COUNT>\d+)")

        # Total IPV6 EID prefixes  : 0
        p16 = re.compile(r"^Total\sIPV6\sEID\sprefixes\s+:\s+(?P<TOTAL_IPV6_PREFIX_COUNT>\d+)")

        # Total EID prefixes  : 4
        p17 = re.compile(r"^Total\sEID\sprefixes\s+:\s+(?P<TOTAL_PREFIX_COUNT>\d+)")

        for line in output.splitlines():
            line = line.strip()

            if not lisp_id:
                lisp_id = 0
            else:
                lisp_id = int(lisp_id)

            lisp_id_dict = parsed_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})

            # Total extranets: 1
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                total_ext = int(groups['total_ext'])
                lisp_id_dict.update({'total_extranets': total_ext})
                continue

            # Max allowed Extranet IPV4 EID prefixes: 4294967295
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                max_allowed_ipv4_prefix = int(groups['MAX_ALLOWED_IPV4_PREFIX'])
                lisp_id_dict.update({'max_allowed_ipv4_prefix': max_allowed_ipv4_prefix})
                continue

            # Total Extranet IPV4 EID prefixes      : 4
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                total_ipv4_prefix = int(groups['TOTAL_IPV4_PREFIX'])
                lisp_id_dict.update({'total_ipv4_prefix': total_ipv4_prefix})
                continue

            # Max allowed Extranet IPV6 EID prefixes: 4294967295
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                max_allowed_ipv6_prefix = int(groups['MAX_ALLOWED_IPV6_PREFIX'])
                lisp_id_dict.update({'max_allowed_ipv6_prefix': max_allowed_ipv6_prefix})
                continue

            # Total Extranet IPV6 EID prefixes      : 0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                total_ipv6_prefix = int(groups['TOTAL_IPV6_PREFIX'])
                lisp_id_dict.update({'total_ipv6_prefix': total_ipv6_prefix})
                continue

            # Extranet name: ext1
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                ext_name = groups['EXTRANET_NAME']
                ext_dict = lisp_id_dict.setdefault('extranet_name', {}).setdefault(ext_name, {})
                continue

            # Provider Instance ID: 111
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                prov_iid = int(groups['PROVIDER_IID'])
                ext_dict.update({'provider_iid': prov_iid})

            # Total Provider IPV4 EID prefixes : 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                provider_ipv4_prefix_count = int(groups['PROVIDER_IPV4_PREFIX_COUNT'])
                ext_dict.update({'provider_ipv4_prefix_count': provider_ipv4_prefix_count})

            # Total Provider IPV6 EID prefixes : 0
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                provider_ipv6_prefix_count = int(groups['PROVIDER_IPV6_PREFIX_COUNT'])
                ext_dict.update({'provider_ipv6_prefix_count': provider_ipv6_prefix_count})

            # Total Provider EID prefixes : 0
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                provider_total_prefix_count = int(groups['PROVIDER_TOTAL_PREFIX_COUNT'])
                ext_dict.update({'provider_total_prefix_count': provider_total_prefix_count})

            # Total Subscriber Instances : 1
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                subscriber_inst_count = int(groups['SUBSCRIBER_INST_COUNT'])
                ext_dict.update({'subscriber_inst_count': subscriber_inst_count})

            # Total Subscriber IPV4 EID prefixes  : 4
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                subscriber_ipv4_prefix_count = int(groups['SUBSCRIBER_IPV4_PREFIX_COUNT'])
                ext_dict.update({'subscriber_ipv4_prefix_count': subscriber_ipv4_prefix_count})

            # Total Subscriber IPV6 EID prefixes  : 0
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                subscriber_ipv6_prefix_count = int(groups['SUBSCRIBER_IPV6_PREFIX_COUNT'])
                ext_dict.update({'subscriber_ipv6_prefix_count': subscriber_ipv6_prefix_count})

            # Total Subscriber EID prefixes  : 4
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                subscriber_total_prefix_count = int(groups['SUBSCRIBER_TOTAL_PREFIX_COUNT'])
                ext_dict.update({'subscriber_total_prefix_count': subscriber_total_prefix_count})

            # Total IPV4 EID prefixes : 4
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                total_ipv4_prefix_count = int(groups['TOTAL_IPV4_PREFIX_COUNT'])
                ext_dict.update({'total_ipv4_prefix_count': total_ipv4_prefix_count})

            # Total IPV6 EID prefixes  : 0
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                total_ipv6_prefix_count = int(groups['TOTAL_IPV6_PREFIX_COUNT'])
                ext_dict.update({'total_ipv6_prefix_count': total_ipv6_prefix_count})

            # Total EID prefixes : 4
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                total_prefix_count = int(groups['TOTAL_PREFIX_COUNT'])
                ext_dict.update({'total_prefix_count': total_prefix_count})

        return parsed_dict



class ShowLispSiteDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        *  show lisp site detail
        *  show lisp site name {site_name}
        *  show lisp site {eid}
        *  show lisp site {eid} instance-id {instance_id}
        *  show lisp site {eid} eid-table {eid_table}
        *  show lisp site {eid} eid-table vrf {vrf}
        *  show lisp {lisp_id} site detail
        *  show lisp {lisp_id} site name {site_name}
        *  show lisp {lisp_id} site {eid}
        *  show lisp {lisp_id} site {eid} instance-id {instance_id}
        *  show lisp {lisp_id} site {eid} eid-table {eid_table}
        *  show lisp {lisp_id} site {eid} eid-table vrf {vrf}
        *  show lisp locator-table {locator_table} site detail
        *  show lisp locator-table {locator_table} site name {site_name}
        *  show lisp locator-table {locator_table} site {eid}
        *  show lisp locator-table {locator_table} site {eid} instance-id {instance_id}
        *  show lisp locator-table {locator_table} site {eid} eid-table {eid_table}
        *  show lisp locator-table {locator_table} site {eid} eid-table vrf {vrf}
    '''
    cli_command = ['show lisp site detail',
                   'show lisp site name {site_name}',
                   'show lisp site {eid}',
                   'show lisp site {eid} instance-id {instance_id}',
                   'show lisp site {eid} eid-table {eid_table}',
                   'show lisp site {eid} eid-table vrf {vrf}',
                   'show lisp {lisp_id} site detail',
                   'show lisp {lisp_id} site name {site_name}',
                   'show lisp {lisp_id} site {eid}',
                   'show lisp {lisp_id} site {eid} instance-id {instance_id}',
                   'show lisp {lisp_id} site {eid} eid-table {eid_table}',
                   'show lisp {lisp_id} site {eid} eid-table vrf {vrf}',
                   'show lisp locator-table {locator_table} site detail',
                   'show lisp locator-table {locator_table} site name {site_name}',
                   'show lisp locator-table {locator_table} site {eid}',
                   'show lisp locator-table {locator_table} site {eid} instance-id {instance_id}',
                   'show lisp locator-table {locator_table} site {eid} eid-table {eid_table}',
                   'show lisp locator-table {locator_table} site {eid} eid-table vrf {vrf}']

    def cli(self, output=None, lisp_id=None, eid=None, instance_id=None, eid_table=None,
            vrf=None, locator_table=None, site_name=None):

        if output is None:
            if lisp_id and instance_id and eid:
                output = self.device.execute(self.cli_command[9].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, eid=eid))
            elif lisp_id and eid and eid_table:
                 output = self.device.execute(self.cli_command[10].\
                                             format(lisp_id=lisp_id, eid=eid, eid_table=eid_table))
            elif lisp_id and eid and vrf:
                 output = self.device.execute(self.cli_command[11].\
                                             format(lisp_id=lisp_id, eid=eid, vrf=vrf))
            elif locator_table and instance_id and eid:
                output = self.device.execute(self.cli_command[15].\
                                            format(locator_table=locator_table, instance_id=instance_id, eid=eid))
            elif locator_table and eid_table and eid:
                output = self.device.execute(self.cli_command[16].\
                                            format(locator_table=locator_table, eid_table=eid_table, eid=eid))
            elif locator_table and vrf and eid:
                output = self.device.execute(self.cli_command[17].\
                                            format(locator_table=locator_table, vrf=vrf, eid=eid))
            elif locator_table and eid:
                output = self.device.execute(self.cli_command[14].\
                                            format(locator_table=locator_table, eid=eid))
            elif locator_table and site_name:
                output = self.device.execute(self.cli_command[13].\
                                            format(locator_table=locator_table, site_name=site_name))
            elif lisp_id and eid:
                output = self.device.execute(self.cli_command[8].\
                                            format(lisp_id=lisp_id, eid=eid))
            elif lisp_id and site_name:
                output = self.device.execute(self.cli_command[7].\
                                            format(lisp_id=lisp_id, site_name=site_name))
            elif eid and instance_id:
                output = self.device.execute(self.cli_command[3].\
                                            format(eid=eid, instance_id=instance_id))
            elif eid and eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid=eid, eid_table=eid_table))
            elif eid and vrf:
                output = self.device.execute(self.cli_command[5].\
                                            format(eid=eid, vrf=vrf))
            elif eid:
                output = self.device.execute(self.cli_command[2].format(eid=eid))
            elif lisp_id:
                output = self.device.execute(self.cli_command[6].format(lisp_id=lisp_id))
            elif locator_table:
                output = self.device.execute(self.cli_command[12].format(locator_table=locator_table))
            elif site_name:
                output = self.device.execute(self.cli_command[1].format(site_name=site_name))
            else:
                output = self.device.execute(self.cli_command[0])
        return super().cli(output=output)


class ShowLispEthernetServerDetail(ShowLispSiteDetailSuperParser):
    ''' Parser for
        * show lisp instance-id {instance_id} ethernet server detail
        * show lisp instance-id {instance_id} ethernet server name {site_name}
        * show lisp instance-id {instance_id} ethernet server {eid}
        * show lisp instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server name {site_name}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server {eid}
        * show lisp {lisp_id} instance-id {instance_id} ethernet server etr-address {etr_address}
        * show lisp eid-table vrf {vrf} ethernet server detail
        * show lisp eid-table vrf {vrf} ethernet server name {site_name}
        * show lisp eid-table vrf {vrf} ethernet server {eid}
        * show lisp eid-table vrf {vrf} ethernet server etr-address {etr_address}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server detail
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server name {site_name}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server {eid}
        * show lisp locator-table {locator_table} instance-id {instance_id} ethernet server etr-address {etr_address}
    '''
    cli_command = ['show lisp instance-id {instance_id} ethernet server detail',
                   'show lisp instance-id {instance_id} ethernet server name {site_name}',
                   'show lisp instance-id {instance_id} ethernet server {eid}',
                   'show lisp instance-id {instance_id} ethernet server etr-address {etr_address}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server detail',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server name {site_name}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server {eid}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet server etr-address {etr_address}',
                   'show lisp eid-table vrf {vrf} ethernet server detail',
                   'show lisp eid-table vrf {vrf} ethernet server name {site_name}',
                   'show lisp eid-table vrf {vrf} ethernet server {eid}',
                   'show lisp eid-table vrf {vrf} ethernet server etr-address {etr_address}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server detail',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server name {site_name}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server {eid}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server etr-address {etr_address}']
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
            else:
                output = self.device.execute(self.cli_command[0].\
                                            format(instance_id=instance_id))
        return super().cli(output=output)


class ShowLispRegistrationHistorySchema(MetaParser):
    """
    Schema for 'show lisp {lisp_id} instance-id {instance_id} {address-family} server registration-history'
    """
    schema = {
        'lisp_id': {
            int: {
                'eid_address': {
                    str: ListOf({
                        'time': str,
                        'instance_id': int,
                        'protocol': str,
                        'roam': str,
                        'wlc': str,
                        'source': str,
                        'reg_type': str,
                        'eid': str,
                        'mask': int
                        })
                    }
                }
            }
        }


class ShowLispRegistrationHistory(ShowLispRegistrationHistorySchema):
    """
    Parser for 'show lisp {lisp_id} instance-id {instance_id} {address-family} server registration-history'
    """
    cli_command = ['show lisp {lisp_id} instance-id {instance_id} {address_family} server {eid} registration-history',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server registration-history',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server {address_resolution} {eid} registration-history',
                   'show lisp {lisp_id} instance-id {instance_id} {address_family} server {address_resolution} registration-history',
                   'show lisp instance-id {instance_id} {address_family} server registration-history',
                   'show lisp server registration-history']

    def cli(self, output=None, lisp_id=None, instance_id=None, address_family=None, eid=None, address_resolution=None):

        if output is None:
            if lisp_id and instance_id and address_family and address_resolution and eid:
                output = self.device.execute(self.cli_command[2].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family,\
                                                address_resolution=address_resolution, eid=eid))
            elif lisp_id and instance_id and address_family and address_resolution:
                output = self.device.execute(self.cli_command[3].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family,\
                                                address_resolution=address_resolution))
            elif lisp_id and instance_id and address_family and eid:
                output = self.device.execute(self.cli_command[0].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family,\
                                                eid=eid))
            elif lisp_id and instance_id and address_family:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family))
            elif instance_id and address_family:
                output = self.device.execute(self.cli_command[4].\
                                            format(instance_id=instance_id, address_family=address_family))
            else:
                output = self.device.execute(self.cli_command[5])
        ret_dict ={}

        # *Mar  5 20:40:31.737 17476    TCP   No   No  80.80.80.11
        p1 = re.compile(r"^(\*?)(?P<time>([\w:\s\.]+))\s+(?P<instance_id>\d+)\s+"
                        r"(?P<protocol>\S+)\s+(?P<roam>\S+)\s+(?P<wlc>\S+)\s+"
                        r"((?P<source>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|[a-fA-F\d\:]+)))$")

        # +*2001:192:168:1::71/128 / aabb.cc00.c901
        # + 0.0.0.0/0
        p2 = re.compile(r"^(?P<reg_type>\+|\-)\*?\s?(?P<eid>([0-9a-fA-F.:]+))"
                        r"\/(?P<mask>\d{1,3})(\s\/\s([a-fA-F\d]{4}\.){2}[a-fA-F\d]{4})?")

        for line in output.splitlines():
            line = line.strip()

            # *Mar  5 20:40:31.737 17476    TCP   No   No  80.80.80.11
            m = p1.match(line)
            if m:
                if lisp_id != "all":
                    lisp_id = int(lisp_id) if lisp_id else 0
                groups = m.groupdict()
                time = groups['time'].strip()
                instance_id = int(groups['instance_id'])
                protocol = groups['protocol']
                roam = groups['roam']
                wlc = groups['wlc']
                source = groups['source']
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                continue

            # +*2001:192:168:1::71/128 / aabb.cc00.c901
            # + 0.0.0.0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                reg_type = groups['reg_type']
                eid = groups['eid']
                mask = int(groups['mask'])
                eid_address = "{}/{}".format(eid,mask)
                eid_dict = lisp_id_dict.setdefault('eid_address',{})\
                                       .setdefault(eid_address,[])
                eid_dict.append({'time':time,
                                 'instance_id':instance_id,
                                 'protocol':protocol,
                                 'roam':roam,
                                 'wlc':wlc,
                                 'source':source,
                                 'reg_type':reg_type,
                                 'eid':eid,
                                 'mask':mask})
                continue
        return ret_dict


class ShowLispSchema(MetaParser):
    """
    Schema for 'show lisp'
    """
    schema = {
        'lisp_id': {
            int: {
                Optional('domain_id'): int,
                Optional('multihoming_id'): int,
                'locator_table': str,
                'locator_default_set': str,
                'eid_instance_count': str,
                'capability': ListOf(str),
                'tcp_path_mtu_discovery': bool
                }
            }
        }


class ShowLisp(ShowLispSchema):
    """
    Parser for 'show lisp'
    """
    cli_command = ['show lisp',
                   'show lisp {lisp_id}']

    def cli(self, output=None, lisp_id=None):

        if output is None:
            if lisp_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])
        ret_dict ={}

        # Output for router lisp 0
        p1 = re.compile(r'^Output\s+for\s+router\s+lisp\s+(?P<lisp_id>\d+)$')

        # Router-lisp ID:        0
        p2 = re.compile(r'^Router-lisp\s+ID:\s+(?P<lisp_id>\d+)$')

        # Domain ID:             0
        p3 = re.compile(r'^Domain\s+ID:\s+(?P<domain_id>\d+)$')

        # Multihoming ID:        0
        p4 = re.compile(r'^Multihoming\s+ID:\s+(?P<multihoming_id>\d+)$')

        # Locator table:         default
        p5 = re.compile(r'^Locator\s+table:\s+(?P<locator_table>\S+)$')

        # Locator default-set:   N/A
        p6 = re.compile(r'^Locator\s+default-set:\s+(?P<locator_default_set>\S+)$')

        # EID instance count:    7
        p7 = re.compile(r'^EID\s+instance count:\s+(?P<eid_instance_count>\d+)$')

        # Capability:            Publish-Subscribe Instance-ID
        # Capability:            Domain-Info
        p8 = re.compile(r'^Capability:\s+(?P<capability>Publish-Subscribe\s+Instance-ID|\S+)$')

        # Domain-Info
        p9 = re.compile(r'^(?P<domain>Domain-Info)$')

        # Route-Tag
        p10 = re.compile(r'^(?P<route>Route-Tag)$')

        # SGT
        p11 = re.compile(r'^(?P<sgt>SGT)$')

        # Default-originate
        p12 = re.compile(r'^(?P<default>Default-originate)$')

        # Service-registration
        p13 = re.compile(r'^(?P<service>Service-registration)$')

        # Extranet-policy-propagation
        p14 = re.compile(r'^(?P<extranet>Extranet-policy-propagation)$')

        # Default-ETR Route-metric
        p15 = re.compile(r'^(?P<etr>Default-ETR Route-metric)$')

        # Unknown vendor type skip
        p16 = re.compile(r'^(?P<vendor>Unknown\s+vendor\s+type\s+skip)$')

        # RAR-notify
        p17 = re.compile(r'^(?P<rar>RAR-notify)$')

        # Extended Subscription
        p18 = re.compile(r'^(?P<extended>Extended\s+Subscription)$')

        # Silent Host Detection
        p19 = re.compile(r'^(?P<shd>Silent\s+Host\s+Detection)$')
        
        # RTT Refresh
        p20 = re.compile(r'^(?P<rtt>RTT\s+Refresh)$')
        
        # RLOC Domain Path 
        p21 = re.compile(r'^(?P<rdp>RLOC\s+Domain\s+Path)$')

        # Publish-Subscribe EID
        p22 = re.compile(r'^(?P<pub_sub_eid>Publish-Subscribe\s+EID)$')

        # TCP path mtu discovery OFF
        p23 = re.compile(r'^TCP\s+path\s+mtu\s+discovery\s+(?P<tcp_path_mtu_discovery>ON|OFF)$')

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(lisp_id,{})
                continue

            # Router-lisp ID:        0
            m = p2.match(line)
            if m:
                if not lisp_id:
                    groups = m.groupdict()
                    lisp_id = int(groups['lisp_id'])
                    lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                           .setdefault(lisp_id,{})
                    continue

            # Domain ID:             0
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                domain_id = int(groups['domain_id'])
                lisp_id_dict.update({'domain_id':domain_id})
                continue

            # Multihoming ID:        0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = int(groups['multihoming_id'])
                lisp_id_dict.update({'multihoming_id':multihoming_id})
                continue

            # Locator table:         default
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                locator_table = groups['locator_table']
                lisp_id_dict.update({'locator_table':locator_table})
                continue

            # Locator default-set:   N/A
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                locator_default_set = groups['locator_default_set']
                lisp_id_dict.update({'locator_default_set':locator_default_set})
                continue

            # EID instance count:    7
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                eid_instance_count = groups['eid_instance_count']
                lisp_id_dict.update({'eid_instance_count':eid_instance_count})
                continue

            # Capability:            Publish-Subscribe Instance-ID
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                capability = groups['capability']
                capability_list = lisp_id_dict.setdefault('capability',[])
                capability_list.append(capability)
                continue

            # Domain-Info
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                domain = groups['domain']
                capability_list.append(domain)
                continue

            # Route-Tag
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                route = groups['route']
                capability_list.append(route)
                continue

            # SGT
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                sgt = groups['sgt']
                capability_list.append(sgt)
                continue

            # Default-originate
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                default = groups['default']
                capability_list.append(default)
                continue

            # Service-registration
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                service = groups['service']
                capability_list.append(service)
                continue

            # Extranet-policy-propagation
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                extranet = groups['extranet']
                capability_list.append(extranet)
                continue

            # Default-ETR Route-metric
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                etr = groups['etr']
                capability_list.append(etr)
                continue

            # Unknown vendor type skip
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                vendor = groups['vendor']
                capability_list.append(vendor)
                continue

            # RAR-notify
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                rar = groups['rar']
                capability_list.append(rar)
                continue
            
            # Extended Subscription
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                extended = groups['extended']
                capability_list.append(extended)
                continue

            # Silent Host Detection
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                shd = groups['shd']
                capability_list.append(shd)
                continue

            # RTT Refresh
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                rtt = groups['rtt']
                capability_list.append(rtt)
                continue

            # RLOC Domain Path
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                rdp = groups['rdp']
                capability_list.append(rdp)
                continue

            # Publish-Subscribe EID
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                pub_sub_eid = groups['pub_sub_eid']
                capability_list.append(pub_sub_eid)
                continue

            # TCP path mtu discovery OFF
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                tcp_path_mtu = groups['tcp_path_mtu_discovery']
                tcp_path_mtu_discovery = bool(re.search("ON",tcp_path_mtu))
                lisp_id_dict.update({'tcp_path_mtu_discovery':tcp_path_mtu_discovery})
                lisp_id_dict.update({'capability':capability_list})
                continue
        return ret_dict


class ShowLispInstanceIdServiceSchema(MetaParser):

    '''Schema for "show lisp all instance-id <instance_id> <service>" '''

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'locator_table': str,
                        'eid_table': str,
                        'itr': {
                            'enabled': bool,
                            'proxy_itr_router': bool,
                            Optional('proxy_itr_rloc'): str,
                            Optional('local_rloc_last_resort'): str,
                            Optional('use_proxy_etr_rloc'): list,
                            'solicit_map_request': str,
                            'max_smr_per_map_cache': str,
                            'multiple_smr_supression_time': int
                            },
                        'etr': {
                            'enabled': bool,
                            'proxy_etr_router': bool,
                            'accept_mapping_data': str,
                            'map_cache_ttl': str
                            },
                        Optional('nat_traversal_router'): bool,
                        Optional('mobility_first_hop_router'): str,
                        'map_server': {
                            'enabled': bool
                            },
                        'map_resolver': {
                            'enabled': bool
                            },
                        'delegated_database_tree': str,
                        'mr_use_petr': {
                            'role': str,
                            Optional('locator_set'): str,
                            },
                        'first_packet_petr': {
                            'role': str,
                            Optional('locator_set'): str
                            },
                        Optional('multiple_ip_per_mac'): bool,
                        Optional('mcast_flood_access_tunnel'): bool,
                        Optional('pub_sub_eid'): bool,
                        Optional('pub_sub'): {
                            'role': bool,
                            Optional('publishers'): ListOf(str),
                            Optional('subscribers'): ListOf(str)
                            },
                        Optional('site_registration_limit'): int,
                        Optional('mapping_servers'): {
                            Any():{
                                'ms_address': str,
                                Optional('prefix_list'): str
                                },
                            },
                        Optional('map_resolvers'): {
                            Any(): {
                                'mr_address': str,
                                Optional('prefix_list'): str
                                }
                            },
                        Optional('xtr_id'): str,
                        Optional('site_id'): str,
                        'locator_status_algorithms': {
                            'rloc_probe_algorithm': str,
                            'rloc_probe_on_route_change': bool,
                            'rloc_probe_member_change': str,
                            'lsb_reports': str,
                            'ipv4_rloc_min_mask_len': int,
                            'ipv6_rloc_min_mask_len': int
                            },
                        'map_cache': {
                            'static_mappings': int,
                            'size': int,
                            'limit': int,
                            'imported_route': {
                                'count': int,
                                'limit': int
                                },
                            'activity_check_period': int,
                            'signal_supress': bool,
                            'conservative_allocation': bool,
                            Optional('fib_updates'): str,
                            'persistent': str,
                            'activity_tracking': bool
                            },
                        'database': {
                            'total_database_mapping': int,
                            'static_database': {
                                'size': int,
                                'limit': int
                                },
                            'dynamic_database': {
                                'size': int,
                                'limit': int
                                },
                            'route_import': {
                                'size': int,
                                'limit': int
                                },
                            'import_site_reg': {
                                'size': int,
                                'limit': int
                                },
                            'dummy_database': {
                                'size': int,
                                'limit': int
                                },
                            'import_publication': {
                                'size': int,
                                'limit': int
                                },
                            'proxy_database': {
                                'size': int
                                },
                            'inactive': {
                                'size': int
                                }
                            },
                        'publication_entries_exported': {
                            'map_cache': int,
                            'rib': int,
                            'database': int,
                            'prefix_list': int
                            },
                        'site_reg_entries_exported': {
                            'map_cache': int,
                            'rib': int
                            },
                        Optional('source_locator_configuration'): {
                            'vlans': {
                                Any(): {
                                    'address': str,
                                    'interface': str,
                                    },
                                },
                            },
                        'encapsulation_type': str,
                        Optional('ethernet_fast_detection'): bool
                    }
                }
            }
        }
    }


class ShowLispInstanceIdService(ShowLispInstanceIdServiceSchema):

    '''Parser for "show lisp instance-id {instance_id} {service}"'''

    cli_command = ['show lisp instance-id {instance_id} {service}',
                   'show lisp all instance-id {instance_id} {service}',
                   'show lisp {lisp_id} instance-id {instance_id} {service}',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {service}']

    def cli(self, service, instance_id, lisp_id=None, locator_table=None, output=None):
        if output is None:
            if locator_table and instance_id and service:
                cmd = self.cli_command[3].format(locator_table=locator_table, instance_id=instance_id, service=service)
            elif lisp_id and instance_id and service:
                cmd = self.cli_command[2].format(lisp_id=lisp_id, instance_id=instance_id, service=service)
            elif instance_id and service:
                if "all" in self.cli_command:
                    cmd = self.cli_command[1].format(instance_id=instance_id, service=service)
                else:
                    cmd = self.cli_command[0].format(instance_id=instance_id, service=service)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        state_dict = {
            'disabled': False,
            'enabled': True}

        # Instance ID:                              4100
        p1 = re.compile(r'Instance ID:\s+(?P<instance_id>\d+)$')

        # Router-lisp ID:                      0
        p2 = re.compile(r'Router-lisp +ID *: +(?P<lisp_id>\d+)$')

        # Locator table:                       default
        p3 = re.compile(r'Locator +table *: +(?P<locator_table>\S+)$')

        # EID table:                                vrf red
        p4 = re.compile(r'EID table:\s+(?P<eid_table>.*)$')

        # Ingress Tunnel Router (ITR):         enabled
        # Egress Tunnel Router (ETR):          enabled
        p5 = re.compile(r'(Ingress|Egress) +Tunnel +Router '
                        r'+\((?P<type>(ITR|ETR))\) *: '
                        r'+(?P<enabled>(enabled|disabled))$')

        # Proxy-ITR Router (PITR):             disabled
        # Proxy-ETR Router (PETR):             disabled
        # Proxy-ETR Router (PETR):             enabled RLOCs: 10.10.10.10
        # Proxy-ITR Router (PITR):             enabled RLOCs: 2001:10:10:10::10
        p6 = re.compile(r'Proxy\-(ITR|ETR) +Router +\((?P<proxy_type>(PITR|PETR))\)'
                        r'*: +(?P<proxy_itr_router>(enabled|disabled))'
                        r'(?: +RLOCs: +(?P<proxy_itr_rloc>'
                        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|[a-fA-F\d\:]+))?$')

        # ITR local RLOC (last resort):             *** NOT FOUND ***
        p7 = re.compile(r'^ITR +local +RLOC +\(last +resort\):\s+'
                        r'(?P<local_rloc_last_resort>.*)$')

        # ITR use proxy ETR RLOC(Encap IID):        1.1.1.1 (self), 66.66.66.66
        p8 = re.compile(r'^ITR\s+use +proxy +ETR +RLOC\(Encap IID\) *'
                        r': +(?P<use_proxy_etr_rloc_1>[\d.]+ *'
                        r'(\(self\))?),? *(?P<use_proxy_etr_rloc_2>([\d.]+)|([a-fA-F\d\:]+))?$')

        # ITR Solicit Map Request (SMR):       accept and process
        p9 = re.compile(r'^ITR +Solicit +Map +Request +\(SMR\) *:'
                        r'+(?P<solicit_map_request>.*)$')

        # Max SMRs per map-cache entry:      8 more specifics
        p10 = re.compile(r'^Max SMRs per map-cache entry:\s+(?P<max_smr_per_map_cache>.*)$')

        # Multiple SMR suppression time:     20 secs
        p11 = re.compile(r'^Multiple +SMR +suppression +time *: +'
                        r'(?P<multiple_smr_supression_time>\d+) +secs$')

        # ETR accept mapping data:             disabled, verify disabled
        p12 = re.compile(r'^ETR +accept +mapping +data *: +(?P<accept_mapping_data>.*)$')

        # ETR map-cache TTL:                   1d00h
        p13 = re.compile(r'^ETR +map-cache +TTL *: +(?P<map_cache_ttl>\S+)$')

        # NAT-traversal Router (NAT-RTR):      disabled
        p14 = re.compile(r'^NAT-traversal +Router +\(NAT\-RTR\) *: +'
                         r'(?P<nat_traversal_router>(enabled|disabled))$')

        # Mobility First-Hop Router:           disabled
        p15 = re.compile(r'Mobility +First-Hop +Router *:'
                         r' +(?P<mobility_first_hop_router>(enabled|disabled))$')

        # Map Server (MS):                     disabled
        p16 = re.compile(r'Map +Server +\(MS\) *:'
                        r' +(?P<enabled>(enabled|disabled))$')

        # Map Resolver (MR):                   disabled
        p17 = re.compile(r'Map +Resolver +\(MR\) *:'
                         r' +(?P<enabled>enabled|disabled)$')

        # Delegated Database Tree (DDT):       disabled
        p18 = re.compile(r'Delegated +Database +Tree +\(DDT\) *:'
                         r' +(?P<delegated_database_tree>enabled|disabled)$')

        # Mr-use-petr:                              enabled
        p19 = re.compile(r'^Mr-use-petr:\s+(?P<role>enabled|disabled)$')

        # Mr-use-petr locator set name:             RLOC1
        p20 = re.compile(r'^Mr-use-petr locator set name:\s+(?P<locator_set>\S+)$')

        # First-Packet pETR:                        enabled
        p21 = re.compile(r'^First-Packet pETR:\s+(?P<role>enabled|disabled)$')

        # First-Packet pETR locator set name:       RLOC1
        p22 = re.compile(r'^First-Packet pETR locator set name:\s+(?P<locator_set>\S+)$')

        # Multiple IP per MAC support:              disabled
        p23 = re.compile(r'^Multiple IP per MAC support:\s+'
                         r'(?P<multiple_ip_per_mac>disabled|enabled)$')

        # Multicast Flood Access-Tunnel:            disabled
        p24 = re.compile(r'^Multicast Flood Access-Tunnel:\s+'
                         r'(?P<mcast_flood_access_tunnel>disabled|enabled)$')

        # Publication-Subscription-EID:             disabled
        p25_1 = re.compile(r'^Publication-Subscription-EID:\s+'
                         r'(?P<pub_sub_eid>disabled|enabled)$')

        # Publication-Subscription:                 enabled
        p25 = re.compile(r'^Publication-Subscription:\s+(?P<role>enabled|disabled)$')

        # Publisher(s):                           *** NOT FOUND ***
        p26 = re.compile(r'^Publisher\(s\):\s+(?P<publishers>[\d.:]+)(?: +.*)?$')

        # Subscriber(s):                           *** NOT FOUND ***
        p27 = re.compile(r'^Subscriber\(s\):\s+(?P<subscribers>.*)')

        # Site Registration Limit:                  0
        p28 = re.compile(r'Site Registration Limit:\s+(?P<site_registration_limit>\d+)$')

        # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
        p29 = re.compile(r'ITR +Map\-Resolver\(s\) *: +(?P<mr_address>.*)$')

        #                                      10.84.66.66 *** not reachable ***
        p30 = re.compile(r'^(?P<prefix_list>[\d.:]+)(?: +.*)?$')

        # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
        p31 = re.compile(r'ETR +Map\-Server\(s\) *: +(?P<ms_address>.*)$')

        # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
        p32 = re.compile(r'^xTR-ID *: +(?P<xtr_id>[a-fA-F0-9x-]+)$')

        # site-ID:                             unspecified
        p33 = re.compile(r'site-ID *: +(?P<site_id>\S+)$')

        # RLOC-probe algorithm:              disabled
        p34 = re.compile(r'RLOC\-probe +algorithm *: '
                         r'+(?P<rloc_probe_algorithm>enabled|disabled)$')

        # RLOC-probe on route change:        N/A (periodic probing disabled)
        p35 = re.compile(r'RLOC\-probe +on +route +change *: +(?P<rloc_probe_on_route_change>.*)$')

        # RLOC-probe on member change:       disabled
        p36 = re.compile(r'RLOC\-probe +on +member +change *:'
                         r' +(?P<rloc_probe_member_change>enabled|disabled)$')

        # LSB reports:                       process
        p37 = re.compile(r'LSB +reports *: +(?P<lsb_reports>\S+)$')

        # IPv4 RLOC minimum mask length:     /0
        p38 = re.compile(r'IPv4 +RLOC +minimum +mask +length *:'
                         r' +\/(?P<ipv4_rloc_min_mask_len>\d+)$')

        # IPv6 RLOC minimum mask length:     /0
        p39 = re.compile(r'IPv6 +RLOC +minimum +mask +length *:'
                         r' +\/(?P<ipv6_rloc_min_mask_len>\d+)$')

        # Static mappings configured:             1
        p40 = re.compile(r'Static mappings configured:\s+(?P<static_mappings>\d+)$')

        # Map-cache size/limit:                   2/4294967295
        p41 = re.compile(r'Map-cache size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # Imported route count/limit:             0/5000
        p42 = re.compile(r'Imported route count\/limit:\s+(?P<count>\d+)\/(?P<limit>\d+)$')

        # Map-cache activity check period:   60 secs
        p43 = re.compile(r'Map-cache +activity +check +period *:'
                         r' +(?P<activity_check_period>\d+) +secs$')

        # Map-cache signal suppress:              disabled
        p44 = re.compile(r'Map-cache signal suppress:\s+(?P<signal_supress>disabled|enabled)$')

        # Conservative-allocation:                disabled
        p45 = re.compile(r'Conservative-allocation:\s+(?P<conservative_allocation>disabled|enabled)$')

        # Map-cache FIB updates:                  established
        p46 = re.compile(r'Map-cache FIB updates:\s+(?P<fib_updates>\S+)$')

        # Persistent map-cache:              disabled
        p47 = re.compile(r'Persistent +map\-cache *:'
                         r' +(?P<persistent>enabled|disabled)$')

        # Map-cache activity-tracking:            enabled
        p48 = re.compile(r'Map-cache activity-tracking:\s+(?P<activity_tracking>\S+)$')

        # Total database mapping size:            2
        p49 = re.compile(r'Total database mapping size:\s+(?P<total_database_mapping>\d+)')

        # static database size/limit:             0/4294967295
        p50 = re.compile(r'static database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # dynamic database size/limit:            2/4294967295
        p51 = re.compile(r'dynamic database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # route-import database size/limit:       0/5000
        p52 = re.compile(r'route-import database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # import-site-reg database size/limit:    0/4294967295
        p53 = re.compile(r'import-site-reg database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # dummy database size/limit:              0/4294967295
        p54 = re.compile(r'dummy database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # import-publication database size/limit: 0/4294967295
        p55 = re.compile(r'import-publication database size\/limit:\s+(?P<size>\d+)\/(?P<limit>\d+)$')

        # proxy database size:                    0
        p56 = re.compile(r'proxy database size:\s+(?P<size>\d+)$')

        # Inactive (deconfig/away) size:          0
        p57 = re.compile(r'Inactive \(deconfig\/away\) size:\s+(?P<size>\d+)$')

        # Map-cache:                              0
        p58 = re.compile(r'Map-cache:\s+(?P<map_cache>\d+)')

        # RIB:                                    0
        p59 = re.compile(r'RIB:\s+(?P<rib>\d+)')

        # Database:                               0
        p60 = re.compile(r'Database:\s+(?P<database>\d+)')

        # Prefix-list:                            0
        p61 = re.compile(r'Prefix-list:\s+(?P<prefix_list>\d+)')

        #   Vlan100: 10.229.11.1 (Loopback0)
        p62 = re.compile(r'Vlan(?P<vlans>(\d+))\: +(?P<address>([0-9\.\:]+)) +'
                         r'\((?P<interface>(\S+))\)$')

        # Encapsulation type:                       vxlan
        p63 = re.compile(r'Encapsulation type:\s+(?P<encapsulation_type>\S+)$')

        # Ethernet Fast Detection:                  enabled
        # Ethernet Fast Detection:                  disabled
        p64 = re.compile(r'^Ethernet Fast Detection:\s+(?P<eth_fast_detect>enabled|disabled)$')

        count = 0
        for line in out.splitlines():
            line = line.strip()

            # Instance ID:                              4100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance_id = int(group['instance_id'])
                instance_dict = ret_dict.setdefault('lisp_id', {}).\
                                setdefault(None, {}).\
                                setdefault('instance_id',{}).\
                                setdefault(instance_id,{})
                continue

            # Router-lisp ID:                      0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                ret_dict['lisp_id'][lisp_id] = ret_dict['lisp_id'].pop(None)
                continue

            # Locator table:                       default
            m = p3.match(line)
            if m:
                group = m.groupdict()
                locator_table = group['locator_table']
                instance_dict.update({'locator_table':locator_table})
                continue

            # EID table:                                vrf red
            m = p4.match(line)
            if m:
                group = m.groupdict()
                eid_table = group['eid_table']
                instance_dict.update({'eid_table':eid_table})
                continue

            # Ingress Tunnel Router (ITR):         enabled
            # Egress Tunnel Router (ETR):          enabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                enabled = state_dict[group['enabled'].lower()]
                tunnel_type = m.groupdict()['type'].lower()
                if tunnel_type == 'itr':
                    itr_dict = instance_dict.setdefault('itr', {})
                    itr_dict.update({'enabled':enabled})
                elif tunnel_type == 'etr':
                    etr_dict = instance_dict.setdefault('etr', {})
                    etr_dict.update({'enabled':enabled})
                continue

            # Proxy-ITR Router (PITR):             disabled
            # Proxy-ETR Router (PETR):             disabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                proxy_type = group['proxy_type'].lower()
                proxy_itr_rloc = group['proxy_itr_rloc']
                proxy_itr_router = state_dict[group['proxy_itr_router'].lower()]
                if proxy_type == 'pitr':
                    itr_dict.update({'proxy_itr_router':proxy_itr_router})
                elif proxy_type == 'petr':
                    etr_dict.update({'proxy_etr_router':proxy_itr_router})
                if group['proxy_itr_rloc']:
                    itr_dict.update({'proxy_itr_rloc':proxy_itr_rloc})
                continue

            # ITR local RLOC (last resort):             *** NOT FOUND ***
            m = p7.match(line)
            if m:
                group = m.groupdict()
                local_rloc_last_resort = group['local_rloc_last_resort']
                itr_dict.update({'local_rloc_last_resort':local_rloc_last_resort})
                continue

            # ITR use proxy ETR RLOC(Encap IID):        1.1.1.1 (self), 66.66.66.66
            m = p8.match(line)
            if m:
                group = m.groupdict()
                proxy_list = itr_dict.setdefault('use_proxy_etr_rloc',[])
                if group['use_proxy_etr_rloc_1']:
                    use_proxy_etr_rloc_val = group['use_proxy_etr_rloc_1']
                    proxy_list.append(use_proxy_etr_rloc_val)
                if group['use_proxy_etr_rloc_2']:
                    use_proxy_etr_rloc_val = group['use_proxy_etr_rloc_2']
                    proxy_list.append(use_proxy_etr_rloc_val)
                continue

            # ITR Solicit Map Request (SMR):       accept and process
            m = p9.match(line)
            if m:
                group = m.groupdict()
                solicit_map_request = group['solicit_map_request'].strip()
                itr_dict.update({'solicit_map_request':solicit_map_request})
                continue

            # Max SMRs per map-cache entry:      8 more specifics
            m = p10.match(line)
            if m:
                group = m.groupdict()
                max_smr_per_map_cache = group['max_smr_per_map_cache']
                itr_dict.update({'max_smr_per_map_cache':max_smr_per_map_cache})
                continue

            # Multiple SMR suppression time:     20 secs
            m = p11.match(line)
            if m:
                group = m.groupdict()
                multiple_smr_supression_time = int(group['multiple_smr_supression_time'])
                itr_dict.update({'multiple_smr_supression_time':multiple_smr_supression_time})
                continue

            # ETR accept mapping data:             disabled, verify disabled
            m = p12.match(line)
            if m:
                group = m.groupdict()
                accept_mapping_data = group['accept_mapping_data']
                etr_dict.update({'accept_mapping_data':accept_mapping_data})
                continue

            # ETR map-cache TTL:                   1d00h
            m = p13.match(line)
            if m:
                group = m.groupdict()
                map_cache_ttl = group['map_cache_ttl']
                etr_dict.update({'map_cache_ttl':map_cache_ttl})
                continue

            # NAT-traversal Router (NAT-RTR):      disabled
            m = p14.match(line)
            if m:
                group = m.groupdict()
                nat_traversal_router = state_dict[group['nat_traversal_router'].lower()]
                instance_dict.update({'nat_traversal_router':nat_traversal_router})
                continue

            # Mobility First-Hop Router:           disabled
            m = p15.match(line)
            if m:
                group = m.groupdict()
                mobility_first_hop_router = group['mobility_first_hop_router']
                instance_dict.update({'mobility_first_hop_router':mobility_first_hop_router})
                continue

            # Map Server (MS):                     disabled
            m = p16.match(line)
            if m:
                group = m.groupdict()
                enabled = state_dict[group['enabled'].lower()]
                map_server_dict = instance_dict.setdefault('map_server',{})
                map_server_dict.update({'enabled':enabled})
                continue

            # Map Resolver (MR):                   disabled
            m = p17.match(line)
            if m:
                group = m.groupdict()
                enabled = state_dict[group['enabled'].lower()]
                map_resolver_dict = instance_dict.setdefault('map_resolver',{})
                map_resolver_dict.update({'enabled':enabled})
                continue

            # Delegated Database Tree (DDT):       disabled
            m = p18.match(line)
            if m:
                group = m.groupdict()
                delegated_database_tree = group['delegated_database_tree']
                instance_dict.update({'delegated_database_tree':delegated_database_tree})
                continue

            # Mr-use-petr:                              enabled
            m = p19.match(line)
            if m:
                group = m.groupdict()
                role = group['role']
                mr_dict = instance_dict.setdefault('mr_use_petr',{})
                mr_dict.update({'role':role})
                continue

            # Mr-use-petr locator set name:             RLOC1
            m = p20.match(line)
            if m:
                group = m.groupdict()
                locator_set = group['locator_set']
                mr_dict.update({'locator_set':locator_set})
                continue

            # First-Packet pETR:                        enabled
            m = p21.match(line)
            if m:
                group = m.groupdict()
                role = group['role']
                first_dict = instance_dict.setdefault('first_packet_petr',{})
                first_dict.update({'role':role})
                continue

            # First-Packet pETR locator set name:       RLOC1
            m = p22.match(line)
            if m:
                group = m.groupdict()
                locator_set = group['locator_set']
                first_dict.update({'locator_set':locator_set})
                continue

            # Multiple IP per MAC support:              disabled
            m = p23.match(line)
            if m:
                group = m.groupdict()
                multiple_ip_per_mac = state_dict[group['multiple_ip_per_mac'].lower()]
                instance_dict.update({'multiple_ip_per_mac':multiple_ip_per_mac})
                continue

            # Multicast Flood Access-Tunnel:            disabled
            m = p24.match(line)
            if m:
                group = m.groupdict()
                mcast_flood_access_tunnel = state_dict[group['mcast_flood_access_tunnel'].lower()]
                instance_dict.update({'mcast_flood_access_tunnel':mcast_flood_access_tunnel})
                continue

            # Publication-Subscription-EID:             disabled
            m = p25_1.match(line)
            if m:
                group = m.groupdict()
                pub_sub_eid = state_dict[group['pub_sub_eid'].lower()]
                instance_dict.update({'pub_sub_eid':pub_sub_eid})
                continue

            # Publication-Subscription:                 enabled
            m = p25.match(line)
            if m:
                group = m.groupdict()
                role = state_dict[group['role'].lower()]
                pub_sub_dict = instance_dict.setdefault('pub_sub',{})
                pub_sub_dict.update({'role':role})
                continue

            # Publisher(s):                           *** NOT FOUND ***
            m = p26.match(line)
            if m:
                group = m.groupdict()
                publishers = group['publishers'].split(',')
                publishers_list = pub_sub_dict.setdefault('publishers',[])
                for publish in publishers:
                    publishers_list.append(publish)

            # Subscriber(s):                           *** NOT FOUND ***
            m = p27.match(line)
            if m:
                group = m.groupdict()
                subscribers = group['subscribers'].split(',')
                subscribers_list = pub_sub_dict.setdefault('subscribers',[])
                for subscribers in subscribers_list:
                    subscribers.append(subscribers)

            # Site Registration Limit:                  0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                site_registration_limit = int(group['site_registration_limit'])
                instance_dict.update({'site_registration_limit':site_registration_limit})
                continue

            # ITR Map-Resolver(s):                 10.64.4.4, 10.166.13.13
            m = p29.match(line)
            if m:
                map_resolvers = m.groupdict()['mr_address'].split(',')
                for ms in map_resolvers:
                    try:
                        map_resolver, uptime = ms.split()
                        map_resolver = map_resolver.replace(' ', '')
                    except ValueError:
                        map_resolver = ms.replace(' ', '')
                    # Set etr_dict under service
                    etr_mr_dict = instance_dict.setdefault('map_resolvers', {}).\
                                    setdefault(map_resolver, {})
                    etr_mr_dict.update({'mr_address':map_resolver})
                    count = 1
                continue

            #                                  10.84.66.66 (never)
            m = p30.match(line)
            if m:
                group = m.groupdict()
                prefix_list = group['prefix_list']
                if count == 0:
                    publishers_list.append(prefix_list)
                elif etr_mr_dict:
                    etr_mr_dict.update({'prefix_list':prefix_list})
                else:
                    etr_ms_dict.update({'prefix_list':prefix_list})
                continue

            # ETR Map-Server(s):                   10.64.4.4 (17:49:58), 10.166.13.13 (00:00:35)
            m = p31.match(line)
            if m:
                map_servers = m.groupdict()['ms_address'].split(',')
                for ms in map_servers:
                    try:
                        map_server, uptime = ms.split()
                        map_server = map_server.replace(' ', '')
                    except:
                        map_server = ms.replace(' ', '')
                    # Set etr_dict under service
                    etr_ms_dict = instance_dict.setdefault('mapping_servers', {}).\
                                    setdefault(map_server, {})
                    etr_ms_dict.update({'ms_address':map_server})
                continue

            # xTR-ID:                              0x730E0861-0x12996F6D-0xEFEA2114-0xE1C951F7
            m = p32.match(line)
            if m:
                group = m.groupdict()
                xtr_id = group['xtr_id']
                instance_dict.update({'xtr_id':xtr_id})
                continue

            # site-ID:                             unspecified
            m = p33.match(line)
            if m:
                group = m.groupdict()
                site_id = group['site_id']
                instance_dict.update({'site_id':site_id})
                continue

            # RLOC-probe algorithm:              disabled
            m = p34.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_algorithm = group['rloc_probe_algorithm']
                locator_dict = instance_dict.setdefault('locator_status_algorithms',{})
                locator_dict.update({'rloc_probe_algorithm':rloc_probe_algorithm})
                continue

            # RLOC-probe on route change:        N/A (periodic probing disabled)
            m = p35.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_on_route_change = group['rloc_probe_on_route_change']
                if rloc_probe_on_route_change == "enabled":
                    locator_dict.update({'rloc_probe_on_route_change':True})
                else:
                    locator_dict.update({'rloc_probe_on_route_change':False})
                continue

            # RLOC-probe on member change:       disabled
            m = p36.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_member_change = group['rloc_probe_member_change']
                locator_dict.update({'rloc_probe_member_change':rloc_probe_member_change})
                continue

            # LSB reports:                       process
            m = p37.match(line)
            if m:
                group = m.groupdict()
                lsb_reports = group['lsb_reports']
                locator_dict.update({'lsb_reports':lsb_reports})
                continue

            # IPv4 RLOC minimum mask length:     /0
            m = p38.match(line)
            if m:
                group = m.groupdict()
                ipv4_rloc_min_mask_len = int(group['ipv4_rloc_min_mask_len'])
                locator_dict.update({'ipv4_rloc_min_mask_len':ipv4_rloc_min_mask_len})
                continue

            # IPv6 RLOC minimum mask length:     /0
            m = p39.match(line)
            if m:
                group = m.groupdict()
                ipv6_rloc_min_mask_len = int(group['ipv6_rloc_min_mask_len'])
                locator_dict.update({'ipv6_rloc_min_mask_len':ipv6_rloc_min_mask_len})
                continue

            # Static mappings configured:             1
            m = p40.match(line)
            if m:
                group = m.groupdict()
                static_mappings = int(group['static_mappings'])
                map_cache_dict = instance_dict.setdefault('map_cache',{})
                map_cache_dict.update({'static_mappings':static_mappings})
                continue

            # Map-cache size/limit:                   2/4294967295
            m = p41.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                map_cache_dict.update({'size':size,
                                       'limit':limit})
                continue

            # Imported route count/limit:             0/5000
            m = p42.match(line)
            if m:
                group = m.groupdict()
                count = int(group['count'])
                limit = int(group['limit'])
                imported_dict = map_cache_dict.setdefault('imported_route',{})
                imported_dict.update({'count':count,
                                       'limit':limit})
                continue

            # Map-cache activity check period:   60 secs
            m = p43.match(line)
            if m:
                group = m.groupdict()
                activity_check_period = int(group['activity_check_period'])
                map_cache_dict.update({'activity_check_period':activity_check_period})
                continue

            # Map-cache signal suppress:              disabled
            m = p44.match(line)
            if m:
                group = m.groupdict()
                signal_supress = state_dict[group['signal_supress'].lower()]
                map_cache_dict.update({'signal_supress':signal_supress})
                continue

            # Conservative-allocation:                disabled
            m = p45.match(line)
            if m:
                group = m.groupdict()
                conservative_allocation = state_dict[group['conservative_allocation'].lower()]
                map_cache_dict.update({'conservative_allocation':conservative_allocation})
                continue

            # Map-cache FIB updates:                  established
            m = p46.match(line)
            if m:
                group = m.groupdict()
                fib_updates = group['fib_updates']
                map_cache_dict.update({'fib_updates':fib_updates})
                continue

            # Persistent map-cache:              disabled
            m = p47.match(line)
            if m:
                group = m.groupdict()
                persistent = group['persistent']
                map_cache_dict.update({'persistent':persistent})
                continue

            # Map-cache activity-tracking:            enabled
            m = p48.match(line)
            if m:
                group = m.groupdict()
                activity_tracking = state_dict[group['activity_tracking'].lower()]
                map_cache_dict.update({'activity_tracking':activity_tracking})
                continue

            # Total database mapping size:            2
            m = p49.match(line)
            if m:
                group = m.groupdict()
                total_database_mapping = int(group['total_database_mapping'])
                database_dict = instance_dict.setdefault('database',{})
                database_dict.update({'total_database_mapping':total_database_mapping})
                continue

            # static database size/limit:             0/4294967295
            m = p50.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                static_dict = database_dict.setdefault('static_database',{})
                static_dict.update({'size':size,
                                    'limit':limit})
                continue

            # dynamic database size/limit:            2/4294967295
            m = p51.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                dynamic_dict = database_dict.setdefault('dynamic_database',{})
                dynamic_dict.update({'size':size,
                                    'limit':limit})
                continue

            # route-import database size/limit:       0/5000
            m = p52.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                route_dict = database_dict.setdefault('route_import',{})
                route_dict.update({'size':size,
                                    'limit':limit})
                continue

            # import-site-reg database size/limit:    0/4294967295
            m = p53.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                import_dict = database_dict.setdefault('import_site_reg',{})
                import_dict.update({'size':size,
                                    'limit':limit})
                continue

            # dummy database size/limit:              0/4294967295
            m = p54.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                dummy_dict = database_dict.setdefault('dummy_database',{})
                dummy_dict.update({'size':size,
                                   'limit':limit})
                continue

            # import-publication database size/limit: 0/4294967295
            m = p55.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                limit = int(group['limit'])
                import_dict = database_dict.setdefault('import_publication',{})
                import_dict.update({'size':size,
                                    'limit':limit})
                continue

            # proxy database size:                    0
            m = p56.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                proxy_dict = database_dict.setdefault('proxy_database',{})
                proxy_dict.update({'size':size})
                continue

            # Inactive (deconfig/away) size:          0
            m = p57.match(line)
            if m:
                group = m.groupdict()
                size = int(group['size'])
                inactive_dict = database_dict.setdefault('inactive',{})
                inactive_dict.update({'size':size})
                continue

            # Map-cache:                              0
            m = p58.match(line)
            if m:
                group = m.groupdict()
                map_cache = int(group['map_cache'])
                publication_dict = instance_dict.setdefault('publication_entries_exported',{})
                if 'map_cache' not in publication_dict:
                    publication_dict.update({'map_cache':map_cache})
                else:
                    site_reg_dict = instance_dict.setdefault('site_reg_entries_exported',{})
                    site_reg_dict.update({'map_cache':map_cache})
                continue

            # RIB:                                    0
            m = p59.match(line)
            if m:
                group = m.groupdict()
                rib = int(group['rib'])
                if 'rib' not in publication_dict:
                    publication_dict.update({'rib':rib})
                else:
                    site_reg_dict.update({'rib':rib})
                continue

            # Database:                               0
            m = p60.match(line)
            if m:
                group = m.groupdict()
                database = int(group['database'])
                publication_dict.update({'database':database})
                continue

            # Prefix-list:                            0
            m = p61.match(line)
            if m:
                group = m.groupdict()
                prefix_list = int(group['prefix_list'])
                publication_dict.update({'prefix_list':prefix_list})
                continue

            #    Vlan100: 10.229.11.1 (Loopback0)
            m = p62.match(line)
            if m:
                group = m.groupdict()
                vlans = group['vlans']
                address = group['address']
                interface = group['interface']
                source_dict = instance_dict.setdefault('source_locator_configuration',{}).\
                                setdefault('vlans',{}).\
                                setdefault(vlans,{})
                source_dict.update({'address':address,
                                    'interface':interface})
                continue

            # Encapsulation type:                       vxlan
            m = p63.match(line)
            if m:
                group = m.groupdict()
                encapsulation_type = group['encapsulation_type']
                instance_dict.update({'encapsulation_type':encapsulation_type})
                continue

            # Ethernet Fast Detection:                  enabled
            # Ethernet Fast Detection:                  disabled
            m = p64.match(line)
            if m:
                group = m.groupdict()
                fast_detect = group['eth_fast_detect'] == 'enabled'
                instance_dict.update({'ethernet_fast_detection': fast_detect})
                continue

        return ret_dict


class ShowLispSiteSummarySchema(MetaParser):
    """
    Schema for 'show lisp site summary'
    """
    schema = {
        'lisp_id': {
            int: {
                'site': {
                    str: {
                        'ipv4': {
                            'configured': int,
                            'registered': int,
                            'inconsistent': int
                            },
                        'ipv6': {
                            'configured': int,
                            'registered': int,
                            'inconsistent': int
                            },
                        'mac': {
                            'configured': int,
                            'registered': int,
                            'inconsistent': int
                            }
                        }
                    },
                'site_registration_limit': int,
                'site_registration_count': int,
                'ar_entries': int,
                'configured_sites': int,
                'registered_sites': int,
                'sites_with_inconsistent_reg': int,
                'configured_registered_prefixes': {
                    'ipv4': {
                        'configured': int,
                        'registered': int
                        },
                    Optional('ipv6'): {
                        'configured': int,
                        'registered': int
                        },
                    'mac': {
                        'configured': int,
                        'registered': int
                        }
                    }
                }
            }
        }


class ShowLispSiteSummary(ShowLispSiteSummarySchema):
    """
    Parser for 'show lisp site summary'
    """
    cli_command = ['show lisp site summary',
                   'show lisp {lisp_id} site summary',
                   'show lisp site summary instance-id {instance_id}',
                   'show lisp site summary eid-table vrf {vrf}',
                   'show lisp site summary eid-table {eid_table}']

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, eid_table=None):

        if output is None:
            if instance_id:
                output = self.device.execute(self.cli_command[2].\
                                            format(instance_id=instance_id))
            elif vrf:
                output = self.device.execute(self.cli_command[3].\
                                            format(vrf=vrf))
            elif eid_table:
                output = self.device.execute(self.cli_command[4].\
                                            format(eid_table=eid_table))
            elif lisp_id:
                output = self.device.execute(self.cli_command[1].\
                                            format(lisp_id=lisp_id))
            else:
                output = self.device.execute(self.cli_command[0])
        ret_dict = {}

        # Edoras                        0          0      0          0          0      0          0          0      0
        p1 = re.compile(r'^(?P<site>\S+)\s+(?P<v4_configured>\d+)\s+'
                        r'(?P<v4_registered>\d+)\s+(?P<v4_inconsistent>\d+)\s+'
                        r'(?P<v6_configured>\d+)\s+(?P<v6_registered>\d+)\s+'
                        r'(?P<v6_inconsistent>\d+)\s+(?P<mac_configured>\d+)\s+'
                        r'(?P<mac_registered>\d+)\s+(?P<mac_inconsistent>\d+)$')

        # Site-registration limit for router lisp 0:              0
        p2 = re.compile(r'^Site-registration\s+limit\s+for\s+'
                        r'router\s+lisp\s+(?P<lisp_id>\d+):\s+(?P<site_registration_limit>\d+)$')

        # Site-registration count for router lisp 0:              5
        p3 = re.compile(r'^Site-registration\s+count\s+for\s+router\s+lisp\s+\d+'
                        r':\s+(?P<site_registration_count>\d+)$')

        # Number of address-resolution entries:                   3
        p4 = re.compile(r'^Number\s+of\s+address-resolution\s+entries:\s+(?P<ar_entries>\d+)$')

        # Number of configured sites:                             2
        p5 = re.compile(r'^Number\s+of\s+configured\s+sites:\s+(?P<configured_sites>\d+)$')

        # Number of registered sites:                             1
        p6 = re.compile(r'^Number\s+of\s+registered\s+sites:\s+(?P<registered_sites>\d+)$')

        # Sites with inconsistent registrations:                  0
        p7 = re.compile(r'^Sites\s+with\s+inconsistent\s+registrations:'
                        r'\s+(?P<sites_with_inconsistent_reg>\d+)$')

        # Number of configured EID prefixes:                    4
        p8 = re.compile(r'^Number\s+of\s+configured\s+EID\s+prefixes:'
                        r'\s+(?P<ipv4_configured>\d+)$')

        # Number of registered EID prefixes:                    2
        p9 = re.compile(r'^Number\s+of\s+registered\s+EID\s+prefixes:'
                        r'\s+(?P<ipv4_registered>\d+)$')

        # IPv4
        # IPv6
        # MAC
        p10 = re.compile(r'^(?P<ip_version>IPv4|IPv6|MAC)$')

        for line in output.splitlines():
            line = line.strip()

            # Edoras                        0          0      0          0          0      0          0          0      0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                site = groups['site']
                v4_configured = int(groups['v4_configured'])
                v4_registered = int(groups['v4_registered'])
                v4_inconsistent = int(groups['v4_inconsistent'])
                v6_configured = int(groups['v6_configured'])
                v6_registered = int(groups['v6_registered'])
                v6_inconsistent = int(groups['v6_inconsistent'])
                mac_configured = int(groups['mac_configured'])
                mac_registered = int(groups['mac_registered'])
                mac_inconsistent = int(groups['mac_inconsistent'])
                lisp_id_dict = ret_dict.setdefault('lisp_id',{})\
                                       .setdefault(None,{})
                site_dict = lisp_id_dict.setdefault('site',{})\
                                        .setdefault(site,{})
                ipv4_dict = site_dict.setdefault('ipv4',{})
                ipv4_dict.update({'configured':v4_configured,
                                  'registered':v4_registered,
                                  'inconsistent':v4_inconsistent})
                ipv6_dict = site_dict.setdefault('ipv6',{})
                ipv6_dict.update({'configured':v6_configured,
                                  'registered':v6_registered,
                                  'inconsistent':v6_inconsistent})
                mac_dict = site_dict.setdefault('mac',{})
                mac_dict.update({'configured':mac_configured,
                                  'registered':mac_registered,
                                  'inconsistent':mac_inconsistent})
                continue

            # Site-registration limit for router lisp 0:              0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                site_registration_limit = int(groups['site_registration_limit'])
                ret_dict['lisp_id'][lisp_id] = ret_dict['lisp_id'].pop(None)
                lisp_id_dict.update({'site_registration_limit':site_registration_limit})
                continue

            # Site-registration count for router lisp 0:              5
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                site_registration_count = int(groups['site_registration_count'])
                lisp_id_dict.update({'site_registration_count':site_registration_count})
                continue

            # Number of address-resolution entries:                   3
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                ar_entries = int(groups['ar_entries'])
                lisp_id_dict.update({'ar_entries':ar_entries})
                continue

            # Number of configured sites:                             2
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                configured_sites = int(groups['configured_sites'])
                lisp_id_dict.update({'configured_sites':configured_sites})
                continue

            # Number of registered sites:                             1
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                registered_sites = int(groups['registered_sites'])
                lisp_id_dict.update({'registered_sites':registered_sites})
                continue

            # Sites with inconsistent registrations:                  0
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                sites_with_inconsistent_reg = int(groups['sites_with_inconsistent_reg'])
                lisp_id_dict.update({'sites_with_inconsistent_reg':sites_with_inconsistent_reg})
                continue

            # IPv4
            # IPv6
            # MAC
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                ip_version = groups['ip_version'].lower()
                ip_dict = lisp_id_dict.setdefault('configured_registered_prefixes',{})\
                                      .setdefault(ip_version,{})

            # Number of configured EID prefixes:                    4
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                configured = int(groups['ipv4_configured'])
                configured_reg_dict = lisp_id_dict.setdefault('configured_registered_prefixes',{})
                ip_dict.update({'configured':configured})
                continue

            # Number of registered EID prefixes:                    2
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                registered = int(groups['ipv4_registered'])
                ip_dict.update({'registered':registered})
                continue
        return ret_dict


class ShowLispInstanceIdServiceStatisticsSchema(MetaParser):

    ''' Schema for
    * show lisp instance-id {instance_id} {service} statistics
    * show lisp {lisp_id} {instance_id} {service} statistics
    * show lisp locator-table {locator_table} instance-id {instance_id} {service} statistics'''
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'last_cleared': str,
                        'control_packets': {
                            'map_requests': {
                                'in': int,
                                'out': int,
                                '5_sec': int,
                                '1_min': int,
                                '5_min': int,
                                'encapsulated': {
                                    'in': int,
                                    'out': int
                                    },
                                'rloc_probe': {
                                    'in': int,
                                    'out': int
                                    },
                                'smr_based': {
                                    'in': int,
                                    'out': int
                                    },
                                'expired': {
                                    'on_queue': int,
                                    'no_reply': int
                                    },
                                'map_resolver_forwarded': int,
                                'map_server_forwarded': int
                                },
                            'map_reply': {
                                'in': int,
                                'out': int,
                                'authoritative': {
                                    'in': int,
                                    'out': int
                                    },
                                'non_authoritative': {
                                    'in': int,
                                    'out': int
                                    },
                                'negative': {
                                    'in': int,
                                    'out': int
                                    },
                                'rloc_probe': {
                                    'in': int,
                                    'out': int
                                    },
                                'map_server_proxy_reply': {
                                    'out': int
                                    }
                                },
                            'wlc_map_subscribe': {
                                'in': int,
                                'out': int,
                                'failures': {
                                    'in': int,
                                    'out': int
                                    }
                                },
                            'wlc_map_unsubscribe': {
                                'in': int,
                                'out': int,
                                'failures': {
                                    'in': int,
                                    'out': int
                                    }
                                },
                            'map_register': {
                                'in': int,
                                'out': int,
                                '5_sec': int,
                                '1_min': int,
                                '5_min': int,
                                'map_server_af_disabled': int,
                                'not_valid_site_eid_prefix': int,
                                'authentication_failures': int,
                                'disallowed_locators': int,
                                'misc': int
                                },
                            'wlc_map_registers': {
                                'in': int,
                                'out': int,
                                'ap': {
                                    'in': int,
                                    'out': int
                                    },
                                'client': {
                                    'in': int,
                                    'out': int
                                    },
                                'failures': {
                                    'in': int,
                                    'out': int
                                    }
                                },
                            'map_notify': {
                                'in': int,
                                'out': int,
                                'authentication_failures': int
                                },
                            'wlc_map_notify': {
                                'in': int,
                                'out': int,
                                'ap': {
                                    'in': int,
                                    'out': int
                                    },
                                'client': {
                                    'in': int,
                                    'out': int
                                    },
                                'failures': {
                                    'in': int,
                                    'out': int
                                    }
                                },
                            'publish_subscribe': {
                                'subscription_request': {
                                    'in': int,
                                    'out': int,
                                    'iid': {
                                        'in': int,
                                        'out': int
                                        },
                                    'pub_refresh': {
                                        'in': int,
                                        'out': int
                                        },
                                    'policy': {
                                        'in': int,
                                        'out': int
                                        },
                                    'failures': {
                                        'in': int,
                                        'out': int
                                        }
                                    },
                                'subscription_status': {
                                    'in': int,
                                    'out': int,
                                    'end_of_publication': {
                                        'in': int,
                                        'out': int
                                        },
                                    'subscription_rejected': {
                                        'in': int,
                                        'out': int
                                        },
                                    'subscription_removed': {
                                        'in': int,
                                        'out': int
                                        },
                                    'failures': {
                                        'in': int,
                                        'out': int
                                        }
                                    },
                                'solicit_subscription': {
                                    'in': int,
                                    'out': int,
                                    'failures': {
                                        'in': int,
                                        'out': int
                                        }
                                    },
                                'publication': {
                                'in': int,
                                'out': int,
                                'failures': {
                                    'in': int,
                                    'out': int
                                    }
                                }
                                }
                            },
                        'errors': {
                            'mapping_rec_ttl_alerts': int,
                            'map_request_invalid_source_rloc_drops': int,
                            'map_register_invalid_source_rloc_drops': int,
                            'ddt_requests_failed': int,
                            'ddt_itr_map_requests': {
                                'dropped': int,
                                'nonce_collision': int,
                                'bad_xtr_nonce': int
                                }
                            },
                        'cache_related': {
                            'cache_entries': {
                                'created': int,
                                'deleted': int
                                },
                            'nsf_cef_replay_entry_count': int,
                            'eid_prefix_map_cache': int,
                            'rejected_eid_prefix_due_to_limit': int,
                            'times_signal_suppresion_turned_on': int,
                            'time_since_last_signal_suppressed': str,
                            'negative_entries_map_cache': int,
                            'total_rlocs_map_cache': int,
                            'average_rlocs_per_eid_prefix': int,
                            'policy_active_entries': int
                            },
                        'forwarding': {
                            'data_signals': {
                                'processed': int,
                                'dropped': int
                                },
                            'reachability_reports': {
                                'count': int,
                                'dropped': int
                                },
                            'smr_signals': {
                                'dropped': int
                                }
                            },
                        'itr_map_resolvers': {
                            str: {
                                'last_reply': str,
                                'metric': int,
                                'req_sent': int,
                                'positive': int,
                                'negative': int,
                                'no_reply': int,
                                'avgrtt': {
                                    '5_sec': int,
                                    '1_min': int,
                                    '5_min': int
                                    }
                                }
                            },
                        'etr_map_servers': {
                            str: {
                                'avgrtt': {
                                    '5_sec': int,
                                    '1_min': int,
                                    '5_min': int
                                    }
                                }
                            },
                        'rloc_statistics': {
                            'last_cleared': str,
                            'control_packets': {
                                'rtr': {
                                    'map_requests_forwarded': int,
                                    'map_notifies_forwarded': int
                                    },
                                'ddt': {
                                    'map_requests': {
                                        'in': int,
                                        'out': int
                                        },
                                    'map_referrals': {
                                        'in': int,
                                        'out': int
                                        }
                                    }
                                },
                            'errors': {
                                'map_request_format': int,
                                'map_reply_format': int,
                                'map_referral': int
                                }
                            },
                        'misc_statistics': {
                            'invalid': {
                                'ip_version_drops': int,
                                'ip_header_drops': int,
                                'ip_proto_field_drops': int,
                                'packet_size_drops': int,
                                'lisp_control_port_drops': int,
                                'lisp_checksum_drops': int,
                                },
                            'unsupported_lisp_packet_drops': int,
                            'unknown_packet_drops': int
                            }
                        }
                    }
                }
            }
        }



class ShowLispInstanceIdServiceStatistics(ShowLispInstanceIdServiceStatisticsSchema):
    ''' Parser for
    * show lisp instance-id {instance_id} {service} statistics
    * show lisp {lisp_id} {instance_id} {service} statistics
    * show lisp locator-table {locator_table} instance-id {instance_id} {service} statistics'''

    cli_command = ['show lisp instance-id {instance_id} {service} statistics',
                   'show lisp {lisp_id} {instance_id} {service} statistics',
                   'show lisp locator-table {locator_table} instance-id {instance_id} {service} statistics']

    def cli(self, output=None, lisp_id=None, instance_id=None, service=None, locator_table=None):

        if output is None:
            if lisp_id and instance_id and service:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, instance_id=instance_id, service=service))
            elif locator_table and instance_id and service:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, instance_id=instance_id, service=service))
            elif instance_id and service:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id, service=service))
            else:
                raise TypeError("No arguments provided to parser")
        ret_dict = {}

        # Output for router lisp 0
        # Output for router lisp 0 instance-id 101
        p1 = re.compile(r'^Output for router lisp (?P<lisp_id>\d+)(\s+instance-id\s+\d+)?$')

        # LISP EID Statistics for instance ID 4100 - last cleared: never
        p2 = re.compile(r'^LISP EID Statistics for instance ID (?P<instance_id>\d+) - last cleared: (?P<last_cleared>\S+)$')

        # Map-Requests in/out:                              1/24
        p3 = re.compile(r'^Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Requests in (5 sec/1 min/5 min):            0/0/0
        p4 = re.compile(r'^Map-Requests in \(5 sec\/1 min\/5 min\):\s+(?P<sec>\d+)\/(?P<min1>\d+)\/(?P<min5>\d+)$')

        # Encapsulated Map-Requests in/out:               0/23
        p5 = re.compile(r'^Encapsulated Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # RLOC-probe Map-Requests in/out:                 1/1
        p6 = re.compile(r'^RLOC-probe Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # SMR-based Map-Requests in/out:                  0/0
        p7 = re.compile(r'^SMR-based Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Requests expired on-queue/no-reply          0/3
        p8 = re.compile(r'^Map-Requests expired on-queue\/no-reply\s+(?P<on_queue>\d+)\/(?P<no_reply>\d+)$')

        # Map-Resolver Map-Requests forwarded:            0
        p9 = re.compile(r'^Map-Resolver Map-Requests forwarded:\s+(?P<map_resolver_forwarded>\d+)$')

        # Map-Server Map-Requests forwarded:              0
        p10 = re.compile(r'^Map-Server Map-Requests forwarded:\s+(?P<map_server_forwarded>\d+)$')

        # Map-Reply records in/out:                         24/1
        p11 = re.compile(r'^Map-Reply records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Authoritative records in/out:                   23/1
        p12 = re.compile(r'^Authoritative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Non-authoritative records in/out:               1/0
        p13 = re.compile(r'^Non-authoritative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Negative records in/out:                        22/0
        p14 = re.compile(r'^Negative records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # RLOC-probe records in/out:                      1/1
        p15 = re.compile(r'^RLOC-probe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Server Proxy-Reply records out:             0
        p16 = re.compile(r'^Map-Server Proxy-Reply records out:\s+(?P<out>\d+)$')

        # WLC Map-Subscribe records in/out:                 0/2
        p17 = re.compile(r'^WLC Map-Subscribe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Subscribe failures in/out:                  0/0
        p18 = re.compile(r'^Map-Subscribe failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Map-Unsubscribe records in/out:               0/0
        p19 = re.compile(r'^WLC Map-Unsubscribe records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Unsubscribe failures in/out:                0/0
        p20 = re.compile(r'^Map-Unsubscribe failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Register records in/out:                      0/6
        p21 = re.compile(r'^Map-Register records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Registers in (5 sec/1 min/5 min):           0/0/0
        p22 = re.compile(r'^Map-Registers in \(5 sec\/1 min\/5 min\):\s+(?P<sec_5>\d+)\/(?P<min_1>\d+)\/(?P<min_5>\d+)$')

        # Map-Server AF disabled:                         0
        p23 = re.compile(r'^Map-Server AF disabled:\s+(?P<map_server_af_disabled>\d+)$')

        # Not valid site eid prefix:                      0
        p24 = re.compile(r'^Not valid site eid prefix:\s+(?P<not_valid_site_eid_prefix>\d+)$')

        # Authentication failures:                        0
        p25 = re.compile(r'^Authentication failures:\s+(?P<authentication_failures>\d+)$')

        # Disallowed locators:                            0
        p26 = re.compile(r'^Disallowed locators:\s+(?P<disallowed_locators>\d+)$')

        # Miscellaneous:                                  0
        p27 = re.compile(r'^Miscellaneous:\s+(?P<misc>\d+)$')

        # WLC Map-Register records in/out:                  0/0
        p28 = re.compile(r'^WLC Map-Register records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC AP Map-Register in/out:                     0/0
        p29 = re.compile(r'^WLC AP Map-Register in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Client Map-Register in/out:                 0/0
        p30 = re.compile(r'^WLC Client Map-Register in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # WLC Map-Register failures in/out:               0/0
        p31 = re.compile(r'^WLC Map-Register failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Notify records in/out:                        8/0
        p32 = re.compile(r'^Map-Notify records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Authentication failures:                        0
        p33 = re.compile(r'^Authentication failures:\s+(?P<authentication_failures>\d+)')

        # WLC Map-Notify records in/out:                    0/0
        p34 = re.compile(r'^WLC Map-Notify records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC AP Map-Notify in/out:                       0/0
        p35 = re.compile(r'^WLC AP Map-Notify in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC Client Map-Notify in/out:                   0/0
        p36 = re.compile(r'^WLC Client Map-Notify in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)')

        # WLC Map-Notify failures in/out:                 0/0
        p37 = re.compile(r'^WLC Map-Notify failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Request records in/out:            0/4
        p38 = re.compile(r'^Subscription Request records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # IID subscription requests in/out:             0/0
        p39 = re.compile(r'^IID subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Pub-refresh subscription requests in/out:     0/0
        p40 = re.compile(r'^Pub-refresh subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Policy subscription requests in/out:          0/4
        p41 = re.compile(r'^Policy subscription requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Request failures in/out:           0/0
        p42 = re.compile(r'^Subscription Request failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Status records in/out:             2/0
        p43 = re.compile(r'^Subscription Status records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # End of Publication records in/out:            0/0
        p44 = re.compile(r'^End of Publication records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription rejected records in/out:         0/0
        p45 = re.compile(r'^Subscription rejected records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription removed records in/out:          0/0
        p46 = re.compile(r'^Subscription removed records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Subscription Status failures in/out:            0/0
        p47 = re.compile(r'^Subscription Status failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Solicit Subscription records in/out:            2/0
        p48 = re.compile(r'^Solicit Subscription records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Solicit Subscription failures in/out:           0/0
        p49 = re.compile(r'^Solicit Subscription failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Publication records in/out:                     0/0
        p50 = re.compile(r'^Publication records in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Publication failures in/out:                    0/0
        p51 = re.compile(r'^Publication failures in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Mapping record TTL alerts:                        0
        p52 = re.compile(r'^Mapping record TTL alerts:\s+(?P<mapping_rec_ttl_alerts>\d+)$')

        # Map-Request invalid source rloc drops:            0
        p53 = re.compile(r'^Map-Request invalid source rloc drops:\s+(?P<map_request_invalid_source_rloc>\d+)$')

        # Map-Register invalid source rloc drops:           0
        p54 = re.compile(r'^Map-Register invalid source rloc drops:\s+(?P<map_register_invalid_source_rloc>\d+)$')

        # DDT Requests failed:                              0
        p55 = re.compile(r'^DDT Requests failed:\s+(?P<ddt_requests_failed>\d+)$')

        # DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
        p56 = re.compile(r'^DDT ITR Map-Requests dropped:\s+(?P<dropped>\d+)\s+'
                         r'\(nonce-collision:\s+(?P<nonce_collision>\d+), '
                         r'bad-xTR-nonce:\s+(?P<bad_xtr_nonce>\d+)\)$')

        # Cache entries created/deleted:                    10/8
        p57 = re.compile(r'^Cache entries created\/deleted:\s+(?P<created>\d+)\/(?P<deleted>\d+)$')

        # NSF CEF replay entry count                        0
        p58 = re.compile(r'^NSF CEF replay entry count\s+(?P<nsf_cef_replay_entry_count>\d+)$')

        # Number of EID-prefixes in map-cache:              2
        p59 = re.compile(r'^Number of EID-prefixes in map-cache:\s+(?P<eid_prefix_map_cache>\d+)$')

        # Number of rejected EID-prefixes due to limit:     0
        p60 = re.compile(r'^Number of rejected EID-prefixes due to limit:\s+'
                         r'(?P<rejected_eid_prefix_due_to_limit>\d+)$')

        # Number of times signal suppression was turned on: 0
        p61 = re.compile(r'^Number of times signal suppression was turned on:\s+'
                         r'(?P<times_signal_suppresion_turned>\d+)$')

        # Time since last signal suppressed change:         never
        p62 = re.compile(r'^Time since last signal suppressed change:\s+'
                         r'(?P<time_since_last_signal>never|\d+)$')

        # Number of negative entries in map-cache:          2
        p63 = re.compile(r'^Number of negative entries in map-cache:\s+'
                         r'(?P<negative_entries_map_cache>\d+)$')

        # Total number of RLOCs in map-cache:               0
        p64 = re.compile(r'^Total number of RLOCs in map-cache:\s+(?P<total_rlocs_map_cache>\d+)$')

        # Average RLOCs per EID-prefix:                     0
        p65 = re.compile(r'^Average RLOCs per EID-prefix:\s+(?P<average_rlocs_per_eid_prefix>\d+)$')

        # Policy active entries:                            0
        p66 = re.compile(r'^Policy active entries:\s+(?P<policy_active_entries>\d+)$')

        # Number of data signals processed:                 2 (+ dropped 0)
        p67 = re.compile(r'^Number of data signals processed:\s+'
                         r'(?P<processed>\d+)\s+\(\+\s+dropped\s(?P<dropped>\d+)\)$')

        # Number of reachability reports:                   0 (+ dropped 0)
        p68 = re.compile(r'^Number of reachability reports:\s+'
                         r'(?P<count>\d+)\s+\(\+\s+dropped\s(?P<dropped>\d+)\)$')

        # Number of SMR signals dropped:                    0
        p69 = re.compile(r'^Number of SMR signals dropped:\s+(?P<dropped>\d+)$')

        #   44.44.44.44          6d21h      202176        8        0        0        6    0/ 0/ 0
        #   44:44:44:44::        6d21h      202176        8        0        0        6    0/ 0/ 0
        p70 = re.compile(r'^(?P<itr_map_resolvers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))'
                         r'\s+(?P<last_reply>\S+)\s+(?P<metric>\d+)\s+(?P<req_sent>\d+)\s+'
                         r'(?P<positive>\d+)\s+(?P<negative>\d+)\s+(?P<no_reply>\d+)\s+'
                         r'(?P<sec_5>\d+)\/\s(?P<min_1>\d+)\/\s(?P<min_5>\d+)$')

        # 44.44.44.44          0/ 0/ 0
        # 44:44:44:44::        0/ 0/ 0
        p71 = re.compile(r'^(?P<etr_map_servers>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+'
                         r'(?P<sec_5>\d+)\/\s+(?P<min_1>\d+)\/\s(?P<min_5>\d+)$')

        # LISP RLOC Statistics - last cleared: never
        p72 = re.compile(r'^LISP RLOC Statistics - last cleared:\s(?P<last_cleared>\S+)$')

        # RTR Map-Requests forwarded:                       0
        p73 = re.compile(r'^RTR Map-Requests forwarded:\s+(?P<map_requests_forwarded>\d+)$')

        # RTR Map-Notifies forwarded:                       0
        p74 = re.compile(r'^RTR Map-Notifies forwarded:\s+(?P<map_notifies_forwarded>\d+)$')

        # DDT-Map-Requests in/out:                          0/0
        p75 = re.compile(r'^DDT-Map-Requests in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # DDT-Map-Referrals in/out:                         0/0
        p76 = re.compile(r'^DDT-Map-Referrals in\/out:\s+(?P<in>\d+)\/(?P<out>\d+)$')

        # Map-Request format errors:                        0
        p77 = re.compile(r'^Map-Request format errors:\s+(?P<map_request_format>\d+)$')

        # Map-Reply format errors:                          0
        p78 = re.compile(r'^Map-Reply format errors:\s+(?P<map_reply_format>\d+)$')

        # Map-Referral format errors:                       0
        p79 = re.compile(r'^Map-Referral format errors:\s+(?P<map_referral>\d+)$')

        # Invalid IP version drops:                         0
        p80 = re.compile(r'^Invalid IP version drops:\s+(?P<ip_version_drops>\d+)$')

        # Invalid IP header drops:                          0
        p81 = re.compile(r'^Invalid IP header drops:\s+(?P<ip_header_drops>\d+)$')

        # Invalid IP proto field drops:                     0
        p82 = re.compile(r'^Invalid IP proto field drops:\s+(?P<ip_proto_field_drops>\d+)$')

        # Invalid packet size drops:                        0
        p83 = re.compile(r'^Invalid packet size drops:\s+(?P<packet_size_drops>\d+)$')

        # Invalid LISP control port drops:                  0
        p84 = re.compile(r'^Invalid LISP control port drops:\s+(?P<lisp_control_port_drops>\d+)$')

        # Invalid LISP checksum drops:                      0
        p85 = re.compile(r'^Invalid LISP checksum drops:\s+(?P<lisp_checksum_drops>\d+)$')

        # Unsupported LISP packet type drops:               0
        p86 = re.compile(r'^Unsupported LISP packet type drops:\s+(?P<unsupported_lisp_packet_drops>\d+)$')

        # Unknown packet drops:                             0
        p87 = re.compile(r'^Unknown packet drops:\s+(?P<unknown_packet_drops>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # Output for router lisp 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                lisp_dict = ret_dict.setdefault('lisp_id',{}).\
                                     setdefault(lisp_id,{})
                continue

            # LISP EID Statistics for instance ID 4100 - last cleared: never
            m = p2.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                lisp_dict = ret_dict.setdefault('lisp_id', {}).setdefault(lisp_id, {})
                group = m.groupdict()
                instance_id = int(group['instance_id'])
                last_cleared = group['last_cleared']
                instance_dict = lisp_dict.setdefault('instance_id',{}).\
                                          setdefault(instance_id,{})
                instance_dict.update({'last_cleared':last_cleared})
                continue

            # Map-Requests in/out:                              1/24
            m = p3.match(line)
            if m:
                group = m.groupdict()
                map_in = int(group['in'])
                out = int(group['out'])
                control_dict = instance_dict.setdefault('control_packets',{})
                map_dict = control_dict.setdefault('map_requests',{})
                map_dict.update({'in':map_in,
                                 'out':out})
                continue

            # Map-Requests in (5 sec/1 min/5 min):            0/0/0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sec = int(group['sec'])
                min5 = int(group['min5'])
                min1 = int(group['min1'])
                map_dict.update({'5_sec':sec,
                                 '1_min':min1,
                                 '5_min':min5})
                continue

            # Encapsulated Map-Requests in/out:               0/23
            m = p5.match(line)
            if m:
                group = m.groupdict()
                encap_in = int(group['in'])
                out = int(group['out'])
                encap_dict = map_dict.setdefault('encapsulated',{})
                encap_dict.update({'in':encap_in,
                                 'out':out})
                continue

            # RLOC-probe Map-Requests in/out:                 1/1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                encap_in = int(group['in'])
                out = int(group['out'])
                rloc_dict = map_dict.setdefault('rloc_probe',{})
                rloc_dict.update({'in':encap_in,
                                 'out':out})
                continue

            # SMR-based Map-Requests in/out:                  0/0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                smr_in = int(group['in'])
                out = int(group['out'])
                smr_dict = map_dict.setdefault('smr_based',{})
                smr_dict.update({'in':smr_in,
                                 'out':out})
                continue

            # Map-Requests expired on-queue/no-reply          0/3
            m = p8.match(line)
            if m:
                group = m.groupdict()
                on_queue = int(group['on_queue'])
                no_reply = int(group['no_reply'])
                expired_dict = map_dict.setdefault('expired',{})
                expired_dict.update({'on_queue':on_queue,
                                     'no_reply':no_reply})
                continue

            # Map-Resolver Map-Requests forwarded:            0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                map_resolver_forwarded = int(group['map_resolver_forwarded'])
                map_dict.update({'map_resolver_forwarded':map_resolver_forwarded})
                continue

            # Map-Server Map-Requests forwarded:              0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                map_server_forwarded = int(group['map_server_forwarded'])
                map_dict.update({'map_server_forwarded':map_server_forwarded})
                continue

            # Map-Reply records in/out:                         24/1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                map_reply_in = int(group['in'])
                out = int(group['out'])
                map_reply_dict = control_dict.setdefault('map_reply',{})
                map_reply_dict.update({'in':map_reply_in,
                                       'out':out})
                continue

            # Authoritative records in/out:                   23/1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                auth_in = int(group['in'])
                out = int(group['out'])
                auth_dict = map_reply_dict.setdefault('authoritative',{})
                auth_dict.update({'in':auth_in,
                                  'out':out})
                continue

            # Non-authoritative records in/out:               1/0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                non_auth_in = int(group['in'])
                out = int(group['out'])
                non_auth_dict = map_reply_dict.setdefault('non_authoritative',{})
                non_auth_dict.update({'in':non_auth_in,
                                      'out':out})
                continue

            # Negative records in/out:                        22/0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                negative_in = int(group['in'])
                out = int(group['out'])
                negative_dict = map_reply_dict.setdefault('negative',{})
                negative_dict.update({'in':negative_in,
                                      'out':out})
                continue

            # RLOC-probe records in/out:                      1/1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                rloc_probe_in = int(group['in'])
                out = int(group['out'])
                rloc_probe_dict = map_reply_dict.setdefault('rloc_probe',{})
                rloc_probe_dict.update({'in':rloc_probe_in,
                                        'out':out})
                continue

            # Map-Server Proxy-Reply records out:             0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                out = int(group['out'])
                map_server_dict = map_reply_dict.setdefault('map_server_proxy_reply',{})
                map_server_dict.update({'out':out})
                continue

            # WLC Map-Subscribe records in/out:                 0/2
            m = p17.match(line)
            if m:
                group = m.groupdict()
                wlc_in = int(group['in'])
                out = int(group['out'])
                wlc_dict = control_dict.setdefault('wlc_map_subscribe',{})
                wlc_dict.update({'in':wlc_in,
                                 'out':out})
                continue

            # Map-Subscribe failures in/out:                  0/0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                sub_in = int(group['in'])
                out = int(group['out'])
                fail_dict = wlc_dict.setdefault('failures',{})
                fail_dict.update({'in':sub_in,
                                  'out':out})
                continue

            # WLC Map-Unsubscribe records in/out:               0/0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                unsub_in = int(group['in'])
                out = int(group['out'])
                wlc_unsub_dict = control_dict.setdefault('wlc_map_unsubscribe',{})
                wlc_unsub_dict.update({'in':unsub_in,
                                       'out':out})
                continue

            # Map-Unsubscribe failures in/out:                0/0
            m = p20.match(line)
            if m:
                group = m.groupdict()
                fail_unsub_in = int(group['in'])
                out = int(group['out'])
                wlc_map_unsub_dict = wlc_unsub_dict.setdefault('failures',{})
                wlc_map_unsub_dict.update({'in':fail_unsub_in,
                                           'out':out})
                continue

            # Map-Register records in/out:                      0/6
            m = p21.match(line)
            if m:
                group = m.groupdict()
                map_record_in = int(group['in'])
                out = int(group['out'])
                map_reg_record_dict = control_dict.setdefault('map_register',{})
                map_reg_record_dict.update({'in':map_record_in,
                                           'out':out})
                continue

            # Map-Registers in (5 sec/1 min/5 min):           0/0/0
            m = p22.match(line)
            if m:
                group = m.groupdict()
                sec_5 = int(group['sec_5'])
                min_1 = int(group['min_1'])
                min_5 = int(group['min_5'])
                map_reg_record_dict.update({'5_sec':sec_5,
                                           '1_min':min_1,
                                           '5_min':min_5})
                continue

            # Map-Server AF disabled:                         0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                map_server_af_disabled = int(group['map_server_af_disabled'])
                map_reg_record_dict.update({'map_server_af_disabled':map_server_af_disabled})
                continue

            # Not valid site eid prefix:                      0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                not_valid_site_eid_prefix = int(group['not_valid_site_eid_prefix'])
                map_reg_record_dict.update({'not_valid_site_eid_prefix':not_valid_site_eid_prefix})
                continue

            # Authentication failures:                        0
            m = p25.match(line)
            if m and "authentication_failures" not in map_reg_record_dict:
                group = m.groupdict()
                authentication_failures = int(group['authentication_failures'])
                map_reg_record_dict.update({'authentication_failures':authentication_failures})
                continue

            # Disallowed locators:                            0
            m = p26.match(line)
            if m:
                group = m.groupdict()
                disallowed_locators = int(group['disallowed_locators'])
                map_reg_record_dict.update({'disallowed_locators':disallowed_locators})
                continue

            # Miscellaneous:                                  0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                misc = int(group['misc'])
                map_reg_record_dict.update({'misc':misc})
                continue

            # WLC Map-Register records in/out:                  0/0
            m = p28.match(line)
            if m:
                group = m.groupdict()
                wlc_map_in = int(group['in'])
                out = int(group['out'])
                wlc_map_registers_dict = control_dict.setdefault('wlc_map_registers',{})
                wlc_map_registers_dict.update({'in':wlc_map_in,
                                               'out':out})
                continue

            # WLC AP Map-Register in/out:                     0/0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                wlc_ap_map_in = int(group['in'])
                out = int(group['out'])
                wlc_ap_dict = wlc_map_registers_dict.setdefault('ap',{})
                wlc_ap_dict.update({'in':wlc_ap_map_in,
                                    'out':out})
                continue

            # WLC Client Map-Register in/out:                 0/0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                wlc_client_map_in = int(group['in'])
                out = int(group['out'])
                wlc_client_dict = wlc_map_registers_dict.setdefault('client',{})
                wlc_client_dict.update({'in':wlc_client_map_in,
                                        'out':out})
                continue

            # WLC Map-Register failures in/out:               0/0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                wlc_fail_map_in = int(group['in'])
                out = int(group['out'])
                wlc_fail_dict = wlc_map_registers_dict.setdefault('failures',{})
                wlc_fail_dict.update({'in':wlc_fail_map_in,
                                      'out':out})
                continue

            # Map-Notify records in/out:                        8/0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                map_notify_in = int(group['in'])
                out = int(group['out'])
                map_notify_dict = control_dict.setdefault('map_notify',{})
                map_notify_dict.update({'in':map_notify_in,
                                        'out':out})
                continue

            # Authentication failures:                        0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                authentication_failures = int(group['authentication_failures'])
                map_notify_dict.update({'authentication_failures':authentication_failures})
                continue

            # WLC Map-Notify records in/out:                    0/0
            m = p34.match(line)
            if m:
                group = m.groupdict()
                wlc_map_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_map_notify_dict = control_dict.setdefault('wlc_map_notify',{})
                wlc_map_notify_dict.update({'in':wlc_map_notify_in,
                                            'out':out})
                continue

            # WLC AP Map-Notify in/out:                       0/0
            m = p35.match(line)
            if m:
                group = m.groupdict()
                wlc_ap_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_ap_notify_dict = wlc_map_notify_dict.setdefault('ap',{})
                wlc_ap_notify_dict.update({'in':wlc_ap_notify_in,
                                           'out':out})
                continue

            # WLC Client Map-Notify in/out:                   0/0
            m = p36.match(line)
            if m:
                group = m.groupdict()
                wlc_client_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_client_notify_dict = wlc_map_notify_dict.setdefault('client',{})
                wlc_client_notify_dict.update({'in':wlc_client_notify_in,
                                               'out':out})
                continue

            # WLC Map-Notify failures in/out:                 0/0
            m = p37.match(line)
            if m:
                group = m.groupdict()
                wlc_failures_notify_in = int(group['in'])
                out = int(group['out'])
                wlc_fail_notify_dict = wlc_map_notify_dict.setdefault('failures',{})
                wlc_fail_notify_dict.update({'in':wlc_failures_notify_in,
                                             'out':out})
                continue

            # Subscription Request records in/out:            0/4
            m = p38.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                publish_dict = control_dict.setdefault('publish_subscribe',{})
                subscription_request_dict = publish_dict.setdefault('subscription_request',{})
                subscription_request_dict.update({'in':sub_request_in,
                                                  'out':out})
                continue

            # IID subscription requests in/out:             0/0
            m = p39.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                iid_dict = subscription_request_dict.setdefault('iid',{})
                iid_dict.update({'in':iid_in,
                                 'out':out})
                continue

            # Pub-refresh subscription requests in/out:     0/0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                pub_in = int(group['in'])
                out = int(group['out'])
                pub_refresh_dict = subscription_request_dict.setdefault('pub_refresh',{})
                pub_refresh_dict.update({'in':pub_in,
                                         'out':out})
                continue

            # Policy subscription requests in/out:          0/4
            m = p41.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                policy_dict = subscription_request_dict.setdefault('policy',{})
                policy_dict.update({'in':policy_in,
                                    'out':out})
                continue

            # Subscription Request failures in/out:           0/0
            m = p42.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                failures_dict = subscription_request_dict.setdefault('failures',{})
                failures_dict.update({'in':policy_in,
                                      'out':out})
                continue

            # Subscription Status records in/out:             2/0
            m = p43.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                sub_status_dict = publish_dict.setdefault('subscription_status',{})
                sub_status_dict.update({'in':sub_request_in,
                                        'out':out})
                continue

            # End of Publication records in/out:            0/0
            m = p44.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                end_pub_dict = sub_status_dict.setdefault('end_of_publication',{})
                end_pub_dict.update({'in':iid_in,
                                     'out':out})
                continue

            # Subscription rejected records in/out:         0/0
            m = p45.match(line)
            if m:
                group = m.groupdict()
                pub_in = int(group['in'])
                out = int(group['out'])
                sub_reject_dict = sub_status_dict.setdefault('subscription_rejected',{})
                sub_reject_dict.update({'in':pub_in,
                                        'out':out})
                continue

            # Subscription removed records in/out:          0/0
            m = p46.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                sub_removed_dict = sub_status_dict.setdefault('subscription_removed',{})
                sub_removed_dict.update({'in':policy_in,
                                         'out':out})
                continue

            # Subscription Status failures in/out:            0/0
            m = p47.match(line)
            if m:
                group = m.groupdict()
                policy_in = int(group['in'])
                out = int(group['out'])
                sub_failures_dict = sub_status_dict.setdefault('failures',{})
                sub_failures_dict.update({'in':policy_in,
                                          'out':out})
                continue

            # Solicit Subscription records in/out:            2/0
            m = p48.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                solicit_subscription_dict = publish_dict.setdefault('solicit_subscription',{})
                solicit_subscription_dict.update({'in':sub_request_in,
                                                  'out':out})
                continue

            # Solicit Subscription failures in/out:           0/0
            m = p49.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                solicit_fail_dict = solicit_subscription_dict.setdefault('failures',{})
                solicit_fail_dict.update({'in':iid_in,
                                          'out':out})
                continue

            # Publication records in/out:                     0/0
            m = p50.match(line)
            if m:
                group = m.groupdict()
                sub_request_in = int(group['in'])
                out = int(group['out'])
                solicit_publication_dict = publish_dict.setdefault('publication',{})
                solicit_publication_dict.update({'in':sub_request_in,
                                                 'out':out})
                continue

            # Publication failures in/out:                    0/0
            m = p51.match(line)
            if m:
                group = m.groupdict()
                iid_in = int(group['in'])
                out = int(group['out'])
                solicit_failure_dict = solicit_publication_dict.setdefault('failures',{})
                solicit_failure_dict.update({'in':iid_in,
                                             'out':out})
                continue

            # Mapping record TTL alerts:                        0
            m = p52.match(line)
            if m:
                group = m.groupdict()
                mapping_rec_ttl_alerts = int(group['mapping_rec_ttl_alerts'])
                error_dict = instance_dict.setdefault('errors',{})
                error_dict.update({'mapping_rec_ttl_alerts':mapping_rec_ttl_alerts})
                continue

            # Map-Request invalid source rloc drops:            0
            m = p53.match(line)
            if m:
                group = m.groupdict()
                map_request_invalid_source_rloc_drops = int(group['map_request_invalid_source_rloc'])
                error_dict.update({'map_request_invalid_source_rloc_drops':map_request_invalid_source_rloc_drops})
                continue

            # Map-Register invalid source rloc drops:           0
            m = p54.match(line)
            if m:
                group = m.groupdict()
                map_register_invalid_source_rloc_drops = int(group['map_register_invalid_source_rloc'])
                error_dict.update({'map_register_invalid_source_rloc_drops':map_register_invalid_source_rloc_drops})
                continue

            # DDT Requests failed:                              0
            m = p55.match(line)
            if m:
                group = m.groupdict()
                ddt_requests_failed = int(group['ddt_requests_failed'])
                error_dict.update({'ddt_requests_failed':ddt_requests_failed})
                continue

            # DDT ITR Map-Requests dropped:                     0 (nonce-collision: 0, bad-xTR-nonce: 0)
            m = p56.match(line)
            if m:
                group = m.groupdict()
                dropped = int(group['dropped'])
                nonce_collision = int(group['nonce_collision'])
                bad_xtr_nonce = int(group['bad_xtr_nonce'])
                ddt_itr_map = error_dict.setdefault('ddt_itr_map_requests',{})
                ddt_itr_map.update({'dropped':dropped,
                                    'nonce_collision':nonce_collision,
                                    'bad_xtr_nonce':bad_xtr_nonce})
                continue

            # Cache entries created/deleted:                    10/8
            m = p57.match(line)
            if m:
                group = m.groupdict()
                created = int(group['created'])
                deleted = int(group['deleted'])
                cache_dict = instance_dict.setdefault('cache_related',{})
                cache_entries_dict = cache_dict.setdefault('cache_entries',{})
                cache_entries_dict.update({'created':created,
                                           'deleted':deleted})
                continue

            # NSF CEF replay entry count                        0
            m = p58.match(line)
            if m:
                group = m.groupdict()
                nsf_cef_replay_entry_count = int(group['nsf_cef_replay_entry_count'])
                cache_dict.update({'nsf_cef_replay_entry_count':nsf_cef_replay_entry_count})
                continue

            # Number of EID-prefixes in map-cache:              2
            m = p59.match(line)
            if m:
                group = m.groupdict()
                eid_prefix_map_cache = int(group['eid_prefix_map_cache'])
                cache_dict.update({'eid_prefix_map_cache':eid_prefix_map_cache})
                continue

            # Number of rejected EID-prefixes due to limit:     0
            m = p60.match(line)
            if m:
                group = m.groupdict()
                rejected_eid_prefix_due_to_limit = int(group['rejected_eid_prefix_due_to_limit'])
                cache_dict.update({'rejected_eid_prefix_due_to_limit':rejected_eid_prefix_due_to_limit})
                continue

            # Number of times signal suppression was turned on: 0
            m = p61.match(line)
            if m:
                group = m.groupdict()
                times_signal_suppresion_turned_on = int(group['times_signal_suppresion_turned'])
                cache_dict.update({'times_signal_suppresion_turned_on':times_signal_suppresion_turned_on})
                continue

            # Time since last signal suppressed change:         never
            m = p62.match(line)
            if m:
                group = m.groupdict()
                time_since_last_signal_suppressed = group['time_since_last_signal']
                cache_dict.update({'time_since_last_signal_suppressed':time_since_last_signal_suppressed})
                continue

            # Number of negative entries in map-cache:          2
            m = p63.match(line)
            if m:
                group = m.groupdict()
                negative_entries_map_cache = int(group['negative_entries_map_cache'])
                cache_dict.update({'negative_entries_map_cache':negative_entries_map_cache})
                continue

            # Total number of RLOCs in map-cache:               0
            m = p64.match(line)
            if m:
                group = m.groupdict()
                total_rlocs_map_cache = int(group['total_rlocs_map_cache'])
                cache_dict.update({'total_rlocs_map_cache':total_rlocs_map_cache})
                continue

            # Average RLOCs per EID-prefix:                     0
            m = p65.match(line)
            if m:
                group = m.groupdict()
                average_rlocs_per_eid_prefix = int(group['average_rlocs_per_eid_prefix'])
                cache_dict.update({'average_rlocs_per_eid_prefix':average_rlocs_per_eid_prefix})
                continue

            # Policy active entries:                            0
            m = p66.match(line)
            if m:
                group = m.groupdict()
                policy_active_entries = int(group['policy_active_entries'])
                cache_dict.update({'policy_active_entries':policy_active_entries})
                continue

            # Number of data signals processed:                 2 (+ dropped 0)
            m = p67.match(line)
            if m:
                group = m.groupdict()
                processed = int(group['processed'])
                dropped = int(group['dropped'])
                forwarding_dict = instance_dict.setdefault('forwarding',{})
                data_signal_dict = forwarding_dict.setdefault('data_signals',{})
                data_signal_dict.update({'processed':processed,
                                         'dropped':dropped})
                continue

            # Number of reachability reports:                   0 (+ dropped 0)
            m = p68.match(line)
            if m:
                group = m.groupdict()
                count = int(group['count'])
                dropped = int(group['dropped'])
                reachability_dict = forwarding_dict.setdefault('reachability_reports',{})
                reachability_dict.update({'count':count,
                                         'dropped':dropped})
                continue

            # Number of SMR signals dropped:                    0
            m = p69.match(line)
            if m:
                group = m.groupdict()
                dropped = int(group['dropped'])
                smr_signal_dict = forwarding_dict.setdefault('smr_signals',{})
                smr_signal_dict.update({'dropped':dropped})
                continue

            # 44.44.44.44          6d21h      202176        8        0        0        6    0/ 0/ 0
            # 44:44:44:44::        6d21h      202176        8        0        0        6    0/ 0/ 0
            m = p70.match(line)
            if m:
                group = m.groupdict()
                itr_map_resolvers = group['itr_map_resolvers']
                last_reply = group['last_reply']
                metric = int(group['metric'])
                req_sent = int(group['req_sent'])
                positive = int(group['positive'])
                negative = int(group['negative'])
                no_reply = int(group['no_reply'])
                sec_5 = int(group['sec_5'])
                min_1 = int(group['min_1'])
                min_5 = int(group['min_5'])
                itr_map_dict = instance_dict.setdefault('itr_map_resolvers',{})
                itr_map_resolvers_dict = itr_map_dict.setdefault(itr_map_resolvers,{})
                itr_map_resolvers_dict.update({'last_reply':last_reply,
                                               'metric':metric,
                                               'req_sent':req_sent,
                                               'positive':positive,
                                               'negative':negative,
                                               'no_reply':no_reply})
                avg_dict = itr_map_resolvers_dict.setdefault('avgrtt',{})
                avg_dict.update({'5_sec':sec_5,
                                 '1_min':min_1,
                                 '5_min':min_5})
                continue

            # 44.44.44.44          0/ 0/ 0
            # 44:44:44:44::        0/ 0/ 0
            m = p71.match(line)
            if m:
                group = m.groupdict()
                etr_map_servers = group['etr_map_servers']
                sec_5 = int(group['sec_5'])
                min_1 = int(group['min_1'])
                min_5 = int(group['min_5'])
                etr_map_dict = instance_dict.setdefault('etr_map_servers',{})
                etr_map_servers_dict = etr_map_dict.setdefault(etr_map_servers,{})\
                                                   .setdefault('avgrtt',{})
                etr_map_servers_dict.update({'5_sec':sec_5,
                                             '1_min':min_1,
                                             '5_min':min_5})
                continue

            # LISP RLOC Statistics - last cleared: never
            m = p72.match(line)
            if m:
                group = m.groupdict()
                last_cleared = group['last_cleared']
                rloc_stat_dict = instance_dict.setdefault('rloc_statistics',{})
                rloc_stat_dict.update({'last_cleared':last_cleared})
                continue

            # RTR Map-Requests forwarded:                       0
            m = p73.match(line)
            if m:
                group = m.groupdict()
                map_requests_forwarded = int(group['map_requests_forwarded'])
                control_packets_dict = rloc_stat_dict.setdefault('control_packets',{})
                rtr_dict = control_packets_dict.setdefault('rtr',{})
                rtr_dict.update({'map_requests_forwarded':map_requests_forwarded})
                continue

            # RTR Map-Notifies forwarded:                       0
            m = p74.match(line)
            if m:
                group = m.groupdict()
                map_notifies_forwarded = int(group['map_notifies_forwarded'])
                rtr_dict.update({'map_notifies_forwarded':map_notifies_forwarded})
                continue

            # DDT-Map-Requests in/out:                          0/0
            m = p75.match(line)
            if m:
                group = m.groupdict()
                map_requests_in = int(group['in'])
                out = int(group['out'])
                ddt_dict = control_packets_dict.setdefault('ddt',{})
                map_requests_request = ddt_dict.setdefault('map_requests',{})
                map_requests_request.update({'in':map_requests_in,
                                             'out':out})
                continue

            # DDT-Map-Referrals in/out:                         0/0
            m = p76.match(line)
            if m:
                group = m.groupdict()
                map_requests_in = int(group['in'])
                out = int(group['out'])
                map_referral_request = ddt_dict.setdefault('map_referrals',{})
                map_referral_request.update({'in':map_requests_in,
                                             'out':out})
                continue

            # Map-Request format errors:                        0
            m = p77.match(line)
            if m:
                group = m.groupdict()
                map_request_format = int(group['map_request_format'])
                map_errors_dict = rloc_stat_dict.setdefault('errors',{})
                map_errors_dict.update({'map_request_format':map_request_format})
                continue

            # Map-Reply format errors:                          0
            m = p78.match(line)
            if m:
                group = m.groupdict()
                map_reply_format = int(group['map_reply_format'])
                map_errors_dict.update({'map_reply_format':map_reply_format})
                continue

            # Map-Referral format errors:                       0
            m = p79.match(line)
            if m:
                group = m.groupdict()
                map_referral = int(group['map_referral'])
                map_errors_dict.update({'map_referral':map_referral})
                continue

            # Invalid IP version drops:                         0
            m = p80.match(line)
            if m:
                group = m.groupdict()
                ip_version_drops = int(group['ip_version_drops'])
                misc_dict = instance_dict.setdefault('misc_statistics',{})
                invalid_dict = misc_dict.setdefault('invalid',{})
                invalid_dict.update({'ip_version_drops':ip_version_drops})
                continue

            # Invalid IP header drops:                          0
            m = p81.match(line)
            if m:
                group = m.groupdict()
                ip_header_drops = int(group['ip_header_drops'])
                invalid_dict.update({'ip_header_drops':ip_header_drops})
                continue

            # Invalid IP proto field drops:                     0
            m = p82.match(line)
            if m:
                group = m.groupdict()
                ip_proto_field_drops = int(group['ip_proto_field_drops'])
                invalid_dict.update({'ip_proto_field_drops':ip_proto_field_drops})
                continue

            # Invalid packet size drops:                        0
            m = p83.match(line)
            if m:
                group = m.groupdict()
                packet_size_drops = int(group['packet_size_drops'])
                invalid_dict.update({'packet_size_drops':packet_size_drops})
                continue

            # Invalid LISP control port drops:                  0
            m = p84.match(line)
            if m:
                group = m.groupdict()
                lisp_control_port_drops = int(group['lisp_control_port_drops'])
                invalid_dict.update({'lisp_control_port_drops':lisp_control_port_drops})
                continue

            # Invalid LISP checksum drops:                      0
            m = p85.match(line)
            if m:
                group = m.groupdict()
                lisp_checksum_drops = int(group['lisp_checksum_drops'])
                invalid_dict.update({'lisp_checksum_drops':lisp_checksum_drops})
                continue

            # Unsupported LISP packet type drops:               0
            m = p86.match(line)
            if m:
                group = m.groupdict()
                unsupported_lisp_packet_drops = int(group['unsupported_lisp_packet_drops'])
                misc_dict.update({'unsupported_lisp_packet_drops':unsupported_lisp_packet_drops})
                continue

            # Unknown packet drops:                             0
            m = p87.match(line)
            if m:
                group = m.groupdict()
                unknown_packet_drops = int(group['unknown_packet_drops'])
                misc_dict.update({'unknown_packet_drops':unknown_packet_drops})
                continue
        return ret_dict


# ==============================
# Schema for
# 'show lisp remote-locator-set {remote_locator_type}',
# 'show lisp remote-locator-set name {remote_locator_name}',
# 'show lisp {lisp_id} remote-locator-set {remote_locator_type}',
# 'show lisp {lisp_id} remote-locator-set name {remote_locator_name}'
# ==============================
class ShowLispRemoteLocatorSetSchema(MetaParser):
    """Schema for
        'show lisp remote-locator-set {remote_locator_type}',
        'show lisp remote-locator-set name {remote_locator_name}',
        'show lisp {lisp_id} remote-locator-set {remote_locator_type}',
        'show lisp {lisp_id} remote-locator-set name {remote_locator_name}'
    """
    schema = {
        'lisp_id': {
            int: {
                'remote_locator_name': {
                    str: {
                        'rloc': {
                            str: {
                                'instance_id':{
                                    str: {
                                        'priority': str,
                                        'weight': str,
                                        Optional('metric'): str,
                                        Optional('domain_id'): str,
                                        Optional('multihome_id'): str,
                                        Optional('etr_type'): str,
                                        Optional('srvc_ins_id'): str,
                                        Optional('srvc_ins_type'): str
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }


class ShowLispRemoteLocatorSet(ShowLispRemoteLocatorSetSchema):
    cli_command = ['show lisp remote-locator-set {remote_locator_type}',
                    'show lisp remote-locator-set name {remote_locator_name}',
                    'show lisp {lisp_id} remote-locator-set {remote_locator_type}',
                    'show lisp {lisp_id} remote-locator-set name {remote_locator_name}']

    def cli(self, lisp_id=None, remote_locator_type=None, remote_locator_name=None, output=None):
        if output is None:
            if lisp_id and remote_locator_type:
                cmd = self.cli_command[2].format(lisp_id=lisp_id, remote_locator_type=remote_locator_type)
            elif lisp_id and remote_locator_name:
                cmd = self.cli_command[3].format(lisp_id=lisp_id, remote_locator_name=remote_locator_name)
            elif remote_locator_type:
                cmd = self.cli_command[0].format(remote_locator_type=remote_locator_type)
            else:
                cmd = self.cli_command[1].format(remote_locator_name=remote_locator_name)
            output = self.device.execute(cmd)
        ret_dict = {}

        # LISP remote-locator-set default-etr-locator-set-ipv4 Information
        p1 = re.compile(r'^LISP\s+remote-locator-set\s+(?P<remote_locator_name>\S+)\s+Information$')

        # 7.7.7.7         2/3  /-          101                0/0      Default
        # 32.32.32.32   32/10 /0          -                  0/0      Service
        # 32:32:32:32:: 32/10 /0          -                  0/0      Service
        p2 = re.compile(r'^(?P<rloc>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))(\*)?\s+'
                        r'(?P<priority>\d+)\/(?P<weight>[\d\s]+)'
                        r'(\/(?P<metric>[\d-]+))?\s+(?P<instance_id>\d+|-)'
                        r'(\s+)?(?P<domain_id>\d+)?(\/)?(?P<multihome_id>\d+)?'
                        r'(\s+(?P<etr_type>\S+))?(\s+)?(?P<srvc_ins_id>\S+)?(\s+)?'
                        r'(\/(?P<srvc_ins_type>\S+))?$')

        for line in output.splitlines():
            line = line.strip()

            # LISP remote-locator-set default-etr-locator-set-ipv4 Information
            m = p1.match(line)
            if m:
                lisp_id = int(lisp_id) if lisp_id else 0
                group = m.groupdict()
                remote_locator_name = group['remote_locator_name']
                lisp_dict = ret_dict.setdefault('lisp_id',{}).\
                                     setdefault(lisp_id,{}).\
                                     setdefault('remote_locator_name',{}).\
                                     setdefault(remote_locator_name,{})
                continue

            # 7.7.7.7         2/3  /-          101                0/0      Default
            # 32:32:32:32::  32/10 /0          -                  0/0      Service
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rloc = group['rloc']
                priority = group['priority']
                weight = group['weight']
                instance_id = group['instance_id']
                rloc_dict = lisp_dict.setdefault('rloc',{}).\
                                      setdefault(rloc,{}).\
                                      setdefault('instance_id',{}).\
                                      setdefault(instance_id,{})
                rloc_dict.update({'priority':priority,
                                  'weight':weight})
                if group['metric']:
                    metric = group['metric']
                    rloc_dict.update({'metric':metric})
                if group['domain_id']:
                    domain_id = group['domain_id']
                    rloc_dict.update({'domain_id':domain_id})
                if group['multihome_id']:
                    multihome_id = group['multihome_id']
                    rloc_dict.update({'multihome_id':multihome_id})
                if group['etr_type']:
                    etr_type = group['etr_type']
                    rloc_dict.update({'etr_type':etr_type})
                if group['srvc_ins_id']:
                    srvc_ins_id = group['srvc_ins_id']
                    rloc_dict.update({'srvc_ins_id':srvc_ins_id})
                if group['srvc_ins_type']:
                    srvc_ins_type = group['srvc_ins_type']
                    rloc_dict.update({'srvc_ins_type':srvc_ins_type})
                continue
        return ret_dict


class ShowLispInstanceServerRARSchema(MetaParser):
    """ Parser for show lisp instance ethernet server reverse-address-resolution
        * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution
        * show lisp instance-id {instance_id} ethernet server reverse-address-resolution
    """
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                   int: {
                       'eid': {
                           str: {
                               'host_address' : list
                            }
                       }
                   }
                }
           }
        }
    }


# ===================
# Parser for:
#  * 'show lisp instance-id <iid> ethernet server reverse-address-resolution'
# ===================
class ShowLispInstanceServerRAR(ShowLispInstanceServerRARSchema):

    """ Parser for show lisp instance ethernet server reverse-address-resolution
        * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution
        * show lisp instance-id {instance_id} ethernet server reverse-address-resolution
    """
    # all relevant cli commands
    cli_command = ['show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution',
                   'show lisp instance-id {instance_id} ethernet server reverse-address-resolution']

    def cli(self, lisp_id=None, instance_id=None, output=None):

        if output is None:
            # both lisp_id and instance_id are sent in the function call
            if lisp_id and instance_id:
                cmd = self.cli_command[0].format(lisp_id=lisp_id,\
                                                   instance_id=instance_id)

            # only instance_id is sent in the function call
            elif instance_id:
                cmd = self.cli_command[1].format(instance_id=instance_id)

            #raise error
            else:
                raise TypeError("No arguments provided to parser")

            output = self.device.execute(cmd)

        ret_dict = {}
        instance_dict = {}
        host_address_list = []
        # Reverse-Address-resolution data for router lisp 0 instance-id 1031
        p1 = re.compile(r'Reverse-Address-resolution data for router lisp (?P<lisp_id>\d+) instance-id (?P<instance_id>\d+)')

        ''' aabb.cc00.c900/48     192.168.3.2
                                  2001:192:168:3::2
                                  FE80::A8BB:CCFF:FE00:C900
        '''
        p2 = re.compile(r'(?P<eid>[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\.[0-9a-fA-F]{4}\/\d+\s+)?'
                        r'(?P<host_address>[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}|[a-fA-F\d\:]+)')

        for line in output.splitlines():
            line = line.strip()

            m=p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                instance_id = int(group['instance_id'])
                lisp_dict = ret_dict.setdefault('lisp_id',{}).\
                                     setdefault(lisp_id,{})
                instance_dict = lisp_dict.setdefault('instance_id',{}).\
                                     setdefault(instance_id,{})
                continue

            m=p2.match(line)
            if m:

                 group = m.groupdict()
                 if group['eid'] is not None:
                     eid = group['eid'].strip()
                     host_address_list = []

                 host_address_list.append(group['host_address'].strip())
                 eid_dict = instance_dict.setdefault('eid',{}).\
                                          setdefault(eid,{})
                 eid_dict['host_address'] = host_address_list
                 continue

        return ret_dict


class ShowLispInstanceServerRARDetailSchema(MetaParser):
    """ Parser for show lisp instance ethernet server reverse-address-resolution detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution detail
        * show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution {mac}
        * show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail
        * show lisp instance-id {instance_id} ethernet server reverse-address-resolution {mac}
    """
    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'site': str,
                        'eid': {
                            str: {
                                'host_address': list,
                                'first_registered': str,
                                'last_registered': str,
                                'registration_failures': {
                            str : {
                                'auth_failures' : int
                            }
                        },
                        'etr': {
                            str : {
                                'last_registered' : str,
                                'ttl': str,
                                'xtr_id': str,
                                'site_id': str,
                                'registered_addr': list
                                }
                            }
                        }
                    }
               }
            }
        }
    }
}



# ===================
# Parser for:
#  * 'show lisp instance-id <iid> ethernet server reverse-address-resolution detail'
#  * 'show lisp instance-id <iid> ethernet server reverse-address-resolution <mac>'
# ===================
class ShowLispInstanceServerRARDetail(ShowLispInstanceServerRARDetailSchema):
    """ Parser for show lisp instance ethernet server reverse-address-resolution detail
        *show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution detail
        *show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution {mac}
        *show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail
        *show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail {mac}
    """
    # all relevant cli commands
    cli_command = [ 'show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution detail',
                    'show lisp {lisp_id} instance-id {instance_id} ethernet server reverse-address-resolution {mac}',
                    'show lisp instance-id {instance_id} ethernet server reverse-address-resolution detail',
                    'show lisp instance-id {instance_id} ethernet server reverse-address-resolution {mac}'
                  ]

    def cli(self, lisp_id=None, instance_id=None, mac=None, output=None):

        if output is None:
            #lisp id ,instance id and mac are sent in the function call
            if lisp_id and instance_id and mac:
                cmd = self.cli_command[1].format(lisp_id=lisp_id,\
                                                   instance_id=instance_id, mac=mac)

            #lisp id and instance id are sent in the function call
            elif lisp_id and instance_id:
                cmd = self.cli_command[0].format(lisp_id=lisp_id,\
                                                   instance_id=instance_id)
            #instance id and mac are sent in the function call
            elif instance_id and mac:
                cmd = self.cli_command[3].format(instance_id=instance_id, mac=mac)

            #only instance id is sent in the function call
            elif instance_id:
                cmd = self.cli_command[2].format(instance_id=instance_id)

            #raise error.
            else:
                raise TypeError("No arguments provided to parser")

            output = self.device.execute(cmd)

        ret_dict = {}
        host_list = []
        registration_failures = {}
        reg_list = []
        etr_dict = {}
        last_reg_flag = False
        eid_flag = False

        # Reverse-Address-resolution data for router lisp 0 instance-id 1031
        p1 = re.compile(r'Reverse-Address-resolution data for router lisp (?P<lisp_id>\d+)'
                        r' instance-id (?P<instance_id>\d+)')

        # Site name: wired
        p2 = re.compile(r'Site name:\s+(?P<site>\S+)')

        # Hardware Address:     aabb.cc00.c900/48
        p3 = re.compile(r'Hardware Address:\s+(?P<eid>([0-9a-fA-F]{4}\.){2}[0-9a-fA-F]{4}\/\d{2})')

        '''Host Address:         192.168.3.2
                                2001:192:168:3::2
                                FE80::A8BB:CCFF:FE00:C900'''
        p4 = re.compile(r'(Host Address:\s+)?(?P<host_address>((\d{1,3}\.){3}\d{1,3})|([a-fA-F\d\:]+))$')

        #First registered:     04:21:34
        p5 = re.compile(r'First registered:\s+(?P<first_registered>(\d{2}\:){2}(\d{2}))')

        #Last registered:      04:21:34
        p6 = re.compile(r'Last registered:\s+(?P<last_registered>(\d{2}\:){2}(\d{2}))')

        #  Authentication failures:   0
        p7 = re.compile(r'Authentication failures:\s+(?P<auth_failures>\d+)')

        p8 = re.compile(r'Last registered:\s+(?P<last_registered_etr>(\d{2}\:){2}(\d{2}))')
        # TTL:                   00:01:00
        p9 = re.compile(r'TTL:\s+(?P<ttl>(\d{2}\:){2}(\d{2}))')

        #xTR-ID:                N/A
        p10 = re.compile(r'xTR-ID:\s+(?P<xtr_id>\S+)')

        #Site-ID:               N/A
        p11 = re.compile(r'Site-ID:\s+(?P<site_id>\S+)')

        #Registered addr:       192.168.3.2
        #                       2001:192:168:3::2
        #                       FE80::A8BB:CCFF:FE00:C900
        p12 = re.compile(r'(Registered addr:\s+)?(?P<registered_address>((\d{1,3}\.){3}\d{1,3})|([a-fA-F\d\:]+))$')

        for line in output.splitlines():
            line = line.strip()

            m=p1.match(line)
            if m:
                group = m.groupdict()
                lisp_id = int(group['lisp_id'])
                instance_id = int(group['instance_id'])
                lisp_dict = ret_dict.setdefault('lisp_id',{}).\
                                     setdefault(lisp_id,{})
                instance_dict = lisp_dict.setdefault('instance_id',{}).\
                                     setdefault(instance_id,{})
                continue

            m=p2.match(line)
            if m:
                group = m.groupdict()
                site = group['site']
                instance_dict.update({'site': site})
                continue

            m=p3.match(line)
            if m:
                group = m.groupdict()
                eid = group['eid']
                eid_dict = instance_dict.setdefault('eid',{}).\
                                          setdefault(eid,{})
                host_list = []
                reg_list = []
                reg_flag = False
                continue

            m=p4.match(line)
            if m and not(reg_flag):
                group = m.groupdict()
                if group['host_address'] not in host_list and not(line.startswith('Registered')):
                   host_list.append(group['host_address'])

                eid_dict.update({'host_address': host_list})

                continue

            m=p5.match(line)
            if m:
                group = m.groupdict()
                first_registered = group['first_registered']
                eid_dict.update({'first_registered': first_registered})
                continue

            if not(last_reg_flag):
               m=p6.match(line)
               if m:
                   group = m.groupdict()
                   last_registered = group['last_registered']
                   eid_dict.update({'last_registered': last_registered})
                   last_reg_flag = True
                   continue

            m=p7.match(line)
            if m:
                group = m.groupdict()
                reg_fail_dict = eid_dict.setdefault('registration_failures',{}).\
                                         setdefault('registration_failures',{})
                reg_fail_dict['auth_failures'] = int(group['auth_failures'])
                etr_dict = eid_dict.setdefault('etr',{}).setdefault('local',{})
                continue

            m=p9.match(line)
            if m:
                group = m.groupdict()
                etr_dict['ttl']= group['ttl']
                continue

            m=p8.match(line)
            if m and last_reg_flag:
                group = m.groupdict()
                last_registered_etr = group['last_registered_etr']
                last_reg_flag = False
                etr_dict['last_registered'] = last_registered_etr
                continue

            m=p10.match(line)
            if m:
                group = m.groupdict()
                etr_dict['xtr_id'] = group['xtr_id']
                continue

            m=p11.match(line)
            if m:
                group = m.groupdict()
                etr_dict['site_id'] = group['site_id']
                continue

            m=p12.match(line)
            if m:
                group = m.groupdict()
                if group['registered_address'] not in reg_list and not(line.startswith('Host')):
                   reg_list.append(group['registered_address'])
                etr_dict['registered_addr'] = reg_list
                reg_flag = True
                continue
        return ret_dict


class ShowLispInstanceIdEthernetMapCacheRAR(ShowLispMapCacheSuperParser):

    """
    Parser for
    * sh lisp instance-id {instance_id} ethernet map-cache reverse-address-resolution
    * sh lisp {lisp_id} instance-id {instance_id} ethernet map-cache reverse-address-resolution
    * show lisp locator-table {locator_table} instance-id {instance_id} ethernet map-cache reverse-address-resolution
    """
    cli_command = ['show lisp instance-id {instance_id} ethernet map-cache reverse-address-resolution',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache reverse-address-resolution',
                   'sh lisp locator-table {locator_table} instance-id {instance_id} ethernet map-cache reverse-address-resolution']

    def cli(self, lisp_id=None, instance_id=None, eid_table=None, locator_table=None, vrf=None, output=None):
        if output is None:
            if locator_table and instance_id:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, \
                                             instance_id=instance_id))
            elif lisp_id and instance_id:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, \
                                             instance_id=instance_id))
            elif instance_id:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
            else:
                raise TypeError("No arguments provided to parser")
        return super().cli(output=output)


class ShowLispInstanceIdEthernetMapCachePrefixRAR(ShowLispIpMapCachePrefixSuperParser):

    """
    Parser for
    * sh lisp instance-id {instance_id} ethernet map-cache reverse-address-resolution {eid_prefix}
    * sh lisp {lisp_id} instance-id {instance_id} ethernet map-cache reverse-address-resolution
    * show lisp locator-table {locator_table} instance-id {instance_id} ethernet map-cache reverse-address-resolution
    """
    cli_command = ['show lisp instance-id {instance_id} ethernet map-cache reverse-address-resolution {prefix}',
                   'show lisp {lisp_id} instance-id {instance_id} ethernet map-cache reverse-address-resolution {prefix}',
                   'sh lisp locator-table {locator_table} instance-id {instance_id} ethernet map-cache reverse-address-resolution {prefix}']

    def cli(self, lisp_id=None, instance_id=None, locator_table=None, prefix=None, output=None):
        if output is None:
            if locator_table and instance_id and prefix:
                output = self.device.execute(self.cli_command[2].format(locator_table=locator_table, \
                                            instance_id=instance_id, prefix=prefix))
            elif lisp_id and instance_id and prefix:
                output = self.device.execute(self.cli_command[1].format(lisp_id=lisp_id, \
                                            instance_id=instance_id,prefix=prefix))
            elif instance_id and prefix:
                output = self.device.execute(self.cli_command[0].format(instance_id=instance_id,\
                                             prefix=prefix))
            else:
                raise TypeError("No arguments provided to parser")
        return super().cli(output=output,prefix=prefix,lisp_id=lisp_id,locator_table=locator_table,\
                           instance_id=instance_id)


class ShowLispEthernetServerSubscription(ShowLispServerSubscriptionSuperParser, ShowLispServerSubscriptionSchema):
    ''' Show Command ethernet Subscription
        show lisp instance-id {instance_id} ethernet server subscription
        show lisp {lisp_id} instance-id {instance_id} ethernet server subscription
        show lisp locator-table {locator_table} instance-id {instance_id} ethernet server subscription
        show lisp eid-table vlan {vlan} ethernet server subscription
    '''

    cli_command = [
        'show lisp instance-id {instance_id} ethernet server subscription',
        'show lisp {lisp_id} instance-id {instance_id} ethernet server subscription',
        'show lisp locator-table {locator_table} instance-id {instance_id} ethernet server subscription',
        'show lisp eid-table vlan {vlan} ethernet server subscription'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vlan=None, locator_table=None,
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
            else:
                output = self.device.execute(self.cli_command[3].\
                                                format(vlan=vlan))

        return super().cli(output=output)


class ShowLispAFServerSubscriptionPrefix(ShowLispServerSubscriptionPrefixSuperParser, ShowLispServerSubscriptionPrefixSchema):
    ''' Show command for {address_family} server subscription prefix/detail
        show lisp instance-id {instance_id} {address_family} server subscription {eid_prefix}/detail
        show lisp {lisp_id} instance-id {instance_id} {address_family} server subscription {eid_prefix}/detail
        show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server subscription {eid_prefix}/detail
        show lisp eid-table {eid_table} {address_family} server subscription {eid_prefix}/detail
        show lisp eid-table vrf {eid_table} {address_family} server subscription {eid_prefix}/detail
    '''

    cli_command = [
        'show lisp instance-id {instance_id} {address_family} server subscription {eid_prefix}',
        'show lisp {lisp_id} instance-id {instance_id} {address_family} server subscription {eid_prefix}',
        'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server subscription {eid_prefix}',
        'show lisp eid-table {eid_table} {address_family} server subscription {eid_prefix}',
        'show lisp eid-table vrf {vrf} {address_family} server subscription {eid_prefix}',
        'show lisp instance-id {instance_id} {address_family} server subscription detail',
        'show lisp {lisp_id} instance-id {instance_id} {address_family} server subscription detail',
        'show lisp locator-table {locator_table} instance-id {instance_id} {address_family} server subscription detail',
        'show lisp eid-table {eid_table} {address_family} server subscription detail',
        'show lisp eid-table vrf {vrf} {address_family} server subscription detail'
    ]

    def cli(self, output=None, lisp_id=None, instance_id=None, vrf=None, locator_table=None,
            eid_table=None, eid=None, eid_prefix=None, address_family='ipv4'):
        if output is None:
            if lisp_id and instance_id and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[1].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, eid_prefix=eid_prefix, address_family=address_family))
            elif instance_id and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[0].\
                                                format(instance_id=instance_id, eid_prefix=eid_prefix, address_family=address_family))
            elif locator_table and instance_id and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[2].\
                                                format(locator_table=locator_table, instance_id=instance_id, eid_prefix=eid_prefix, address_family=address_family))
            elif eid_table and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[3].\
                                                format(eid_table=eid_table, eid_prefix=eid_prefix, address_family=address_family))
            elif vrf and eid_prefix and address_family:
                output = self.device.execute(self.cli_command[4].\
                                                format(vrf=vrf, eid_prefix=eid_prefix, address_family=address_family))
            elif lisp_id and instance_id and address_family:
                output = self.device.execute(self.cli_command[6].\
                                                format(lisp_id=lisp_id, instance_id=instance_id, address_family=address_family))
            elif instance_id and address_family:
                output = self.device.execute(self.cli_command[5].\
                                                format(instance_id=instance_id, address_family=address_family))
            elif locator_table and instance_id and address_family:
                output = self.device.execute(self.cli_command[7].\
                                                format(locator_table=locator_table, instance_id=instance_id, address_family=address_family))
            elif eid_table and address_family:
                output = self.device.execute(self.cli_command[8].\
                                                format(eid_table=eid_table, address_family=address_family))
            else:
                output = self.device.execute(self.cli_command[9].\
                                                format(vrf=vrf, address_family=address_family))

        return super().cli(output=output)


class ShowLispDecapsulationFilterSchema(MetaParser):

    schema = {
        'eid_table': str,
        'iid': str,
        'entries': int,
        Optional('source_rloc'): {
            str: {
                'added_by': ListOf(str)
            }
        }
    }


class ShowLispDecapsulationFilterParser(ShowLispDecapsulationFilterSchema):

    """
    Parser for
      show lisp instance-id <iid> decapsulation filter
    """

    cli_command = ['show lisp instance-id {instance_id} decapsulation filter']

    def cli(self, instance_id, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0].format(instance_id=instance_id))
        else:
            out = output

        ret_dict = {}

        # LISP decapsulation filter for EID table vrf red (IID 101), 1 entries
        p1 = re.compile(r'^LISP decapsulation filter for EID table '
                        r'(?P<eid_table>.+) \(IID (?P<iid>\d+)\), '
                        r'(?P<entries>\d+) entries$')

        # Source RLOC      Added by
        # 100:33:33::33    MS 100:44:44::44, MS 100:55:55::55
        p2 = re.compile(r'^(?P<source_rloc>(\d{1,3}\.\d{1,3}\.\d{1,3}\.'
                        r'\d{1,3})|([a-fA-F\d\:]+))\s+(?P<added_by>.+)$')

        for line in out.splitlines():
            line = line.strip()

            # LISP decapsulation filter for EID table vrf red (IID 101), 1 entries
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                ret_dict['eid_table'] = groups['eid_table']
                ret_dict['iid'] = groups['iid']
                ret_dict['entries'] = int(groups['entries'])
                continue

            # Source RLOC      Added by
            # 100:33:33::33    MS 100:44:44::44, MS 100:55:55::55  
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                locator = groups['source_rloc']
                added_by = groups['added_by']

                source_list = ret_dict.setdefault('source_rloc', {}).\
                                       setdefault(locator, {}).\
                                       setdefault('added_by', [])

                # Post pocessing
                sources = added_by.split(",")
                for source in sources:
                    element = source.strip()
                    source_list.append(element)
                continue

        return ret_dict

class ShowLispVrfSchema(MetaParser):

    ''' Schema for "show lisp vrf {vrf}" '''
    schema = {
    'vrf': {
        Any(): {
            'iid': {
                Any(): {
                    'lock_count': int,
                    'top_id': int,
                    'watch_count': int
                }
            },
            'v4_topoid': {
                Any(): {
                    'lock_no': int,
                    'rib': str,
                    'status': str
                }
            },
            'v6_topoid': {
                Any(): {
                    'lock_no': int,
                    'rib': str,
                    'status': str
                }
            },
            'vrf_id': str
        }
    }
}
    
class ShowLispVrf(ShowLispVrfSchema):

    ''' Parser for "show lisp vrf {vrf}"'''
    cli_command = [
                    'show lisp vrf {vrf}',
                  ]

    def cli(self, vrf, output=None):
        if output is None:
            cmd = self.cli_command[0].format(vrf=vrf)            
            output = self.device.execute(cmd)
        # Init vars
        ret_dict = {}
    
        # vrf VN_1 ID 0x2 UP users  EID
        p1 = re.compile(r'vrf\s+(?P<vrf>\S+)+\s+ID\s+(?P<vrf_id>\S+)\s+UP\s+users+\s+EID$')
        
        # Topology IPv4 UP, topoid 0x2, locks 2, RIB registered
        p2 = re.compile(r'Topology\s+IPv4\s+(?P<status>\w+),\s+topoid\s+(?P<v4_topoid>\S+),\s+locks\s+(?P<lock_no>(\d+)),\s+RIB\s+(?P<rib>\S+)$')
    
        # User EID, top ID 0, IID 4105, lock count 4, RIB watch count 0
        p3 = re.compile(
            r'User\s+EID,\s+top\s+ID (?P<top_id>(\d+)),\s+IID (?P<iid>(\d+)),\s+lock\s+count (?P<lock_count>(\d+)),\s+RIB\s+watch\s+count (?P<watch_count>(\d+))$')
    
        # Topology IPv6 DOWN, topoid 0x503316482, locks 0, RIB no
        p4 = re.compile(r'Topology\s+IPv6\s+(?P<status>\w+),\s+topoid\s+(?P<v6_topoid>\S+),\s+locks\s+(?P<lock_no>(\d+)),\s+RIB\s+(?P<rib>\S+)$')
    
        for line in output.splitlines():
            line = line.strip()
    
            # Sessions for VRF default, total: 7, established: 4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf = group['vrf']
                vrf_id = group['vrf_id']
                vrf_dict = ret_dict.setdefault('vrf', {}). \
                    setdefault(vrf, {})
                vrf_dict['vrf_id'] = group['vrf_id']
                continue
            
            # Topology IPv4 UP, topoid 0x2, locks 2, RIB registered
            m = p2.match(line)
            if m:
                group = m.groupdict()
                v4_topoid = group['v4_topoid']
                status = group['status']
                lock_no = group['lock_no']
                rib = group['rib']
                topo_dict = vrf_dict.setdefault('v4_topoid', {}). \
                    setdefault(v4_topoid, {})
                topo_dict['status'] = group['status']
                topo_dict['lock_no'] = int(group['lock_no'])
                topo_dict['rib'] = group['rib']
                continue
    
            # User EID, top ID 0, IID 4105, lock count 4, RIB watch count 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                top_id = group['top_id']
                iid = group['iid']
                lock_count = group['lock_count']
                watch_count = group['watch_count']
                topo_dict = vrf_dict.setdefault('iid', {}). \
                    setdefault(iid, {})
                topo_dict['top_id'] = int(group['top_id'])
                topo_dict['lock_count'] = int(group['lock_count'])
                topo_dict['watch_count'] = int(group['watch_count'])
                continue
    
            # Topology IPv6 DOWN, topoid 0x503316482, locks 0, RIB no
            m = p4.match(line)
            if m:
                group = m.groupdict()
                status = group['status']
                v6_topoid = group['v6_topoid']
                lock_no = group['lock_no']
                rib = group['rib']
                topo_dict = vrf_dict.setdefault('v6_topoid', {}). \
                    setdefault(v6_topoid, {})
                topo_dict['status'] = group['status']
                topo_dict['lock_no'] = int(group['lock_no'])
                topo_dict['rib'] = group['rib']
                continue
    
        return ret_dict