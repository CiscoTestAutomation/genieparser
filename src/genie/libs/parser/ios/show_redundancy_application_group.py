# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowRedundancyApplicationGroupSchema(MetaParser):
    ''' Schema for show redundancy application group {group_id}
    show redundancy application group all'''

    schema = {
            Optional("fault_state_group_id"):
            {
                Any():
                {
                    Optional("runtime_priority"):
                    {
                        Any():
                        {
                            Optional("rg_faults_rg_state"):
                            {
                                Any():
                                {
                                    Optional("total_switchovers_due_to_faults"): str,
                                    Optional("total_down_or_up_state_changes_due_to_faults"): str
                                },
                            }
                        },
                    }    
                },
            },
            "group_id": {
                Any():
                {
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
                },
            },
            Optional("rg_protocol_for_rg"):
            {
                Any():
                {
                    Optional("role"): str,
                    Optional("negotiation"): str,
                    Optional("priority"): str,
                    Optional("protocol_state"): str,
                    Optional("ctrl_intf_state"): str,
                    Optional("active_peer_address"): str,
                    Optional("active_peer_priority"): str,
                    Optional("active_peer_intf"): str,
                    Optional("standby_peer"): str,
                    Optional("log_counters"):{
                        Any():
                        {
                            Optional("role_change_to_active"): str,
                            Optional('role_change_to_standby'): str,
                            Optional('disable_events'): str,
                            Optional('ctrl_intf_events'): str,
                            Optional('reload_events'): str
                        },
                    }
                },
            },
            Optional("rg_media_context_for_rg"):
            {
                Any():
                {
                    Optional("ctx_state"): str,
                    Optional("protocol_id"): str,
                    Optional("media_type"): str,
                    Optional("control_interface"): str,
                    Optional("current_hello_timer"): str,
                    Optional("configured_hello_timer"): str,
                    Optional("hold_timer"): str,
                    Optional("peer_hello_timer"): str,
                    Optional("peer_hold_timer"): str,
                    Optional("stats"):
                    {
                        Any():
                        {
                           Optional("pkts"): str,
                           Optional("bytes"): str,
                           Optional("ha_seq"): str,
                           Optional("seq_number"): str,
                           Optional("pkt_loss"): str,
                           Optional("authentication_status"): str,
                           Optional("authentication_failure"): str,
                           Optional("reload_peer"): str,
                           Optional("resign"): str,
                        },
                    },
                    Optional("active_peer_status"): str,
                    Optional("active_peer_hold_timer"): str,
                    Optional("active_peer_stats"):
                    {
                        Any():
                        {
                           Optional("pkts"): str,
                           Optional("bytes"): str,
                           Optional("ha_seq"): str,
                           Optional("seq_number"): str,
                           Optional("pkt_loss"): str, 
                        },
                    }      
                },
            }
        } 

        


class ShowRedundancyApplicationGroup(ShowRedundancyApplicationGroupSchema):

    """ Parser for show redundancy application group {group_id}
                    show redundancy application group all """ 
    
    cli_command = ['show redundancy application group {group_id}','show redundancy application group all'] 

    def cli(self,group_id='',output=None):
        if output is None:
            if group_id=="all":
                out = self.device.execute(self.cli_command[1])
            else:
                out = self.device.execute(self.cli_command[0].format(group_id=group_id))
                
        else:
            out = output
        print(out)
        #Faults states Group 1 info:
        p1=re.compile(r'Faults+\s+states+\s+Group+\s+(?P<fault_group_id>\w+)+\s+info+\:')

        #Runtime priority: [200]
        p2=re.compile(r'\s*Runtime+\s+priority+\:+\s+\[+(?P<runtime_priority>\d+)+\]')

        #RG Faults RG State: Up
        p3=re.compile(r'\s*RG+\s+Faults+\s+RG+\s+State+\:+\s+(?P<rg_fault_State>\w+)')

        #Total # of switchovers due to faults:           0
        p4=re.compile(r'\s*Total+\s+\#+\s+of+\s+switchovers+\s+due+\s+to+\s+faults+\:+\s+(?P<total_switchover_due_to_faults>\d+)')

        #Total # of down/up state changes due to faults: 0
        p5=re.compile(r'\s*Total+\s+\#+\s+of+\s+down+\/+up+\s+state+\s+changes+\s+due+\s+to+\s+faults+\:+\s+(?P<total_down_or_up_due_to_faults>\d+)')

        #Group ID:1
        p6=re.compile(r'Group+\s+ID+\:+(?P<group_id>[\w\d]+)')

        #Group Name:group1
        p7=re.compile(r'Group+\s+Name+\:+(?P<group_name>[\w\d]+)')

        #Administrative State: No Shutdown
        p8=re.compile(r'Administrative+\s+State+\:+\s+(?P<administrative_state>[\w\s\d]+)')

        #Aggregate operational state : Up
        p9=re.compile(r'Aggregate+\s+operational+\s+state+\s+\:+\s+(?P<aggr_oper_state>\w+)')

        #My Role: ACTIVE
        p10=re.compile(r'My+\s+Role+\:+\s+(?P<my_role>\w+)')

        #Peer Role: STANDBY
        p11=re.compile(r'Peer+\s+Role+\:+\s+(?P<peer_role>\w+)')

        #Peer Presence: Yes
        p12=re.compile(r'Peer+\s+Presence+\:+\s+(?P<peer_presence>\w+)')

        #Peer Comm: Yes
        p13=re.compile(r'Peer+\s+Comm+\:+\s+(?P<peer_comm>\w+)')

        #Peer Progression Started: Yes
        p14=re.compile(r'Peer+\s+Progression+\s+Started+\:+\s+(?P<peer_progress>\w+)')

        #RF Domain: btob-one
        p15=re.compile(r'RF+\s+Domain+\:+\s+(?P<rf_domain>[\w\W]+)')

        #RF state: ACTIVE
        p16=re.compile(r'\s*RF+\s+state+\:+\s+(?P<rf_state>[\w\W]+)')

        #Peer RF state: STANDBY HOT
        p17=re.compile(r'\s*Peer+\s+RF+\s+state+\:+\s+(?P<peer_rf_state>[\w\W]+)')

        #RG Protocol RG 1
        p18=re.compile(r'RG+\s+Protocol+\s+RG+\s+(?P<rg_protocol_id>\w+)')

        #Role: Standby
        p19=re.compile(r'\s*Role+\:+\s+(?P<role>[\w\W]+)')

        #Negotiation: Enabled
        p20=re.compile(r'\s*Negotiation+\:+\s+(?P<negotiation>[\w\W]+)')

        #Priority: 200
        p21=re.compile(r'\s*Priority+\:+\s+(?P<priority>\d+)')

        #Protocol state: Standby-hot
        p22=re.compile(r'\s*Protocol+\s+state+\:+\s+(?P<protocol_state>[\w\W]+)')

        #Ctrl Intf(s) state: Up
        p23=re.compile(r'\s*Ctrl+\s+Intf+\(+s+\)+\s+state+\:+\s+(?P<ctrl_intf_state>[\w\W]+)')

        #Active Peer: address 9.1.1.1, priority 200, intf Po10.100
        p24=re.compile(r'\s*Active+\s+Peer+\:+\s+address+\s+(?P<active_peer_addr>[\w\.]+)+\,+\s+priority+\s+(?P<active_peer_priority>\d+)+\,+\s+intf+\s+(?P<active_peer_intf>[\w\W]+)')

        #Standby Peer: Local
        p25=re.compile(r'\s*Standby+\s+Peer+\:+\s+(?P<standby_peer>[\w\W]+)')
        
        #Log counters:
        p26=re.compile(r'\s*Log+\s+counters+\:')

        #role change to active: 0
        p27=re.compile(r'\s*role+\s+change+\s+to+\s+active+\:+\s+(?P<role_change_to_active>\d+)')

        #role change to standby: 1
        p28=re.compile(r'\s*role+\s+change+\s+to+\s+standby+\:+\s+(?P<role_change_to_standby>\d+)')

        #disable events: rg down state 0, rg shut 0
        p29=re.compile(r'\s*disable+\s+events+\:+\s+(?P<disable_events>[\w\W]+)')

        #ctrl intf events: up 1, down 1, admin_down 0
        p30=re.compile(r'\s*ctrl+\s+intf+\s+events+\:+\s+(?P<ctrl_intf_events>[\w\W]+)')

        #reload events: local request 0, peer request 0
        p31=re.compile(r'\s*reload+\s+events+\:+\s+(?P<reload_events>[\w\W]+)')

        #RG Media Context for RG 1
        p32=re.compile(r'RG+\s+Media+\s+Context+\s+for+\s+RG+\s+(?P<rg_media_id>\d+)')

        #Ctx State: Standby
        p33=re.compile(r'\s*Ctx+\s+State+\:+\s+(?P<ctx_state>[\w\W]+)')

        #Protocol ID: 1
        p34=re.compile(r'\s*Protocol+\s+ID+\:+\s+(?P<protocol_id>[\w\W]+)')

        #Media type: Default
        p35=re.compile(r'\s*Media+\s+type+\:+\s+(?P<media_type>[\w\W]+)')

        #Control Interface: Port-channel10.100
        p36=re.compile(r'\s*Control+\s+Interface+\:+\s+(?P<control_interface>[\w\W]+)')

        #Current Hello timer: 3000
        p37=re.compile(r'\s*Current+\s+Hello+\s+timer+\:+\s+(?P<current_hello_timer>\d+)')

        #Configured Hello timer: 3000, Hold timer: 9000
        p38=re.compile(r'\s*Configured+\s+Hello+\s+timer+\:+\s+(?P<conf_hello_timer>\d+)+\,+\s+Hold+\s+timer+\:+\s+(?P<hold_timer>\d+)')

        #Peer Hello timer: 3000, Peer Hold timer: 9000
        p39=re.compile(r'\s*Peer+\s+Hello+\s+timer+\:+\s+(?P<peer_hello_timer>\d+)+\,+\s+Peer+\s+Hold+\s+timer+\:+\s+(?P<peer_hold_timer>\d+)')

        #Stats:
        p40=re.compile(r'\s*Stats+\:')

        #Pkts 144780, Bytes 8976360, HA Seq 0, Seq Number 144780, Pkt Loss 0
        p41=re.compile(r'\s*Pkts+\s+(?P<pkts>\d+)+\,+\s+Bytes+\s+(?P<bytes>\d+)+\,+\s+HA+\s+Seq+\s+(?P<ha_seq>\d+)+\,+\s+Seq+\s+Number+\s+(?P<seq_number>\d+)+\,+\s+Pkt+\s+Loss+\s+(?P<pkt_loss>\d+)')

        #Authentication not configured
        p42=re.compile(r'\s*Authentication+\s+(?P<auth_status>[configured|not configured]+)')

        #Authentication Failure: 0
        p43=re.compile(r'\s*Authentication+\s+Failure+\:+\s+(?P<auth_failure>[\w\W]+)')

        #Reload Peer: TX 0, RX 0
        p44=re.compile(r'\s*Reload+\s+Peer+\:+\s+(?P<reload_peer>[\w\W]+)')

        #Resign: TX 0, RX 0
        p45=re.compile(r'\s*Resign+\:+\s+(?P<resign>[\w\W]+)')

        #Active Peer: Present. Hold Timer: 9000
        p46=re.compile(r'\s*Active+\s+Peer+\:+\s+(?P<active_peer>\w+)+\.+\s+Hold+\s+Timer+\:+\s+(?P<active_peer_hold_timer>\d+)')

        parsed_dict={}
        fault_state_check=1
        run_time_check=1
        rg_fault_check=1
        group_id_check=1
        rf_domain_check=1
        rg_protocol_check=1
        log_counter_check=1
        log_index=1
        rg_media_check=1
        stats_check=1
        stats_index=1
        active_peer_check=1
        active_peer_enabled=0
        active_peer_index=1

        for line in out.splitlines():
            #Faults states Group 1 info
            m1= p1.match(line)
            if m1:
                #{'fault_group_id':'1'}
                if fault_state_check==1:
                    parsed_dict['fault_state_group_id']= {}
                    cur_dict1= parsed_dict['fault_state_group_id']
                    fault_state_check=0
                groups=m1.groupdict()
                cur_dict1[groups['fault_group_id']]={}
                cur_dict2= cur_dict1[groups['fault_group_id']]
                run_time_check=1
                rg_fault_check=1

            #Runtime priority: [200]
            m2= p2.match(line)
            if m2:
                #{'runtime_priority':'200'}
                if run_time_check==1:
                    cur_dict2['runtime_priority']= {}
                    cur_dict3= cur_dict2['runtime_priority']
                    run_time_check=0
                groups=m2.groupdict()
                cur_dict3[groups['runtime_priority']]={}
                cur_dict4= cur_dict3[groups['runtime_priority']]

            #RG Faults RG State: Up
            m3= p3.match(line)
            if m3:
                #{'rg_fault_State':'Up'}
                if rg_fault_check==1:
                    cur_dict4['rg_faults_rg_state']= {}
                    cur_dict5= cur_dict4['rg_faults_rg_state']
                    rg_fault_check=0
                groups=m3.groupdict()
                cur_dict5[groups['rg_fault_State']]={}
                cur_dict6= cur_dict5[groups['rg_fault_State']]

            #Total # of switchovers due to faults:           0
            m4= p4.match(line)
            if m4:
                #{'total_switchover_due_to_faults':'0'}
                groups=m4.groupdict()
                cur_dict6['total_switchovers_due_to_faults']=groups['total_switchover_due_to_faults']

            #Total # of down/up state changes due to faults: 0
            m5= p5.match(line)
            if m5:
                #{'total_down_or_up_due_to_faults':'0'}
                groups=m5.groupdict()
                cur_dict6['total_down_or_up_state_changes_due_to_faults']=groups['total_down_or_up_due_to_faults']

            #Group ID:1
            m6= p6.match(line)
            if m6:
                #{'group_id':'1'}
                if group_id_check==1:
                    parsed_dict['group_id']= {}
                    cur_dict7= parsed_dict['group_id']
                    group_id_check=0
                groups=m6.groupdict()
                cur_dict7[groups['group_id']]={}
                cur_dict8= cur_dict7[groups['group_id']]
                rf_domain_check=1

            #Group Name:group1
            m7= p7.match(line)
            if m7:
                #{'group_name':'group1'}
                groups=m7.groupdict()
                cur_dict8['group_name']=groups['group_name']

            #Administrative State: No Shutdown
            m8= p8.match(line)
            if m8:
                #{'administrative_state':'No Shutdown'}
                groups=m8.groupdict()
                cur_dict8['administrative_state']= groups['administrative_state']

            #Aggregate operational state : Up
            m9= p9.match(line)
            if m9:
                #{'aggr_oper_state':'Up'}
                groups=m9.groupdict()
                cur_dict8['aggregate_oper_state']=groups['aggr_oper_state']

            #My Role: ACTIVE
            m10= p10.match(line)
            if m10:
                #{'my_role':'ACTIVE'}
                groups=m10.groupdict()
                cur_dict8['my_role']= groups['my_role']

            #Peer Role: STANDBY
            m11= p11.match(line)
            if m11:
                #{'peer_role':'STANDBY'}
                groups= m11.groupdict()
                cur_dict8['peer_role']= groups['peer_role']

            #Peer Presence: Yes
            m12=p12.match(line)
            if m12:
                #{'peer_presence':'Yes'}
                groups=m12.groupdict()
                cur_dict8['peer_presence']= groups['peer_presence']

            #Peer Comm: Yes
            m13=p13.match(line)
            if m13:
                #{'peer_comm':'Yes'}
                groups=m13.groupdict()
                cur_dict8['peer_comm']= groups['peer_comm']

            #Peer Progression Started: Yes
            m14=p14.match(line)
            if m14:
                #{'peer_progress':'Yes'}
                groups=m14.groupdict()
                cur_dict8['peer_progression_started']= groups['peer_progress']
                
            #RF Domain: btob-one
            m15=p15.match(line)
            if m15:
                #{'rf_domain':'btob-one'}
                if rf_domain_check==1:
                    cur_dict8['rf_domain']={}
                    cur_dict9= cur_dict8['rf_domain']
                    rf_domain_check=0
                groups=m15.groupdict()
                cur_dict9[groups['rf_domain']]={}
                cur_dict10= cur_dict9[groups['rf_domain']]

            #RF state: ACTIVE
            m16=p16.match(line)
            if m16:
                #{'rf_state':'ACTIVE'}
                groups=m16.groupdict()
                cur_dict10['rf_state']= groups['rf_state']

            #Peer RF state: STANDBY HOT
            m17=p17.match(line)
            if m17:
                #{'peer_rf_state':'STANDBY HOT'}
                groups=m17.groupdict()
                cur_dict10['peer_rf_state']= groups['peer_rf_state']
            
            #RG Protocol RG 1
            m18= p18.match(line)
            if m18:
                #{'rg_protocol_id':'1'}
                if rg_protocol_check==1:
                    parsed_dict['rg_protocol_for_rg']= {}
                    cur_dict11= parsed_dict['rg_protocol_for_rg']
                    rg_protocol_check=0
                groups=m18.groupdict()
                cur_dict11[groups['rg_protocol_id']]={}
                cur_dict12= cur_dict11[groups['rg_protocol_id']]
                log_counter_check=1
                log_index=1

            #Role: Standby
            m19=p19.match(line)
            if m19:
                #{'role':'Standby'}
                groups=m19.groupdict()
                cur_dict12['role']= groups['role']
            
            #Negotiation: Enabled
            m20=p20.match(line)
            if m20:
                #{'negotiation':'Enabled'}
                groups=m20.groupdict()
                cur_dict12['negotiation']= groups['negotiation']
            
            #Priority: 200
            m21=p21.match(line)
            if m21:
                #{'priority':'200'}
                groups=m21.groupdict()
                cur_dict12['priority']= groups['priority']
            
            #Protocol state: Standby-hot
            m22=p22.match(line)
            if m22:
                #{'protocol_state':'Standby-hot'}
                groups=m22.groupdict()
                cur_dict12['protocol_state']= groups['protocol_state']
            
            #Ctrl Intf(s) state: Up
            m23=p23.match(line)
            if m23:
                #{'ctrl_intf_state':'Up'}
                groups=m23.groupdict()
                cur_dict12['ctrl_intf_state']= groups['ctrl_intf_state']
            
            #Active Peer: address 9.1.1.1, priority 200, intf Po10.100
            m24=p24.match(line)
            if m24:
                #{'active_peer_addr':'9.1.1.1','active_peer_priority':'200','active_peer_intf':'Po10.100'}
                groups=m24.groupdict()
                cur_dict12['active_peer_address']= groups['active_peer_addr']
                cur_dict12['active_peer_priority']= groups['active_peer_priority']
                cur_dict12['active_peer_intf']= groups['active_peer_intf']
            
            #Standby Peer: Local
            m25=p25.match(line)
            if m25:
                #{'standby_peer':'Local'}
                groups=m25.groupdict()
                cur_dict12['standby_peer']= groups['standby_peer']
            ######################################################################
            
            ##Log counters:
            m26=p26.match(line)
            if m26:
                if log_counter_check==1:
                    cur_dict12['log_counters']= {}
                    cur_dict13= cur_dict12['log_counters']
                    log_counter_check=0
                cur_dict13[str(log_index)]= {}
                cur_dict14= cur_dict13[str(log_index)]
                log_index+=1
            
            #role change to active: 0
            m27=p27.match(line)
            if m27:
                #{'role_change_to_active':'0'}
                groups=m27.groupdict()
                cur_dict14['role_change_to_active']= groups['role_change_to_active']
            
            #role change to standby: 1
            m28=p28.match(line)
            if m28:
                #{'role_change_to_standby':'1}
                groups=m28.groupdict()
                cur_dict14['role_change_to_standby']= groups['role_change_to_standby']
            
            #disable events: rg down state 0, rg shut 0
            m29=p29.match(line)
            if m29:
                #{'disable_events':'rg down state 0, rg shut 0'}
                groups=m29.groupdict()
                cur_dict14['disable_events']= groups['disable_events']

            #ctrl intf events: up 1, down 1, admin_down 0
            m30=p30.match(line)
            if m30:
                #{'ctrl_intf_events':'STANDBY HOT'}
                groups=m30.groupdict()
                cur_dict14['ctrl_intf_events']= groups['ctrl_intf_events']

            #reload events: local request 0, peer request 0
            m31=p31.match(line)
            if m31:
                #{'reload_events':'local request 0, peer request 0'}
                groups=m31.groupdict()
                cur_dict14['reload_events']= groups['reload_events']

            ###########################################################

            #RG Media Context for RG 1
            m32=p32.match(line)
            if m32:
                if rg_media_check==1:
                    parsed_dict['rg_media_context_for_rg']= {}
                    cur_dict15= parsed_dict['rg_media_context_for_rg']
                    rg_media_check=0
                #{'rg_media_id':'1'}
                groups=m32.groupdict()
                cur_dict15[groups['rg_media_id']]= {}
                cur_dict16= cur_dict15[groups['rg_media_id']]
                stats_index=1
                stats_check=1
                active_peer_enabled=0
                active_peer_check=1
                active_peer_index=1
            
            #Ctx State: Standby
            m33=p33.match(line)
            if m33:
                #{'ctx_state':'Standby'}
                groups=m33.groupdict()
                cur_dict16['ctx_state']= groups['ctx_state']
            
            #Protocol ID: 1
            m34=p34.match(line)
            if m34:
                #{'protocol_id':'1'}
                groups=m34.groupdict()
                cur_dict16['protocol_id']= groups['protocol_id']
            
            #Media type: Default
            m35=p35.match(line)
            if m35:
                #{'media_type':'Default'}
                groups=m35.groupdict()
                cur_dict16['media_type']= groups['media_type']
            
            #Control Interface: Port-channel10.100
            m36=p36.match(line)
            if m36:
                #{'control_interface':'Port-channel10.100'}
                groups=m36.groupdict()
                cur_dict16['control_interface']= groups['control_interface']
            
            #Current Hello timer: 3000
            m37=p37.match(line)
            if m37:
                #{'current_hello_timer':'3000'}
                groups=m37.groupdict()
                cur_dict16['current_hello_timer']= groups['current_hello_timer']
            
            #Configured Hello timer: 3000, Hold timer: 9000
            m38=p38.match(line)
            if m38:
                #{'conf_hello_timer':'3000','hold_timer':'9000'}
                groups=m38.groupdict()
                cur_dict16['configured_hello_timer']= groups['conf_hello_timer']
                cur_dict16['hold_timer']= groups['hold_timer']

            #Peer Hello timer: 3000, Peer Hold timer: 9000
            m39=p39.match(line)
            if m39:
                #{'peer_hello_timer':'3000','peer_hold_timer':'9000'}
                groups=m39.groupdict()
                cur_dict16['peer_hello_timer']= groups['peer_hello_timer']
                cur_dict16['peer_hold_timer']= groups['peer_hold_timer']
            
            #Stats:
            m40=p40.match(line)
            if m40:
                if stats_check==1:
                    cur_dict16['stats']= {}
                    cur_dict17= cur_dict16['stats']
                    stats_check=0
                
                cur_dict17[str(stats_index)]= {}
                cur_dict18= cur_dict17[str(stats_index)]
                stats_index+=1

            #Pkts 108621, Bytes 6734502, HA Seq 0, Seq Number 108621, Pkt Loss 0
            m41=p41.match(line)
            if m41:
                #{'pkts':'108621','bytes':'6734502','ha_seq':'0','seq_number':'108621','pkt_loss':'0'}
                groups=m41.groupdict()
                if active_peer_enabled==0:
                    cur_dict18['pkts']= groups['pkts']
                    cur_dict18['bytes']= groups['bytes']
                    cur_dict18['ha_seq']= groups['ha_seq']
                    cur_dict18['seq_number']= groups['seq_number']
                    cur_dict18['pkt_loss']= groups['pkt_loss']
                else:
                    cur_dict20['pkts']= groups['pkts']
                    cur_dict20['bytes']= groups['bytes']
                    cur_dict20['ha_seq']= groups['ha_seq']
                    cur_dict20['seq_number']= groups['seq_number']
                    cur_dict20['pkt_loss']= groups['pkt_loss']
            
            #Authentication not configured
            m42=p42.match(line)
            if m42:
                #{'auth_status':'not configured'}
                groups=m42.groupdict()
                cur_dict18['authentication_status']= groups['auth_status']
                
            
            #Authentication Failure: 0
            m43=p43.match(line)
            if m43:
                #{'auth_failure':'0'}
                groups=m43.groupdict()
                cur_dict18['authentication_failure']= groups['auth_failure']
                
            
            #Reload Peer: TX 0, RX 0
            m44=p44.match(line)
            if m44:
                #{'reload_peer':'TX 0, RX 0'}
                groups=m44.groupdict()
                cur_dict18['reload_peer']= groups['reload_peer']
                
            #Resign: TX 0, RX 0
            m45=p45.match(line)
            if m45:
                #{'resign':'TX 0, RX 0'}
                groups=m45.groupdict()
                cur_dict18['resign']= groups['resign']
            
            #Active Peer: Present. Hold Timer: 9000
            m46=p46.match(line)
            if m46:
                #{'active_peer':'Present','active_peer_hold_timer':'9000'}
                groups=m46.groupdict()
                cur_dict16['active_peer_status']= groups['active_peer']
                cur_dict16['active_peer_hold_timer']= groups['active_peer_hold_timer']
                if active_peer_check==1:
                    cur_dict16['active_peer_stats']={}
                    cur_dict19= cur_dict16['active_peer_stats']
                    active_peer_check=0
                    active_peer_enabled=1
                    cur_dict19[str(active_peer_index)]={}
                    cur_dict20=cur_dict19[str(active_peer_index)]
                    active_peer_index+=1
        
        return parsed_dict
