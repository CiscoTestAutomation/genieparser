"""starOS implementation of show_boot.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowBootSchema(MetaParser):
    """Schema for show boot"""

    schema = {
        'boot_prio': {
            Any(): {
                'image': str,
                'config': str
            },
        }     
    }


class ShowBoot(ShowBootSchema):
    """Parser for show boot"""

    cli_command = 'show boot'

    """
[local]COR-VPC-1> show boot 
Monday July 11 11:05:31 ART 2022

boot system priority 10 \
    image /flash/qvpc-di-21.19.11.bin \
    config /flash/COR-VPC-1_Production.cfg

boot system priority 20 \
    image /flash/qvpc-di-21.19.11.bin \
    config /flash/COR-VPC-1_Backup.cfg

boot system priority 30 \
    image /flash/staros.bin \
    config /flash/system.cfg
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        boot_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(boot system priority\s(?P<priority>\d+))')
        p1 = re.compile(r'(image\s(?P<image>\S*))')
        p2 = re.compile(r'(config\s(?P<config>\S*))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            #boot sys priority
            if m:
                if 'boot_prio' not in boot_dict:
                    result_dict = boot_dict.setdefault('boot_prio',{})
                prio = m.groupdict()['priority']
                result_dict[prio] = {}
                continue
                
            m = p1.match(line)
            #image
            if m:
                image = m.groupdict()['image']
                result_dict[prio]['image'] = image

            m = p2.match(line)
            #config
            if m:
                config = m.groupdict()['config']
                result_dict[prio]['config'] = config
                continue

        return boot_dict