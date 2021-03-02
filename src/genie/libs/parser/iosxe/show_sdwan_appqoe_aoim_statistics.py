'''show_sdwan_appqoe_aoim_statistics.py
IOSXE parser for the following show command
	* show sdwan appqoe aoim-statistics
'''
# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowSdwanAppqoeAoimStatisticsSchema(MetaParser):
    ''' Schema for show sdwan appqoe aoim-statistics'''
    schema = {
        "total_peer_syncs": int,
        "current_peer_syncs_in_progress": int,
        "Needed_peer_resyncs": int,
        "passthrough_connections_dueto_peer_version_mismatch": int,
        "aoim_db_size_in_bytes": int,
        "local_ao_stats":{
            "number_of_aos": int,
            "ao_name":{
                Any():
                {
                    "version" : str,
                    "registered": str
                },
            }
        },
        "peer_stats":{
            "number_of_peers": int,
            "peer_id":{
                Any():{
                    "number_of_peer_aos": int,
                    "ao_name":{
                        Any():
                        {
                            "version" : str,
                            "incompatible": str
                        },
                    }
                },
            }
        }
    }


class ShowSdwanAppqoeAoimStatistics(ShowSdwanAppqoeAoimStatisticsSchema):

    """ Parser for "show sdwan appqoe aoim-statistics" """
    
    cli_command = "show sdwan appqoe aoim-statistics"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Total Number Of Peer Syncs      : 2
        p1=re.compile(r'\s*Total Number Of Peer Syncs+\s+\:+\s+(?P<total_peer_syncs>[\d]+)')

        #Current Number Of Peer Syncs in Progress      : 0
        p2=re.compile(r'\s*Current Number Of Peer Syncs in Progress+\s+\:+\s+(?P<current_peer_syncs>[\d]+)')

        #Number Of Peer Re-Syncs Needed      : 0
        p3=re.compile(r'\s*Number Of Peer Re-Syncs Needed+\s+\:+\s+(?P<peer_resyncs>[\d]+)')

        #Total Passthrough Connections Due to Peer Version Mismatch   : 0
        p4=re.compile(r'\s*Total Passthrough Connections Due to Peer Version Mismatch+\s+\:+\s+(?P<passthrough_connections>[\d]+)')

        #AOIM DB Size (Bytes): 4194304
        p5=re.compile(r'\s*AOIM DB Size +\(+Bytes+\)+\:+\s+(?P<aoim_db_size>\d+)')

        #LOCAL AO Statistics
        p6=re.compile(r'\s*LOCAL AO Statistics')

        #Number Of AOs      : 2
        p7=re.compile(r'\s*Number Of AOs +\s+\:+\s+(?P<ao_number>\d+)')

        #AO             Version   Registered
        #AO             Version   InCompatible
        p8=re.compile(r'\s*AO+\s+Version+\s+\w+')

        #SSL             1.2        N 
        p9=re.compile(r'\s*(?P<ao_name>\w+)+\s+(?P<ao_version>[\d.]+)+\s+(?P<ao_status>\w+)')

        #PEER Statistics
        p10=re.compile(r'\s*PEER Statistics')

        #Number Of Peers      : 2
        p11=re.compile(r'\s*Number Of Peers+\s+\:+\s+(?P<peer_total>\d+)')

        #Peer ID: 10.220.100.214
        p12=re.compile(r'\s*Peer ID:+\s+(?P<peer_id>[\d.]+)')

        #Peer Num AOs      : 2
        p13=re.compile(r'\s*Peer Num AOs+\s+\:+\s+(?P<peer_ao_num>\d+)')

        parsed_dict={}
        check_flag=0

        for line in out.splitlines():
            m1= p1.match(line)
            if m1:
                #{'total_peer_syncs':'2'}
                groups=m1.groupdict()
                parsed_dict['total_peer_syncs']=int(groups['total_peer_syncs'])

            m2= p2.match(line)
            if m2:
                #{'current_peer_syncs':'0'}
                groups=m2.groupdict()
                parsed_dict['current_peer_syncs_in_progress']=int(groups['current_peer_syncs'])

            m3= p3.match(line)
            if m3:
                #{'peer_resyncs':'0'}
                groups=m3.groupdict()
                parsed_dict['Needed_peer_resyncs']=int(groups['peer_resyncs'])

            m4= p4.match(line)
            if m4:
                #{'passthrough_connections':'0'}
                groups=m4.groupdict()
                parsed_dict['passthrough_connections_dueto_peer_version_mismatch']=int(groups['passthrough_connections'])

            m5= p5.match(line)
            if m5:
                #{'aoim_db_size':'4194304'}
                groups=m5.groupdict()
                parsed_dict['aoim_db_size_in_bytes']=int(groups['aoim_db_size'])

            m6= p6.match(line)
            if m6:
                #LOCAL AO Statistics
                parsed_dict['local_ao_stats']={}
                cur_dict=parsed_dict['local_ao_stats']

            m7=p7.match(line)
            if m7:
                #{'ao_number':'2'}
                groups=m7.groupdict()
                cur_dict['number_of_aos']= int(groups['ao_number'])
                cur_dict['ao_name']={}
                cur_dict=cur_dict['ao_name']

            #AO             Version   Registered
            #AO             Version   InCompatible
            m8=p8.match(line)

            #SSL             1.2        N 
            m9=p9.match(line)
            if m9 and not m8:
                #{'ao_name':'SSL','ao_version':'1.2','ao_status':'N'}
                groups=m9.groupdict()
                cur_dict[groups['ao_name']]={}
                cur_dict[groups['ao_name']]['version']=groups['ao_version']
                if check_flag==0:
                    cur_dict[groups['ao_name']]['registered']=groups['ao_status']
                else:
                    cur_dict[groups['ao_name']]['incompatible']=groups['ao_status']

            #PEER Statistics
            m10=p10.match(line)
            if m10:
                parsed_dict['peer_stats'] = {}
                cur_dict=parsed_dict['peer_stats']
                check_flag=1

            m11=p11.match(line)
            if m11:
                #{'peer_total':'2'}
                groups=m11.groupdict()
                cur_dict['number_of_peers']=int(groups['peer_total'])
                cur_dict['peer_id']={}
                cur_dict=cur_dict['peer_id']
                temp_dict=parsed_dict['peer_stats']['peer_id']

            m12=p12.match(line)
            if m12:
                #{'peer_id':'10.220.100.214'}
                groups=m12.groupdict()
                cur_dict=temp_dict
                cur_dict[groups['peer_id']]={}
                cur_dict=cur_dict[groups['peer_id']]
                

            m13=p13.match(line)
            if m13:
                #{'peer_ao_num':'2'}
                groups=m13.groupdict()
                cur_dict['number_of_peer_aos'] = int(groups['peer_ao_num'])
                cur_dict['ao_name']={}
                cur_dict=cur_dict['ao_name']
        
        return parsed_dict


