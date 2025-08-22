"""starOS implementation of show diameter peers full.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use, Or, ListOf

class ShowDiameterSchema(MetaParser):
    """Schema for show diameter peers full"""

    schema = {
        'diameter_info': {
            Any(): {
                'Peer Hostname': str,
                'Local Hostname': str,
                'Peer Realm': str,
                'Local Realm': str,
                'Priority channel': str,
                'DSCP configured': str,
                Optional('Peer Address'): ListOf(str),
                Optional('Local Address'): ListOf(str),
                'State': str,
                'Task': str,
                'Admin Status': str,
                },
            'Peer Summary':{
                 'OPEN':str,
                 'CLOSED':str,
                 'INTERMEDIATE':str,
                },
            },
        }


class ShowDiameter(ShowDiameterSchema):
    """Parser for show diameter peers full"""

    cli_command = 'show diameter peers full'

    """
 Peer Hostname: s6b.nz.1dra01.mty.ims.mnc050.mcc334.3gppnetwork.org
  Local Hostname: s6b.sz.2pgw07.leo.ims.mnc050.mcc334.3gppnetwork.org
  Peer Realm: ims.mnc050.mcc334.3gppnetwork.org
  Local Realm: ims.mnc050.mcc334.3gppnetwork.org
  Priority channel: No
  DSCP configured: 0x28
  Peer Address: 10.194.65.36:3869
  Local Address: 10.33.10.198:52302
  State: OPEN [TCP]
  CPU: 8/0                                Task: diamproxy-2                     
  Messages Out/Queued: N/A              
  Supported Vendor IDs: 10415
  Admin Status: Enable 
  DPR Disconnect: N/A
  Peer Backoff Timer running:N/A

 Peer Hostname: s6b.nz.1dra01.mty.ims.mnc050.mcc334.3gppnetwork.org
  Local Hostname: s6b.sz.2pgw02.leo.ims.mnc050.mcc334.3gppnetwork.org
  Peer Realm: ims.mnc050.mcc334.3gppnetwork.org
  Local Realm: ims.mnc050.mcc334.3gppnetwork.org
  Priority channel: No
  DSCP configured: 0x28
  Peer Address: 10.194.65.36:3869
  Local Address: 10.33.10.193:55533
  State: OPEN [TCP]
  CPU: 10/0                               Task: diamproxy-3                     
  Messages Out/Queued: N/A              
  Supported Vendor IDs: 10415
  Admin Status: Enable 
  DPR Disconnect: N/A
  Peer Backoff Timer running:N/A

 Peer Hostname: s6b.nz.1dra01.mty.ims.mnc050.mcc334.3gppnetwork.org
  Local Hostname: s6b.sz.2pgw06.leo.ims.mnc050.mcc334.3gppnetwork.org
  Peer Realm: ims.mnc050.mcc334.3gppnetwork.org
  Local Realm: ims.mnc050.mcc334.3gppnetwork.org
  Priority channel: No
  DSCP configured: 0x28
  Peer Address: 10.194.65.36:3869
  Local Address: 10.33.10.197:40193
  State: OPEN [TCP]
  CPU: 3/0                                Task: diamproxy-4                     
  Messages Out/Queued: N/A              
  Supported Vendor IDs: 10415
  Admin Status: Enable 
  DPR Disconnect: N/A
  Peer Backoff Timer running:N/A

 Peer Hostname: s6b.nz.1dra01.mty.ims.mnc050.mcc334.3gppnetwork.org
  Local Hostname: s6b.sz.2pgw04.leo.ims.mnc050.mcc334.3gppnetwork.org
  Peer Realm: ims.mnc050.mcc334.3gppnetwork.org
  Local Realm: ims.mnc050.mcc334.3gppnetwork.org
  Priority channel: No
  DSCP configured: 0x28
  Peer Address: 10.194.65.36:3869
  Local Address: 10.33.10.195:47995
  State: OPEN [TCP]
  CPU: 1/0                                Task: diamproxy-5                     
  Messages Out/Queued: N/A              
  Supported Vendor IDs: 10415
  Admin Status: Enable 
  DPR Disconnect: N/A
  Peer Backoff Timer running:N/A

 Peer Hostname: s6b.nz.1dra01.mty.ims.mnc050.mcc334.3gppnetwork.org
  Local Hostname: s6b.sz.2pgw03.leo.ims.mnc050.mcc334.3gppnetwork.org
  Peer Realm: ims.mnc050.mcc334.3gppnetwork.org
  Local Realm: ims.mnc050.mcc334.3gppnetwork.org
  Priority channel: No
  DSCP configured: 0x28
  Peer Address: 10.194.65.36:3869
  Local Address: 10.33.10.194:44689
  State: OPEN [TCP]
  CPU: 2/0                                Task: diamproxy-6                     
  Messages Out/Queued: N/A              
  Supported Vendor IDs: 10415
  Admin Status: Enable 
  DPR Disconnect: N/A
  Peer Backoff Timer running:N/A

 Peer Hostname: s6b.nz.1dra01.mty.ims.mnc050.mcc334.3gppnetwork.org
  Local Hostname: s6b.sz.2pgw05.leo.ims.mnc050.mcc334.3gppnetwork.org
  Peer Realm: ims.mnc050.mcc334.3gppnetwork.org
  Local Realm: ims.mnc050.mcc334.3gppnetwork.org
  Priority channel: No
  DSCP configured: 0x28
  Peer Address: 10.194.65.36:3869
  Local Address: 10.33.10.196:40478
  State: OPEN [TCP]
  CPU: 7/0                                Task: diamproxy-7                     
  Messages Out/Queued: N/A              
  Supported Vendor IDs: 10415
  Admin Status: Enable 
  DPR Disconnect: N/A
  Peer Backoff Timer running:N/A

 Peers Summary:
  Peers in OPEN state: 70 
  Peers in CLOSED state: 0 
  Peers in intermediate state: 0 
  Total peers matching specified criteria: 70

    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        diameter_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'Peer\sHostname:\s(?P<hostname>.+$)')
        p1 = re.compile(r'Local\sHostname:\s(?P<l_hostname>.+$)')
        p2 = re.compile(r'Peer\sRealm:\s(?P<realm>.+$)')
        p3 = re.compile(r'Local\sRealm:\s(?P<l_realm>.+$)')
        p4 = re.compile(r'Priority\schannel:\s(?P<channel>.+$)')
        p5 = re.compile(r'DSCP\sconfigured:\s(?P<dscp>.+$)')
        p6 = re.compile(r'Peer\sAddress:\s(?P<address>.+$)')
        p7 = re.compile(r'Local\sAddress:\s(?P<l_address>.+$)')
        p8 = re.compile(r'State:\s(?P<state>\w+)')
        p9 = re.compile(r'CPU:\s+(?P<cpu>\d+.\d+)\s+Task:\s+(?P<task>.+$)')
        p10 = re.compile(r'Admin\sStatus:\s+(?P<status>\w+)')
        p11 = re.compile(r'Peers\sin\sOPEN\sstate:\s(?P<open>\d+)')
        p12 = re.compile(r'Peers\sin\sCLOSED\sstate:\s(?P<closed>\d+)')
        p13 = re.compile(r'Peers\sin\sintermediate\sstate:\s(?P<inter>\d+)')
        p14 = re.compile(r'Context:\s\w+\s*Endpoint:\s(?P<endpoint>\w+)')
        e_number=1
        for line in out.splitlines():
            line = line.strip()
            m = p14.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                endpoint = m.groupdict()['endpoint']
                if e_number>1:
                    e_number =1
            
            m = p9.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                task = m.groupdict()['task']
                result_dict[endpoint_num]['Task']= task
                
            m = p0.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                hostname = m.groupdict()['hostname']
                endpoint_num = str(e_number)+"_"+endpoint
                result_dict[endpoint_num] = {}
                e_number+=1
                result_dict[endpoint_num]['Peer Hostname'] = hostname

            m = p1.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                l_hostname = m.groupdict()['l_hostname']
                result_dict[endpoint_num]['Local Hostname'] = l_hostname
            
            m = p2.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                realm = m.groupdict()['realm']
                result_dict[endpoint_num]['Peer Realm'] = realm

            m = p3.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                l_realm = m.groupdict()['l_realm']
                result_dict[endpoint_num]['Local Realm'] = l_realm

            m = p4.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                channel = m.groupdict()['channel']
                result_dict[endpoint_num]['Priority channel'] = channel

            m = p5.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                dscp = m.groupdict()['dscp']
                result_dict[endpoint_num]['DSCP configured'] = dscp

            m = p6.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
        
                if "Peer Address" not in result_dict[endpoint_num]:
                    result_dict[endpoint_num]['Peer Address'] = []

                address = m.groupdict()['address']
                result_dict[endpoint_num]['Peer Address'].append(address)

            m = p7.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                
                if "Local Address" not in result_dict[endpoint_num]:
                    result_dict[endpoint_num]['Local Address'] = []
                
                l_address = m.groupdict()['l_address']
                result_dict[endpoint_num]['Local Address'].append(l_address)

            m = p8.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                state = m.groupdict()['state']
                result_dict[endpoint_num]['State'] = state

            m = p10.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                status = m.groupdict()['status']
                result_dict[endpoint_num]['Admin Status'] = status

            m = p11.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                if 'Peer Summary' not in diameter_dict['diameter_info']:
                    result_dict.setdefault('Peer Summary',{})
                open = m.groupdict()['open']
                result_dict['Peer Summary']['OPEN'] = open

            m = p12.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                if 'Peer Summary' not in diameter_dict['diameter_info']:
                    result_dict.setdefault('Peer Summary',{})
                closed = m.groupdict()['closed']
                result_dict['Peer Summary']['CLOSED'] = closed

            m = p13.match(line)
            if m:
                if 'diameter_info' not in diameter_dict:
                    result_dict = diameter_dict.setdefault('diameter_info',{})
                if 'Peer Summary' not in diameter_dict['diameter_info']:
                    result_dict.setdefault('Peer Summary',{})
                inter = m.groupdict()['inter']
                result_dict['Peer Summary']['INTERMEDIATE'] = inter
      
        return diameter_dict
