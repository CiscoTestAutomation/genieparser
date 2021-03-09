# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowCryptoSessionDetailSchema(MetaParser):
    ''' Schema for show crypto session detail'''
    schema = {
    "interface":{
        Any():
        {
            "uptime": str,
            "session_status": str,
            "peer": str,
            "port": str,
            "fvrf": str,
            "ivrf": str,
            "phase1_id": str,
            "desc": str,
            "session_id":{
                Any():
                {
                    "ike_sa_conn_id":{
                        Any():
                        {
                            "local": str,
                            "remote": str,
                            "conn_status": str,
                            "capabilities":str,
                            "lifetime": str
                        },
                    }
                },
            },
            "ipsec_flow": str,
            "active_sa": int,
            "origin": str,
            "inbound_pkts_dec": int,
            "inbound_drop": int,
            "inbound_life_in_kb/sec": str,
            "outbound_pkts_enc": int,
            "outbound_drop": int,
            "outbound_life_in_kb/sec": str
        },
    }
}
                                
class ShowCryptoSessionDetail(ShowCryptoSessionDetailSchema):

    """ Parser for "show crypto session detail" """
    
    cli_command = "show crypto session detail"

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Interface: Tunnel13
        p1=re.compile(r'Interface+\:+\s+(?P<interface_name>\w+)')

        #Uptime: 5d23h
        p2=re.compile(r'Uptime+\:+\s+(?P<up_time>\w+)')

        #Session status: UP-ACTIVE
        p3=re.compile(r'Session status+\:+\s+(?P<session_status>[\w-]+)')

        #Peer: 11.0.1.2 port 500 fvrf: (none) ivrf: (none)
        p4=re.compile(r'Peer+\:+\s+(?P<peer>[\d\.]+)+\s+port+\s+(?P<port>\d+)+\s+fvrf+\:+\s+\(*(?P<fvrf>\w+)+\)*\s+ivrf+\:+\s+\(*(?P<ivrf>\w+)+\)*')

        # Phase1_id: 11.0.1.2
        p5=re.compile(r'\s*Phase1+\_+id+\:+\s+(?P<phase_id>[\d\.]+)')

        # Desc: (none)
        p6=re.compile(r'\s*Desc+\:+\s+\(*(?P<desc>[\w\s]+)+\)*')

        # Session ID: 0  
        p7=re.compile(r'\s*Session+\s+ID+\:+\s+(?P<session_id>\d+)')

        #IKEv1 SA: local 11.0.1.1/500 remote 11.0.1.2/500 Active 
        p8=re.compile(r'\s*IKEv1+\s+SA+\:+\s+local+\s+(?P<local>[\d\.\/]+)+\s+remote+\s+(?P<remote>[\d\.\/]+)+\s+(?P<conn_status>\w+)')

        #    Capabilities:(none) connid:1025 lifetime:03:04:13
        p9=re.compile(r'\s*Capabilities+\:+\(*(?P<capabilities>\w+)+\)*\s+connid+\:+(?P<conn_id>\d+)+\s+lifetime+\:+(?P<lifetime>[\d\:]+)')

        # IPSEC FLOW: permit 47 host 11.0.1.1 host 11.0.1.2 
        p10=re.compile(r'\s*IPSEC+\s+FLOW+\:+\s+(?P<ipsec_flow>[\w\W]+)')

        #Active SAs: 2, origin: crypto map
        p11=re.compile(r'\s*Active+\s+SAs+\:+\s+(?P<active_sa>\d+)+\,+\s+origin+\:+\s+(?P<origin>[\w\s]+)')

        #Inbound:  #pkts dec'ed 4172534851 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p12=re.compile(r'\s*Inbound+\:+\s+\#+pkts+\s+dec+\'+ed+\s+(?P<inbound_pkts_dec>\d+)+\s+drop+\s+(?P<inbound_drop>\d+)+\s+life+\s+\(+KB+\/+Sec+\)+\s+(?P<inbound_life>[\w\s\/]+)')

        #Outbound: #pkts enc'ed 4146702954 drop 0 life (KB/Sec) KB Vol Rekey Disabled/2576
        p13=re.compile(r'\s*Outbound+\:+\s+\#+pkts+\s+enc+\'+ed+\s+(?P<outbound_pkts_enc>\d+)+\s+drop+\s+(?P<outbound_drop>\d+)+\s+life+\s+\(+KB+\/+Sec+\)+\s+(?P<outbound_life>[\w\s\/]+)')

        parsed_dict={}
        check_flag=1
        
        for line in out.splitlines():
            if check_flag==1:
                parsed_dict['interface']={}
                cur_dict1=parsed_dict['interface']
                check_flag=0
         
            m1= p1.match(line)
            if m1:
                #{'interface_name':'Tunnel13'}
                groups=m1.groupdict()
                cur_dict1[groups['interface_name']]={}
                cur_dict2=cur_dict1[groups['interface_name']]

            m2= p2.match(line)
            if m2:
                #{'up_time':'6d00h'}
                groups=m2.groupdict()
                cur_dict2['uptime']=groups['up_time']

            m3= p3.match(line)
            if m3:
                #{'session_status':'UP-ACTIVE'}
                groups=m3.groupdict()
                cur_dict2['session_status']=groups['session_status']

            m4= p4.match(line)
            if m4:
                #{'peer':'11.0.1.2','port':'500','fvrf':'none','ivrf:'none'}
                groups=m4.groupdict()
                cur_dict2['peer']=groups['peer']
                cur_dict2['port']=groups['port']
                cur_dict2['fvrf']=groups['fvrf']
                cur_dict2['ivrf']=groups['ivrf'] 

            m5= p5.match(line)
            if m5:
                #{'phase_id':'11.0.1.2'}
                groups=m5.groupdict()
                cur_dict2['phase1_id']=groups['phase_id']

            m6= p6.match(line)
            if m6:
                #{'desc':'none'}
                groups=m6.groupdict()
                cur_dict2['desc']=groups['desc']
                cur_dict2['session_id']={}
                cur_dict3=cur_dict2['session_id']

            m7= p7.match(line)
            if m7:
                #{'session_id':'0'}
                groups=m7.groupdict()
                if groups['session_id'] not in cur_dict3.keys():
                    cur_dict3[groups['session_id']]={}
                    cur_dict4=cur_dict3[groups['session_id']]
                    cur_dict4['ike_sa_conn_id']={}
                    cur_dict5= cur_dict4['ike_sa_conn_id']
            
            m8= p8.match(line)
            if m8:
                #{'local':'11.0.1.1/500','remote':'11.0.1.2/500','conn_status':'active'}
                groups=m8.groupdict()
                local =groups['local']
                remote = groups['remote']
                conn_status =groups['conn_status']

            m9= p9.match(line)
            if m9:
                #{'capabilities':'none','conn_id':'1025','lifetime':'03:04:13'}
                groups=m9.groupdict()
                cur_dict5[groups['conn_id']] = {}
                cur_dict6 = cur_dict5[groups['conn_id']]
                cur_dict6['local']=local
                cur_dict6['remote']= remote
                cur_dict6['conn_status']= conn_status
                cur_dict6['capabilities']= groups['capabilities']
                cur_dict6['lifetime']= groups['lifetime']
                
            m10= p10.match(line)
            if m10:
                #{'ipsec_flow': 'permit 47 host 11.0.1.1 host 11.0.1.2'}
                groups=m10.groupdict()
                cur_dict2['ipsec_flow']=groups['ipsec_flow']
                    
            m11= p11.match(line)
            if m11:
                #{'active_sa':2,'origin':'crypto map'}
                groups=m11.groupdict()
                cur_dict2['active_sa']= int(groups['active_sa'])
                cur_dict2['origin']= groups['origin']

            m12= p12.match(line)
            if m12:
                #{'inbound_pkts_dec':4172535666,'inbound_drop':0,'inbound_life_in_kb/sec':'KB Vol Rekey Disabled/2810'}
                groups=m12.groupdict()
                cur_dict2['inbound_pkts_dec']=int(groups['inbound_pkts_dec'])
                cur_dict2['inbound_drop']=int(groups['inbound_drop'])
                cur_dict2['inbound_life_in_kb/sec']=groups['inbound_life']

            m13= p13.match(line)
            if m13:
                #{'outbound_pkts_enc':4172635966,'outbound_drop':0,'outbound_life_in_kb/sec':'KB Vol Rekey Disabled/2710'}
                groups=m13.groupdict()
                cur_dict2['outbound_pkts_enc']=int(groups['outbound_pkts_enc'])
                cur_dict2['outbound_drop']=int(groups['outbound_drop'])
                cur_dict2['outbound_life_in_kb/sec']=groups['outbound_life']

        return parsed_dict


