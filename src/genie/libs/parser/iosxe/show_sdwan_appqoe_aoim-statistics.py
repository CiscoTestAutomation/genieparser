# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional


class ShowSdwanAppqoeAoimStatisticsSchema(MetaParser):
    ''' Schema for show sdwan appqoe aoim-statistics'''
    schema = {
        "total_peer_syncs": int,
        "current_peer_syncs": int,
        "Needed_peer_resyncs": int,
        "passthrough_connections_dueto_peerversion_mismatch": int,
        "aoim_db_size_in_bytes": int,
        "local_ao_stats":{
            "number_of_aos": int,
            "ao_name":{
                Any():
                {
                    "ao_version" : str,
                    "ao_registered": str
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
                            "ao_version" : str,
                            "ao_registered": str
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

        
        p1=re.compile(r'Total Number Of Peer Syncs+\s+\:+\s+(?P<total_peer_syncs>[\d]+)')
        p2=re.compile(r'Current Number Of Peer Syncs in Progress+\s+\:+\s+(?P<current_peer_syncs>[\d]+)')
        p3=re.compile(r'Number Of Peer Re-Syncs Needed+\s+\:+\s+(?P<peer_resyncs>[\d]+)')
        p4=re.compile(r'Total Passthrough Connections Due to Peer Version Mismatch+\s+\:+\s+(?P<passthrough_connections>[\d]+)')
        p5=re.compile(r'AOIM DB Size +\(+Bytes+\)+\:+\s+(?P<aoim_db_size>\d+)')
        p6=re.compile(r'LOCAL AO Statistics')
        p7=re.compile(r'Number Of AOs +\s+\:+\s+(?P<ao_number>\d+)')
        p8=re.compile(r'AO+\s+Version+\s+\w+')
        p9=re.compile(r'\s*(?P<ao_name>\w+)+\s+(?P<ao_version>[\d.]+)+\s+(?P<ao_status>\w+)')
        p10=re.compile(r'PEER Statistics')
        p11=re.compile(r'Number Of Peers+\s+\:+\s+(?P<peer_total>\d+)')
        p12=re.compile(r'\s*Peer ID:+\s+(?P<peer_id>[\d.]+)')
        p13=re.compile(r'Peer Num AOs+\s+\:+\s+(?P<peer_ao_num>\d+)')

        parsed_dict={}

        for line in out.splitlines():
            m1= p1.match(line)
            if m1:
                groups=m1.groupdict()
                parsed_dict['total_peer_syncs']=int(groups['total_peer_syncs'])

            m2= p2.match(line)
            if m2:
                groups=m2.groupdict()
                parsed_dict['current_peer_syncs']=int(groups['current_peer_syncs'])

            m3= p3.match(line)
            if m3:
                groups=m3.groupdict()
                parsed_dict['Needed_peer_resyncs']=int(groups['peer_resyncs'])

            m4= p4.match(line)
            if m4:
                groups=m4.groupdict()
                parsed_dict['passthrough_connections_dueto_peerversion_mismatch']=int(groups['passthrough_connections'])

            m5= p5.match(line)
            if m5:
                groups=m5.groupdict()
                parsed_dict['aoim_db_size_in_bytes']=int(groups['aoim_db_size'])

            m6= p6.match(line)
            if m6:
                parsed_dict['local_ao_stats']={}
                cur_dict=parsed_dict['local_ao_stats']

            m7=p7.match(line)
            if m7:
                groups=m7.groupdict()
                cur_dict['number_of_aos']= int(groups['ao_number'])
                cur_dict['ao_name']={}
                cur_dict=cur_dict['ao_name']

            m8=p8.match(line)
            m9=p9.match(line)
            if m9 and not m8:
                groups=m9.groupdict()
                cur_dict[groups['ao_name']]={}
                cur_dict[groups['ao_name']]['ao_version']=groups['ao_version']
                cur_dict[groups['ao_name']]['ao_registered']=groups['ao_status']

            m10=p10.match(line)
            if m10:
                parsed_dict['peer_stats'] = {}
                cur_dict=parsed_dict['peer_stats']

            m11=p11.match(line)
            if m11:
                groups=m11.groupdict()
                cur_dict['number_of_peers']=int(groups['peer_total'])
                cur_dict['peer_id']={}
                cur_dict=cur_dict['peer_id']
                temp_dict=parsed_dict['peer_stats']['peer_id']

            m12=p12.match(line)
            if m12:
                groups=m12.groupdict()
                cur_dict=temp_dict
                cur_dict[groups['peer_id']]={}
                cur_dict=cur_dict[groups['peer_id']]
                

            m13=p13.match(line)
            if m13:
                groups=m13.groupdict()
                cur_dict['number_of_peer_aos'] = int(groups['peer_ao_num'])
                cur_dict['ao_name']={}
                cur_dict=cur_dict['ao_name']
        
        return parsed_dict


