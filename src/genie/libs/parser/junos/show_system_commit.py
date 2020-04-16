# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use
from genie.metaparser.util.exceptions import SchemaTypeError

class ShowSystemCommitSchema(MetaParser):
    """ Schema for:
            * show sysyem commit
    """

    # Sub Schema commit-history
    def validate_commit_history_list(value):
        # Pass commit-history list as value
        if not isinstance(value, list):
            raise SchemaTypeError('commit-history is not a list')
        commit_history_schema = Schema({
                    "client": str,
                    "date-time": {
                        "#text": str
                    },
                    "sequence-number": str,
                    "user": str
                })
        # Validate each dictionary in list
        for item in value:
            commit_history_schema.validate(item)
        return value

    schema = {
        "commit-information": {
            "commit-history": Use(validate_commit_history_list)
        }
    }

class ShowSystemCommit(ShowSystemCommitSchema):
    """ Parser for:
            * show sysyem commit
    """
    cli_command = 'show system commit'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 0   2020-03-05 16:04:34 UTC by kddi via cli
        p1 = re.compile(r'^(?P<sequence_number>\d+) +(?P<date_time>([\d\-]+) +'
        r'(([\d\:]+)) (\S+)) +by +(?P<user>\S+) +via +(?P<client>\S+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 0   2020-03-05 16:04:34 UTC by kddi via cli
            m = p1.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("commit-information", {})\
                    .setdefault("commit-history", [])
                entry = {}
                entry['client'] = group['client']
                entry['date-time'] = {"#text": group['date_time']}
                entry['sequence-number'] = group['sequence_number']
                entry['user'] = group['user']

                entry_list.append(entry)
                continue

        return ret_dict
