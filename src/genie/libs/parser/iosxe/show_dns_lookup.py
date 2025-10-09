'''  show_dns_lookup.py

IOSXE parsers for the following show commands:

    * 'show dns-lookup cache'
    * 'show dns-lookup hostname {hostname}'

'''

# Python
import re

# Metaparser
from genie.libs.parser.utils.common import Common
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowDnsLookupSchema(MetaParser):
    ''' Schema for:
        * 'show dns-lookup cache'
        * 'show dns-lookup hostname {hostname}'
    '''

        # Job Id: 6
        #  Status: JOB_COMPLETED
        #  Request Info:
        #   VRF Name: Mgmt-intf
        #   Host Name: yahoo.com
        #   DNS Server: 72.163.128.140
        #  Request-time: *Sep 19 20:22:29.836 Completion-time: *Sep 19 20:22:29.847
        #  Error Code: No Error
        #  DNS Response: 
        #   Id: 0
        #   Flags: qr-response opcode-query rd ra rcode-noerr 
        #   Qdcount: 1 Ancount: 6 Nscount: 0 Arcount: 1 
        #   Class: IN Type: IPv6 RTT: 11ms
        #   Payload Size: 206
        #   IP: 2001:4998:44:3507::8001                   TTL: 0
        #   IP: 2001:4998:24:120D::1:1                    TTL: 0
        #   IP: 2001:4998:124:1507::F001                  TTL: 0
        #   IP: 2001:4998:24:120D::1:0                    TTL: 0
        #   IP: 2001:4998:44:3507::8000                   TTL: 0
        #   IP: 2001:4998:124:1507::F000                  TTL: 0

    schema = {
        'total_number_of_jobs': int,
        Optional('job_id'): {
            Any(): {
                Optional('status'): str,
                Optional('request_info'): {
                    Optional('vrf_name'): str,
                    Optional('host_name'): str,
                    Optional('dns_server'): str,
                },
                Optional('request_time'): str,
                Optional('completion_time'): str,
                Optional('error_code'): str,
                Optional('dns_response'): {
                    Any(): {
                        Optional('dns_id'): int,
                        Optional('dns_flags'): str,
                        Optional('dns_qdcnt'): int,
                        Optional('dns_ancnt'): int,
                        Optional('dns_nscnt'): int,
                        Optional('dns_arcnt'): int,
                        Optional('dns_class'): str,
                        Optional('dns_type'): str,
                        Optional('dns_rtt'): str,
                        Optional('dns_payload_size'): int,
                        Optional('dns_ip'): {
                            Any(): {
                                Optional('dns_ttl'): int
                            },
                        },
                    },
                }
            }
        }
    }
# =======================================
# Parser for 'show dns-lookup cache'
# =======================================
class ShowDnsLookup(ShowDnsLookupSchema):
    ''' Parse for:
        * 'show dns-lookup cache'
        * 'show dns-lookup hostname {hostname}'
        *
    '''
    cli_command = ['show dns-lookup cache', 'show dns-lookup hostname {hostname}']

    exclude = ['request_time','completion_time']

    def cli(self, hostname=None, output=None):

        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Job Id: 6
        jobid_re = re.compile(r'Job\s+Id:\s*(?P<job_id>\d+)?')
        #  Status: JOB_COMPLETED
        jobstatus_re = re.compile(r'Status:\s*(?P<status>\S*)')
        #  Request Info:
        requestinfo_re = re.compile(r'Request\s*Info:\s*')
        #   VRF Name: Mgmt-intf
        #   VRF Name: default
        vrfname_re = re.compile(r'VRF\s*Name:\s*(?P<vrf_name>(\S*))')
        #   Host Name: yahoo.com
        #   Host Name: test123.com
        hostname_re = re.compile(r'Host\s*Name:\s*(?P<host_name>\S*)')
        #   DNS Server: 72.163.128.140
        #   DNS Server: FE80::203:E3FF:FE6A:BF81
        #   DNS Server: 1::1
        dnsserver_re = re.compile(r'DNS\s*Server:\s*(?P<dns_server>\S*)')
        #  Request-time: *Sep 19 20:22:29.836 Completion-time: *Sep 19 20:22:29.847
        requestcompletiontime_re = re.compile(r'Request-time:\s*\*(?P<request_time>\w+\s*\d+\s\d{2}:\d{2}:\d{2}\.\d{3})\s*(Completion-time:\s*\*(?P<completion_time>\w+\s*\d+\s\d{2}:\d{2}:\d{2}\.\d{3})?)?$')
        #  Error Code: No Error
        #  Error Code: Lookup Timeout
        errorcode_re = re.compile(r'Error\s*Code:\s*(?P<error_code>[a-zA-Z ]*)')
        #  DNS Response: 
        dnsresp_re = re.compile(r'DNS\s*Response:\s*')
        #   Id: 0
        dnsrespid_re = re.compile(r'Id:\s*(?P<dns_id>\d+)')
        #   Flags: qr-response opcode-query rd ra rcode-noerr 
        dnsrespflags_re = re.compile(r'Flags:\s*(?P<dns_flags>[a-zA-Z -]*)')
        #   Qdcount: 1 Ancount: 6 Nscount: 0 Arcount: 1 
        dnsrespcnt_re = re.compile(r'Qdcount:\s(?P<dns_qdcnt>\d+)\sAncount:\s(?P<dns_ancnt>\d+)\sNscount:\s(?P<dns_nscnt>\d+)\sArcount:\s(?P<dns_arcnt>\d+)')
        #   Class: IN Type: IPv6 RTT: 11ms
        dnsrespclass_re = re.compile(r'Class:\s(?P<dns_class>\w+)\sType:\s(?P<dns_type>\w+)\sRTT:\s(?P<dns_rtt>\d+ms)')
        #   Payload Size: 206
        dnsresppayloadsize_re = re.compile(r'Payload\s*Size:\s*(?P<dns_payload_size>\d*)')
        #   IP: 2001:4998:44:3507::8001                   TTL: 0
        #   IP: 2001:4998:24:120D::1:1                    TTL: 0
        #   IP: 2001:4998:124:1507::F001                  TTL: 0
        dnsrespip_re = re.compile(r'IP:\s*(?P<dns_ip>\S*)\s*TTL:\s*(?P<dns_ttl>\d*)')
        
        # Init vars
        request_info_var = 0
        parsed_dict = {}
        index_device = 0
        dns_id_index = 0
        for line in out.splitlines():
            line = line.strip()

            # Job Id: 6
            result = jobid_re.match(line)
            if result:
                index_device += 1
                dns_id_index = 0
                parsed_dict['total_number_of_jobs'] = index_device
                if result.group('job_id'):
                    job_id = int(result.group('job_id'))
                    devices_dict = parsed_dict.setdefault('job_id', {})\
                        .setdefault(job_id, {})
                continue

            #  Status: JOB_COMPLETED
            result = jobstatus_re.match(line)
            if result:
                if result.group('status'):
                    devices_dict['status'] = result.group('status')
                continue

            #  Request Info:
            result = requestinfo_re.match(line)

            if result:
                request_info_var = 1
                continue
            
            #   VRF Name: Mgmt-intf
            result = vrfname_re.match(line)
            if result:
                if result.group('vrf_name'):
                    vrf_name = result.group('vrf_name')
                continue

            #   Host Name: yahoo.com
            result = hostname_re.match(line)    
            if result:
                if result.group('host_name'):
                    host_name = result.group('host_name')
                continue
            
            #   DNS Server: 72.163.128.140
            result = dnsserver_re.match(line)    
            if result:
                if result.group('dns_server'):
                    dns_server = result.group('dns_server')
                continue

            if request_info_var:
                reqinfo_dict = devices_dict.setdefault('request_info',{})
                reqinfo_dict.update({'vrf_name': vrf_name})
                reqinfo_dict.update({'host_name': host_name})
                reqinfo_dict.update({'dns_server': dns_server})
            
            #  Request-time: *Sep 19 20:22:29.836 Completion-time: *Sep 19 20:22:29.847
            result = requestcompletiontime_re.match(line) 
            if result:
                groups = result.groupdict()
                request_time = groups['request_time']
                completion_time = groups['completion_time']
                if request_time and completion_time:
                    devices_dict.update({'request_time':request_time})
                    devices_dict.update({'completion_time':completion_time})
                continue

            #  Error Code: No Error
            result = errorcode_re.match(line)
            if result:
                devices_dict['error_code'] = result.group('error_code')
                continue

            #  DNS Response: 
            #   Id: 0
            result = dnsrespid_re.match(line)
            if result:
                dns_id_index += 1
                dns_id = result.group('dns_id')
                dnsresp_dict = devices_dict.setdefault('dns_response',{})
                dnsrespid_dict = dnsresp_dict.setdefault(dns_id_index,{})
                dnsrespid_dict.update({'dns_id':int(dns_id)})
                continue

            #   Flags: qr-response opcode-query rd ra rcode-noerr
            result = dnsrespflags_re.match(line)
            if result:
                dnsrespid_dict.update({'dns_flags': result.group('dns_flags')})
                continue

            #   Qdcount: 1 Ancount: 6 Nscount: 0 Arcount: 1 
            result = dnsrespcnt_re.match(line)
            if result:
                groups = result.groupdict()
                dnsrespid_dict.update({
                    'dns_qdcnt': int(groups['dns_qdcnt']),
                    'dns_ancnt': int(groups['dns_ancnt']),
                    'dns_nscnt': int(groups['dns_nscnt']),
                    'dns_arcnt': int(groups['dns_arcnt']),
                })
                continue

            #   Class: IN Type: IPv6 RTT: 11ms
            result = dnsrespclass_re.match(line)
            if result:
                groups = result.groupdict()
                dnsrespid_dict.update({
                    'dns_class': groups['dns_class'],
                    'dns_type': groups['dns_type'],
                    'dns_rtt': groups['dns_rtt']
                })
                continue
            
            #   Payload Size: 206
            result = dnsresppayloadsize_re.match(line)
            if result:
                dns_payload_size = result.group('dns_payload_size')
                dnsrespid_dict.update({'dns_payload_size':int(dns_payload_size)})
                continue

            #   IP: 2001:4998:44:3507::8001                   TTL: 0
            #   IP: 2001:4998:24:120D::1:1                    TTL: 0
            #   IP: 2001:4998:124:1507::F001                  TTL: 0
            result = dnsrespip_re.match(line)
            if result:
                groups = result.groupdict()
                dnsrespip_dict = dnsrespid_dict.setdefault('dns_ip',{}).setdefault(groups['dns_ip'],{})
                dnsrespip_dict.update({'dns_ttl':int(groups['dns_ttl'])})
                continue

        return parsed_dict