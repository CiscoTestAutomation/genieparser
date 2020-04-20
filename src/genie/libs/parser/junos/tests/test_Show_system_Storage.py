
# =========================================================
# Unit test for show system storage
# =========================================================
class test_show_system_storage(unittest.TestCase):

    device = Device(name="aDevice")

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "system-storage-information": {
            "filesystem": [
                {
                    "available-blocks": {"junos:format": "17G"},
                    "filesystem-name": "/dev/gpt/junos",
                    "mounted-on": "/.mount",
                    "total-blocks": {"junos:format": "20G"},
                    "used-blocks": {"junos:format": "1.2G"},
                    "used-percent": "7%",
                },
                {
                    "available-blocks": {"junos:format": "730M"},
                    "filesystem-name": "/dev/gpt/config",
                    "mounted-on": "/.mount/config",
                    "total-blocks": {"junos:format": "793M"},
                    "used-blocks": {"junos:format": "60K"},
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {"junos:format": "6.3G"},
                    "filesystem-name": "/dev/gpt/var",
                    "mounted-on": "/.mount/var",
                    "total-blocks": {"junos:format": "7.0G"},
                    "used-blocks": {"junos:format": "117M"},
                    "used-percent": "2%",
                },
                {
                    "available-blocks": {"junos:format": "3.2G"},
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/tmp",
                    "total-blocks": {"junos:format": "3.2G"},
                    "used-blocks": {"junos:format": "196K"},
                    "used-percent": "0%",
                },
                {
                    "available-blocks": {"junos:format": "333M"},
                    "filesystem-name": "tmpfs",
                    "mounted-on": "/.mount/mfs",
                    "total-blocks": {"junos:format": "334M"},
                    "used-blocks": {"junos:format": "748K"},
                    "used-percent": "0%",
                },
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value": """
                show system storage | no-more
        Filesystem              Size       Used      Avail  Capacity   Mounted on
        /dev/gpt/junos           20G       1.2G        17G        7%  /.mount
        /dev/gpt/config         793M        60K       730M        0%  /.mount/config
        /dev/gpt/var            7.0G       117M       6.3G        2%  /.mount/var
        tmpfs                   3.2G       196K       3.2G        0%  /.mount/tmp
        tmpfs                   334M       748K       333M        0%  /.mount/mfs
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemStorage(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemStorage(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)
