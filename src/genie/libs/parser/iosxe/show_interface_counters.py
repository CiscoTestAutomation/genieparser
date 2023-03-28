import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================
# Schema for:
#  * 'show interface <intf> counters'
#  * 'show interface <intf> counters | begin <field>'
# =================
class ShowInterfaceCountersSchema(MetaParser):
    """Schema for show interface <intf> counters."""

    schema = {
        "port": {
            Any(): {
                Optional("inoctets"): int,
                Optional("inucastpkts"): int,
                Optional("inmcastpkts"): int,
                Optional("inbcastpkts"): int,
                Optional("outoctets"): int,
                Optional("outucastpkts"): int,
                Optional("outmcastpkts"): int,
                Optional("outbcastpkts"): int,
            }
        }
    }


# =================
# Parser for:
#  * 'show interface <intf> counters'
#  * 'show interface <intf> counters | begin <field>'
# =================
class ShowInterfaceCounters(ShowInterfaceCountersSchema):

    """Parser for show interface <intf> counters
       Parser for show interface <intf> counters | begin <field>  
    """

    cli_command = ['show interface {intf} counters','show interface {intf} counters | begin {field}']

    def cli(self, intf="",field=None,output=None):
        if output is None:
            if field is None:
                output = self.device.execute(self.cli_command[0].format(intf=intf))
            else:
                output= self.device.execute(self.cli_command[1].format(intf=intf,field=field))
        else:
            output=output
        
        if not output:
            return {}
        '''
        Sw3# show interface po60 counters
        Port        InOctets    InUcastPkts    InMcastPkts    InBcastPkts
        Po60        1066             12              14              0
        
        Port       OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts
        Po60        39019226         539205              0              0        
        
        Sw3# show interface po60 counters | begin outUcastPkts
        Port        InOctets    InUcastPkts    InMcastPkts    InBcastPkts
        Po60        1066             12              14              0
        
        '''
            
        ###Po60        39019226         539205              0              0
        m1 = re.compile(r"[a-zA-Z]+[0-9]+")
            
        key=[]
        value=[]
        res_dict={}
        for line in output.splitlines():
            line=line.strip()
            if line:
                if m1.match(line):
                    value.append(line) ##Po60        39019226         539205              0              0
                else:
                    key.append(line) ###Port       OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts
        
        ##Gets the port from key, Eg;{port:{}}
        main_key=key[0].split()[0].lower()
        ##Gets the portname for port  Eg;{port:{po60:{}}} 
        port=value[0].split()[0].lower()
        
        res_dict[main_key]={}
        res_dict[main_key][port]={}
        
        for i,j in zip(key,value):
            r=i.split()[1:] ###OutOctets   OutUcastPkts   OutMcastPkts   OutBcastPkts
            l=j.split()[1:] ###39019226         539205              0              0
            for p,k in zip(r,l):
                res_dict[main_key][port][p.lower()]=int(k.lower())
        return res_dict                

# ==============================================================================
# Schema for show interfaces counters errors
# ==============================================================================
class ShowInterfacesCountersErrorsSchema(MetaParser):
    """Schema for show interfaces counters errors"""

    schema = {
        "ports": {
            Any(): {
                "align_err": int,
                "fcs_err": int,
                "xmit_err": int,
                "rcv_err": int,
                "under_size": int,
                "out_discards": int,
                "single_col": int,
                "multi_col": int,
                "late_col": int,
                "excess_col": int,
                "carri_sen": int,
                "runts": int,

            }
        }
    }

class ShowInterfacesCountersErrors(ShowInterfacesCountersErrorsSchema):

    """Parser for show interfaces counters errors"""

    cli_command = ['show interfaces counters errors']

    def cli(self, output=None):
        cmd = self.cli_command[0]
        if output is None:
            output = self.device.execute(self.cli_command[0])
        
        ret_dict = {}

        # Ap2/0/1                0           0           0           0          0            0             m = p1.match(line)
        p1 = re.compile(r'^(?P<port_name>\S+) +(?P<align_err>\d+) +(?P<fcs_err>\d+) +(?P<xmit_err>\d+) +(?P<rcv_err>\d+) +(?P<under_size>\d+) +(?P<out_discards>\d+)$')
        # Port         Single-Col  Multi-Col   Late-Col  Excess-Col  Carri-Sen      Runts 
        p2 = re.compile(r'^Port +Single-Col +Multi-Col +Late-Col +Excess-Col +Carri-Sen +Runts$')
        # Ap2/0/1                0           0           0           0          0            0             m = p1.match(line)
        p3 = re.compile(r'^(?P<port_name>\S+) +(?P<single_col>\d+) +(?P<multi_col>\d+) +(?P<late_col>\d+) +(?P<excess_col>\d+) +(?P<carri_sen>\d+) +(?P<runts>\d+)$')
        extra_counters = False

        for line in output.splitlines():
            line = line.strip()
            
            # Ap2/0/1                0           0           0           0          0            0             m = p1.match(line)
            m = p1.match(line)
            if m and not extra_counters:
                group = m.groupdict()
                ports = ret_dict.setdefault('ports',{}).setdefault(group['port_name'],{})
                ports['align_err'] = int(group['align_err'])
                ports['fcs_err'] = int(group['fcs_err'])
                ports['xmit_err'] = int(group['xmit_err'])
                ports['rcv_err'] = int(group['rcv_err'])
                ports['under_size'] = int(group['under_size'])
                ports['out_discards'] = int(group['out_discards'])
                continue
            # Port         Single-Col  Multi-Col   Late-Col  Excess-Col  Carri-Sen      Runts 
            m = p2.match(line)
            if m:
                extra_counters = True
                continue
            # Ap2/0/1                0           0           0           0          0            0             m = p1.match(line)
            m = p3.match(line)
            if m and extra_counters:
                group = m.groupdict()
                ret_dict['ports'][group['port_name']]['single_col'] = int(group['single_col'])
                ret_dict['ports'][group['port_name']]['multi_col'] = int(group['multi_col'])
                ret_dict['ports'][group['port_name']]['late_col'] = int(group['late_col'])
                ret_dict['ports'][group['port_name']]['excess_col'] = int(group['excess_col'])
                ret_dict['ports'][group['port_name']]['carri_sen'] = int(group['carri_sen'])
                ret_dict['ports'][group['port_name']]['runts'] = int(group['runts'])
                continue

        return ret_dict