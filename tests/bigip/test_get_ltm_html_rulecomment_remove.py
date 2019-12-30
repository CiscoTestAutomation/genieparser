# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_html_rulecomment_remove
from genie.libs.parser.bigip.get_ltm_html_rulecomment_remove import (
    LtmHtmlruleCommentremove,
)

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/html-rule/comment-remove'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:html-rule:comment-remove:comment-removecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/html-rule/comment-remove?ver=14.1.2.1",
            "items": [],
        }


class test_get_ltm_html_rulecomment_remove(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [],
        "kind": "tm:ltm:html-rule:comment-remove:comment-removecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/html-rule/comment-remove?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmHtmlruleCommentremove(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmHtmlruleCommentremove(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
