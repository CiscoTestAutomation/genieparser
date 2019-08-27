#!/bin/env python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowSegmentRoutingPrefixSidMapSchema(MetaParser):
    ''' Schema for:
          *  show isis segment-routing prefix-sid-map active-policy
          *  show isis segment-routing prefix-sid-map backup-policy
        '''
    schema = {
        Any() : {
            'name' : str,
            Any() : {
                'status' : bool,
                'entries' : int,
                'algorithm' : {
                    'prefix' : str,
                    'sid_index' : int,
                    'range' : int,
                    Optional('flags'): str,
                },
                Optional('isis_id'): int,
                Optional('process_id') : int,
            },
        }
    }

class ShowSegmentRoutingPrefixSidMap(ShowSegmentRoutingPrefixSidMapSchema):
    ''' Parser for:
          *  show isis segment-routing prefix-sid-map active-policy
          *  show isis segment-routing prefix-sid-map backup-policy
        '''

    cli_command = 'show isis segment-routing prefix-sid-map {status}'

    def cli(self, output= None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        p1 = re.compile(r'RP\/0\/0\/CPU0:router# show '
            '(?P<name>\w+)\s+segment-routing prefix-sid-map '
            '(?P<status>\w+)-policy$')
        
        p2 = re.compile(r'^SRMS \w+ policy for Process ID (?P<process_id>\d+)$')
        
        p3 = re.compile(r'^IS-IS (?P<isis_id>\d+) \w+ policy$')

        p4 = re.compile(r'(?P<prefix>[\w\.\/]+)\s+(?P<sid_index>\d+)'
            '\s+(?P<range>\d+)(\s+(?P<flags>)[\w\s]+$)?')
        
        p5 = re.compile(r'Number of mapping entries:\s+(?P<entries>\d+)')

        for line in out.splitlines():
            line = line.strip()
        
            # RP/0/0/CPU0:router# show isis segment-routing prefix-sid-map active-policy
            m = p1.match(line)
            if m:
                status_bool = True if 'active' in m.groupdict()['status'].lower()\
                    else False
                name = m.groupdict()['name']
                status = m.groupdict()['status']

                router_dict = ret_dict.setdefault(name, {})
                router_dict['name'] = name
                status_dict = router_dict.setdefault(status, {})
                status_dict['status'] = status_bool

            # SRMS active policy for Process ID 1
            m = p2.match(line)
            if m:
                status_dict.setdefault('process_id', \
                    int(m.groupdict()['process_id']))
            
            # IS-IS 1 active policy
            m = p3.match(line)
            if m:
                status_dict.setdefault('isis_id', int(m.groupdict()['isis_id']))


            # Prefix               SID Index    Range        Flags
            # 1.1.1.100/32         100          20          
            # 1.1.1.150/32         150          10          
            m = p4.match(line)
            if m:
                algo_dict = status_dict.setdefault('algorithm', {})
                algo_dict.setdefault('prefix', m.groupdict()['prefix'])
                algo_dict.setdefault('sid_index', int(m.groupdict()['sid_index']))
                algo_dict.setdefault('range', int(m.groupdict()['range']))
                if 'flag' in line.lower():
                    algo_dict.setdefault('flags', m.groupdict()['flags'])

            # Number of mapping entries: 2
            m = p5.match(line)
            if m:
                status_dict['entries'] = int(m.groupdict()['entries'])
        
        return ret_dict
