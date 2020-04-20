
class ShowSystemQueuesSchema(MetaParser):
    """ Schema for:
            * show sysyem queues
    """

    """
        {
        "queues-statistics": {
            "interface-queues-statistics": {
                "interface-queue": [
                    {
                        "max-octets-allowed": str,
                        "max-packets-allowed": str,
                        "name": str,
                        "number-of-queue-drops": str,
                        "octets-in-queue": str,
                        "packets-in-queue": str
                    }
                ]
            },
            "protocol-queues-statistics": {
                "protocol-queue": [
                    {}
                ]
            }
        }
    }
    """

    # Sub Schema interface-queue
    def validate_interface_queue_list(value):
        # Pass interface-queue list as value
        if not isinstance(value, list):
            raise SchemaTypeError('commit-history is not a list')
        interface_queue_schema = Schema({
                    "max-octets-allowed": str,
                        "max-packets-allowed": str,
                        "name": str,
                        "number-of-queue-drops": str,
                        "octets-in-queue": str,
                        "packets-in-queue": str
                })
        # Validate each dictionary in list
        for item in value:
            interface_queue_schema.validate(item)
        return value

    schema = {
        "queues-statistics": {
            "interface-queues-statistics": {
                "interface-queue": Use(validate_interface_queue_list)
            },
            "protocol-queues-statistics": {
                "protocol-queue": Use(validate_interface_queue_list)
            }
        }
    }

class ShowSystemQueues(ShowSystemQueuesSchema):
    """ Parser for:
            * show system queues
    """
    cli_command = 'show system queues'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # lsi                             0        12500        0       41        0
        p1 = re.compile(r'^(?P<name>\S+) +(?P<octets_in_queue>\d+) +(?P<max_octets_allowed>\d+) +(?P<packets_in_queue>\d+) +(?P<max_packets_allowed>\d+) +(?P<number_of_queue_drops>\d+)$')

        # input protocol              bytes          max  packets      max    drops
        p2 = re.compile(r'^input +protocol +bytes +max +packets +max +drops$')

        interface_flag = True
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # lsi                             0        12500        0       41        0
            m = p1.match(line)
            if m:
                group = m.groupdict()

                if interface_flag:
                    entry_list = ret_dict.setdefault("queues-statistics", {}).setdefault("interface-queues-statistics", {}).setdefault("interface-queue", [])
                else:
                    entry_list = ret_dict.setdefault("queues-statistics", {}).setdefault("protocol-queues-statistics", {}).setdefault("protocol-queue", [])

                group = m.groupdict()
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value

                entry_list.append(entry)
                continue

            # input protocol              bytes          max  packets      max    drops
            m = p2.match(line)
            if m:
                interface_flag = False

        return ret_dict

class ShowSystemQueuesNoForwarding(ShowSystemQueues):
    """ Parser for:
            * show system queues no-forwarding
    """
    cli_command = 'show system queues no-forwarding'
