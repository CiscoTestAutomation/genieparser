''' show_bgp.py

Example parser class

'''

import re   
from metaparser import MetaParser   
from metaparser.util.schemaengine import Schema, Any 

#*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

class ShowIpBgpSummarySchema(MetaParser):

    schema = {
        'bgp_summary': 
            {'identifier': 
                {Any(): 
                    {'version': str,
                     'autonomous_system_number': str,
                     'table_version': str,
                    },
                },
             'neighbor': 
                {Any(): 
                    {'ver': str,
                     'asn': str,
                     'msgr': str,
                     'msgs': str,
                     'tblv': str,
                     'inq': str,
                     'outq': str,
                     'up_down': str,
                     'state_pfxrcd': str,
                     },
                },
            },
        }

class ShowIpBgpSummary(ShowIpBgpSummarySchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show ip bgp summary'.format()
        out = self.device.execute(cmd)
        bgp_summary_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*BGP +router +identifier +(?P<router_id>[0-9\.]+)\, +local +AS +number +(?P<as_number>[0-9]+)$')
            m = p1.match(line)
            if m:
                router_id = m.groupdict()['router_id']
                autonomous_system_number = m.groupdict()['as_number']
                if 'bgp_summary' not in bgp_summary_dict:
                    bgp_summary_dict['bgp_summary'] = {}
                if 'identifier' not in bgp_summary_dict['bgp_summary']:
                    bgp_summary_dict['bgp_summary']['identifier'] = {}
                if router_id not in bgp_summary_dict['bgp_summary']['identifier']:
                    bgp_summary_dict['bgp_summary']['identifier'][router_id] = {}
                bgp_summary_dict['bgp_summary']['identifier'][router_id]['autonomous_system_number'] = autonomous_system_number
                continue

            p2 = re.compile(r'^\s*BGP +table +version +is +(?P<table_ver>([0-9]+))\, +main +routing +table +version +(?P<r_t_ver>[0-9]+)$')
            m = p2.match(line)
            if m:
                table_version = m.groupdict()['table_ver']
                version = m.groupdict()['r_t_ver']

                bgp_summary_dict['bgp_summary']['identifier'][router_id]['table_version'] = table_version
                bgp_summary_dict['bgp_summary']['identifier'][router_id]['version'] = version
                continue

            p3 = re.compile(r'^\s*Neighbor +V +AS +MsgRcvd +MsgSent +TblVer +InQ +OutQ +Up/Down +State/PfxRcd$')
            m = p3.match(line)
            if m:
                continue

            p4 = re.compile(r'^\s*(?P<neighbor>[0-9\.]+) +(?P<ver>[0-9]+) +(?P<asn>[0-9]+) +(?P<msgr>[0-9]+) +(?P<msgs>[0-9]+) +(?P<tblv>[0-9]+) +(?P<inq>[0-9]+) +(?P<outq>[0-9]+) +(?P<up_down>[a-zA-Z0-9\:]+) +(?P<state_pfxrcd>[a-zA-Z0-9]+)$')
            m = p4.match(line) 
            if m:
                neighbor = m.groupdict()['neighbor']
                if 'neighbor' not in bgp_summary_dict['bgp_summary']:
                    bgp_summary_dict['bgp_summary']['neighbor'] = {}
                if neighbor not in bgp_summary_dict['bgp_summary']['neighbor']:
                    bgp_summary_dict['bgp_summary']['neighbor'][neighbor] = {}
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['ver'] = str(m.groupdict()['ver'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['asn'] = str(m.groupdict()['asn'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['msgr'] = str(m.groupdict()['msgr'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['msgs'] = str(m.groupdict()['msgs'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['tblv'] = str(m.groupdict()['tblv'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['inq'] = str(m.groupdict()['inq'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['outq'] = str(m.groupdict()['outq'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['up_down'] = str(m.groupdict()['up_down'])
                bgp_summary_dict['bgp_summary']['neighbor'][neighbor]['state_pfxrcd'] = str(m.groupdict()['state_pfxrcd'])
                continue

        return bgp_summary_dict