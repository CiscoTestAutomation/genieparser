"""show_task.py

JunOS parsers for the following show commands:
    - 'show task replication'
      'show task memory'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema)


class ShowTaskReplicationSchema(MetaParser):
    """ Schema for:
            * show task replication
    """
    # main schema
    schema =  {
        "task-replication-state": {
            "task-gres-state": str,
            Optional("task-protocol-replication-name"): list,
            Optional("task-protocol-replication-state"): list,
            "task-re-mode": str,
        }
    }

class ShowTaskReplication(ShowTaskReplicationSchema):
    """ Parser for:
            * show task replication
    """
    cli_command = 'show task replication'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Stateful Replication: Disabled
        p1 = re.compile(r'^Stateful +Replication: +(?P<task_gres_state>\S+)$')

        # RE mode: Master
        p2 = re.compile(r'^RE +mode: +(?P<task_re_mode>\S+)$')

        # Protocol                Synchronization Status
        # OSPF                    Complete              
        # OSPF3                   Complete              
        # BGP                     Complete  
        p3 = re.compile(r'(?P<name>[A-Z0-6]+)\s+(?P<state>\S+)')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Stateful Replication: Disabled
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("task-replication-state",{})\
                    .setdefault("task-gres-state", group["task_gres_state"])
                continue

            # RE mode: Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault("task-replication-state",{})\
                    .setdefault("task-re-mode", group["task_re_mode"])
                continue
            
            # Protocol                Synchronization Status
            # OSPF                    Complete              
            # BGP                     Complete  
            m = p3.match(line)
            if m:
                group = m.groupdict()
                replication_dict = ret_dict.setdefault("task-replication-state",{})

                if "task-protocol-replication-name" not in replication_dict:
                    replication_dict["task-protocol-replication-name"] = []

                replication_dict["task-protocol-replication-name"].append(group["name"])

                if "task-protocol-replication-state" not in replication_dict:
                    replication_dict["task-protocol-replication-state"] = []

                replication_dict["task-protocol-replication-state"].append(group["state"])    
                continue            

        return ret_dict


class ShowTaskMemorySchema(MetaParser):
    """ Schema for:
            * show task memory
    """

    schema = {
    "task-memory-information": {
        "task-memory-free-size": str,
        "task-memory-in-use-avail": str,
        "task-memory-in-use-size": str,
        "task-memory-max-avail": str,
        "task-memory-max-size": str,
        "task-memory-max-when": str,
        "task-memory-in-use-size-status": str,
        "task-memory-free-size-status": str,
        "task-memory-free-size-avail": str
    }
}

class ShowTaskMemory(ShowTaskMemorySchema):
    """ Parser for:
            * show task memory
    """
    cli_command = 'show task memory'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Currently In Use:        26857          1%  now
        p1 = re.compile(r'Currently +In +Use: +(?P<task_memory_in_use_size>\d+) '
                        r'+(?P<task_memory_in_use_avail>\d+)% +(?P<task_memory_in_use_size_status>\S+)$')

        # Maximum Ever Used:       27300          1%  20/10/01 01:27:19
        p2 = re.compile(r'^Maximum +Ever +Used: +(?P<task_memory_max_size>\d+) '
                        r'+(?P<task_memory_max_avail>\d+)% +(?P<task_memory_max_when>'
                        r'[\d\/\s\:]+)$')

        # Available:             2078171        100%  now
        p3 = re.compile(r'Available: +(?P<task_memory_free_size>\d+) +'
                        r'(?P<task_memory_free_size_avail>\d+)% +'
                        r'(?P<task_memory_free_size_status>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Currently In Use:        26857          1%  now
            m = p1.match(line)
            if m:
                group = m.groupdict()
                task_memory_entry_dict = ret_dict.setdefault("task-memory-information",{})

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    task_memory_entry_dict[entry_key] = group_value
                continue

            # Maximum Ever Used:       27300          1%  20/10/01 01:27:19
            m = p2.match(line)
            if m:
                group = m.groupdict()

                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    task_memory_entry_dict[entry_key] = group_value
                continue

            # Available:             2078171        100%  now
            m = p3.match(line)
            if m:
                group = m.groupdict()
                
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_', '-')
                    task_memory_entry_dict[entry_key] = group_value
                continue

        return ret_dict