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
