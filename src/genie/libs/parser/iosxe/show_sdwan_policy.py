'''
* 'show sdwan policy ipv6 access-list-associations'
* 'show sdwan policy access-list-associations'
* 'show sdwan policy access-list-counters'
* 'show sdwan policy ipv6 access-list-counters'
'''

# Python
import re
# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional



class ShowSdwanPolicyIpv6AccessListAssociationsSchema(MetaParser):
    ''' Schema for show sdwan policy ipv6 access list associations'''
    schema = {
        'name': {
            Any(): {
                Any(): {
                    'direction': str,
                    'interface_name': str,
                    },
                },
            },
        }


class ShowSdwanPolicyIpv6AccessListAssociations(ShowSdwanPolicyIpv6AccessListAssociationsSchema):

    """ Parser for "show sdwan policy ipv6 access list associations" """
    
    cli_command = "show sdwan policy ipv6 access-list-associations"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return_dict={}
        parsed_dict={}
        if out:
            outlist=out.splitlines()
            #acl-v6-apple  TenGigabitEthernet0/0/0.1002  in
            p1=re.compile(r'^(?P<name>[\w\-\s]+) + (?P<interface_name>[\d\w/\.\-]+) + (?P<interface_direction>[\w\s]+)$')
            for line in outlist:
                m1=p1.match(line.rstrip())
                if m1:
                    groups=m1.groupdict()
                    local_dict={}
                    local_dict['interface_name'] = groups['interface_name']
                    local_dict['interface_direction'] = groups['interface_direction'].strip()
                    if groups['name'].replace(' ','') !='':
                        key=groups['name'].replace(' ','')
                        entry=1
                        return_dict[key]={}
                        return_dict[key][entry] = {}
                        return_dict[key][entry] = local_dict
                    else:
                        entry=entry+1
                        return_dict[key][entry]=local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict

class ShowSdwanPolicyAccessListAssociations(ShowSdwanPolicyIpv6AccessListAssociationsSchema):

    """ Parser for "show sdwan policy access list associations" """
    
    cli_command = "show sdwan policy access-list-associations"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        return_dict={}
        parsed_dict={}
        if out:
            outlist=out.splitlines()
            #acl-v6-apple  TenGigabitEthernet0/0/0.1002  in
            p1=re.compile(r'^(?P<name>[\w\-\s]+) + (?P<interface_name>[\d\w/\.\-]+) + (?P<interface_direction>[\w\s]+)$')
            for line in outlist:
                m1=p1.match(line.rstrip())
                if m1:
                    groups=m1.groupdict()
                    local_dict={}
                    local_dict['interface_name'] = groups['interface_name']
                    local_dict['interface_direction'] = groups['interface_direction'].strip()
                    if groups['name'].replace(' ','') !='':
                        key=groups['name'].replace(' ','')
                        entry=1
                        return_dict[key]={}
                        return_dict[key][entry] = {}
                        return_dict[key][entry] = local_dict
                    else:
                        entry=entry+1
                        return_dict[key][entry]=local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict


class ShowSdwanPolicyAccessListCountersSchema(MetaParser):
    ''' Schema for show sdwan policy access-list-counters'''
    schema = {
        'name': {
            Any(): {
                Any(): {
                    'bytes': str,
                    'counter_name': str,
                    'packets':str,
                    },
                },
            },
        }


class ShowSdwanPolicyAccessListCounters(ShowSdwanPolicyAccessListCountersSchema):

    """ Parser for "show sdwan policy access-list-counters" """
    
    cli_command = "show sdwan policy access-list-counters"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        return_dict={}
        final_dict={}
        if out:
            outlist=out.splitlines()
            for lines in range(len(outlist)):
                if len(outlist[lines].rstrip()) < 24:
                    local_list=outlist[lines-1].split()
                    local_list[0] = local_list[0]+ outlist[lines]
                    outlist[lines-1] = "  ".join(local_list)
            p1=re.compile(r'^(?P<name>[\w\-\s]+) + (?P<counter_name>[\d\w/\.\-]+) + (?P<packets>[\d]+) +(?P<bytes>[\d]+)$')
            for line in outlist:
                m1=p1.match(line.rstrip())
                if m1:
                    groups=m1.groupdict()
                    local_dict={}
                    local_dict['counter_name'] = groups['counter_name']
                    local_dict['packets'] = groups['packets']
                    local_dict['bytes'] = groups['bytes']
                    if groups['name'].replace(' ','') !='':
                        key=groups['name'].replace(' ','')
                        entry=1
                        return_dict[key]={}
                        return_dict[key][entry] = {}
                        return_dict[key][entry] = local_dict
                    else:
                        entry=entry+1
                        return_dict[key][entry]=local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict

class ShowSdwanPolicyIpv6AccessListCounters(ShowSdwanPolicyAccessListCountersSchema):

    """ Parser for "show sdwan policy ipv6 access-list-counters" """
    
    cli_command = "show sdwan policy ipv6 access-list-counters"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}

        return_dict={}
        final_dict={}
        if out:
            outlist=out.splitlines()
            for lines in range(len(outlist)):
                if len(outlist[lines].rstrip()) < 24:
                    local_list=outlist[lines-1].split()
                    local_list[0] = local_list[0]+ outlist[lines]
                    outlist[lines-1] = "  ".join(local_list)
            p1=re.compile(r'^(?P<name>[\w\-\s]+) +(?P<counter_name>[\d\w/\.\-]+) +(?P<packets>[\d]+) +(?P<bytes>[\d]+)$')
            for line in outlist:
                m1=p1.match(line.rstrip())
                if m1:
                    groups=m1.groupdict()
                    local_dict={}
                    local_dict['counter_name'] = groups['counter_name']
                    local_dict['packets'] = groups['packets']
                    local_dict['bytes'] = groups['bytes'].strip()
                    if groups['name'].replace(' ','') !='':
                        key=groups['name'].replace(' ','')
                        entry=1
                        return_dict[key]={}
                        return_dict[key][entry] = {}
                        return_dict[key][entry] = local_dict
                    else:
                        entry=entry+1
                        return_dict[key][entry]=local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict
