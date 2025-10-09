# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
                                                ListOf,
                                                Optional,
                                                Or)
from genie.libs.parser.utils.common import Common

class ShowLispPublicationPrefixSchema(MetaParser):

    schema = {
        'lisp_id': {
            int: {
                'instance_id': {
                    int: {
                        'eid_prefixes': {
                            str: {
                                'first_published': str,
                                'last_published': str,
                                'state': str,
                                Optional('exported_to'): list,
                                'publishers': {
                                    str: {
                                        'port': int,
                                        'last_published': str, # (complete|unknown)
                                        'ttl': str,
                                        'publisher_epoch': int,
                                        'entry_epoch': int,
                                        'entry_state': str,
                                        Optional('routing_tag'): int,
                                        'xtr_id': str,
                                        Optional('site_id'): str,
                                        Optional('domain_id'): str,
                                        Optional('sgt'): int,
                                        Optional('multihoming_id'): str,
                                        Optional('extranet_iid'): int,
                                        Optional('publish_mode'): str,
                                        Optional('locators'): {
                                            str: {
                                                'priority': int,
                                                'weight': int,
                                                'state': str, # (up|down)
                                                'encap_iid': str,
                                                Optional('metric'): str,
                                                Optional('domain_id'): int,
                                                Optional('multihoming_id'): int,
                                                Optional('affinity_id_x'): int,
                                                Optional('affinity_id_y'): int,
                                                Optional('rdp'): str
                                            }
                                        }
                                    }
                                },
                                Optional('merged_locators'): {
                                    str: {
                                        'priority': int,
                                        'weight': int,
                                        'state': str, # (up|down)
                                        'encap_iid': str,
                                        'rdp_len': str,
                                        'src_add': str,
                                        'publishers': { # Same as src_add
                                            str: {
                                               'priority': int,
                                                'weight': int,
                                                'state': str,
                                                'encap_iid': str,
                                                'rdp_len': str,
                                                'selected': bool
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
    }


class ShowLispPublicationPrefixSuperParser(ShowLispPublicationPrefixSchema):
    '''Parser for "show lisp {lisp_id} instance-id {instance_id} ipv4 publication {eid_prefix | detail}"'''
    def cli(self, lisp_id=None, instance_id=None, eid_table=None, eid_prefix=None, vrf=None, output=None):
        lisp_v4_pub_pre = {}
        count = 0

        # Publication Information for LISP 0 EID-table vrf red (IID 4100)
        p1 = re.compile(r"^Publication\s+Information\s+for\s+LISP\s+"
                        r"(?P<lisp_id>\d+)\s+EID-table\s+vrf\s+\S+\s+"
                        r"\(IID\s+(?P<instance_id>\d+)\)$")

        # EID-prefix: 192.168.1.71/32
        # EID-prefix: 2001:172:168:1::/64
        p2 = re.compile(r"^EID-prefix:\s+(?P<eid_prefixes>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}"
                        r"|[a-fA-F\d\:]+\/\d{1,3})|([a-fA-F\d\:]+\/\d{1,3}))$")

        # First published:      03:05:56
        p3 = re.compile(r"^First\s+published:\s+(?P<first_published>\S+)$")

        # Last published:      03:05:56
        p4 = re.compile(r"^Last\s+published:\s+(?P<last_published>\S+)$")

        # State:                complete
        p5 = re.compile(r"^State:\s+(?P<state>\S+)$")

        # Exported to:          map-cache
        # Exported to:          local-eid, map-cache
        p6 = re.compile(r"^Exported\s+to:\s+(?P<exported_to>[\s\S]+)$")

        # Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
        # Publisher 2001:13:13:13::13.4342, last published 00:03:35, TTL never, Expires: never
        p7 = re.compile(r"^Publisher\s+(?P<publishers>((\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})?"
                        r"|([a-fA-F\d\:]+)))?\.?\:?(?P<port>\d+),\s+last\s+published\s+"
                        r"(?P<last_published>\S+),\s+TTL\s+(?P<ttl>\w+)")

        # publisher epoch 1, entry epoch 1
        p8 = re.compile(r"^publisher\s+epoch\s+(?P<publisher_epoch>\d+),"
                        r"\s+entry\s+epoch\s+(?P<entry_epoch>\d+)")

        # entry-state complete
        p9 = re.compile(r"^entry-state\s+(?P<entry_state>\S+)")

        # routing table tag 101
        p10 = re.compile(r"^routing\s+table\s+tag\s+(?P<routing_tag>\d+)")

        # xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
        p11 = re.compile(r"^xTR-ID\s+(?P<xtr_id>\S+)")

        # site-ID unspecified
        p12 = re.compile(r"^site-ID\s+(?P<site_id>\S+)")

        # Domain-ID unset
        p13 = re.compile(r"^Domain-ID\s+(?P<domain_id>\S+)")

        # Multihoming-ID unspecified
        p14 = re.compile(r"^Multihoming-ID\s+(?P<multihoming_id>\S+)")

        # Publication-mode  no-extranet
        p14_1 = re.compile(r'^Publish-mode\s+(?P<publish_mode>.+\S)')

        # Merge Locator Information
        # * Indicates the selected rlocs used by consumers
        # Locator        Pri/Wgt  State     Encap-IID  RDP-Len Src-Address
        # 100.88.88.88    20/90   up        -          0       100.77.77.77
        # 100.89.89.89    20/90   up        -          -       100.77.77.77
        # 100.90.90.90    20/90   up        -          ext     100.77.77.77
        # 100::88:88:88   20/90   up        -          0       100.77.77.77
        # 100::88:88:88*  20/90   up        -          0       100.77.77.77
        p15 = re.compile(r"^(?P<merged_locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))"
                         r"(?P<selected>\*)?\s+(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)"
                         r"\s+(?P<encap_iid>\S+)\s+(?P<rdp_len>(\d+|\-|ext))\s+"
                         r"(?P<src_add>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))$")

        # Locator        Pri/Wgt  State     Encap-IID  RDP
        # 100.88.88.88   100/50   up        -          [-]
        p16 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)"
                         r"\s+(?P<rdp>\[[ 0-9\-]+\])$")

        # Locator        Pri/Wgt  State     Encap-IID   Domain-ID/MH-ID   Metric
        # 100.88.88.88   100/50   up        -                   1/1       44
        # 2001:2:2:2::2   50/50   up        -                   1/1       44
        # 2001:2:2:2::2   50/50   up        -                   1/1       -
        p17 = re.compile(r"^(?P<locators>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})|([a-fA-F\d\:]+))\s+"
                         r"(?P<priority>\d+)\/(?P<weight>\d+)\s+(?P<state>\S+)\s+(?P<encap_iid>\S+)"
                         r"\s+(?P<domain_id>\d+)\/(?P<multihoming_id>\d+)\s+(?P<metric>[\d-]+)$")

        # Affinity-id: 20 , 20
        p18 = re.compile(r'^Affinity-id:\s+(?P<affinity_id_x>\d+)(\s+,\s+(?P<affinity_id_y>\d+))?$')

        # Instance ID:                              4100
        p19 = re.compile(r"^\s+Instance\s+ID:\s+(?P<inst_id>\S+)")

        # Publisher 100.100.100.100:4342
        p20 = re.compile(r"^Publisher\s+(?P<publishers>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"
                        r":(?P<port>\d+)$")

        # Publisher 100::100:100:100.4342
        p21 = re.compile(r"^Publisher\s+(?P<publishers>[a-fA-F\d\:]+)\.(?P<port>\d+)$")

        # last published 16:02:47, TTL never
        p22 = re.compile(r"^last\s+published\s+(?P<last_published>\S+),\s+TTL\s+(?P<ttl>\w+)")

        # SGT 100
        p23 = re.compile(r"^SGT\s+(?P<sgt>\d+)$")

        for line in output.splitlines():
            line = line.strip()
            count += 1

            # Publication Information for LISP 0 EID-table vrf red (IID 4100)
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                lisp_id = int(groups['lisp_id'])
                prefix_id = int(groups['instance_id'])
                lisp_id_dict = lisp_v4_pub_pre.setdefault('lisp_id',{})\
                                              .setdefault(lisp_id,{})
                instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(prefix_id,{})
                continue

            # EID-prefix: 192.168.1.71/3
            # EID-prefix: 2001:172:168:1::/64
            m = p2.match(line)
            if m:
                if not lisp_id and instance_id != "*":
                    lisp_id = 0
                    instance_id = int(instance_id)
                    lisp_id_dict = lisp_v4_pub_pre.setdefault('lisp_id',{})\
                                                .setdefault(lisp_id,{})
                    instance_id_dict = lisp_id_dict.setdefault('instance_id',{})\
                                               .setdefault(instance_id,{})
                groups = m.groupdict()
                eid_prefixes = groups['eid_prefixes']
                eid_prefix_dict = instance_id_dict.setdefault('eid_prefixes',{})\
                                                  .setdefault(eid_prefixes,{})
                continue

            # First published:      03:05:56
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                first_published = groups['first_published']
                eid_prefix_dict.update({'first_published':first_published})
                continue

            # Last published:      03:05:56
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                eid_prefix_dict.update({'last_published':last_published})
                continue

            # State:                complete
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                state = groups['state']
                eid_prefix_dict.update({'state':state})
                continue

            # Exported to:          map-cache
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                exported_to = groups['exported_to']
                exported_list = eid_prefix_dict.setdefault('exported_to',[])
                exported_list.append(exported_to)
                eid_prefix_dict.update({'exported_to':exported_list})
                continue

            # Publisher 100.100.100.100:4342, last published 16:02:47, TTL never
            # Publisher 2001:4:4:4::4.4342, last published 00:00:52, TTL never, Expires: never'
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                last_published = groups['last_published']
                ttl = groups['ttl']
                publishers = "{}:{}".format(publishers,port)
                publish_dict = eid_prefix_dict.setdefault('publishers',{})\
                                              .setdefault(publishers,{})
                publish_dict.update({
                    'port': port,
                    'last_published': last_published,
                    'ttl': ttl
                })
                continue

            # publisher epoch 0,entry epoch 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                publisher_epoch = int(groups['publisher_epoch'])
                entry_epoch = int(groups['entry_epoch'])
                publish_dict.update({
                    'publisher_epoch': publisher_epoch,
                    'entry_epoch': entry_epoch
                })
                continue

            # entry-state complete
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                entry_state = groups['entry_state']
                publish_dict.update({'entry_state':entry_state})
                continue

            # routing table tag 101
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                routing_tag = int(groups['routing_tag'])
                publish_dict.update({'routing_tag':routing_tag})
                continue

            # xTR-ID 0x790800FF-0x426D6D8E-0xC6C5F60C-0xB4386D22
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                xtr_id = groups['xtr_id']
                publish_dict.update({'xtr_id':xtr_id})
                continue

            # site-ID unspecified
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                site_id = groups['site_id']
                publish_dict.update({'site_id':site_id})
                continue

            # Domain-ID unset
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                domain_id = (groups['domain_id'])
                publish_dict.update({'domain_id':domain_id})
                continue

            # Multihoming-ID unspecified
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                multihoming_id = (groups['multihoming_id'])
                publish_dict.update({'multihoming_id':multihoming_id})
                continue

            # Publish-mode no-extranet
            m = p14_1.match(line)
            if m:
                groups = m.groupdict()
                publish_mode = groups['publish_mode']
                publish_dict.update({'publish_mode':publish_mode})
                continue

            # Merge Locator Information
            # Locator        Pri/Wgt  State     Encap-IID  RDP-Len Src-Address
            # 100.88.88.88    20/90   up        -          0       100.77.77.77
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                merged_locators = (groups['merged_locators'])
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                state = groups['state']
                encap_iid = groups['encap_iid']
                rdp_len = groups['rdp_len']
                src_add = groups['src_add']

                merged_dict = eid_prefix_dict.setdefault('merged_locators',{})\
                                             .setdefault(merged_locators,{})
                merged_dict.update({
                    'priority': priority,
                    'weight': weight,
                    'state': state,
                    'encap_iid': encap_iid,
                    'rdp_len': rdp_len,
                    'src_add': src_add
                })
                # Merge Locator Information
                # * Indicates the selected rlocs used by consumers
                # Locator        Pri/Wgt  State     Encap-IID  RDP-Len Src-Address
                # 100.88.88.88    20/90   up        -          0       100.77.77.77
                # 100.89.89.89    20/90   up        -          -       100.77.77.77
                # 100.90.90.90    20/90   up        -          ext     100.77.77.77
                # 100::88:88:88   20/90   up        -          0       100.77.77.77
                # 100::88:88:88*  20/90   up        -          0       100.77.77.77
                merged_publisher_dict = merged_dict.setdefault('publishers',{}) \
                                                   .setdefault(src_add,{})
                merged_publisher_dict.update({
                    'priority': priority,
                    'weight': weight,
                    'state': state,
                    'encap_iid': encap_iid,
                    'rdp_len': rdp_len,
                    'selected': groups['selected'] == '*'
                })
                continue

            # 22.22.22.22   10/10   up        -      [-]
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                locators = (groups['locators'])
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                state = groups['state']
                encap_iid = groups['encap_iid']
                locator_dict =  publish_dict.setdefault('locators',{})\
                                            .setdefault(locators,{})
                locator_dict.update({
                    'priority': priority,
                    'weight': weight,
                    'state': state,
                    'encap_iid': encap_iid
                })
                if groups['rdp'] != None:
                    rdp = groups['rdp']
                    locator_dict.update({'rdp':rdp})
                continue

            # 100.88.88.88  100/50   up        -                   1/1       44
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                locators = (groups['locators'])
                priority = int(groups['priority'])
                weight = int(groups['weight'])
                state = groups['state']
                encap_iid = groups['encap_iid']
                locator_dict =  publish_dict.setdefault('locators',{})\
                                            .setdefault(locators,{})
                locator_dict.update({
                    'priority': priority,
                    'weight': weight,
                    'state': state,
                    'encap_iid': encap_iid
                })
                if groups['metric'] != None:
                    metric = groups['metric']
                    locator_dict.update({'metric':metric})
                if groups['domain_id'] != None:
                    domain_id = int(groups['domain_id'])
                    locator_dict.update({'domain_id':domain_id})
                if groups['multihoming_id'] != None:
                    multihoming_id = int(groups['multihoming_id'])
                    locator_dict.update({'multihoming_id':multihoming_id})
                continue

            # Affinity-id: 20 , 20
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                affinity_id_x = int(groups['affinity_id_x'])
                if groups['affinity_id_y']:
                    affinity_id_y = int(groups['affinity_id_y'])
                    locator_dict.update({'affinity_id_x':affinity_id_x,
                                         'affinity_id_y':affinity_id_y})
                else:
                    locator_dict.update({'affinity_id_x':affinity_id_x})
                continue

            # Publisher 100.100.100.100:4342
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                publishers = "{}:{}".format(publishers,port)
                publish_dict = eid_prefix_dict.setdefault('publishers',{})\
                                              .setdefault(publishers,{})
                publish_dict.update({'port':port})
                continue

            # Publisher 100::100:100:100:100:100.4342
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                publishers = groups['publishers']
                port = int(groups['port'])
                publishers = "{}.{}".format(publishers,port)
                publish_dict = eid_prefix_dict.setdefault('publishers',{})\
                                              .setdefault(publishers,{})
                publish_dict.update({'port':port})
                continue

        # last published 16:02:47, TTL never
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                last_published = groups['last_published']
                ttl = groups['ttl']
                publish_dict.update({
                    'last_published': last_published,
                    'ttl': ttl
                })
                continue

            # SGT 100
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                sgt = int(groups['sgt'])
                publish_dict.update({'sgt':sgt})
                continue

        return lisp_v4_pub_pre
