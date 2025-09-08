"""show_monitor_session.py

NXOS parsers for the following show commands:

    * show monitor session
"""

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, ListOf

# import parser utils
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.exceptions import SchemaEmptyParserError

#====================================
# Schema for 'show monitor session'
# ===================================

class ShowMonitorSessionSchema(MetaParser):
    """Schema for:
         show monitor session"""
    schema = {
        'session': {
                'session_number': int,
                'type': str,
                Optional('mode'): str,
                Optional('ssn_direction'): str,
                'state': str,
                Optional('erspan_id'): int,
                Optional('vrf_name'): str,
                Optional('acl_name'): str,
                Optional('ip_ttl'): int,
                Optional('ip_dscp'): int,
                Optional('destination_ip'): str,
                Optional('origin_ip'): str,
                Optional('source_intf'): str,
                Optional('rx'): str,
                Optional('tx'): str,
                Optional('both'): int,
                Optional('source_exception'): str,
                Optional('src_intf_all'): str,
                Optional('filter_vlan'): int,
                Optional('destination_ports'): str,
                Optional('simple_filter'): str,
                Optional('trace_route'): bool, 
                Optional('dest_ip'): str,
                Optional('src_ip'): str,
                Optional('eth_type'): str,
                Optional('frame_type'): str,
                Optional('filter_vlans'): int,
                Optional('feature'): {
                    Any(): {
                        Optional('enabled'): str,
                        Optional('value'): str,
                        Optional('modules_supported'): ListOf(int),
                        Optional('modules_not_supported'): ListOf(int),
                    },
                },
                Optional('legend'): {
                    Optional('mcbe'): str,
                    Optional('l3_tx'): str,
                    Optional('exsp_x'): str,
                },

                },         

            
        
    }

#====================================
# Parser for 'show monitor session'
# ===================================
    
class ShowMonitorSession(ShowMonitorSessionSchema):
    """Parser for show monitor session"""
    
    cli_command = ['show monitor session {session_number}']
    def cli(self, session_number='', output=None):
        if output is None:
            out = self.device.execute(self.cli_command).format(session_number=session_number)
        else:
            out = output
        
        ret_dict = {}
        session_dict = None  
        
        # Session 1
        p1 = re.compile(r'^session +(?P<session_number>\d+)$')

        # Type                   : erspan-source
        p2 = re.compile(r"^type\s+:\s+(?P<type>.+)$")

        # Mode                   : extended
        p3 = re.compile(r"^mode\s+:\s+(?P<mode>.+)$")
        
        # ssn direction          : both
        p4 = re.compile(r"^ssn direction\s+:\s+(?P<ssn_direction>.+)$")

        # State                  : up
        p5 = re.compile(r"^state\s+:\s+(?P<state>.+)$")

        # erspan-id         : 1
        p6 = re.compile(r"^erspan-id\s+:\s+(?P<erspan_id>\d+)$")

        # vrf-name               : default
        p7 = re.compile(r"^vrf-name\s+:\s+(?P<vrf_name>.+)$")

        # acl-name               : acl-name not specified
        p8 = re.compile(r"^acl-name\s+:\s+(?P<acl_name>.+)$")

        # ip-ttl                 : 255
        p9 = re.compile(r"^ip-ttl\s+:\s+(?P<ip_ttl>\d+)$")

        # ip-dscp                : 0
        p10 = re.compile(r"^ip-dscp\s+:\s+(?P<ip_dscp>\d+)$")

        #destination-ip    : 9.1.1.2
        p11 = re.compile(r"^destination-ip\s+:\s+(?P<destination_ip>[0-9.]+)$")

        #origin-ip         : 5.5.5.5 (global)
        p12 = re.compile(r'^#?origin-ip\s*:\s*(?P<origin>.+)$')

        #source intf       :
        p13 = re.compile(r"^#?source intf\s*:\s*(?P<source_intf>.*)$")

        #rx                :
        p14 = re.compile(r"^#?rx\s*:\s*(?P<rx>.*)$")

        #tx                :
        p15 = re.compile(r"^#?tx\s*:\s*(?P<tx>.*)$")

        #both              :
        p16 = re.compile(r"^#?both\s*:\s*(?P<both>.*)$")

        #source VLANS      :
        p17 = re.compile(r"^#?source VLANs\s*:\s*(?P<source_vlans>.*)$")

        #source exception  :
        p18 = re.compile(r"^#?source exception\s*:\s*(?P<source_exception>.*)$")

        #src intf all      :
        p19 = re.compile(r"^src intf all\s+:\s+(?P<src_intf_all>.+)$")

        #filter VLANs      : 100
        p20 = re.compile(r"^filter VLANs\s+:\s+(?P<filter_vlans>\d+)$")

        #simple filter     : 
        p21 = re.compile(r"^simple filter\s+:\s*(?P<simple_filter>.*)$")

        #trace-route       : false
        p22 = re.compile(r"^trace-route\s+:\s+(?P<trace_route>\w+)$")

        #eth-type          : 0x8100
        p23 = re.compile(r"^eth-type\s+:\s+(?P<eth_type>0x[0-9a-fA-F]+)$")

        #frame-type        : ipv4
        p24 = re.compile(r"^frame-type\s+:\s+(?P<frame_type>.+)$")

        #dest-ip       : 10.10.100.11/32
        p25 = re.compile(r"^dest-ip\s+:\s+(?P<dest_ip>[0-9./]+)$")

        #src-ip        : 10.10.100.21/32
        p26 = re.compile(r"^src-ip\s+:\s+(?P<src_ip>[0-9./]+)$")

        # MTU-Trunc     No
        # rate-limit-rx No
        # rate-limit-tx No
        # Sampling      No
        # MCBE          No
        # L3-TX         -         -       1                       3  4  9
        # ERSPAN-ACL    -         -       -                       1  3  4  9
        # ERSPAN-V2     Yes       -       1  3  4  9              -
        # Simpl RB span Yes       -       1  3  4  9              -
        # EXTENDED-SSN  Yes       -       1  3  4  9              -
        # Type-II       Yes       -       3  4  9                 1
        # Type-III      Yes       -       3  4  9                 1
        p27 = re.compile(
            r"^(?P<feature>.+?)\s+(?P<enabled>Yes|No|-)"
            r"(?:\s+(?P<value>[^\s]+|-))?"
            r"(?:\s+(?P<modules_supported>(?:\d+\s+)*\d+|-))?"
            r"(?:\s+(?P<modules_not_supported>(?:\d+\s+)*\d+|-))?$"
        )
        
        #MCBE = Multicast Best Effort
        p28 = re.compile(r'^MCBE\s*=\s*(?P<mcbe>Multicast Best Effort)$')

        #L3-TX = L3 Multicast Egress SPAN
        p29 = re.compile(r'^L3\-TX\s*=\s*(?P<l3_tx>L3 Multicast Egress SPAN)$')


        #ExSP-X = Exception Span for type X (L3, FP, or misc)
        p30 = re.compile(r'^ExSP\-X\s*=\s*Exception Span for type X\s+\((?P<exsp_x>[^)]+)\)$')
        

        for line in out.splitlines():
            line = line.strip()

            # Session 1
            m = p1.match(line)
            if m:
                session_number = int(m.group('session_number'))
                session_dict = ret_dict.setdefault('session', {})
                session_dict.setdefault('session_number', session_number)
                continue

            # Type                   : erspan-source
            m = p2.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['type'] = m.group('type')
                continue

            # Mode                   : extended
            m = p3.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['mode'] = m.group('mode')
                continue

            # ssn direction          : both
            m = p4.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['ssn_direction'] = m.group('ssn_direction')
                continue

            # State                  : up
            m = p5.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['state'] = m.group('state')
                continue

            # erspan-id         : 1
            m = p6.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['erspan_id'] = int(m.group('erspan_id'))
                continue

            # vrf-name               : default
            m = p7.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['vrf_name'] = m.group('vrf_name')
                continue

            # acl-name               : acl-name not specified
            m = p8.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['acl_name'] = m.group('acl_name')
                continue

            # ip-ttl                 : 255
            m = p9.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['ip_ttl'] = int(m.group('ip_ttl'))
                continue

            # ip-dscp                : 0
            m = p10.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['ip_dscp'] = int(m.group('ip_dscp'))
                continue

            #destination-ip    : 9.1.1.2
            m = p11.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['destination_ip'] = m.group('destination_ip')
                continue

            #origin-ip         : 5.5.5.5 (global)
            m = p12.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['origin_ip'] = m.group('origin')
                continue

            #source intf       :
            m = p13.match(line)
            if m:
                source_intf = m.group('source_intf')
                if source_intf:
                    ret_dict.setdefault('session', {})['source_intf'] = source_intf
                continue

            #rx                :
            m = p14.match(line)
            if m:
                rx = m.group('rx')
                if rx:
                    ret_dict.setdefault('session', {})['rx'] = rx  
                continue

            #tx                :
            m = p15.match(line)
            if m:
                tx = m.group('tx')
                if tx:
                    ret_dict.setdefault('session', {})['tx'] = tx
                continue

            #both              :
            m = p16.match(line)
            if m:
                both = m.group('both')
                if both:
                    ret_dict.setdefault('session', {})['both'] = both
                continue

            #source VLANS      :
            m = p17.match(line)
            if m:
                source_vlans = m.group('source_vlans')
                if source_vlans:
                    ret_dict.setdefault('session', {})['source_vlans'] = source_vlans
                continue

            #source exception  :
            m = p18.match(line)
            if m:
                source_exception = m.group('source_exception')
                if source_exception:
                    ret_dict.setdefault('session', {})['source_exception'] = source_exception
                continue

            #src intf all      :
            m = p19.match(line)
            if m:
                src_intf_all = m.group('src_intf_all')
                if src_intf_all:
                    ret_dict.setdefault('session', {})['src_intf_all'] = src_intf_all
                continue

            #filter VLANs      : 100
            m = p20.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['filter_vlans'] = int(m.group('filter_vlans'))
                continue

            #simple filter     :
            m = p21.match(line)
            if m:
                simple_filter = m.group('simple_filter')
                if simple_filter:
                    ret_dict.setdefault('session', {})['simple_filter'] = simple_filter
                continue

            #trace-route       : false
            m = p22.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['trace_route'] = m.group('trace_route').lower() == 'true'
                continue

            #eth-type          : 0x8100
            m = p23.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['eth_type'] = m.group('eth_type')
                continue

            #frame-type        : ipv4
            m = p24.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['frame_type'] = m.group('frame_type')
                continue
            
            # dest-ip       : 10.10.100.11/32
            m = p25.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['dest_ip'] = m.group('dest_ip')
                continue

            # src-ip        : 10.10.100.21/32
            m = p26.match(line)
            if m:
                session_dict = ret_dict.setdefault('session', {})
                session_dict['src_ip'] = m.group('src_ip')
                continue

            # MTU-Trunc     No
            # rate-limit-rx No
            # rate-limit-tx No
            # Sampling      No
            # MCBE          No
            # L3-TX         -         -       1                       3  4  9
            # ERSPAN-ACL    -         -       -                       1  3  4  9
            # ERSPAN-V2     Yes       -       1  3  4  9              -
            # Simpl RB span Yes       -       1  3  4  9              -
            # EXTENDED-SSN  Yes       -       1  3  4  9              -
            # Type-II       Yes       -       3  4  9                 1
            # Type-III      Yes       -       3  4  9                 1
            m = p27.match(line)
            if m:
                feature = m.group('feature').strip().lower().replace('-', '_')
                feature_dict = session_dict.setdefault('feature', {}).setdefault(feature, {})
                feature_dict['enabled'] = m.group('enabled')

                value = m.group('value')
                if value and value != '-':
                    feature_dict['value'] = value

                supported = m.group('modules_supported')
                if supported and supported != '-':
                    feature_dict['modules_supported'] = [int(x) for x in supported.split()]

                not_supported = m.group('modules_not_supported')
                if not_supported and not_supported != '-':
                    feature_dict['modules_not_supported'] = [int(x) for x in not_supported.split()]
                continue
            
            #MCBE = Multicast Best Effort
            m = p28.match(line)
            if m:
                legend = session_dict.setdefault('legend', {})
                legend['mcbe'] = m.group('mcbe')
                continue
            
            #L3-TX = L3 Multicast Egress SPAN
            m = p29.match(line)
            if m:
                legend = session_dict.setdefault('legend', {})
                legend['l3_tx'] = m.group('l3_tx')
                continue
            
            #ExSP-X = Exception Span for type X (L3, FP, or misc)
            m = p30.match(line)
            if m:
                legend = session_dict.setdefault('legend', {})
                legend['exsp_x'] = m.group('exsp_x')
                continue

        return ret_dict