"""
Linux parsers for the following commands:

    * 'docker stats --no-stream'
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any

# ========================================================
# Schema for "docker stats --no-stream"
# ========================================================

class DockerStatsNoStreamSchema(MetaParser):
    """Schema for 'docker stats --no-stream'"""

    schema = {
        Any(): {
            "container_id": str,
            "cpu_usage": str,
            "mem_usage": str,
            "mem_limit": str,
            "percent_mem_usage": str,
            "net_input": str,
            "net_output": str,
            "block_input": str,
            "block_output": str,
            "pids": str,
        }
    }


class DockerStatsNoStream(DockerStatsNoStreamSchema):
    """
    Parser for 'docker stats --no-stream' on Linux devices.
    parser class - implements detail parsing mechanisms for cli output.
    """

    cli_command = "docker stats --no-stream"
    """
        CONTAINER ID        NAME                  CPU %               MEM USAGE / LIMIT     MEM %               NET I/O             BLOCK I/O           PIDS
        a3f78cb32a8e        foo-bar               0.06%               55.69MiB / 1.025GiB   5.31%               31.1kB / 0B         0B / 0B             1
        22e23asfcde8        hello-world           0.24%               11.19MiB / 131.2MiB   8.53%               116MB / 96.1MB      0B / 0B             4
        293fdak28c05        awesome_brattai       0.34%               37.08MiB / 131.2MiB   28.26%              0B / 0B             0B / 0B             3
        c5a5saddd210        looking_good          0.25%               30.73MiB / 262.4MiB   11.71%              1.16GB / 837MB      0B / 0B             2
    """

    def cli(self, output: str = None) -> dict:
        if output is None:
            output = self.device.execute(self.cli_command)
        # a3f78cb32a8e        foo-bar               0.06%               55.69MiB / 1.025GiB   5.31%               31.1kB / 0B         0B / 0B             1
        p = re.compile(
            r"^(?P<container_id>\S+)\s+(?P<container_name>\S+)\s+(?P<cpu_usage>\S+)\s+(?P<mem_usage>\S+)\s+\/\s+(?P<mem_limit>\S+)\s+(?P<percent_mem_usage>\S+)\s+(?P<net_input>\S+)\s+\/\s+(?P<net_output>\S+)\s+(?P<block_input>\S+)\s+\/\s+(?P<block_output>\S+)\s+(?P<pids>\d+)$"
        )

        parsed_dict = {}

        for line in output.splitlines():
            line.strip()

            # a3f78cb32a8e        foo-bar               0.06%               55.69MiB / 1.025GiB   5.31%               31.1kB / 0B         0B / 0B             1
            m = p.match(line)
            if m:
                groups = m.groupdict()
                container_id = groups["container_id"]
                container_name = groups["container_name"]
                cpu_usage = groups["cpu_usage"]
                mem_usage = groups["mem_usage"]
                mem_limit = groups["mem_limit"]
                percent_mem_usage = groups["percent_mem_usage"]
                net_input = groups["net_input"]
                net_output = groups["net_output"]
                block_input = groups["block_input"]
                block_output = groups["block_output"]
                pids = groups["pids"]

                container_name_dict = parsed_dict.setdefault(container_name, {})
                container_name_dict["container_id"] = container_id
                container_name_dict["cpu_usage"] = cpu_usage
                container_name_dict["mem_usage"] = mem_usage
                container_name_dict["mem_limit"] = mem_limit
                container_name_dict["percent_mem_usage"] = percent_mem_usage
                container_name_dict["net_input"] = net_input
                container_name_dict["net_output"] = net_output
                container_name_dict["block_input"] = block_input
                container_name_dict["block_output"] = block_output
                container_name_dict["pids"] = pids

        return parsed_dict
