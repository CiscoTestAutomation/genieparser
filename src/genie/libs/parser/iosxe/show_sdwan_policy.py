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
                'interface_direction': {
                    Any(): {
                        'interface_name': list,
                    },
                }
            },
        }
    }


class ShowSdwanPolicyIpv6AccessListAssociations(ShowSdwanPolicyIpv6AccessListAssociationsSchema):

    """ Parser for "show sdwan policy ipv6 access list associations" """
    
    cli_command = "show sdwan policy ipv6 access-list-associations"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict={}
        return_dict = {}
        if out:
            outlist = out.splitlines()
            p1 = re.compile(r'^(?P<name>[\w\-\s]+) + (?P<interface_name>[\d\w/\.\-]+) + (?P<interface_direction>[\w]+)$')
            for line in outlist:
                m1 = p1.match(line)
                if m1:
                    groups = m1.groupdict()
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        list_in = []
                        list_out = []
                        list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction'] = {}
                        return_dict[key]['interface_direction'][groups['interface_direction']] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                    else:
                        if groups['interface_direction'] == 'out':
                            list_out.append(groups['interface_name'])
                        elif groups['interface_direction'] == 'in':
                            list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction']['out'] = {}
                        return_dict[key]['interface_direction']['out']['interface_name'] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                        return_dict[key]['interface_direction']['out']['interface_name'] = list_out
            parsed_dict['name'] = return_dict
        return parsed_dict


class ShowSdwanPolicyAccessListAssociations(ShowSdwanPolicyIpv6AccessListAssociationsSchema):
    """ Parser for "show sdwan policy ipv6 access list associations" """

    cli_command = "show sdwan policy access-list-associations"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        return_dict = {}
        if out:
            outlist = out.splitlines()
            p1 = re.compile(
                r'^(?P<name>[\w\-\s]+) + (?P<interface_name>[\d\w/\.\-]+) + (?P<interface_direction>[\w]+)$')
            for line in outlist:
                m1 = p1.match(line)
                if m1:
                    groups = m1.groupdict()
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        list_in = []
                        list_out = []
                        list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction'] = {}
                        return_dict[key]['interface_direction'][groups['interface_direction']] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                    else:
                        if groups['interface_direction'] == 'out':
                            list_out.append(groups['interface_name'])
                        elif groups['interface_direction'] == 'in':
                            list_in.append(groups['interface_name'])
                        return_dict[key]['interface_direction']['out'] = {}
                        return_dict[key]['interface_direction']['out']['interface_name'] = {}
                        return_dict[key]['interface_direction']['in']['interface_name'] = list_in
                        return_dict[key]['interface_direction']['out']['interface_name'] = list_out
            parsed_dict['name'] = return_dict
        return parsed_dict


class ShowSdwanPolicyAccessListCountersSchema(MetaParser):
    ''' Schema for show sdwan policy access-list-counters'''
    schema = {
        'name': {
            Any(): {
                'counter_name': {
                    Any(): {
                        'bytes': int,
                        'packets': int
                    }
                }
            },
        }
    }

class ShowSdwanPolicyAccessListCounters(ShowSdwanPolicyAccessListCountersSchema):

    """ Parser for "show sdwan policy access-list-counters" """
    
    cli_command = "show sdwan policy access-list-counters" or "show sdwan policy ipv6 access-list-counters"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        return_dict={}
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
                    groups = m1.groupdict()
                    local_dict = {}
                    local_dict['packets'] = int(groups['packets'])
                    local_dict['bytes'] = int(groups['bytes'])
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        return_dict[key]['counter_name'] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
                    else:
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict


class ShowSdwanPolicyIpv6AccessListCounters(ShowSdwanPolicyAccessListCountersSchema):
    """ Parser for "show sdwan policy access-list-counters" """

    cli_command = "show sdwan policy ipv6 access-list-counters"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        parsed_dict = {}
        return_dict = {}
        if out:
            outlist = out.splitlines()
            for lines in range(len(outlist)):
                if len(outlist[lines].rstrip()) < 24:
                    local_list = outlist[lines - 1].split()
                    local_list[0] = local_list[0] + outlist[lines]
                    outlist[lines - 1] = "  ".join(local_list)
            p1 = re.compile(
                r'^(?P<name>[\w\-\s]+) + (?P<counter_name>[\d\w/\.\-]+) + (?P<packets>[\d]+) +(?P<bytes>[\d]+)$')
            for line in outlist:
                m1 = p1.match(line.rstrip())
                if m1:
                    groups = m1.groupdict()
                    local_dict = {}
                    local_dict['packets'] = int(groups['packets'])
                    local_dict['bytes'] = int(groups['bytes'])
                    if groups['name'].replace(' ', '') != '':
                        key = groups['name'].replace(' ', '')
                        return_dict[key] = {}
                        return_dict[key]['counter_name'] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = {}
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
                    else:
                        return_dict[key]['counter_name'][groups['counter_name']] = local_dict
            parsed_dict['name'] = return_dict
        return parsed_dict