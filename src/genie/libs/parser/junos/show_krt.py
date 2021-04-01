""" show_krt.py

JunOs parsers for the following show commands:
    * show krt state
    * show krt queue
"""

import re

from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, ListOf)

class ShowKrtStateSchema(MetaParser):

    schema = {
    "krt-state-information": {
        "krt-queue-state": {
            "krtq-async-count": str,
            "krtq-async-non-q-count": str,
            "krtq-high-mpls-adds": str,
            "krtq-high-mpls-changes": str,
            "krtq-high-multicast-adds-changes": str,
            "krtq-high-priority-adds": str,
            "krtq-high-priority-changes": str,
            "krtq-high-priority-deletes": str,
            "krtq-indirect-adds-changes": str,
            "krtq-indirect-deletes": str,
            "krtq-interface-routes": str,
            "krtq-kernel-rt-learnt": str,
            "krtq-normal-priority-adds": str,
            "krtq-normal-priority-changes": str,
            "krtq-normal-priority-deletes": str,
            "krtq-normal-priority-gmp": str,
            "krtq-normal-priority-indirects": str,
            "krtq-operations-canceled": str,
            "krtq-operations-deferred": str,
            "krtq-operations-queued": str,
            "krtq-rt-table-adds": str,
            "krtq-rt-table-deletes": str,
            "krtq-time-until-next-run": str
        },
        "rtsock-time-until-next-scan": str
    }
}


class ShowKrtState(ShowKrtStateSchema):
    """ Parser for:
    * show krt state
    """
    cli_command = 'show krt state'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #Number of operations queued: 0
        p1 = re.compile(r'^Number of operations queued: +(?P<krtq_operations_queued>\d+)$')

        #Routing table adds: 0
        p2 = re.compile(r'^Routing table adds: +(?P<krtq_rt_table_adds>\d+)$')

        #Interface routes: 0
        p3 = re.compile(r'^Interface routes: +(?P<krtq_interface_routes>\d+)$')

        #High pri multicast   Adds/Changes: 0
        p4 = re.compile(r'^High pri multicast +Adds\/Changes: +'
                        r'(?P<krtq_high_multicast_adds_changes>\d+)$')

        #Indirect Next Hop    Adds/Changes: 0       Deletes: 0
        p5 = re.compile(r'^Indirect Next Hop +Adds\/Changes: +(?P<krtq_indirect_adds_changes>\d+) +'
                        r'Deletes: +(?P<krtq_indirect_deletes>\d+)$')

        #MPLS        Adds: 0       Changes: 0
        p6 = re.compile(r'^MPLS +Adds: +(?P<krtq_high_mpls_adds>\d+) +Changes: +'
                        r'(?P<krtq_high_mpls_changes>\d+)$')

        #High pri    Adds: 0       Changes: 0       Deletes: 0
        p7 = re.compile(r'^High pri\s+Adds: +(?P<krtq_high_priority_adds>\d+)\s+Changes: +'
                        r'(?P<krtq_high_priority_changes>\d+)\s+Deletes: +'
                        r'(?P<krtq_high_priority_deletes>\d+)$')
        
        #Normal pri Indirects: 0
        p8 = re.compile(r'^Normal pri Indirects: +(?P<krtq_normal_priority_indirects>\d+)$')

        #Normal pri  Adds: 0       Changes: 0       Deletes: 0
        p9 = re.compile(r'^Normal pri\s+Adds: +(?P<krtq_normal_priority_adds>\d+)\s+Changes: +'
                        r'(?P<krtq_normal_priority_changes>\d+)\s+Deletes: +'
                        r'(?P<krtq_normal_priority_deletes>\d+)$')

        #GMP GENCFG Objects: 0
        p10 = re.compile(r'^GMP GENCFG Objects: +(?P<krtq_normal_priority_gmp>\d+)$')

        #Routing Table deletes: 0
        p11 = re.compile(r'^Routing Table deletes: +(?P<krtq_rt_table_deletes>\d+)$')

        #Number of operations deferred: 0
        p12 = re.compile(r'^Number of operations deferred: +(?P<krtq_operations_deferred>\d+)$')

        #Number of operations canceled: 0
        p13 = re.compile(r'^Number of operations canceled: +(?P<krtq_operations_canceled>\d+)$')

        #Number of async queue entries: 0
        p14 = re.compile(r'^Number of async queue entries: +(?P<krtq_async_count>\d+)$')

        #Number of async non queue entries: 0
        p15 = re.compile(r'^Number of async non queue entries: +(?P<krtq_async_non_q_count>\d+)$')

        #Time until next queue run: 0
        p16 = re.compile(r'^Time until next queue run: +(?P<krtq_time_until_next_run>\d+)$')

        #Routes learned from kernel: 34
        p17 = re.compile(r'^Routes learned from kernel: +(?P<krtq_kernel_rt_learnt>\d+)$')

        #Time until next scan: 58
        p18 = re.compile(r'^Time until next scan: +(?P<rtsock_time_until_next_scan>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            #Number of operations queued: 0
            m = p1.match(line)
            if m:
                krt_first_entry = ret_dict.setdefault("krt-state-information", {})

                krt_entry = krt_first_entry.setdefault("krt-queue-state", {})

                group = m.groupdict()

                krt_entry['krtq-operations-queued'] = group['krtq_operations_queued']
                continue

            #Routing table adds: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-rt-table-adds'] = group['krtq_rt_table_adds']
                continue
            
            #Interface routes: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-interface-routes'] = group['krtq_interface_routes']
                continue
            
            #High pri multicast   Adds/Changes: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-high-multicast-adds-changes'] = group['krtq_high_multicast_adds_changes']
                continue
            
            #Indirect Next Hop    Adds/Changes: 0       Deletes: 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-indirect-adds-changes'] = group['krtq_indirect_adds_changes']
                krt_entry['krtq-indirect-deletes'] = group['krtq_indirect_deletes']
                continue

            #MPLS        Adds: 0       Changes: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-high-mpls-changes'] = group['krtq_high_mpls_changes']
                krt_entry['krtq-high-mpls-adds'] = group['krtq_high_mpls_adds']
                continue

            #High pri    Adds: 0       Changes: 0       Deletes: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-high-priority-adds'] = group['krtq_high_priority_adds']
                krt_entry['krtq-high-priority-changes'] = group['krtq_high_priority_changes']
                krt_entry['krtq-high-priority-deletes'] = group['krtq_high_priority_deletes']
                continue

            #Normal pri Indirects: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-normal-priority-indirects'] = group['krtq_normal_priority_indirects']
                continue

            #Normal pri  Adds: 0       Changes: 0       Deletes: 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-normal-priority-adds'] = group['krtq_normal_priority_adds']
                krt_entry['krtq-normal-priority-changes'] = group['krtq_normal_priority_changes']
                krt_entry['krtq-normal-priority-deletes'] = group['krtq_normal_priority_deletes']
                continue
            
            #GMP GENCFG Objects: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-normal-priority-gmp'] = group['krtq_normal_priority_gmp']
                continue

            #Routing Table deletes: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-rt-table-deletes'] = group['krtq_rt_table_deletes']
                continue

            #Number of operations deferred: 0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-operations-deferred'] = group['krtq_operations_deferred']
                continue

            #Number of operations canceled: 0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-operations-canceled'] = group['krtq_operations_canceled']
                continue

            #Number of async queue entries: 0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-async-count'] = group['krtq_async_count']
                continue

            #Number of async non queue entries: 0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-async-non-q-count'] = group['krtq_async_non_q_count']
                continue

            #Time until next queue run: 0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-time-until-next-run'] = group['krtq_time_until_next_run']
                continue

            #Routes learned from kernel: 34
            m = p17.match(line)
            if m:
                group = m.groupdict()
                krt_entry['krtq-kernel-rt-learnt'] = group['krtq_kernel_rt_learnt']
                continue

            #Time until next scan: 58
            m = p18.match(line)
            if m:
                group = m.groupdict()
                krt_first_entry['rtsock-time-until-next-scan'] = group['rtsock_time_until_next_scan']
                continue
        return ret_dict

class ShowKrtQueueSchema(MetaParser):

    '''schema = {
        "krt-queue-information": {
            "krt-queue": [
                {
                    "krtq-queue-length": str,
                    "krtq-type": str
                }
            ]
        }
    }'''

    # Main Schema
    schema = {
        "krt-queue-information": {
            "krt-queue": ListOf({
                "krtq-queue-length": str,
                "krtq-type": str
            })
        }
    }


class ShowKrtQueue(ShowKrtQueueSchema):
    """ Parser for:
    * show krt queue
    """
    cli_command = 'show krt queue'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #Routing table add queue: 0 queued
        p1 = re.compile(r'^(?P<krtq_type>([^:(]+?))(\s*[:(]) (?P<krtq_queue_length>\d+) queued$')

        for line in out.splitlines():
            line = line.strip()

            #Routing table add queue: 0 queued
            m = p1.match(line)
            if m:
                krt_entry = ret_dict.setdefault("krt-queue-information", {}).setdefault("krt-queue", [])
                group = m.groupdict()
                krt_entry_dict = {}
                krt_entry_dict['krtq-type'] = group['krtq_type']
                krt_entry_dict['krtq-queue-length'] = group['krtq_queue_length']
                krt_entry.append(krt_entry_dict)
                continue

        return ret_dict
