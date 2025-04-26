# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, ListOf

# parser utils
from genie.libs.parser.utils.common import Common

# =============================================
# Schema for 'show cce cpdp bindings'
# =============================================

class ShowCceCpdpBindingsSchema(MetaParser):
    """
    Schema for show cce cpdp bindings
    """
    schema = {
        "class_groups": {
            str: {  # Target Class Group ID
                'classes': ListOf({
                    'class_id': str,
                    'class_name': str
                }),
                'features': ListOf(str)
            }
        }
    }

# =============================================
# Parser for 'show cce cpdp bindings'
# =============================================

class ShowCceCpdpBindings(ShowCceCpdpBindingsSchema):
    """Parser for show cce cpdp bindings
    """
    cli_command = 'show cce cpdp bindings'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}
        
        if out:
            ret_dict.setdefault('class_groups', {})
        
        # Target Class Group id 005195C4 (Po2.200):
        p0 = re.compile(r'Target Class Group id\s+(?P<class_group_id>\S+)\s+\((?P<name>[\w\s\.\-]+)\):')
        
        # Class 00509EC1 (epc_class_match_any_IPV6_test)
        p1 = re.compile(r'Class\s+(?P<class_id>\S+)\s+\((?P<class_name>[\w\s\-_]+)\)')
        
        # Feature embedded packet capture
        p2 = re.compile(r'Feature\s+(?P<feature>[\w\s\-_]+)')

        current_class_group = ''
        for line in out.splitlines():
            line = line.strip()
    
            # Target Class Group id 005195C4 (Po2.200):
            m = p0.match(line)
            if m:
                group = m.groupdict()
                current_class_group = group['class_group_id']
                class_group_dict = ret_dict['class_groups'].setdefault(current_class_group, {})
                continue
            
            # Class 00509EC1 (epc_class_match_any_IPV6_test)
            m = p1.match(line)
            if m and current_class_group:                
                group = m.groupdict()
                class_list = class_group_dict.setdefault('classes', [])
                class_list.append({
                    'class_id': group['class_id'],
                    'class_name': group['class_name']
                })
                continue
            
            # Feature embedded packet capture
            m = p2.match(line)
            if m and current_class_group:                
                group = m.groupdict()
                feature_list = class_group_dict.setdefault('features', [])
                feature_list.append(group['feature'].strip())
        
        return ret_dict