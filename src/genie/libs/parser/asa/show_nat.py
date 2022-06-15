''' show_nat.py

ASA parsers for the following show commands:
    * show nat
    * show nat detail
    * show nat {address}
    * show nat {address} detail
    * show nat translated {address}
    * show nat translated {address} detail
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =============================================
# Schema for:
#   *'show nat'
#   * 'show nat detail'
#   * 'show nat {address}'
#   * 'show nat {address} detail'
#   * 'show nat translated {address}'
#   * 'show nat translated {address} detail'
# =============================================
class ShowNatSchema(MetaParser):
    ''''Schema for
        * 'show nat'
        * 'show nat detail'
        * 'show nat {address}'
        * 'show nat {address} detail'
        * 'show nat translated {address}'
        * 'show nat translated {address} detail'
    '''

    schema = {
    	'nat': {
            Any(): {
                'internal-interface': str,
                'external-interface': str,
                'dns': bool,
                'proxy-arp': bool,
                'hits': {
                    'translate': int,
                    'untranslate': int
                },
                Optional('source'): {
                    'object-name': str,
                    'natted-address': str,
                    'type': str,
                    'real-address-and-mask': str,
                    'natted-address-and-mask': str
                },
                Optional('destination'): {
                    'object-name': str,
                    'natted-address': str,
                    'type': str,
                    'real-address-and-mask': str,
                    'natted-address-and-mask': str
                }
            }
        }
    }

# =============================================
# Parser for:
#    *'show nat'
#    * 'show nat detail'
#    * 'show nat {address}'
#    * 'show nat {address} detail'
#    * 'show nat translated {address}'
#    * 'show nat translated {address} detail'
# =============================================
class ShowNat(ShowNatSchema):
    ''''Parser for
        * 'show nat'
        * 'show nat detail'
        * 'show nat {address}'
        * 'show nat {address} detail'
        * 'show nat translated {address}'
        * 'show nat translated {address} detail'
    '''

    cli_command = ['show nat',
                   'show nat detail',
                   'show nat {address}',
                   'show nat {address} detail',
                   'show nat translated {address}',
                   'show nat translated {address} detail' ]

    def cli(self, output=None):
        if output is None:
            # excute command to get output
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        #Auto NAT Policies (Section 2)
        # TODO Not sure what to extract here

        # 1 (if1) to (if2) source static obj_name 1.1.1.1  dns no-proxy-arp
        
        p1 = re.compile(r'(?P<entry_num>\d*)\s+(\((?P<in_if>[^)]*)\)\s+to\s+'
                        r'\((?P<out_if>[^)]*)\))?\s+'
                        r'(source\s+(?P<source>\S*\s+\S+\s+[0-9.]+)\s+)?'
                        r'(destination\s+(?P<destination>\S*\s+\S+\s+[0-9.]+)\s+)?'
                        r'(?P<dns>dns)?\s+(?P<no_proxy_arp>no-proxy-arp)?')

        # for both source and destination
        # static obj_name 1.1.1.1
        # dynamic 2.2.2.2 1.1.1.1
        
        p1_1 = re.compile(r'(?P<type>\S*)\s+'r'(?P<obj_name>\S+)\s+'
                          r'(?P<natted>[0-9.]+)')
        
        # translate_hits = 10, untranslate_hits = 8

        p2 = re.compile(r'translate_hits\s*=\s*(?P<trans>\d+),'
                        r'\s*untranslate_hits\s*=\s*(?P<un_trans>\d*)')
        
        # Source - Origin: 1.1.1.1/32, Translated: 2.2.2.2/32

        p3 = re.compile(r'(?P<src_dst>Source|Destination)\s+-\s+Origin\:\s+(?P<address>[\d.]+\/\d+),\s+'
                        r'Translated\:\s+(?P<trans>[\d.]+\/\d+)')
        
        for line in output.splitlines():
            line = line.strip()

            print('{}'.format(line))

            if line == '':
                continue

            # 1 (if1) to (if2) source static obj_name 1.1.1.1  dns no-proxy-arp
            m = p1.match(line)
            if m:
                print('{} matched p1'.format(line))
                groups = m.groupdict()
                entry_num = groups['entry_num']
                nat_entry = ret_dict.setdefault('nat', {}).setdefault(entry_num, {})
                nat_entry.update({'internal-interface': groups['in_if'] })
                nat_entry.update({'external-interface': groups['out_if'] })
                src_txt = str(groups.get('source', ''))
                m1 = p1_1.match(src_txt)
                if m1:
                    source = nat_entry.setdefault('source',{})
                    src_groups = m1.groupdict()
                    source.update({'type': src_groups['type']})
                    source.update({'object-name': src_groups['obj_name']})
                    source.update({'natted-address': src_groups['natted']})
                dst_txt = str(groups.get('destination', '')) 
                m1 = p1_1.match(dst_txt)
                if m1:
                    dest = nat_entry.setdefault('destination',{})
                    dst_groups = m1.groupdict()
                    dest.update({'type': dst_groups['type']})
                    dest.update({'object-name': dst_groups['obj_name']})
                    dest.update({'natted-address': dst_groups['natted']})
                nat_entry.update({'dns': bool('dns' in groups)})
                nat_entry.update({'proxy-arp': not('no-proxy-arp' in groups)})
                continue
            
            # translate_hits = 10, untranslate_hits = 8
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                hits = nat_entry.setdefault('hits', {})
                hits.update({'translate': int(groups['trans'])})
                hits.update({'untranslate': int(groups['un_trans'])})
                continue

            # Source - Origin: 1.1.1.1/32, Translated: 2.2.2.2/32
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                src_dst = groups['src_dst']
                container = nat_entry.setdefault(src_dst.lower(),{})
                container.update({'real-address-and-mask': groups['address']})
                container.update({'natted-address-and-mask': groups['trans']})
                continue

        return ret_dict
