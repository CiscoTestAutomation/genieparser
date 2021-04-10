# Python
import re
import json
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowCryptoSessionSchema(MetaParser):
    ''' Schema for show crypto session detail
        Schema for show crypto session'''
    schema = {
    "interface":{
        Any():
        {
            Optional("uptime"): str,
            Optional("user_name"): str,
            Optional("profile"): str,
            Optional("group"): str,
            Optional("assigned_address"):str,
            "session_status": str,
            "peer":{
                Any():
                {
                    "port":{
                        Any():
                        {
                        Optional("fvrf"): str,
                        Optional("ivrf"): str,
                        Optional("phase1_id"): str,
                        Optional("desc"): str,
                        "ikev1_sa":{
                            Any():
                            {
                                "local": str,
                                "local_port": str,
                                "remote": str,
                                "remote_port": str,
                                "sa_status": str,
                                Optional("capabilities"):str,
                                Optional("lifetime"): str,
                                Optional("conn_id"):str,
                                Optional("session_id"): str
                            },
                        },
                        "ipsec_flow": {
                            Any():
                                {
                                "active_sas": int,
                                "origin": str,
                                Optional("inbound_pkts_decrypted"): int,
                                Optional("inbound_pkts_drop"): int,
                                Optional("inbound_life_kb"): str,
                                Optional("inbound_life_secs"): str,
                                Optional("outbound_pkts_encrypted"): int,
                                Optional("outbound_pkts_drop"): int,
                                Optional("outbound_life_kb"): str,
                                Optional("outbound_life_secs"): str
                                },
                            }
                        },
                    }
                },
            }   
        },
    }
}
                                
class ShowCryptoSessionSuperParser(ShowCryptoSessionSchema):

    """Super Parser for 
        * 'show crypto session'
        * 'show crypto session detail'
    """
    
    cli_command = "show crypto session {detail}"

    def cli(self,detail_arg='',output=None):

        #Interface: Tunnel13
        p1=re.compile(r'Interface+\:+\s+(?P<interface_name>[\w\W]+)')

        #Uptime: 5d23h
        p2=re.compile(r'Uptime+\:+\s+(?P<up_time>\w+)')

        #Username: cisco
        p3=re.compile(r'Username+\:+\s+(?P<user_name>[\w\W]+)')

        #Profile: prof
        p4=re.compile(r'Profile+\:+\s+(?P<profile>[\w\W]+)')

        #Group: easy
        p5=re.compile(r'Group+\:+\s+(?P<group>[\w\W]+)')

        #Assigned address: 10.3.3.4
        p6=re.compile(r'Assigned+\s+address+\:+\s+(?P<assigned_address>[\w\.]+)')

        #Session status: UP-ACTIVE
        p7=re.compile(r'Session status+\:+\s+(?P<session_status>[\w-]+)')

        #Peer: 11.0.1.2 port 500 fvrf: (none) ivrf: (none)
        p8=re.compile(r'Peer+\:+\s+(?P<peer>[\d\.]+)+\s+port+\s+(?P<port>\d+)+\s+fvrf+\:+\s+\(*(?P<fvrf>\w+)+\)*\s+ivrf+\:+\s+\(*(?P<ivrf>\w+)+\)*')
        
        #Peer: 11.0.1.2 port 500
        p9=re.compile(r'Peer+\:+\s+(?P<peer>[\d\.]+)+\s+port+\s+(?P<port>\d+)')
        
        # Phase1_id: 11.0.1.2
        p10=re.compile(r'\s*Phase1+\_+id+\:+\s+(?P<phase_id>[\d\.]+)')

        # Desc: (none)
        p11=re.compile(r'\s*Desc+\:+\s+\(*(?P<desc>[\w\s]+)+\)*')

        # Session ID: 0  
        p12=re.compile(r'\s*Session+\s+ID+\:+\s+(?P<session_id>\d+)')

        #IKEv1 SA: local 11.0.1.1/500 remote 11.0.1.2/500 Active 
        p13=re.compile(r'\s*IKE+(v1)*\s+SA+\:+\s+local+\s+(?P<local>[\d\.]+)+\/+(?P<local_port>\d+)+\s+remote+\s+(?P<remote>[\d\.]+)+\/+(?P<remote_port>\d+)+\s+(?P<conn_status>\w+)')

        #  Capabilities:(none) connid:1025 lifetime:03:04:13
        p14=re.compile(r'\s*Capabilities+\:+\(*(?P<capabilities>\w+)+\)*\s+connid+\:+(?P<conn_id>\d+)+\s+lifetime+\:+(?P<lifetime>[\d\:]+)')

        # IPSEC FLOW: permit 47 host 11.0.1.1 host 11.0.1.2 
        p15=re.compile(r'\s*IPSEC+\s+FLOW+\:+\s+(?P<ipsec_flow>[\w\W]+)')

        #Active SAs: 2, origin: crypto map
        p16=re.compile(r'\s*Active+\s+SAs+\:+\s+(?P<active_sa>\d+)+\,+\s+origin+\:+\s+(?P<origin>[\w\s]+)')

        #Inbound:  #pkts dec'ed 4172534851 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p17=re.compile(r'\s*Inbound+\:+\s+\#+pkts+\s+dec+\'+ed+\s+(?P<inbound_pkts_dec>\d+)+\s+drop+\s+(?P<inbound_drop>\d+)+\s+life+\s+\(+KB+\/+Sec+\)+\s+(?P<inbound_life_kb>[\w\s]+)+\/+(?P<inbound_life_secs>\w+)')

        #Outbound: #pkts enc'ed 4146702954 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p18=re.compile(r'\s*Outbound+\:+\s+\#+pkts+\s+enc+\'+ed+\s+(?P<outbound_pkts_enc>\d+)+\s+drop+\s+(?P<outbound_drop>\d+)+\s+life+\s+\(+KB+\/+Sec+\)+\s+(?P<outbound_life_kb>[\w\s]+)+\/+(?P<outbound_life_secs>\w+)')

        
        parsed_dict={}
        check_flag= 1
        peer_flag= 1
        sa_flag= 1
        flow_flag= 1
        ike_index=1
        session_id= None
        
        for line in output.splitlines():
            if check_flag==1:
                parsed_dict['interface']={}
                cur_dict1=parsed_dict['interface']
                check_flag=0
         
            #Interface: Tunnel0
            m1= p1.match(line)
            if m1:
                #{'interface_name':'Tunnel13'}
                groups=m1.groupdict()
                cur_dict1[groups['interface_name']]={}
                cur_dict2=cur_dict1[groups['interface_name']]
            
            #Uptime: 3d18h
            m2= p2.match(line)
            if m2:
                #{'up_time':'6d00h'}
                groups=m2.groupdict()
                cur_dict2['uptime']=groups['up_time']

            #Username: cisco
            m3=p3.match(line)
            if m3:
                #{'user_name':'cisco'}
                groups=m3.groupdict()
                cur_dict2['user_name']=groups['user_name']
            
            #Profile: prof
            m4=p4.match(line)
            if m4:
                #{'profile':'prof'}
                groups=m4.groupdict()
                cur_dict2['profile']=groups['profile']
            
            #Group: easy
            m5=p5.match(line)
            if m5:
                #{'group':'easy'}
                groups=m5.groupdict()
                cur_dict2['group']=groups['group']
            
            #Assigned address: 10.3.3.4
            m6=p6.match(line)
            if m6:
                #{'assigned_address':'10.3.3.4'}
                groups=m6.groupdict()
                cur_dict2['assigned_address']=groups['assigned_address']

            #Session status: UP-ACTIVE
            m7= p7.match(line)
            if m7:
                #{'session_status':'UP-ACTIVE'}
                groups=m7.groupdict()
                cur_dict2['session_status']=groups['session_status']

            #Peer: 10.1.1.2 port 500
            #Peer: 10.1.1.3 port 500 fvrf: (none) ivrf: (none)
            m8= p8.match(line)
            m9=p9.match(line)
            if m9:
                #{'peer':'11.0.1.2','port':'500','fvrf':'none','ivrf:'none'}
                #{'peer':'11.0.1.2','port':'500'}
                if peer_flag==1:
                    cur_dict2['peer']={}
                    cur_dict3= cur_dict2['peer']
                    peer_flag=0

                groups=m9.groupdict()
                cur_dict3[groups['peer']]={}
                cur_dict4= cur_dict3[groups['peer']]
                cur_dict4['port']={}
                cur_dict5=cur_dict4['port']
                cur_dict5[groups['port']]={}
                cur_dict6= cur_dict5[groups['port']]
                if m8:
                    groups=m8.groupdict()
                    cur_dict6['fvrf']=groups['fvrf']
                    cur_dict6['ivrf']=groups['ivrf'] 

            #Phase1_id: 10.1.1.3
            m10= p10.match(line)
            if m10:
                #{'phase_id':'11.0.1.2'}
                groups=m10.groupdict()
                cur_dict6['phase1_id']=groups['phase_id']

            #Desc: this is my peer at 10.1.1.3:500 Green
            m11= p11.match(line)
            if m11:
                #{'desc':'none'}
                groups=m11.groupdict()
                cur_dict6['desc']=groups['desc']

            #Session ID: 0
            m12= p12.match(line)
            if m12:
                #{'session_id':'0'}
                groups=m12.groupdict()
                session_id= groups['session_id']
            
            #IKE SA: local 10.1.1.4/500 remote 10.1.1.3/500 Active
            m13= p13.match(line)
            if m13:
                #{'local':'11.0.1.1','local_port':'500','remote':'11.0.1.2','remote_port':'500','conn_status':'active'}
                groups=m13.groupdict()
                if sa_flag==1:
                    cur_dict6['ikev1_sa']={}
                    cur_dict7= cur_dict6['ikev1_sa']
                    sa_flag=0

                cur_dict7[str(ike_index)]={}
                cur_dict8=cur_dict7[str(ike_index)]
                ike_index+= 1

                cur_dict8['local'] =groups['local']
                cur_dict8['local_port'] =groups['local_port']
                cur_dict8['remote'] = groups['remote']
                cur_dict8['remote_port']= groups['remote_port']
                cur_dict8['sa_status']= groups['conn_status']
                if session_id is not None:
                    cur_dict8['session_id']= session_id

            #Capabilities:D connid:1042 lifetime:05:50:03
            m14= p14.match(line)
            if m14:
                #{'capabilities':'none','conn_id':'1025','lifetime':'03:04:13'}
                groups=m14.groupdict()
                cur_dict8['conn_id'] = groups['conn_id']
                cur_dict8['capabilities']= groups['capabilities']
                cur_dict8['lifetime']= groups['lifetime']

            #IPSEC FLOW: permit 47 host 11.0.2.2 host 11.0.2.1     
            m15= p15.match(line)
            if m15:
                #{'ipsec_flow': 'permit 47 host 11.0.1.1 host 11.0.1.2'}
                if flow_flag==1:
                    cur_dict6['ipsec_flow']={}
                    cur_dict9= cur_dict6['ipsec_flow']
                    flow_flag=0

                groups= m15.groupdict()
                cur_dict9[groups['ipsec_flow']]={}
                cur_dict10=cur_dict9[groups['ipsec_flow']]

            # Active SAs: 2, origin: crypto map     
            m16= p16.match(line)
            if m16:
                #{'active_sa':2,'origin':'crypto map'}
                groups=m16.groupdict()
                cur_dict10['active_sas']= int(groups['active_sa'])
                cur_dict10['origin']= groups['origin']

            #Inbound:  #pkts dec'ed 449282 drop 0 life (KB/Sec) KB Vol Rekey Disabled/3060
            m17= p17.match(line)
            if m17:
                #{'inbound_pkts_dec':4172535666,'inbound_drop':0,'inbound_life_kb':'KB Vol Rekey Disabled','inbound_life_sec':'2810'}
                groups=m17.groupdict()
                cur_dict10['inbound_pkts_decrypted']=int(groups['inbound_pkts_dec'])
                cur_dict10['inbound_pkts_drop']=int(groups['inbound_drop'])
                cur_dict10['inbound_life_kb']=groups['inbound_life_kb']
                cur_dict10['inbound_life_secs']=groups['inbound_life_secs']

            #Outbound: #pkts enc'ed 772730 drop 0 life (KB/Sec) KB Vol Rekey Disabled/3060
            m18= p18.match(line)
            if m18:
                #{'outbound_pkts_enc':4172635966,'outbound_drop':0,'inbound_life_kb':'KB Vol Rekey Disabled','inbound_life_sec':'2710'}
                groups=m18.groupdict()
                cur_dict10['outbound_pkts_encrypted']=int(groups['outbound_pkts_enc'])
                cur_dict10['outbound_pkts_drop']=int(groups['outbound_drop'])
                cur_dict10['outbound_life_kb']=groups['outbound_life_kb']
                cur_dict10['outbound_life_secs']=groups['outbound_life_secs']
        return parsed_dict

class ShowCryptoSession(ShowCryptoSessionSuperParser,ShowCryptoSessionSchema):
    '''Parser for:
        * 'show crypto session'
    '''

    cli_command = "show crypto session"

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)

class ShowCryptoSessionDetail(ShowCryptoSessionSuperParser,ShowCryptoSessionSchema):
    '''Parser for:
        * 'show crypto session detail'
    '''

    cli_command = "show crypto session detail"

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)
