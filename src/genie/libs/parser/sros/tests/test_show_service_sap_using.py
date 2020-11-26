# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# sros show_service_sap_using
from genie.libs.parser.sros.show_service_sap_using import ShowServiceSapUsing

# =================================
# Unit test for 'show service sap-using'
# =================================
class test_show_service_sap_using_session(unittest.TestCase):

    '''Unit test for "show service sap-using"'''

    empty_output = {'execute.return_value': ''}

    # Specify the expected result for the parsed output
    golden_parsed_output1 = {
            "sap": {
                "2/1/6:10.*": {
                    "service_id": 10,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/2:8.1": {
                    "service_id": 181,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/2:3101.3101": {
                    "service_id": 1121,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/6:4000.1": {
                    "service_id": 1121,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:3101.*": {
                    "service_id": 1121,
                    "ingress_qos": 4503,
                    "egress_qos": 4503,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:4000.2": {
                    "service_id": 1122,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:3999.1": {
                    "service_id": 1221,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:101.2": {
                    "service_id": 1230,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:4000.101": {
                    "service_id": 2121,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:3999.101": {
                    "service_id": 2221,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:391.*": {
                    "service_id": 4092,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:4092.*": {
                    "service_id": 4092,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:4092.*": {
                    "service_id": 4092,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/2/1:1001": {
                    "service_id": 5051,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/2/1:1002": {
                    "service_id": 5051,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2990": {
                    "service_id": 10010,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3990": {
                    "service_id": 10010,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:980": {
                    "service_id": 10010,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2991": {
                    "service_id": 10011,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3991": {
                    "service_id": 10011,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:981": {
                    "service_id": 10011,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2992": {
                    "service_id": 10012,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3992": {
                    "service_id": 10012,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:982": {
                    "service_id": 10012,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2993": {
                    "service_id": 10013,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3993": {
                    "service_id": 10013,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:983": {
                    "service_id": 10013,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2994": {
                    "service_id": 10014,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3994": {
                    "service_id": 10014,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:984": {
                    "service_id": 10014,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2995": {
                    "service_id": 10015,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3995": {
                    "service_id": 10015,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:985": {
                    "service_id": 10015,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2996": {
                    "service_id": 10016,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3996": {
                    "service_id": 10016,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:986": {
                    "service_id": 10016,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2997": {
                    "service_id": 10017,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3997": {
                    "service_id": 10017,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:987": {
                    "service_id": 10017,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2998": {
                    "service_id": 10018,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3998": {
                    "service_id": 10018,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:988": {
                    "service_id": 10018,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2999": {
                    "service_id": 10019,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3999": {
                    "service_id": 10019,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:989": {
                    "service_id": 10019,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:2888": {
                    "service_id": 10020,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/7:3888": {
                    "service_id": 10020,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:888": {
                    "service_id": 10020,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/4:100": {
                    "service_id": 30001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:380.*": {
                    "service_id": 40001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "ip4",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/4:741": {
                    "service_id": 40001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:3000.100": {
                    "service_id": 40001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:3117.*": {
                    "service_id": 40001,
                    "ingress_qos": 3515,
                    "egress_qos": 3515,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "3/1/5": {
                    "service_id": 40001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "1/1/1:100": {
                    "service_id": 42001,
                    "ingress_qos": 1,
                    "egress_qos": 4201,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/8:4004": {
                    "service_id": 42001,
                    "ingress_qos": 1,
                    "egress_qos": 3512,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/2/1:4006": {
                    "service_id": 42001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:4010": {
                    "service_id": 52001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "ip4",
                    "egress_filter": "ip4",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/6:3331.1": {
                    "service_id": 91009,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:3332.1": {
                    "service_id": 91009,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:11.*": {
                    "service_id": 100001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/1:100.200": {
                    "service_id": 100100,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "1/2/1:888.888": {
                    "service_id": 100101,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/1:999.1": {
                    "service_id": 100101,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/1:120.5": {
                    "service_id": 100101,
                    "ingress_qos": 1,
                    "egress_qos": 3507,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/1:99.99": {
                    "service_id": 100101,
                    "ingress_qos": 10001,
                    "egress_qos": 10001,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/1:100.100": {
                    "service_id": 100101,
                    "ingress_qos": 10001,
                    "egress_qos": 10001,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/1:100.101": {
                    "service_id": 100101,
                    "ingress_qos": 10001,
                    "egress_qos": 10001,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/1:100.199": {
                    "service_id": 100101,
                    "ingress_qos": 3504,
                    "egress_qos": 3504,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "1/2/1:3993.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3994.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3995.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3996.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3997.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "ip4",
                    "egress_filter": "ip4",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3998.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3999.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:4000.1": {
                    "service_id": 100201,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/8:995": {
                    "service_id": 100201,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "ip4",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "1/2/1:3993.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3994.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3995.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3996.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3997.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3998.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3999.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:4000.2": {
                    "service_id": 100202,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/8:994": {
                    "service_id": 100202,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "ip4",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/2/1:802": {
                    "service_id": 100202,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:999": {
                    "service_id": 100204,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:998": {
                    "service_id": 100205,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:997": {
                    "service_id": 100401,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/8:996": {
                    "service_id": 100402,
                    "ingress_qos": 3511,
                    "egress_qos": 3511,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/2:3975.1": {
                    "service_id": 100702,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/2:1.2": {
                    "service_id": 100702,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "1/2/1:3000.1": {
                    "service_id": 101199,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/2:9.1": {
                    "service_id": 189901,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/2:9.2": {
                    "service_id": 189901,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/2:9.3": {
                    "service_id": 189901,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/2:9.4": {
                    "service_id": 189901,
                    "ingress_qos": 3501,
                    "egress_qos": 3501,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "1/2/1:3993.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3994.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3995.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3996.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3997.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3998.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:3999.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "1/2/1:4000.101": {
                    "service_id": 200201,
                    "ingress_qos": 3502,
                    "egress_qos": 3502,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/2:100.100": {
                    "service_id": 500100,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "3/1/4:4000.101": {
                    "service_id": 4810101,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "3/1/4:4000.201": {
                    "service_id": 4810102,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/6:151.1": {
                    "service_id": 91034501,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Up",
                },
                "2/1/9:4002.1": {
                    "service_id": 540020001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/10:4002.1": {
                    "service_id": 540020001,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/9:4002.2": {
                    "service_id": 540020002,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
                "2/1/10:4002.2": {
                    "service_id": 540020002,
                    "ingress_qos": 1,
                    "egress_qos": 1,
                    "ingress_filter": "none",
                    "egress_filter": "none",
                    "admin_state": "Up",
                    "oper_state": "Down",
                },
            },
            "total": 115,
        }

    # Specify the expected unparsed output
    golden_output1 = {'execute.return_value': '''
===============================================================================
Service Access Points
===============================================================================
PortId                          SvcId      Ing.  Ing.    Egr.  Egr.   Adm  Opr
                                           QoS   Fltr    QoS   Fltr
-------------------------------------------------------------------------------
2/1/6:10.*                      10         1     none    1     none   Up   Up
2/1/2:8.1                       181        1     none    1     none   Up   Down
2/1/2:3101.3101                 1121       3501  none    3501  none   Up   Down
2/1/6:4000.1                    1121       1     none    1     none   Up   Up
2/1/6:3101.*                    1121       4503  none    4503  none   Up   Up
2/1/6:4000.2                    1122       1     none    1     none   Up   Up
2/1/6:3999.1                    1221       1     none    1     none   Up   Up
2/1/6:101.2                     1230       1     none    1     none   Up   Up
2/1/6:4000.101                  2121       1     none    1     none   Up   Up
2/1/6:3999.101                  2221       1     none    1     none   Up   Up
1/2/1:391.*                     4092       1     none    1     none   Up   Up
1/2/1:4092.*                    4092       1     none    1     none   Up   Up
2/1/6:4092.*                    4092       1     none    1     none   Up   Up
2/2/1:1001                      5051       1     none    1     none   Up   Down
2/2/1:1002                      5051       1     none    1     none   Up   Down
2/1/7:2990                      10010      1     none    1     none   Up   Down
2/1/7:3990                      10010      1     none    1     none   Up   Down
2/1/8:980                       10010      3511  none    3511  none   Up   Down
2/1/7:2991                      10011      1     none    1     none   Up   Down
2/1/7:3991                      10011      1     none    1     none   Up   Down
2/1/8:981                       10011      3511  none    3511  none   Up   Down
2/1/7:2992                      10012      1     none    1     none   Up   Down
2/1/7:3992                      10012      1     none    1     none   Up   Down
2/1/8:982                       10012      3511  none    3511  none   Up   Down
2/1/7:2993                      10013      1     none    1     none   Up   Down
2/1/7:3993                      10013      1     none    1     none   Up   Down
2/1/8:983                       10013      3511  none    3511  none   Up   Down
2/1/7:2994                      10014      1     none    1     none   Up   Down
2/1/7:3994                      10014      1     none    1     none   Up   Down
2/1/8:984                       10014      3511  none    3511  none   Up   Down
2/1/7:2995                      10015      1     none    1     none   Up   Down
2/1/7:3995                      10015      1     none    1     none   Up   Down
2/1/8:985                       10015      3511  none    3511  none   Up   Down
2/1/7:2996                      10016      1     none    1     none   Up   Down
2/1/7:3996                      10016      1     none    1     none   Up   Down
2/1/8:986                       10016      3511  none    3511  none   Up   Down
2/1/7:2997                      10017      1     none    1     none   Up   Down
2/1/7:3997                      10017      1     none    1     none   Up   Down
2/1/8:987                       10017      3511  none    3511  none   Up   Down
2/1/7:2998                      10018      1     none    1     none   Up   Down
2/1/7:3998                      10018      1     none    1     none   Up   Down
2/1/8:988                       10018      3511  none    3511  none   Up   Down
2/1/7:2999                      10019      1     none    1     none   Up   Down
2/1/7:3999                      10019      1     none    1     none   Up   Down
2/1/8:989                       10019      3511  none    3511  none   Up   Down
2/1/7:2888                      10020      1     none    1     none   Up   Down
2/1/7:3888                      10020      1     none    1     none   Up   Down
2/1/8:888                       10020      3511  none    3511  none   Up   Down
2/1/4:100                       30001      1     none    1     none   Up   Up
1/2/1:380.*                     40001      1     ip4     1     none   Up   Up
2/1/4:741                       40001      1     none    1     none   Up   Up
2/1/6:3000.100                  40001      1     none    1     none   Up   Up
2/1/6:3117.*                    40001      3515  none    3515  none   Up   Up
3/1/5                           40001      1     none    1     none   Up   Down
1/1/1:100                       42001      1     none    4201  none   Up   Up
2/1/8:4004                      42001      1     none    3512  none   Up   Down
2/2/1:4006                      42001      1     none    1     none   Up   Down
2/1/8:4010                      52001      1     ip4     1     ip4    Up   Down
2/1/6:3331.1                    91009      1     none    1     none   Up   Up
2/1/6:3332.1                    91009      1     none    1     none   Up   Up
2/1/6:11.*                      100001     1     none    1     none   Up   Down
2/1/1:100.200                   100100     1     none    1     none   Up   Down
1/2/1:888.888                   100101     1     none    1     none   Up   Down
2/1/1:999.1                     100101     1     none    1     none   Up   Down
2/1/1:120.5                     100101     1     none    3507  none   Up   Down
2/1/1:99.99                     100101     10001 none    10001 none   Up   Down
2/1/1:100.100                   100101     10001 none    10001 none   Up   Down
2/1/1:100.101                   100101     10001 none    10001 none   Up   Down
2/1/1:100.199                   100101     3504  none    3504  none   Up   Down
1/2/1:3993.1                    100201     3501  none    3501  none   Up   Up
1/2/1:3994.1                    100201     3501  none    3501  none   Up   Up
1/2/1:3995.1                    100201     3501  none    3501  none   Up   Up
1/2/1:3996.1                    100201     3501  none    3501  none   Up   Up
1/2/1:3997.1                    100201     3501  ip4     3501  ip4    Up   Up
1/2/1:3998.1                    100201     3501  none    3501  none   Up   Up
1/2/1:3999.1                    100201     3501  none    3501  none   Up   Up
1/2/1:4000.1                    100201     3501  none    3501  none   Up   Up
2/1/8:995                       100201     3511  ip4     3511  none   Up   Down
1/2/1:3993.2                    100202     3501  none    3501  none   Up   Up
1/2/1:3994.2                    100202     3501  none    3501  none   Up   Up
1/2/1:3995.2                    100202     3501  none    3501  none   Up   Up
1/2/1:3996.2                    100202     3501  none    3501  none   Up   Up
1/2/1:3997.2                    100202     3501  none    3501  none   Up   Up
1/2/1:3998.2                    100202     3501  none    3501  none   Up   Up
1/2/1:3999.2                    100202     3501  none    3501  none   Up   Up
1/2/1:4000.2                    100202     3501  none    3501  none   Up   Up
2/1/8:994                       100202     3511  ip4     3511  none   Up   Down
2/2/1:802                       100202     1     none    1     none   Up   Down
2/1/8:999                       100204     3511  none    3511  none   Up   Down
2/1/8:998                       100205     3511  none    3511  none   Up   Down
2/1/8:997                       100401     3511  none    3511  none   Up   Down
2/1/8:996                       100402     3511  none    3511  none   Up   Down
2/1/2:3975.1                    100702     3501  none    3501  none   Up   Down
2/1/2:1.2                       100702     3501  none    3501  none   Up   Down
1/2/1:3000.1                    101199     1     none    1     none   Up   Up
2/1/2:9.1                       189901     3501  none    3501  none   Up   Down
2/1/2:9.2                       189901     3501  none    3501  none   Up   Down
2/1/2:9.3                       189901     3501  none    3501  none   Up   Down
2/1/2:9.4                       189901     3501  none    3501  none   Up   Down
1/2/1:3993.101                  200201     3502  none    3502  none   Up   Up
1/2/1:3994.101                  200201     3502  none    3502  none   Up   Up
1/2/1:3995.101                  200201     3502  none    3502  none   Up   Up
1/2/1:3996.101                  200201     3502  none    3502  none   Up   Up
1/2/1:3997.101                  200201     3502  none    3502  none   Up   Up
1/2/1:3998.101                  200201     3502  none    3502  none   Up   Up
1/2/1:3999.101                  200201     3502  none    3502  none   Up   Up
1/2/1:4000.101                  200201     3502  none    3502  none   Up   Up
2/1/2:100.100                   500100     1     none    1     none   Up   Down
3/1/4:4000.101                  4810101    1     none    1     none   Up   Up
3/1/4:4000.201                  4810102    1     none    1     none   Up   Up
2/1/6:151.1                     91034501   1     none    1     none   Up   Up
2/1/9:4002.1                    540020001  1     none    1     none   Up   Down
2/1/10:4002.1                   540020001  1     none    1     none   Up   Down
2/1/9:4002.2                    540020002  1     none    1     none   Up   Down
2/1/10:4002.2                   540020002  1     none    1     none   Up   Down
-------------------------------------------------------------------------------
Number of SAPs : 115
-------------------------------------------------------------------------------
===============================================================================
        '''}

    def test_show_service_sap_using_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowServiceSapUsing(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_service_sap_using_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowServiceSapUsing(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()