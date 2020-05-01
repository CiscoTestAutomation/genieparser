"""show_task.py

JunOS parsers for the following show commands:
    - 'show task replication'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)


class ShowTaskReplicationSchema(MetaParser):
    """ Schema for:
            * show task replication
    """

    schema = {
    "task-replication-state": {
        "task-gres-state": str,
        "task-re-mode": str
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

        return ret_dict