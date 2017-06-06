''' showplatform.py

Example parser class

'''
import re
import xmltodict
from ats import tcl
from metaparser import MetaParser
from metaparser.util.schemaengine import Any, Optional, Or, And, Default, Use
# from cnetconf import testmodel
import parsergen as pg
from parsergen import oper_fill
from .tests import test_show_platform_mrkup_package


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match


class ShowVersionSchema(MetaParser):
    schema = {'platform':
                  {'reason': str,
                   'system_version': str,
                   'os': str,
                   'hardware':
                      {'bootflash': str,
                      'chassis': str,
                      'cpu': str,
                      'device_name': str,
                      'memory': str,
                      'model': str,
                      'processor_board_id': str,
                      'slots': str},
                  'kernel_uptime':
                      {'days': str,
                      'hours': str,
                      'minutes': str,
                      'seconds': str},
                  'software':
                      {'bios': str,
                      'bios_compile_time': str,
                      'kickstart': str,
                      'kickstart_compile_time': str,
                      'kickstart_image_file': str,
                      'system': str,
                      'system_compile_time': str,
                      'system_image_file': str}
                  }
              }

class ShowVersion(ShowVersionSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show version'.format()
        self.device.execute(cmd)

        attrValPairsToParse = [
          ('show.version.platform', 'Nexus'),
        ]

        pgfill = oper_fill (
                  self.device,
                  ('show_version'),
                  attrValPairsToParse,
                  refresh_cache=True,
                  regex_tag_fill_pattern='show\.version',
                  skip=True)

        result = pgfill.parse()
        out = pg.ext_dictio[self.device.name]
        version_dict = {}

        if 'platform' not in version_dict:
            version_dict['platform'] = {}

        if 'hardware' not in version_dict['platform']:
            version_dict['platform']['hardware'] = {}
        version_dict['platform']['hardware']['bootflash'] = out['show.version.bootflash']
        version_dict['platform']['hardware']['chassis'] = out['show.version.chassis']
        version_dict['platform']['hardware']['cpu'] = out['show.version.cpu']
        version_dict['platform']['hardware']['device_name'] = out['show.version.device_name']
        version_dict['platform']['hardware']['memory'] = out['show.version.memory']
        version_dict['platform']['hardware']['model'] = out['show.version.model']
        version_dict['platform']['hardware']['processor_board_id'] = out['show.version.processor_board_id']
        version_dict['platform']['hardware']['slots'] = out['show.version.slots']

        if 'kernel_uptime' not in version_dict['platform']:
            version_dict['platform']['kernel_uptime'] = {}
        version_dict['platform']['kernel_uptime']['days'] = out['show.version.days']
        version_dict['platform']['kernel_uptime']['hours'] = out['show.version.hours']
        version_dict['platform']['kernel_uptime']['minutes'] = out['show.version.minutes']
        version_dict['platform']['kernel_uptime']['seconds'] = out['show.version.seconds']

        version_dict['platform']['reason'] = out['show.version.reason']

        if 'software' not in version_dict['platform']:
            version_dict['platform']['software'] = {}
        version_dict['platform']['software']['bios'] = out['show.version.bios']
        version_dict['platform']['software']['bios_compile_time'] = out['show.version.bios_compile_time']
        version_dict['platform']['software']['kickstart'] = out['show.version.kickstart']
        version_dict['platform']['software']['kickstart_compile_time'] = out['show.version.kickstart_compile_time']
        version_dict['platform']['software']['kickstart_image_file'] = out['show.version.kickstart_image_file']
        version_dict['platform']['software']['system'] = out['show.version.system']
        version_dict['platform']['software']['system_compile_time'] = out['show.version.system_compile_time']
        version_dict['platform']['software']['system_image_file'] = out['show.version.system_image_file']

        version_dict['platform']['system_version'] = out['show.version.system_version']
        version_dict['platform']['os'] = out['show.version.os']

        return version_dict

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle, 
                                      exec='show version | xml')
        result = tcl.cast_any(output[1])

        # transform the parser output to compliance with CLI version
        result.update({'cmp':{'module':{'*':{'bios_compile_time':'',
                                             'bios_version':'',
                                             'image_compile_time':'',
                                             'image_version':'',
                                             'status':'',}}}})
        return result

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        base = testmodel.BaseTest()
        base.connect_netconf()

        netconf_request = """
          <rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
            <get>
              <filter>
                <native xmlns="">
                    <version>
                    </version>
                </native>
              </filter>
            </get>
          </rpc>
        """
        
        netconf_request += "\n##\n"
        ncout = base.netconf.send_config(netconf_request)
        
        #    ### XML output from yang
        #    <ns0:rpc-reply xmlns:ns0="urn:ietf:params:xml:ns:netconf:base:1.0" 
        #    xmlns:ns1="urn:ios" message-id="101"><ns0:data><ns1:native>
        #    ....
        #    </ns1:native></ns0:data></ns0:rpc-reply>
        
        filtered_result = xmltodict.parse(ncout, 
                                          process_namespaces=True,
                                          namespaces={
                            'urn:ietf:params:xml:ns:netconf:base:1.0':None,
                            'urn:ios':None,'urn:iosxr':None,'urn:nxos':None,})
        partial_result = dict(
                            filtered_result['rpc-reply']['data'].get('native'))
        # to satisfy the schema, need to complete the dict by merging cli output
        result = self.cli()
        result.update(partial_result)
        return result

class ShowInventorySchema(MetaParser):
    schema = {'name':
                {Any():
                    {'description': str,
                     'slot': str,
                     'pid': str,
                     'vid': str,
                     'serial_number': str}
                },
            }


class ShowInventory(ShowInventorySchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show inventory'.format()
        out = self.device.execute(cmd)
        inventory_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*NAME: +\"(?P<name>[a-zA-Z\s]+)(?P<slot>[0-9]+)?\"\, +DESCR: +\"(?P<description>[a-zA-Z0-9\-\/\s()]+)\"$')
            m = p1.match(line)
            if m:
                name = m.groupdict()['name']
                slot_number = m.groupdict()['slot']
                if slot_number:
                    name += slot_number
                else:
                    slot_number = 'None'
                description = m.groupdict()['description']
                if 'name' not in inventory_dict:
                    inventory_dict['name'] = {}
                if name not in inventory_dict['name']:
                    inventory_dict['name'][name] = {}
                inventory_dict['name'][name]['description'] = description
                inventory_dict['name'][name]['slot'] = slot_number
                continue

            p2 = re.compile(r'^\s*PID: +(?P<pid>[a-zA-z0-9\-\.]+) +\, +VID: +(?P<vid>[A-Z0-9\/]+) +\, +SN: +(?P<serial_number>[A-Z0-9\/]+)$')
            m = p2.match(line)
            if m:
                inventory_dict['name'][name]['pid'] = m.groupdict()['pid']
                inventory_dict['name'][name]['vid'] = m.groupdict()['vid']
                inventory_dict['name'][name]['serial_number'] = m.groupdict()['serial_number']
                continue

        return inventory_dict

class ShowInstallActiveSchema(MetaParser):
    schema = {'boot_images':
                {'kickstart_image': str,
                 'system_image': str},
              'active_packages':
                {Any():
                  {'active_package_name': str}
                },
              }


class ShowInstallActive(ShowInstallActiveSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show install active'.format()
        out = self.device.execute(cmd)
        active_dict = {}
        active_package_module_number = 0
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Boot Images:$')
            m = p1.match(line)
            if m:
                if 'Boot Images' not in active_dict:
                    active_dict['boot_images'] = {}
                continue

            p2 = re.compile(r'^\s*Kickstart Image: +(?P<kickstart_image>[a-zA-z0-9\:\/\-\.]+)$')
            m = p2.match(line)
            if m:
                active_dict['boot_images']['kickstart_image'] = m.groupdict()['kickstart_image']
                continue

            p3 = re.compile(r'^\s*System Image: +(?P<system_image>[a-zA-z0-9\:\/\-\.]+)$')
            m = p3.match(line)
            if m:
                active_dict['boot_images']['system_image'] = m.groupdict()['system_image']
                continue

            p4 = re.compile(r'^\s*Active Packages:$')
            m = p4.match(line)
            if m:
                if 'active_packages' not in active_dict:
                    active_dict['active_packages'] = {}
                continue

            p5 = re.compile(r'^\s*Active Packages on Module #(?P<module_number>[0-9]+):$')
            m = p5.match(line)
            if m:
                active_package_module_number = m.groupdict()['module_number']
                if 'active_packages' not in active_dict:
                    active_dict['active_packages'] = {}
                continue

            p6 = re.compile(r'^\s*(?P<active_package_name>[a-zA-z0-9\-\.]+)$')
            m = p6.match(line)
            if m:
                module_number = 'active_package_module_' + str(active_package_module_number)
                if module_number not in active_dict['active_packages']:
                    active_dict['active_packages'][module_number] = {}
                active_dict['active_packages'][module_number]['active_package_name'] = m.groupdict()['active_package_name']
                continue

        return active_dict

class ShowSystemRedundancyStatusSchema(MetaParser):
    schema = {'redundancy_mode':
                  {'administrative': str,
                   'operational': str},
              'supervisor_1':
                  {'redundancy_state': str,
                   'supervisor_state': str,
                   'internal_state':str},
              'supervisor_2':
                  {'redundancy_state': str,
                   'supervisor_state': str,
                   'internal_state':str},
            }


class ShowSystemRedundancyStatus(ShowSystemRedundancyStatusSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show system redundancy status'.format()
        out = self.device.execute(cmd)
        redundancy_dict = {}
        sup_number = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Redundancy mode$')
            m = p1.match(line)
            if m:
                if 'redundancy_mode' not in redundancy_dict:
                    redundancy_dict['redundancy_mode'] = {}
                continue

            p2 = re.compile(r'^\s*administrative: +(?P<administrative>[a-zA-z\s]+)$')
            m = p2.match(line)
            if m:
                redundancy_dict['redundancy_mode']['administrative'] = m.groupdict()['administrative']
                continue

            p3 = re.compile(r'^\s*operational: +(?P<operational>[a-zA-z\s]+)$')
            m = p3.match(line)
            if m:
                redundancy_dict['redundancy_mode']['operational'] = m.groupdict()['operational']
                continue

            p4 = re.compile(r'^\s*This supervisor \(sup-1\)$')
            m = p4.match(line)
            if m:
                sup_number = 'sup-1'
                if 'supervisor_1' not in redundancy_dict:
                    redundancy_dict['supervisor_1'] = {}
                continue

            p5 = re.compile(r'^\s*Other supervisor \(sup-2\)$')
            m = p5.match(line)
            if m:
                sup_number = 'sup-2'
                if 'supervisor_2' not in redundancy_dict:
                    redundancy_dict['supervisor_2'] = {}
                continue

            p6 = re.compile(r'^\s*Redundancy state: +(?P<redundancy_state>[a-zA-z\s]+)$')
            m = p6.match(line)
            if m:
                if sup_number is 'sup-1':
                  redundancy_dict['supervisor_1']['redundancy_state'] = m.groupdict()['redundancy_state']
                elif sup_number is 'sup-2':
                  redundancy_dict['supervisor_2']['redundancy_state'] = m.groupdict()['redundancy_state']
                continue

            p7 = re.compile(r'^\s*Supervisor state: +(?P<supervisor_state>[a-zA-z\s]+)$')
            m = p7.match(line)
            if m:
                if sup_number is 'sup-1':
                  redundancy_dict['supervisor_1']['supervisor_state'] = m.groupdict()['supervisor_state']
                elif sup_number is 'sup-2':
                  redundancy_dict['supervisor_2']['supervisor_state'] = m.groupdict()['supervisor_state']
                continue

            p8 = re.compile(r'^\s*Internal state: +(?P<internal_state>[a-zA-z\s]+)$')
            m = p8.match(line)
            if m:
                if sup_number is 'sup-1':
                  redundancy_dict['supervisor_1']['internal_state'] = m.groupdict()['internal_state']
                elif sup_number is 'sup-2':
                  redundancy_dict['supervisor_2']['internal_state'] = m.groupdict()['internal_state']
                continue

        return redundancy_dict

class ShowRedundancyStatusSchema(MetaParser):
    schema = {'redundancy_mode':
                  {'administrative': str,
                   'operational': str},
              'supervisor_1':
                  {'redundancy_state': str,
                   'supervisor_state': str,
                   'internal_state':str},
              'supervisor_2':
                  {'redundancy_state': str,
                   'supervisor_state': str,
                   'internal_state':str},
              'system_start_time': str,
              'system_uptime': str,
              'kernel_uptime': str,
              'active_supervisor_time': str}


class ShowRedundancyStatus(ShowRedundancyStatusSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show redundancy status'.format()
        out = self.device.execute(cmd)
        redundancy_dict = {}
        sup_number = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Redundancy mode$')
            m = p1.match(line)
            if m:
                if 'redundancy_mode' not in redundancy_dict:
                    redundancy_dict['redundancy_mode'] = {}
                continue

            p2 = re.compile(r'^\s*administrative: +(?P<administrative>[a-zA-z\s]+)$')
            m = p2.match(line)
            if m:
                redundancy_dict['redundancy_mode']['administrative'] = m.groupdict()['administrative']
                continue

            p3 = re.compile(r'^\s*operational: +(?P<operational>[a-zA-z\s]+)$')
            m = p3.match(line)
            if m:
                redundancy_dict['redundancy_mode']['operational'] = m.groupdict()['operational']
                continue

            p4 = re.compile(r'^\s*This supervisor \(sup-1\)$')
            m = p4.match(line)
            if m:
                sup_number = 'sup-1'
                if 'supervisor_1' not in redundancy_dict:
                    redundancy_dict['supervisor_1'] = {}
                continue

            p5 = re.compile(r'^\s*Other supervisor \(sup-2\)$')
            m = p5.match(line)
            if m:
                sup_number = 'sup-2'
                if 'supervisor_2' not in redundancy_dict:
                    redundancy_dict['supervisor_2'] = {}
                continue

            p6 = re.compile(r'^\s*Redundancy state: +(?P<redundancy_state>[a-zA-z\s]+)$')
            m = p6.match(line)
            if m:
                if sup_number is 'sup-1':
                  redundancy_dict['supervisor_1']['redundancy_state'] = m.groupdict()['redundancy_state']
                elif sup_number is 'sup-2':
                  redundancy_dict['supervisor_2']['redundancy_state'] = m.groupdict()['redundancy_state']
                continue

            p7 = re.compile(r'^\s*Supervisor state: +(?P<supervisor_state>[a-zA-z\s]+)$')
            m = p7.match(line)
            if m:
                if sup_number is 'sup-1':
                  redundancy_dict['supervisor_1']['supervisor_state'] = m.groupdict()['supervisor_state']
                elif sup_number is 'sup-2':
                  redundancy_dict['supervisor_2']['supervisor_state'] = m.groupdict()['supervisor_state']
                continue

            p8 = re.compile(r'^\s*Internal state: +(?P<internal_state>[a-zA-z\s]+)$')
            m = p8.match(line)
            if m:
                if sup_number is 'sup-1':
                  redundancy_dict['supervisor_1']['internal_state'] = m.groupdict()['internal_state']
                elif sup_number is 'sup-2':
                  redundancy_dict['supervisor_2']['internal_state'] = m.groupdict()['internal_state']
                continue

            p9 = re.compile(r'^\s*System start time: +(?P<system_start_time>[a-zA-z0-9\:\s]+)$')
            m = p9.match(line)
            if m:
                redundancy_dict['system_start_time'] = m.groupdict()['system_start_time']
                continue

            p10 = re.compile(r'^\s*System uptime: +(?P<system_uptime>[a-zA-z0-9\:\,\s]+)$')
            m = p10.match(line)
            if m:
                redundancy_dict['system_uptime'] = m.groupdict()['system_uptime']
                continue

            p11 = re.compile(r'^\s*Kernel uptime: +(?P<kernel_uptime>[a-zA-z0-9\:\,\s]+)$')
            m = p11.match(line)
            if m:
                redundancy_dict['kernel_uptime'] = m.groupdict()['kernel_uptime']
                continue

            p12 = re.compile(r'^\s*Active supervisor uptime: +(?P<active_supervisor_time>[a-zA-z0-9\:\,\s]+)$')
            m = p12.match(line)
            if m:
                redundancy_dict['active_supervisor_time'] = m.groupdict()['active_supervisor_time']
                continue

        return redundancy_dict


class ShowBootSchema(MetaParser):
    schema = {'current_boot_variable':
                  {Optional('sup_number'):
                      {Optional(Any()):
                          {'kickstart_variable': str,
                           'system_variable': str,
                           'boot_poap':str}
                      },
                  Optional('kickstart_variable'): str,
                  Optional('system_variable'): str,
                  Optional('boot_poap'):str},
              'next_reload_boot_variable':
                  {Optional('sup_number'):
                      {Optional(Any()):
                          {'kickstart_variable': str,
                           'system_variable': str,
                           'boot_poap':str}
                      },
                  Optional('kickstart_variable'): str,
                  Optional('system_variable'): str,
                  Optional('boot_poap'):str}
              }

class ShowBoot(ShowBootSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show boot'.format()
        out = self.device.execute(cmd)
        boot_dict = {}
        boot_variable = None
        sup_number = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Current Boot Variables:$')
            m = p1.match(line)
            if m:
                boot_variable = 'current'
                if 'current_boot_variable' not in boot_dict:
                    boot_dict['current_boot_variable'] = {}
                continue

            p2 = re.compile(r'^\s*Boot Variables on next reload:$')
            m = p2.match(line)
            if m:
                boot_variable = 'next'
                if 'next_reload_boot_variable' not in boot_dict:
                    boot_dict['next_reload_boot_variable'] = {}
                continue

            p3 = re.compile(r'^\s*sup-1$')
            m = p3.match(line)
            if m:
                sup_number = 'sup-1'
                if boot_variable is 'current':
                    if 'sup_number' not in boot_dict['current_boot_variable']:
                        boot_dict['current_boot_variable']['sup_number'] = {}
                    if 'sup-1' not in boot_dict['current_boot_variable']['sup_number']:
                        boot_dict['current_boot_variable']['sup_number']['sup-1'] = {}
                elif boot_variable is 'next':
                    if 'sup_number' not in boot_dict['next_reload_boot_variable']:
                        boot_dict['next_reload_boot_variable']['sup_number'] = {}
                    if 'sup-1' not in boot_dict['next_reload_boot_variable']['sup_number']:
                        boot_dict['next_reload_boot_variable']['sup_number']['sup-1'] = {}
                continue

            p4 = re.compile(r'^\s*sup-2$')
            m = p4.match(line)
            if m:
                sup_number = 'sup-2'
                if boot_variable is 'current':
                    if 'sup_number' not in boot_dict['current_boot_variable']:
                        boot_dict['current_boot_variable']['sup_number'] = {}
                    if 'sup-2' not in boot_dict['current_boot_variable']['sup_number']:
                        boot_dict['current_boot_variable']['sup_number']['sup-2'] = {}
                elif boot_variable is 'next':
                    if 'sup_number' not in boot_dict['next_reload_boot_variable']:
                        boot_dict['next_reload_boot_variable']['sup_number'] = {}
                    if 'sup-2' not in boot_dict['next_reload_boot_variable']['sup_number']:
                        boot_dict['next_reload_boot_variable']['sup_number']['sup-2'] = {}
                continue


            p5 = re.compile(r'^\s*kickstart variable = +(?P<kickstart_variable>[a-zA-z0-9\:\-\.\/\s]+)$')
            m = p5.match(line)
            if m:
                if boot_variable is 'current':
                    if sup_number:
                        if sup_number is 'sup-1':
                            boot_dict['current_boot_variable']['sup_number']['sup-1']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                        elif sup_number is 'sup-2':
                            boot_dict['current_boot_variable']['sup_number']['sup-2']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                    else:
                        boot_dict['current_boot_variable']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                elif boot_variable is 'next':
                    if sup_number:
                        if sup_number is 'sup-1':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-1']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                        elif sup_number is 'sup-2':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-2']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                    else:
                        boot_dict['next_reload_boot_variable']['kickstart_variable'] = m.groupdict()['kickstart_variable']
                continue

            p6 = re.compile(r'^\s*system variable = +(?P<system_variable>[a-zA-z0-9\:\-\.\/\s]+)$')
            m = p6.match(line)
            if m:
                if boot_variable is 'current':
                    if sup_number:
                        if sup_number is 'sup-1':
                            boot_dict['current_boot_variable']['sup_number']['sup-1']['system_variable'] = m.groupdict()['system_variable']
                        elif sup_number is 'sup-2':
                            boot_dict['current_boot_variable']['sup_number']['sup-2']['system_variable'] = m.groupdict()['system_variable']
                    else:
                        boot_dict['current_boot_variable']['system_variable'] = m.groupdict()['system_variable']
                elif boot_variable is 'next':
                    if sup_number:
                        if sup_number is 'sup-1':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-1']['system_variable'] = m.groupdict()['system_variable']
                        elif sup_number is 'sup-2':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-2']['system_variable'] = m.groupdict()['system_variable']
                    else:
                        boot_dict['next_reload_boot_variable']['system_variable'] = m.groupdict()['system_variable']
                continue

            p7 = re.compile(r'^\s*Boot POAP +(?P<boot_poap>[a-zA-z]+)$')
            m = p7.match(line)
            if m:
                if boot_variable is 'current':
                    if sup_number:
                        if sup_number is 'sup-1':
                            boot_dict['current_boot_variable']['sup_number']['sup-1']['boot_poap'] = m.groupdict()['boot_poap']
                        elif sup_number is 'sup-2':
                            boot_dict['current_boot_variable']['sup_number']['sup-2']['boot_poap'] = m.groupdict()['boot_poap']
                    else:
                        boot_dict['current_boot_variable']['boot_poap'] = m.groupdict()['boot_poap']
                elif boot_variable is 'next':
                    if sup_number:
                        if sup_number is 'sup-1':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-1']['boot_poap'] = m.groupdict()['boot_poap']
                        elif sup_number is 'sup-2':
                            boot_dict['next_reload_boot_variable']['sup_number']['sup-2']['boot_poap'] = m.groupdict()['boot_poap']
                    else:
                        boot_dict['next_reload_boot_variable']['boot_poap'] = m.groupdict()['boot_poap']
                continue

        return boot_dict

class ShowModuleSchema(MetaParser):

    schema = {'slot':
                  {'rp':
                    {Any():
                      {Any():
                        {'ports': str,
                         'model': str,
                         'status': str,
                         'software': str,
                         'hardware': str,
                         'mac_address': str,
                         'serial_number': str,
                         'online_diag_status': str,
                         Optional('world_wide_name'): str}
                      },
                    },
                   'lc':
                    {Any():
                      {Any():
                        {'ports': str,
                         'model': str,
                         'status': str,
                         'software': str,
                         'hardware': str,
                         'mac_address': str,
                         'serial_number': str,
                         'online_diag_status': str,
                         Optional('world_wide_name'): str}
                      },
                    }
                  },
              'xbar':
                  {Any():
                      {'ports': str,
                       'module_type': str,
                       'model': str,
                       'status': str,
                       'software': str,
                       'hardware': str,
                       'mac_address': str,
                       'serial_number': str}
                  },
              }

class ShowModule(ShowModuleSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show module'.format()
        out = self.device.execute(cmd)
        module_dict = {}
        table_header = None
        header_type = None
        rp_list = []
        map_dic = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Mod.*$')
            m = p1.match(line)
            if m:
                table_header = 'slot'
                if 'slot' not in module_dict:
                    module_dict['slot'] = {}
                continue

            p2 = re.compile(r'^\s*Xbar.*$')
            m = p2.match(line)
            if m:
                table_header = 'xbar'
                if 'xbar' not in module_dict:
                    module_dict['xbar'] = {}
                continue

            p3 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<ports>[0-9]+) +(?P<module_type>[a-zA-Z0-9\/\-\s]+) +(?P<model>[a-zA-Z0-9\-]+) +(?P<status>[a-zA-Z\-\s]+) ?\*?$')
            m = p3.match(line)
            if m:
                header_number = m.groupdict()['number']
                module_type = m.groupdict()['module_type']
                if 'Supervisor' in module_type:
                  header_type = 'rp'
                  if header_type not in module_dict['slot']:
                      module_dict['slot'][header_type] = {}
                  rp_list.append(header_number)
                  rp_name =  m.groupdict()['module_type'].strip()
                  map_dic[header_number] = rp_name
                else:
                  header_type = 'lc'
                  if header_type not in module_dict['slot']:
                      module_dict['slot'][header_type] = {}
                  lc_name =  m.groupdict()['module_type'].strip()
                  map_dic[header_number] = lc_name
                if table_header is 'slot':
                    if header_number in rp_list:
                        if header_number not in module_dict['slot']['rp']:
                            module_dict['slot']['rp'][header_number] = {}
                        if rp_name not in module_dict['slot']['rp'][header_number]:
                            module_dict['slot']['rp'][header_number][rp_name] = {}
                        module_dict['slot']['rp'][header_number][rp_name]['ports'] = m.groupdict()['ports'].strip()
                        module_dict['slot']['rp'][header_number][rp_name]['model'] = m.groupdict()['model'].strip()
                        module_dict['slot']['rp'][header_number][rp_name]['status'] = m.groupdict()['status'].strip()
                    else:
                        if header_number not in module_dict['slot']['lc']:
                            module_dict['slot']['lc'][header_number] = {}
                        if lc_name not in module_dict['slot']['lc'][header_number]:
                            module_dict['slot']['lc'][header_number][lc_name] = {}
                        module_dict['slot']['lc'][header_number][lc_name]['ports'] = m.groupdict()['ports'].strip()
                        module_dict['slot']['lc'][header_number][lc_name]['model'] = m.groupdict()['model'].strip()
                        module_dict['slot']['lc'][header_number][lc_name]['status'] = m.groupdict()['status'].strip()
                elif table_header is 'xbar':
                    if header_number not in module_dict['xbar']:
                        module_dict['xbar'][header_number] = {}
                    module_dict['xbar'][header_number]['ports'] = m.groupdict()['ports'].strip()
                    module_dict['xbar'][header_number]['module_type'] = m.groupdict()['module_type'].strip()
                    module_dict['xbar'][header_number]['model'] = m.groupdict()['model'].strip()
                    module_dict['xbar'][header_number]['status'] = m.groupdict()['status'].strip()
                continue

            p4 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<software>[A-Z0-9\(\)\.]+) +(?P<hardware>[0-9\.]+)( +)?(?P<world_wide_name>[\-]+)?$')
            m = p4.match(line)
            if m:
                header_number = m.groupdict()['number']
                world_wide_name = m.groupdict()['world_wide_name']
                if table_header is 'slot':
                    if header_number in rp_list:
                        rp_name = map_dic[header_number]
                        module_dict['slot']['rp'][header_number][rp_name]['software'] = m.groupdict()['software'].strip()
                        module_dict['slot']['rp'][header_number][rp_name]['hardware'] = m.groupdict()['hardware'].strip()
                    else:
                        lc_name = map_dic[header_number]
                        module_dict['slot']['lc'][header_number][lc_name]['software'] = m.groupdict()['software'].strip()
                        module_dict['slot']['lc'][header_number][lc_name]['hardware'] = m.groupdict()['hardware'].strip()
                    if world_wide_name:
                        if header_number in rp_list:
                            module_dict['slot']['rp'][header_number][rp_name]['world_wide_name'] = m.groupdict()['world_wide_name'].strip()
                        else:
                            module_dict['slot']['lc'][header_number][lc_name]['world_wide_name'] = m.groupdict()['world_wide_name'].strip()
                elif table_header is 'xbar':
                    module_dict['xbar'][header_number]['software'] = m.groupdict()['software'].strip()
                    module_dict['xbar'][header_number]['hardware'] = m.groupdict()['hardware'].strip()
                    if world_wide_name:
                        module_dict['xbar'][header_number]['world_wide_name'] = m.groupdict()['world_wide_name']
                continue

            p5 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<mac_address>[a-zA-Z0-9\.\-\s]+) +(?P<serial_number>[A-Z0-9]+)$')
            m = p5.match(line)
            if m:
                header_number = m.groupdict()['number']
                if table_header is 'slot':
                    if header_number in rp_list:
                        rp_name = map_dic[header_number]
                        module_dict['slot']['rp'][header_number][rp_name]['mac_address'] = m.groupdict()['mac_address'].strip()
                        module_dict['slot']['rp'][header_number][rp_name]['serial_number'] = m.groupdict()['serial_number'].strip()
                    else:
                        lc_name = map_dic[header_number]
                        module_dict['slot']['lc'][header_number][lc_name]['mac_address'] = m.groupdict()['mac_address'].strip()
                        module_dict['slot']['lc'][header_number][lc_name]['serial_number'] = m.groupdict()['serial_number'].strip()
                elif table_header is 'xbar':
                    module_dict['xbar'][header_number]['mac_address'] = m.groupdict()['mac_address'].strip()
                    module_dict['xbar'][header_number]['serial_number'] = m.groupdict()['serial_number'].strip()
                continue

            p6 = re.compile(r'^\s*(?P<number>[0-9]+) +(?P<online_diag_status>[a-zA-Z]+)$')
            m = p6.match(line)
            if m:
                header_number = m.groupdict()['number']
                if header_number in rp_list:
                    rp_name = map_dic[header_number]
                    module_dict['slot']['rp'][header_number][rp_name]['online_diag_status'] = m.groupdict()['online_diag_status'].strip()
                else:
                    lc_name = map_dic[header_number]
                    module_dict['slot']['lc'][header_number][lc_name]['online_diag_status'] = m.groupdict()['online_diag_status'].strip()
                continue

        return module_dict

class DirSchema(MetaParser):
    schema = {'disk_used_space': str,
              'disk_free_space': str,
              'disk_total_space': str,
              'dir': str,
              'files':
                  {Any():
                      {'size': str,
                       'date': str,
                       'time': str}
                  },
              }

class Dir(DirSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'dir'.format()
        out = self.device.execute(cmd)
        dir_dict = {}
        file = None
        disk_type = None
        date = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*(?P<size>[0-9]+) +(?P<month>[a-zA-Z]+) +(?P<day>[0-9]+) +(?P<time>[0-9\:]+) +(?P<year>[0-9]+) +(?P<file>[a-zA-Z0-9\.\/\_\-\+]+)$')
            m = p1.match(line)
            if m:
                file = m.groupdict()['file']
                date = m.groupdict()['month'].strip() + ' ' + m.groupdict()['day'].strip() + ' ' + m.groupdict()['year'].strip()
                if 'files' not in dir_dict:
                    dir_dict['files'] = {}
                dir_dict['files'][file] = {}
                dir_dict['files'][file]['size'] = m.groupdict()['size']
                dir_dict['files'][file]['time'] = m.groupdict()['time']
                dir_dict['files'][file]['date'] = date
                continue

            p2 = re.compile(r'^\s*(?P<disk_space>[0-9]+) bytes +(?P<type>[a-z]+)$')
            m = p2.match(line)
            if m:
                disk_type = m.groupdict()['type']
                if disk_type == 'used':
                    dir_dict['disk_used_space'] = m.groupdict()['disk_space']
                if disk_type == 'free':
                    dir_dict['disk_free_space'] = m.groupdict()['disk_space']
                if disk_type == 'total':
                    dir_dict['disk_total_space'] = m.groupdict()['disk_space']
                continue

            p3 = re.compile(r'^\s*Usage +for +(?P<directory_name>[a-z\:]+).*$')
            m = p3.match(line)
            if m:
                dir_dict['dir'] = m.groupdict()['directory_name']
                continue

        return dir_dict

class ShowVdcDetailSchema(MetaParser):
    schema = {'vdc':
                {Any():
                  {'name': str,
                  'state': str,
                  'mac_address': str,
                  'ha_policy': str,
                  'dual_sup_ha_policy': str,
                  'boot_order': str,
                  Optional('cpu_share'): str,
                  Optional('cpu_share_percentage'): str,
                  'create_time': str,
                  'reload_count': str,
                  Optional('uptime'): str,
                  'restart_count': str,
                  Optional('restart_time'): str,
                  'type': str,
                  'supported_linecards': str}
                },
            }

class ShowVdcDetail(ShowVdcDetailSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show vdc detail'.format()
        out = self.device.execute(cmd)
        vdc_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Switchwide +mode +is +.*$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*vdc +id: +(?P<id>[0-9]+)$')
            m = p2.match(line)
            if m:
                identity = m.groupdict()['id']
                if 'vdc' not in vdc_dict:
                    vdc_dict['vdc'] = {}
                if identity not in vdc_dict['vdc']:
                    vdc_dict['vdc'][identity] = {}
                continue

            p2 = re.compile(r'^\s*vdc +name: +(?P<name>[a-zA-Z0-9\-]+)$')
            m = p2.match(line)
            if m:
                vdc_dict['vdc'][identity]['name'] = m.groupdict()['name']
                continue

            p3 = re.compile(r'^\s*vdc +state: +(?P<state>[a-z]+)$')
            m = p3.match(line)
            if m:
                vdc_dict['vdc'][identity]['state'] = m.groupdict()['state']
                continue

            p4 = re.compile(r'^\s*vdc +mac +address: +(?P<mac>[a-z0-9\:]+)$')
            m = p4.match(line)
            if m:
                vdc_dict['vdc'][identity]['mac_address'] = m.groupdict()['mac']
                continue

            p5 = re.compile(r'^\s*vdc +ha +policy: +(?P<policy>[A-Z]+)$')
            m = p5.match(line)
            if m:
                vdc_dict['vdc'][identity]['ha_policy'] = m.groupdict()['policy']
                continue

            p6 = re.compile(r'^\s*vdc +dual-sup +ha +policy: +(?P<dual_policy>[A-Z]+)$')
            m = p6.match(line)
            if m:
                vdc_dict['vdc'][identity]['dual_sup_ha_policy'] = m.groupdict()['dual_policy']
                continue

            p7 = re.compile(r'^\s*vdc +boot +Order: +(?P<boot_order>[0-9]+)$')
            m = p7.match(line)
            if m:
                vdc_dict['vdc'][identity]['boot_order'] = m.groupdict()['boot_order']
                continue

            p8 = re.compile(r'^\s*CPU +Share: +(?P<cpu_share>[0-9]+)$')
            m = p8.match(line)
            if m:
                vdc_dict['vdc'][identity]['cpu_share'] = m.groupdict()['cpu_share']
                continue

            p9 = re.compile(r'^\s*CPU +Share +Percentage: +(?P<cpu_share_percentage>[0-9\%]+)$')
            m = p9.match(line)
            if m:
                vdc_dict['vdc'][identity]['cpu_share_percentage'] = m.groupdict()['cpu_share_percentage']
                continue

            p10 = re.compile(r'^\s*vdc +create +time: +(?P<vdc_create_time>[a-zA-Z0-9\:\s]+)$')
            m = p10.match(line)
            if m:
                vdc_dict['vdc'][identity]['create_time'] = m.groupdict()['vdc_create_time']
                continue

            p11 = re.compile(r'^\s*vdc +reload +count: +(?P<reload_count>[0-9]+)$')
            m = p11.match(line)
            if m:
                vdc_dict['vdc'][identity]['reload_count'] = m.groupdict()['reload_count']
                continue

            p12 = re.compile(r'^\s*vdc +uptime: +(?P<uptime>[a-z0-9\(\)\s\,]+)$')
            m = p12.match(line)
            if m:
                vdc_dict['vdc'][identity]['uptime'] = m.groupdict()['uptime']
                continue

            p13 = re.compile(r'^\s*vdc +restart +count: +(?P<count>[0-9]+)$')
            m = p13.match(line)
            if m:
                vdc_dict['vdc'][identity]['restart_count'] = m.groupdict()['count']
                continue

            p14 = re.compile(r'^\s*vdc +restart +time: +(?P<restart_time>[a-zA-Z0-9\:\s]+)$')
            m = p14.match(line)
            if m:
                vdc_dict['vdc'][identity]['restart_time'] = m.groupdict()['restart_time']
                continue

            p15 = re.compile(r'^\s*vdc +type: +(?P<type>[a-zA-Z]+)$')
            m = p15.match(line)
            if m:
                if 'vdc' not in vdc_dict:
                    vdc_dict['vdc'] = {}
                vdc_dict['vdc'][identity]['type'] = m.groupdict()['type']
                continue

            p16 = re.compile(r'^\s*vdc +supported +linecards: +(?P<linecards>[a-zA-Z0-9]+)$')
            m = p16.match(line)
            if m:
                if 'vdc' not in vdc_dict:
                    vdc_dict['vdc'] = {}
                vdc_dict['vdc'][identity]['supported_linecards'] = m.groupdict()['linecards']
                continue

        return vdc_dict

class ShowVdcCurrentSchema(MetaParser):
    schema = {'current_vdc':
                {'id': str,
                 'name': str}
             }

class ShowVdcCurrent(ShowVdcCurrentSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show vdc current-vdc'.format()
        out = self.device.execute(cmd)
        current_vdc_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Current +vdc +is +(?P<id>[0-9]+) +- +(?P<name>[a-zA-Z0-9]+)$')
            m = p1.match(line)
            if m:
                if 'current_vdc' not in current_vdc_dict:
                    current_vdc_dict['current_vdc'] = {}
                current_vdc_dict['current_vdc']['id'] = m.groupdict()['id']
                current_vdc_dict['current_vdc']['name'] = m.groupdict()['name']
                continue

        return current_vdc_dict

class ShowVdcMembershipStatusSchema(MetaParser):

    schema = {'virtual_device':
                {Any():
                    {'membership':
                        {Any():
                            {Any():
                                {'vd_ms_status': str,
                                 'vd_ms_type': str}
                            },
                        },
                    }
                },
            }

class ShowVdcMembershipStatus(ShowVdcMembershipStatusSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show vdc membership status'.format()
        out = self.device.execute(cmd)
        member_status_vdc_dict = {}
        port_type = None
        port_number = None
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Flags : b - breakout port$')
            m = p1.match(line)
            if m:
                if 'virtual_device' not in member_status_vdc_dict:
                    member_status_vdc_dict['virtual_device'] = {}
                continue

            p2 = re.compile(r'^\s*vdc_id: +(?P<id>[0-9]+) +vdc_name: +(?P<name>[a-zA-Z0-9]+) +interfaces:$')
            m = p2.match(line)
            if m:
                identity = m.groupdict()['id']
                vdc_name = m.groupdict()['name']
                if identity not in member_status_vdc_dict['virtual_device']:
                    member_status_vdc_dict['virtual_device'][identity] = {}
                if 'membership' not in member_status_vdc_dict['virtual_device'][identity]:
                    member_status_vdc_dict['virtual_device'][identity]['membership'] = {}
                if vdc_name not in member_status_vdc_dict['virtual_device'][identity]['membership']:
                    member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name] = {}
                continue

            p3 = re.compile(r'^\s*Port +Status$')
            m = p3.match(line)
            if m:
                continue

            p4 = re.compile(r'^\s*(?P<port_type>[a-zA-Z]+)(?P<port_number>[0-9a-z/\\(\)]+) +(?P<status>[A-Z]+)$')
            m = p4.match(line)
            if m:
                port_type = m.groupdict()['port_type']
                port_number = m.groupdict()['port_number']
                port = port_type+port_number
                if port not in member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name]:
                    member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name][port] = {}
                status = m.groupdict()['status']
                if 'Eth' in port_type:
                    port_type = 'Ethernet'      
                member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name][port]['vd_ms_status'] = status
                member_status_vdc_dict['virtual_device'][identity]['membership'][vdc_name][port]['vd_ms_type'] = port_type
                continue

        return member_status_vdc_dict
