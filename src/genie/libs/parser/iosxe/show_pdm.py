''' show_pdm.py

IOSXE parsers for the following show commands:
    * show pdm steering policy 
    * show pdm steering policy <steering_policy> details
    * show pdm steering policy | count <service>
'''

# Python
import re
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional
from genie.libs.parser.utils.common import Common


# ==============================
# Schema for 'show pdm steering policy'
# ==============================
class ShowPdmSteeringPolicySchema(MetaParser):

    ''' Schema for "show pdm steering policy" '''

    schema = {
        'contract': {
            Any(): {
                'policy': {
                    Any(): {
                        'protocol': int,
                        'src_port': str,
                        'dst_port': str,
                        'service': str,
                        'pdm_counters': int,
                    },
                },
            },
        },
    }


# ==============================
# Parser for:
# 'show pdm steering policy '
# ==============================
class ShowPdmSteeringPolicy(ShowPdmSteeringPolicySchema):
    """Schema for show pdm steering policy """

    cli_command = 'show pdm steering policy'

    def cli(self, output=None, timeout=240):
        if output is None:
            output = self.device.execute(self.cli_command, timeout=timeout)
        pdm_dict = {}

        # Steering Policy Contract2-01
        p1 = re.compile(r"^Steering\s+Policy\s*(?P<contract>[\w]+)-[\w]+$")
        #     1 redirect protocol 6 src-port any dst-port eq 15000 service \
        #        service_INFRA_VN (0 match)
        p2 = re.compile(r"^(?P<s_no>[\d]+)\s*redirect protocol\s*"\
                "(?P<protocol>[\d]+)\s*src-port\s*(eq)?\s*"\
                "(?P<src_port>[\w]+)\s*dst-port\s*(eq)?\s*"\
                "(?P<dst_port>[\w]+)\s*service\s*(?P<service>[\w]+)"\
                "\s*\(\s*(?P<pdm_counters>[\d]+)\s*(match|matches)\)$")
        for line in output.splitlines():
            line = line.strip()

            # Steering Policy Contract2-01
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                contract = groups['contract']
                new_policy = pdm_dict.setdefault('contract',{}).setdefault(contract,{}).setdefault('policy',{})
                continue
            #     1 redirect protocol 6 src-port any dst-port eq 15000 service service_INFRA_VN (0 match)
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                s_no = int(groups['s_no'])
                protocol = int(groups['protocol'])
                src_port = groups['src_port']
                dst_port = groups['dst_port']
                service = groups['service']
                pdm_counters = int(groups['pdm_counters'])
                new_policy.update({
                    s_no: {
                        'protocol': protocol,
                        'src_port': src_port,
                        'dst_port': dst_port,
                        'service': service,
                        'pdm_counters': pdm_counters
                    }
                })
                continue

        return pdm_dict


# ==============================
# Schema for 'show pdm steering policy <steering_policy> detail'
# ==============================
class ShowPdmSteeringPolicyDetailsSchema(MetaParser):

    ''' Schema for "show pdm steering policy {steering_policy} detail" '''

    
    schema = {
        'policy': str,
        'policy_id': str,
        'policy_entries': {
            Any(): {
                'protocol': int,
                'src_port': str,
                'dst_port': str,
                'service': str,
                'counters': int,
                'service_name': str,
                'firewall_mode': str,
                'service_ip': str,
                'service_locator': str,
                'vrf_id': int,
                'vnid': int,
                'rloc_status': str,
                'no_of_rlocs': int,
                'owner': str,
                Optional('rloc'): {
                    Any(): {
                        'rloc_ip': str,
                        'weight': int,
                        'priority': int,
                    },
                },
            },
        }
    }



# ==============================
# Parser for:
# 'show pdm steering policy <steering_policy> details'
# ==============================
class ShowPdmSteeringPolicyDetails(ShowPdmSteeringPolicyDetailsSchema):
    """Schema for show pdm steering policy {steering_policy} details """

    cli_command = 'show pdm steering policy {steering_policy} detail'

    def cli(self, steering_policy, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(steering_policy=steering_policy))
        parsed_dict = {}

        # Steering Policy Contract2-01
        p1 = re.compile(r"^Steering Policy\s*(?P<policy>[\w]+)-[\w]+$")
        # Policy ID: 577677153
        p2 = re.compile(r"^Policy ID:\s*(?P<policy_id>[\d]+)$")
        # 1 redirect protocol 6 src-port any dst-port eq 15000 service service_INFRA_VN (0 match)
        p3 = re.compile(r"^(?P<s_no>[\d]+)\s*redirect protocol\s*(?P<protocol>[\d]+)\s*src-port\s*(eq)?\s*(?P<src_port>[\w]+)\s*dst-port\s*(eq)?\s*(?P<dst_port>[\w]+)\s*service\s*(?P<service>[\w]+)\s*\(\s*(?P<counters>[\d]+)\s*(match|matches)\)$")
        # Service Name: service_INFRA_VN
        p4 = re.compile(r"^Service Name:\s*(?P<service_name>[\w]+)$")
        # Firewall mode      : routed
        p5 = re.compile(r"^Firewall mode\s*:\s*(?P<firewall_mode>[\w]+)$")
        # Service IP         : 172.18.0.2
        p6 = re.compile(r"^Service IP\s*:\s*(?P<service_ip>[\w.]+)$")
        # Service Locator    : 255
        p7 = re.compile(r"^Service Locator\s*:\s*(?P<service_locator>[\w]+)$")
        # VRF ID             : 0
        p8 = re.compile(r"^VRF ID\s*:\s*(?P<vrf_id>[\w]+)$")
        # Vnid               : 4097
        p9 = re.compile(r"^Vnid\s*:\s*(?P<vnid>[\w]+)$")
        # RLOC Status        : Received
        p10 = re.compile(r"^RLOC Status\s*:\s*(?P<rloc_status>[\w]+)$")
        # no.of rlocs        : 1
        p11 = re.compile(r"^no.of rlocs\s*:\s*(?P<no_of_rlocs>[\w]+)$")
        # *1. RLOC IP: 60.60.60.62    Weight: 10    Priority: 0
        p12 = re.compile(r"^\*?(?P<s_no>[\d]+).\s*RLOC\s*IP:\s*(?P<rloc_ip>[\w.]+)\s*Weight:\s*(?P<weight>[\d]+)\s*Priority:\s*(?P<priority>[\d]+)$")
        # Owner              : GPP
        p13 = re.compile(r"^Owner\s*:\s*(?P<owner>[\w]+)$")

        for line in output.splitlines():
            line = line.strip()
            # Steering Policy Contract2-01
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                policy = groups['policy']
                parsed_dict['policy'] = policy
                continue
            # Policy ID: 577677153
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                policy_id = groups['policy_id']
                parsed_dict['policy_id'] = policy_id
                continue
            # 1 redirect protocol 6 src-port any dst-port eq 15000 service service_INFRA_VN (0 match)
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                if not parsed_dict.get('policy_entries', {}):
                    policy_entries_dict = parsed_dict.setdefault('policy_entries',{})
                s_no = int(groups['s_no'])
                protocol = int(groups['protocol'])
                src_port = groups['src_port']
                dst_port = groups['dst_port']
                service = groups['service']
                counters = int(groups['counters'])
                policy_dic = policy_entries_dict.setdefault(s_no,{})
                policy_dic.update({
                    'protocol': protocol,
                    'src_port': src_port,
                    'dst_port': dst_port,
                    'service': service,
                    'counters': counters
                })
                continue
            # Service Name: service_INFRA_VN
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                service_name = groups['service_name']
                policy_dic.update({'service_name':service_name})
                continue
            # Firewall mode      : routed
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                firewall_mode = groups['firewall_mode']
                policy_dic.update({'firewall_mode':firewall_mode})
                continue
            # Service IP         : 172.18.0.2
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                service_ip = groups['service_ip']
                policy_dic.update({'service_ip':service_ip})
                continue
            # Service Locator    : 255
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                service_locator = groups['service_locator']
                policy_dic.update({'service_locator':service_locator})
                continue
            # VRF ID             : 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                vrf_id = int(groups['vrf_id'])
                policy_dic.update({'vrf_id':vrf_id})
                continue
            # Vnid               : 4097
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                vnid = int(groups['vnid'])
                policy_dic.update({'vnid':vnid})
                continue
            # RLOC Status        : Received
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                rloc_status = groups['rloc_status']
                policy_dic.update({'rloc_status':rloc_status})
                continue
            # no.of rlocs        : 1
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                no_of_rlocs = int(groups['no_of_rlocs'])
                policy_dic.update({'no_of_rlocs':no_of_rlocs})
                continue
            # *1. RLOC IP: 60.60.60.62    Weight: 10    Priority: 0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                s_no = int(groups['s_no'])
                rloc_ip = groups['rloc_ip']
                weight = int(groups['weight'])
                priority = int(groups['priority'])
                rloc_list_dict = policy_dic.setdefault('rloc',{})
                rloc_list_dict.update({
                    s_no: {
                        'rloc_ip': rloc_ip,
                        'weight': weight,
                        'priority':priority
                    }
                })
                continue
            # Owner              : GPP
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                owner = groups['owner']
                policy_dic.update({'owner':owner})
                continue

        return parsed_dict


# ==============================
# Schema for 'show pdm steering service'
# ==============================
class ShowPdmSteeringServiceSchema(MetaParser):

    ''' Schema for "show pdm steering service" '''

    schema = {
        'services': {
            Any(): {
                'mode': str,
                'ip_address': str,
                'selector': int,
                'vnid': int,
            },
        },
    }



# ==============================
# Parser for:
# 'show pdm steering service '
# ==============================
class ShowPdmSteeringService(ShowPdmSteeringServiceSchema):
    """Schema for show pdm steering service """

    cli_command = 'show pdm steering service'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        parsed_dict = {}

        # Steering Service service_INFRA_VN
        p1 = re.compile(r"^Steering Service\s*(?P<service>[\w]+)")
        #     mode routed address 172.18.0.2 selector 255 vnid 4097
        p2 = re.compile(r"^\s*mode\s*(?P<mode>[\w]+)\s*address\s*(?P<ip_address>[\w.]+)\s*selector\s*(?P<selector>[\w]+)\s*vnid\s*(?P<vnid>[\d]+)\s*")
        for line in output.splitlines():
            line = line.strip()

            # # Steering Service service_INFRA_VN
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                service = groups['service']
                if not parsed_dict.get('services', {}):
                    service_dic = parsed_dict.setdefault('services',{})
                service_details = service_dic.setdefault(service,{})
                continue
            #     mode routed address 172.18.0.2 selector 255 vnid 4097
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                mode = groups['mode']
                ip_address = groups['ip_address']
                selector = int(groups['selector'])
                vnid = int(groups['vnid'])
                service_details.update({
                    'mode': mode,
                    'ip_address': ip_address,
                    'selector': selector,
                    'vnid': vnid
                })
                continue

        return parsed_dict


# ==============================
# Schema for 'show pdm steering service <steering_service> detail'
# ==============================
class ShowPdmSteeringServiceDetailSchema(MetaParser):

    ''' Schema for "show pdm steering service {steering_service} detail" '''

    schema = {
        'service_name': str,
        'service_id': str,
        'ref_count': int,
        'stale': str,
        'firewall_mode': str,
        'service_ip': str,
        'service_locator': str,
        'vrf_id': int,
        'vnid': int,
        'rloc_status': str,
        'no_of_rlocs': int,
        'owner': str,
        Optional('rloc'): {
            Any(): {
                'rloc_ip': str,
                'weight': int,
                'priority': int,
            },
        },
    }


# ==============================
# Parser for:
# 'show pdm steering service <steering_service> detail'
# ==============================
class ShowPdmSteeringServiceDetail(ShowPdmSteeringServiceDetailSchema):
    """Schema for show pdm steering service {steering_service} detail """

    cli_command = 'show pdm steering service {steering_service} detail'

    def cli(self, steering_service, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        parsed_dict = {}


        # Service Name   : service_INFRA_VN
        p1 = re.compile(r"^Service Name\s*:\s*(?P<service_name>[\w]+)$")
        # Service ID     : 2068955985
        p2 = re.compile(r"^Service ID\s*:\s*(?P<service_id>[\d]+)$")
        # Ref count      : 2
        p3 = re.compile(r"^Ref count\s*:\s*(?P<ref_count>[\d]+)$")
        # Stale          : FALSE
        p4 = re.compile(r"^Stale\s*:\s*(?P<stale>[\w]+)$")
        # Firewall mode      : routed
        p5 = re.compile(r"^Firewall mode\s*:\s*(?P<firewall_mode>[\w]+)$")
        # Service IP         : 172.18.0.2
        p6 = re.compile(r"^Service IP\s*:\s*(?P<service_ip>[\w.]+)$")
        # Service Locator    : 255
        p7 = re.compile(r"^Service Locator\s*:\s*(?P<service_locator>[\w]+)$")
        # VRF ID             : 0
        p8 = re.compile(r"^VRF ID\s*:\s*(?P<vrf_id>[\w]+)$")
        # Vnid               : 4097
        p9 = re.compile(r"^Vnid\s*:\s*(?P<vnid>[\w]+)$")
        # RLOC Status        : Received
        p10 = re.compile(r"^RLOC Status\s*:\s*(?P<rloc_status>[\w]+)$")
        # no.of rlocs        : 1
        p11 = re.compile(r"^no.of rlocs\s*:\s*(?P<no_of_rlocs>[\w]+)$")
        # *1. RLOC IP: 60.60.60.62    Weight: 10    Priority: 0
        p12 = re.compile(r"^\*?(?P<s_no>[\d]+).\s*RLOC\s*IP:\s*(?P<rloc_ip>[\w.]+)\s*Weight:\s*(?P<weight>[\d]+)\s*Priority:\s*(?P<priority>[\d]+)$")
        # Owner              : GPP
        p13 = re.compile(r"^Owner\s*:\s*(?P<owner>[\w]+)$")



        for line in output.splitlines():
            line = line.strip()

            # Service Name   : service_INFRA_VN
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                service_name = groups['service_name']
                parsed_dict['service_name'] = service_name
                continue
            # Service ID     : 2068955985
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                service_id = groups['service_id']
                parsed_dict['service_id'] = service_id
                continue
            # Ref count      : 2
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                ref_count = int(groups['ref_count'])
                parsed_dict['ref_count'] = ref_count
                continue
            # Stale          : FALSE
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                stale = groups['stale']
                parsed_dict['stale'] = stale
                continue
            #     Firewall mode      : routed
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                firewall_mode = groups['firewall_mode']
                parsed_dict['firewall_mode'] = firewall_mode
                continue
            # Service IP         : 172.18.0.2
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                service_ip = groups['service_ip']
                parsed_dict['service_ip'] = service_ip
                continue
            # Service Locator    : 255
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                service_locator = groups['service_locator']
                parsed_dict['service_locator'] = service_locator
                continue
            # VRF ID             : 0
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                vrf_id = int(groups['vrf_id'])
                parsed_dict['vrf_id'] = vrf_id
                continue
            # Vnid               : 4097
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                vnid = int(groups['vnid'])
                parsed_dict['vnid'] = vnid
                continue
            # RLOC Status        : Received
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                rloc_status = groups['rloc_status']
                parsed_dict['rloc_status'] = rloc_status
                continue
            # no.of rlocs        : 1
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                no_of_rlocs = int(groups['no_of_rlocs'])
                parsed_dict['no_of_rlocs'] = no_of_rlocs
                continue
            # *1. RLOC IP: 60.60.60.62    Weight: 10    Priority: 0
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                s_no = groups['s_no']
                rloc_ip = groups['rloc_ip']
                weight = int(groups['weight'])
                priority = int(groups['priority'])
                rloc_list_dict = parsed_dict.setdefault('rloc',{})
                rloc_list_dict.update({s_no:{'rloc_ip':rloc_ip,'weight':weight,'priority':priority}})
                continue
            # Owner              : GPP
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                owner = groups['owner']
                parsed_dict['owner'] = owner
                continue

        return parsed_dict


# ==============================
# Schema for 'show pdm steering policy | count {service}'
# ==============================
class ShowPdmSteeringPolicyCountSchema(MetaParser):

    ''' Schema for "show pdm steering policy | count {service}" '''

    schema = {
        'count': int
    }
# ==============================
# Parser for:
# 'show pdm steering policy | count <service> '
# ==============================
class ShowPdmSteeringPolicyCount(ShowPdmSteeringPolicyCountSchema):
    """Schema for show pdm steering policy | count {service}"""

    cli_command = 'show pdm steering policy | count {service}'

    def cli(self, service, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(service=service))
        pdm_dict_count = {}

        # Number of lines which match regexp = 2100
        p1 = re.compile(r"^Number of lines which match regexp\s*=\s*(?P<count>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Number of lines which match regexp = 2100
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                count = int(groups['count'])
                pdm_dict_count['count'] = count

        return pdm_dict_count
