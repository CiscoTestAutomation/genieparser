
class ShowSystemStorageSchema(MetaParser):
    """ Schema for:
            * show system storage
    """

    """
    schema = {
        "system-storage-information": {
            "filesystem": [
                {
                    "available-blocks": {
                        "#text": str
                    },
                    "filesystem-name": str,
                    "mounted-on": str,
                    "total-blocks": {
                        "#text": str
                    },
                    "used-blocks": {
                        "#text": str
                    },
                    "used-percent": str
                }
            ]
        }
    }
    """

    # Sub Schema filesystem
    def validate_filesystem_list(value):
        # Pass filesystem list as value
        if not isinstance(value, list):
            raise SchemaTypeError('filesystem is not a list')
        filesystem_schema = Schema(
            {
                "available-blocks": {
                    "junos:format": str
                },
                "filesystem-name": str,
                "mounted-on": str,
                "total-blocks": {
                    Optional("#text"): str,
                    "junos:format": str
                },
                "used-blocks": {
                    "junos:format": str
                },
                "used-percent": str
            })
        # Validate each dictionary in list
        for item in value:
            filesystem_schema.validate(item)
        return value

    schema = {
        "system-storage-information": {
            "filesystem": Use(validate_filesystem_list)
        }
    }

class ShowSystemStorage(ShowSystemStorageSchema):
    """ Parser for:
            * show system storage
    """
    cli_command = 'show system storage'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # /dev/gpt/junos           20G       1.2G        17G        7%  /.mount
        p1 = re.compile(r'^(?P<filesystem_name>\S+) +(?P<total_blocks>\S+) +'
        r'(?P<used_blocks>\S+) +(?P<available_blocks>\S+) +(?P<used_percent>\S+)'
        r' +(?P<mounted_on>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # /dev/gpt/junos           20G       1.2G        17G        7%  /.mount
            m = p1.match(line)
            if m:

                filesystem_list = ret_dict.setdefault("system-storage-information", {})\
                    .setdefault("filesystem", [])

                group = m.groupdict()
                entry = {
                    "available-blocks": {
                        "junos:format": group["available_blocks"]
                    },
                    "filesystem-name": group["filesystem_name"],
                    "mounted-on": group["mounted_on"],
                    "total-blocks": {
                        "junos:format": group["total_blocks"]
                    },
                    "used-blocks": {
                        "junos:format": group["used_blocks"]
                    },
                    "used-percent": group["used_percent"]
                }

                filesystem_list.append(entry)
                continue

        return ret_dict
