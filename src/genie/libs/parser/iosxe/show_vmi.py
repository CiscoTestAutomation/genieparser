''' show_vmi.py

IOSXE parsers for the following show commands:

    * 'show vmi neighbors detail'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
from genie.libs.parser.utils.common import Common


class ShowVmiNeighborsDetailSchema(MetaParser):
    """Schema for 'show vmi neighbors detail' """

    schema = {
        'vmi1_neighbors': int, 
        Any(): {
            'ipv6_address': str, 
            'ipv6_global_addr': str, 
            'ipv4_address': str,
            'uptime': str, 
            'output_pkts': int, 
            'input_pkts': int, 
            'transport_pppoe': {
                'session_id': int,
            }, 
            'interface_stats': {
                Any(): {
                    Any(): {
                        'input_qcount': int,
                        'input_drops': int,
                        'output_qcount': int, 
                        'output_drops': int,
                    }
                },
            }, 
            'pppoe_flow_control_stats': {
                'local_credits': int,
                'peer_credits': int, 
                'local_scaling_value': str, 
                'credit_grant_threshold': int, 
                'max_credits_per_grant': int, 
                'credit_starved_packets': int,
                'padg_xmit_seq_num': int,
                'padg_timer_index': int, 
                'padg_last_rcvd_seq_num': int, 
                'padg_last_nonzero_seq_num': int, 
                'padg_last_nonzero_rcvd_amount': int, 
                'padg_timers_in_milliseconds': {
                    '0': int,
                    '1': int, 
                    '2': int, 
                    '3': int, 
                    '4': int,
                }, 
                'padg_xmit': int,
                'padg_rcvd': int,
                'padc_xmit': int,
                'padc_rcvd': int, 
                'in_band_credit_pkt_xmit': int,
                'in_band_rcvd': int,
                'last_credit_packet_snapshot': {
                    'padg_xmit': {
                        'seq_num': int,
                        'fcn': int,
                        'bcn': int,
                    }, 
                    'padc_rcvd': {
                        'seq_num': int,
                        'fcn': int,
                        'bcn': int,
                    }, 
                    'padg_rcvd': {
                        'seq_num': int,
                        'fcn': int,
                        'bcn': int,
                    }, 
                    'padc_xmit': {
                        'seq_num': int,
                        'fcn': int,
                        'bcn': int,
                    }, 
                    'in_band_credit_pkt_xmit': {
                        'fcn': int,
                        'bcn': int,
                    }, 
                    'in_band_credit_pkt_rcvd': {
                        'fcn': int,
                        'bcn': int,
                    }, 
                    'padq_statistics': {
                        'padq_xmit': int,
                        'rcvd': int
                    }
                }
            }
        }
    }


class ShowVmiNeighborsDetail(ShowVmiNeighborsDetailSchema):
    """
    Parser for 'show vmi neighbors detail'
    """

    cli_command = 'show vmi neighbors detail'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        

        # initial return dictionary
        ret_dict = {}

        # 1 vmi1 Neighbors
        p1 = re.compile(r'^(?P<val>\d+)\s+(?P<var>\w+\s+\w+)$')

        # vmi1   IPV6 Address=FE80::6E13:D5FF:FE3F:9710
        p2 = re.compile(r'^(?P<var>\w+)\s+(?P<var1>[Ii]\w+\s+\w+)\s*=\s*(?P<val1>.+)$')


        # IPV6 Global Addr=::
        p3 = re.compile(r'^(?P<var1>\w+\s+[Gg]\w+\s+\w+)\s*=\s*(?P<val1>.+)$')

        # IPV4 Address=81.0.0.1, Uptime=00:01:26
        p4 = re.compile(r'^(?P<var1>\w+\s+\w+)\s*=\s*(?P<val1>\S+),\s*(?P<var2>\w+)\s*=\s*(?P<val2>\S+)$')

        # Output pkts=0, Input pkts=0
        p5 = re.compile(r'^(?P<var1>\w+\s+\w+)\s*=\s*(?P<val1>\d+)\s*,\s*(?P<var2>\w+\s+\w+)\s*=\s*(?P<val2>\d+)$')

        # Transport PPPoE, Session ID=2
        p6 = re.compile(r'^(?P<var1>\w+\s+\w+)\s*,\s*(?P<var2>\w+\s+\w+)\s*=\s*(?P<val2>\d+)$')

        # INTERFACE STATS:
        p7 = re.compile(r'^(?P<var>[Ii]\w+\s+[Ss]\w+):$')

        # VMI Interface=vmi1,
        p8 = re.compile(r'^(?P<var1>[Vv]\w+\s+\w+)\s*=\s*(?P<val1>\w+),$')

        # V-Access intf=Virtual-Access1.1,
        p9 = re.compile(r'^(?P<var1>[Vv]-\w+\s+\w+)\s*=\s*(?P<val1>\S+),$')

        # Physical intf=GigabitEthernet0/0/4,
        p10 = re.compile(r'^(?P<var1>[Pp]\w+\s+\w+)\s*=\s*(?P<val1>\S+),$')

        # Input qcount=0, drops=0, Output qcount=0, drops=0
        # Input qcount=0, drops=0, Output qcount=0, drops=0
        # Input qcount=0, drops=0, Output qcount=0, drops=0
        p11 = re.compile(r'^(?P<var1>\w+\s+\w+)\s*=\s*(?P<val1>\d+)\s*,\s*(?P<var2>\w+)\s*=\s*(?P<val2>\d+)\s*,\s*(?P<var3>\w+\s+\w+)\s*=\s*(?P<val3>\d+)\s*,\s*(?P<var4>\w+)\s*=\s*(?P<val4>\d+)$')

        # PPPoE Flow Control Stats
        p12 = re.compile(r'^(?P<var>PPPoE\s+.+)$')

        # Local Credits: 1953   Peer Credits: 65535   Local Scaling Value 65534 bytes
        p13 = re.compile(r'^(?P<var1>\w+\s+\w+)\s*:\s*(?P<val1>\d+)\s+(?P<var2>\w+\s+\w+)\s*:\s+(?P<val2>\d+)\s+(?P<var3>\w+\s+\w+\s+\w+)\s+(?P<val3>\d+\s+\w+)$')

        # Credit Grant Threshold: 28000    Max Credits per grant: 65535
        p14 = re.compile(r'^(?P<var1>\w+\s+\w+\s+\w+)\s*:\s*(?P<val1>\d+)\s+(?P<var2>\w+\s+\w+\s+\w+\s+\w+)\s*:\s*(?P<val2>\d+)$')

        # Credit Starved Packets: 0
        p15 = re.compile(r'^(?P<var1>\w+\s+[Ss]\w+\s+\w+)\s*:\s*(?P<val1>\d+)$')

        # PADG xmit Seq Num: 884     PADG Timer index: 148
        p16 = re.compile(r'^(?P<var1>\w+\s+\w+\s+\w+\s+\w+)\s*:\s*(?P<val1>\d+)\s+(?P<var2>\w+\s+\w+\s+\w+)\s*:\s*(?P<val2>\d+)$')

        #  PADG last rcvd Seq Num: 0
        #  PADG last nonzero Seq Num: 148
        #  PADG last nonzero rcvd amount: 0
        p17 = re.compile(r'^(?P<var1>\w+\s+[Ll]\w+\s+\w+\s+\w+\s+\w+)\s*:\s*(?P<val1>\d+)$')

        # PADG Timers: (ms)   [0]-1000    [1]-2000    [2]-3000    [3]-4000    [4]-5000
        p18 = re.compile(r'^(?P<var>\w+\s+\w+)\s*:\s*\(ms\)\s+\[(?P<var1>\d+)\]-(?P<val1>\d+)\s+\[(?P<var2>\d+)\]-(?P<val2>\d+)\s+\[(?P<var3>\d+)\]-(?P<val3>\d+)\s+\[(?P<var4>\d+)\]-(?P<val4>\d+)\s+\[(?P<var5>\d+)\]-(?P<val5>\d+)$')

        # PADG xmit: 864  rcvd: 0
        # PADC xmit: 127926272  rcvd: 864
        p19 = re.compile(r'^(?P<var1>PAD[GC]\s+[Xx]\w+)\s*:\s*(?P<val1>\d+)\s+(?P<var2>\w+)\s*:\s*(?P<val2>\d+)$')

        # In-band credit pkt xmit: 0 rcvd: 0
        p20 = re.compile(r'^(?P<var1>\w+-\w+\s+\w+\s+\w+\s+\w+)\s*:\s*(?P<val1>\d+)\s+(?P<var2>\w+)\s*:\s*(?P<val2>\d+)$')

        # Last credit packet snapshot
        p21 = re.compile(r'^(?P<var>[Ll]ast.+)$')

        # PADG xmit: seq_num = 884, fcn = 65535, bcn = 0
        # PADC xmit: seq_num = 70, fcn = 1952, bcn = 0
        p22 = re.compile(r'^(?P<var>\w+\s+[Xx]\w+)\s*:\s*(?P<var1>\w+_\w+)\s*=\s*(?P<val1>\d+)\s*,\s*(?P<var2>\w+)\s*=\s*(?P<val2>\d+),\s*(?P<var3>\w+)\s*=\s*(?P<val3>\d+)$')

        # PADC rcvd: seq_num = 884, fcn = 1953, bcn = 65535
        # PADG rcvd: seq_num = 0, fcn = 0, bcn = 72
        p23 = re.compile(r'^(?P<var>\w+\s+[Rr]\w+)\s*:\s*(?P<var1>\w+_\w+)\s*=\s*(?P<val1>\d+)\s*,\s*(?P<var2>\w+)\s*=\s*(?P<val2>\d+),\s*(?P<var3>\w+)\s*=\s*(?P<val3>\d+)$')

        #  In-band credit pkt xmit: fcn = 0, bcn = 0
        #  In-band credit pkt rcvd: fcn = 0, bcn = 0
        p24 = re.compile(r'^(?P<var>[Ii]n-\w+\s+\w+\s+\w+\s+\w+)\s*:\s*(?P<var1>\w+)\s*=\s*(?P<val1>\d+),\s*(?P<var2>\w+)\s*=\s*(?P<val2>\d+)$')

        # ==== PADQ Statistics ====
        p25 = re.compile(r'^(=+\s*(?P<var>\w+\s+\w+)\s*=+)$')

        # PADQ xmit: 0  rcvd: 0
        p26 = re.compile(r'^(?P<var1>PADQ\s+[Xx]\w+)\s*:\s*(?P<val1>\d+)\s+(?P<var2>\w+)\s*:\s*(?P<val2>\d+)$')


        vmi_count = 1
        for lines in out.splitlines():
            line = lines.strip()

            # 1 vmi1 Neighbors
            m = p1.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ", "_")
                ret_dict[var] = int(m.groupdict()['val'])
                continue
            
            # vmi1   IPV6 Address=FE80::6E13:D5FF:FE3F:9710
            m = p2.match(line)
            if m:
                var = m.groupdict()['var'].lower()
                vmi = var + '_' + str(vmi_count)
                vmi_count = vmi_count + 1
                var1 = m.groupdict()['var1'].lower().replace(" ","_")
                ret_dict.setdefault(vmi,{})
                ret_dict[vmi][var1] = val1 = m.groupdict()['val1']
                continue
            
            # IPV6 Global Addr=::
            m = p3.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                ret_dict[vmi][var1] = m.groupdict()['val1']
                continue
            
            # IPV4 Address=81.0.0.1, Uptime=00:01:26
            m = p4.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower()
                ret_dict[vmi][var1] = m.groupdict()['val1']
                ret_dict[vmi][var2] = m.groupdict()['val2']
                continue
            
            # Output pkts=0, Input pkts=0
            m = p5.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                ret_dict[vmi][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][var2] = int(m.groupdict()['val2'])
                continue
            
            # Transport PPPoE, Session ID=2
            m = p6.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                ret_dict[vmi].setdefault(var1,{})
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                ret_dict[vmi][var1][var2] = int(m.groupdict()['val2'])
                continue
            
            # INTERFACE STATS:
            m = p7.match(line)
            if m:
                intf_stat = m.groupdict()['var'].lower().replace(" ", "_")
                ret_dict[vmi].setdefault(intf_stat,{})
                continue
            
            # VMI Interface=vmi1,
            m = p8.match(line)
            if m:
                vmi_intf = m.groupdict()['var1'].lower().replace(" ", "_")
                vmi_num = m.groupdict()['val1'].lower()
                ret_dict[vmi][intf_stat].setdefault(vmi_intf,{})
                ret_dict[vmi][intf_stat][vmi_intf].setdefault(vmi_num,{})
                continue
            
            # V-Access intf=Virtual-Access1.1,
            m = p9.match(line)
            if m:
                vacc_intf = m.groupdict()['var1'].lower().replace(" ", "_").replace("-","_")
                vacc_num = m.groupdict()['val1'].lower().replace("-","_")
                ret_dict[vmi][intf_stat].setdefault(vacc_intf,{})
                ret_dict[vmi][intf_stat][vacc_intf].setdefault(vacc_num,{})
                continue
            
            # Physical intf=GigabitEthernet0/0/4,
            m = p10.match(line)
            if m:
                phy_intf = m.groupdict()['var1'].lower().replace(" ", "_")
                phy_num = m.groupdict()['val1'].lower()
                ret_dict[vmi][intf_stat].setdefault(phy_intf,{})
                ret_dict[vmi][intf_stat][phy_intf].setdefault(phy_num,{})
                continue
            
            # Input qcount=0, drops=0, Output qcount=0, drops=0
            # Input qcount=0, drops=0, Output qcount=0, drops=0
            # Input qcount=0, drops=0, Output qcount=0, drops=0
            m = p11.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                var3 = m.groupdict()['var3'].lower().replace(" ", "_")
                var4 = m.groupdict()['var4'].lower().replace(" ", "_")
                if not ret_dict[vmi][intf_stat][vmi_intf][vmi_num]:
                    ret_dict[vmi][intf_stat][vmi_intf][vmi_num][var1] = int(m.groupdict()['val1'])
                    ret_dict[vmi][intf_stat][vmi_intf][vmi_num]['input_drops'] = int(m.groupdict()['val2'])
                    ret_dict[vmi][intf_stat][vmi_intf][vmi_num][var3] = int(m.groupdict()['val3'])
                    ret_dict[vmi][intf_stat][vmi_intf][vmi_num]['output_drops'] = int(m.groupdict()['val4'])
                    continue
                if not ret_dict[vmi][intf_stat][vacc_intf][vacc_num]:
                    ret_dict[vmi][intf_stat][vacc_intf][vacc_num][var1] = int(m.groupdict()['val1'])
                    ret_dict[vmi][intf_stat][vacc_intf][vacc_num]['input_drops'] = int(m.groupdict()['val2'])
                    ret_dict[vmi][intf_stat][vacc_intf][vacc_num][var3] = int(m.groupdict()['val3'])
                    ret_dict[vmi][intf_stat][vacc_intf][vacc_num]['output_drops'] = int(m.groupdict()['val4'])
                    continue
                if not ret_dict[vmi][intf_stat][phy_intf][phy_num]:
                    ret_dict[vmi][intf_stat][phy_intf][phy_num][var1] = int(m.groupdict()['val1'])
                    ret_dict[vmi][intf_stat][phy_intf][phy_num]['input_drops'] = int(m.groupdict()['val2'])
                    ret_dict[vmi][intf_stat][phy_intf][phy_num][var3] = int(m.groupdict()['val3'])
                    ret_dict[vmi][intf_stat][phy_intf][phy_num]['output_drops'] = int(m.groupdict()['val4'])
                    continue
            
            # PPPoE Flow Control Stats
            m = p12.match(line)
            if m:
                flow_stat = m.groupdict()['var'].lower().replace(" ", "_")
                ret_dict[vmi].setdefault(flow_stat,{})
                continue
            
            # Local Credits: 1953   Peer Credits: 65535   Local Scaling Value 65534 bytes
            m = p13.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                var3 = m.groupdict()['var3'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][var2] = int(m.groupdict()['val2'])
                ret_dict[vmi][flow_stat][var3] = m.groupdict()['val3']
                continue
            
            # Credit Grant Threshold: 28000    Max Credits per grant: 65535
            m = p14.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][var2] = int(m.groupdict()['val2'])
                continue
            
            # Credit Starved Packets: 0
            m = p15.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][var1] = int(m.groupdict()['val1'])
                continue
            
            # PADG xmit Seq Num: 884     PADG Timer index: 148
            m = p16.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][var2] = int(m.groupdict()['val2'])
                continue
            
            #  PADG last rcvd Seq Num: 0
            #  PADG last nonzero Seq Num: 148
            #  PADG last nonzero rcvd amount: 0
            m = p17.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][var1] = int(m.groupdict()['val1'])
                continue
            
            # PADG Timers: (ms)   [0]-1000    [1]-2000    [2]-3000    [3]-4000    [4]-5000
            m = p18.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ", "_")
                padg_tim = var + '_in_milliseconds'
                ret_dict[vmi][flow_stat].setdefault(padg_tim,{}) 
                var1 = m.groupdict()['var1']
                var2 = m.groupdict()['var2']
                var3 = m.groupdict()['var3']
                var4 = m.groupdict()['var4']
                var5 = m.groupdict()['var5']
                ret_dict[vmi][flow_stat][padg_tim][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][padg_tim][var2] = int(m.groupdict()['val2'])
                ret_dict[vmi][flow_stat][padg_tim][var3] = int(m.groupdict()['val3'])
                ret_dict[vmi][flow_stat][padg_tim][var4] = int(m.groupdict()['val4'])
                ret_dict[vmi][flow_stat][padg_tim][var5] = int(m.groupdict()['val5'])
                continue
            
            # PADG xmit: 864  rcvd: 0
            # PADC xmit: 127926272  rcvd: 864
            m = p19.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = var1.split('_')[0] + '_' +m.groupdict()['var2'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][var2] = int(m.groupdict()['val2'])
                continue
            
            # In-band credit pkt xmit: 0 rcvd: 0
            m = p20.match(line)
            if m:
                var_1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var1 = var_1.replace("-", "_")
                var2 = (var_1.split('_')[0] + '_' + m.groupdict()['var2'].lower()).replace("-","_")
                ret_dict[vmi][flow_stat][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][var2] = int(m.groupdict()['val2'])
                continue
            
            # Last credit packet snapshot
            m = p21.match(line)
            if m:
                last_cred = m.groupdict()['var'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat].setdefault(last_cred,{})
                continue
            
            # PADG xmit: seq_num = 884, fcn = 65535, bcn = 0
            # PADC xmit: seq_num = 70, fcn = 1952, bcn = 0
            m = p22.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][last_cred].setdefault(var,{})
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                var3 = m.groupdict()['var3'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][last_cred][var][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][last_cred][var][var2] = int(m.groupdict()['val2'])
                ret_dict[vmi][flow_stat][last_cred][var][var3] = int(m.groupdict()['val3'])
                continue
            
            # PADC rcvd: seq_num = 884, fcn = 1953, bcn = 65535
            # PADG rcvd: seq_num = 0, fcn = 0, bcn = 72
            m = p23.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][last_cred].setdefault(var,{})
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                var3 = m.groupdict()['var3'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][last_cred][var][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][last_cred][var][var2] = int(m.groupdict()['val2'])
                ret_dict[vmi][flow_stat][last_cred][var][var3] = int(m.groupdict()['val3'])             
                continue
            
            #  In-band credit pkt xmit: fcn = 0, bcn = 0
            #  In-band credit pkt rcvd: fcn = 0, bcn = 0
            m = p24.match(line)
            if m:
                var = m.groupdict()['var'].lower().replace(" ", "_").replace("-", "_")
                ret_dict[vmi][flow_stat][last_cred].setdefault(var,{})
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][last_cred][var][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][last_cred][var][var2] = int(m.groupdict()['val2'])
                continue
            
            # ==== PADQ Statistics ====
            m = p25.match(line)
            if m:
                padq_stat = m.groupdict()['var'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][last_cred].setdefault(padq_stat,{})
                continue
            
            # PADQ xmit: 0  rcvd: 0
            m = p26.match(line)
            if m:
                var1 = m.groupdict()['var1'].lower().replace(" ", "_")
                var2 = m.groupdict()['var2'].lower().replace(" ", "_")
                ret_dict[vmi][flow_stat][last_cred][padq_stat][var1] = int(m.groupdict()['val1'])
                ret_dict[vmi][flow_stat][last_cred][padq_stat][var2] = int(m.groupdict()['val2'])
                continue
        
        return ret_dict
