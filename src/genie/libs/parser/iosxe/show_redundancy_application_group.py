# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowRedundancyApplicationGroupSchema(MetaParser):
    ''' Schema for show redundancy application group {group_id}'''
    schema = {
            "group_id": str,
            "group_name": str,
            "administrative_state": str,
            "aggregate_oper_state": str,
            "my_role": str,
            "peer_role": str,
            "peer_presence": str,
            "peer_comm": str,
            "peer_progression_started": str,
            "rf_domain":{
                Any():{
                    "rf_state": str,
                    "peer_rf_state": str
                },
            }         
    }
        


class ShowRedundancyApplicationGroup(ShowRedundancyApplicationGroupSchema):

    """ Parser for "show redundancy application group {group_id}" """
    
    cli_command = "show redundancy application group {group_id}"

    def cli(self,group_id='',output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(group_id=group_id))
        else:
            out = output

        #Group ID:1
        p1=re.compile(r'Group+\s+ID+\:+(?P<group_id>[\w\d]+)')

        #Group Name:group1
        p2=re.compile(r'Group+\s+Name+\:+(?P<group_name>[\w\d]+)')

        #Administrative State: No Shutdown
        p3=re.compile(r'Administrative+\s+State+\:+\s+(?P<administrative_state>[\w\s\d]+)')

        #Aggregate operational state : Up
        p4=re.compile(r'Aggregate+\s+operational+\s+state+\s+\:+\s+(?P<aggr_oper_state>\w+)')

        #My Role: ACTIVE
        p5=re.compile(r'My+\s+Role+\:+\s+(?P<my_role>\w+)')

        #Peer Role: STANDBY
        p6=re.compile(r'Peer+\s+Role+\:+\s+(?P<peer_role>\w+)')

        #Peer Presence: Yes
        p7=re.compile(r'Peer+\s+Presence+\:+\s+(?P<peer_presence>\w+)')

        #Peer Comm: Yes
        p8=re.compile(r'Peer+\s+Comm+\:+\s+(?P<peer_comm>\w+)')

        #Peer Progression Started: Yes
        p9=re.compile(r'Peer+\s+Progression+\s+Started+\:+\s+(?P<peer_progress>\w+)')

        #RF Domain: btob-one
        p10=re.compile(r'RF+\s+Domain+\:+\s+(?P<rf_domain>[\w\W]+)')

        #RF state: ACTIVE
        p11=re.compile(r'\s*RF+\s+state+\:+\s+(?P<rf_state>[\w\W]+)')

        #Peer RF state: STANDBY HOT
        p12=re.compile(r'\s*Peer+\s+RF+\s+state+\:+\s+(?P<peer_rf_state>[\w\W]+)')


        parsed_dict={}

        for line in out.splitlines():
            m1= p1.match(line)
            if m1:
                #{'group_id':'1'}
                groups=m1.groupdict()
                parsed_dict['group_id']=groups['group_id']

            m2= p2.match(line)
            if m2:
                #{'group_name':'group1'}
                groups=m2.groupdict()
                parsed_dict['group_name']=groups['group_name']

            m3= p3.match(line)
            if m3:
                #{'administrative_state':'No Shutdown'}
                groups=m3.groupdict()
                parsed_dict['administrative_state']= groups['administrative_state']

            m4= p4.match(line)
            if m4:
                #{'aggr_oper_state':'Up'}
                groups=m4.groupdict()
                parsed_dict['aggregate_oper_state']=groups['aggr_oper_state']

            m5= p5.match(line)
            if m5:
                #{'my_role':'ACTIVE'}
                groups=m5.groupdict()
                parsed_dict['my_role']= groups['my_role']

            m6= p6.match(line)
            if m6:
                #{'peer_role':'STANDBY'}
                groups= m6.groupdict()
                parsed_dict['peer_role']= groups['peer_role']

            m7=p7.match(line)
            if m7:
                #{'peer_presence':'Yes'}
                groups=m7.groupdict()
                parsed_dict['peer_presence']= groups['peer_presence']

            m8=p8.match(line)
            if m8:
                #{'peer_comm':'Yes'}
                groups=m8.groupdict()
                parsed_dict['peer_comm']= groups['peer_comm']

            m9=p9.match(line)
            if m9:
                #{'peer_progress':'Yes'}
                groups=m9.groupdict()
                parsed_dict['peer_progression_started']= groups['peer_progress']
                parsed_dict['rf_domain']={}
                cur_dict= parsed_dict['rf_domain']

            m10=p10.match(line)
            if m10:
                #{'rf_domain':'Yes'}
                groups=m10.groupdict()
                cur_dict[groups['rf_domain']]={}
                sub_dict= cur_dict[groups['rf_domain']]
        
            m11=p11.match(line)
            if m11:
                #{'rf_state':'ACTIVE'}
                groups=m11.groupdict()
                sub_dict['rf_state']= groups['rf_state']

            m12=p12.match(line)
            if m12:
                #{'peer_rf_state':'STANDBY HOT'}
                groups=m12.groupdict()
                sub_dict['peer_rf_state']= groups['peer_rf_state']
              
        return parsed_dict
