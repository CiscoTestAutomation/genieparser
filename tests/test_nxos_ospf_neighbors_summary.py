"""Focused regression tests for NX-OS OSPF neighbor summaries."""
import json
from pathlib import Path
import runpy
import unittest
from unittest.mock import Mock

from genie.conf.base import Device
from genie.libs.parser.nxos.show_ospf import ShowIpOspfNeighbors
from genie.metaparser.util.exceptions import SchemaEmptyParserError


FIXTURES = (Path(__file__).resolve().parents[1] / 'src/genie/libs/parser/nxos'
            / 'tests/ShowIpOspfNeighbors/cli/equal')


class TestOspfNeighborsSummary(unittest.TestCase):
    def test_expected_fixtures(self):
        for path in sorted(FIXTURES.glob('*_output.txt')):
            with self.subTest(fixture=path.name):
                expected = runpy.run_path(str(path.with_name(
                    path.name.replace('_output.txt', '_expected.py'))))['expected_output']
                actual = ShowIpOspfNeighbors(device=None).parse(output=path.read_text())
                self.assertEqual(actual, expected)
                json.dumps(actual)

    def test_runtime_command_lookup(self):
        raw = (FIXTURES / 'golden_output1_output.txt').read_text()
        device = Device(name='offline-nxos', os='nxos')
        self.assertEqual(device.parse('show ip ospf neighbors', output=raw),
                         ShowIpOspfNeighbors(device=None).parse(output=raw))

    def test_execute_when_output_is_not_supplied(self):
        raw = (FIXTURES / 'golden_output1_output.txt').read_text()
        device = Mock()
        device.execute.return_value = raw
        ShowIpOspfNeighbors(device=device).parse()
        device.execute.assert_called_once_with('show ip ospf neighbors')

    def test_empty_output(self):
        with self.assertRaises(SchemaEmptyParserError):
            ShowIpOspfNeighbors(device=None).parse(output='')

    def test_multiple_processes_and_vrfs(self):
        raw = (FIXTURES / 'golden_output5_output.txt').read_text()
        combined = (raw + raw.replace('UNDERLAY', '10')
                    + raw.replace('default', 'tenant-a'))
        parsed = ShowIpOspfNeighbors(device=None).parse(output=combined)
        self.assertEqual(set(parsed['vrf']), {'default', 'tenant-a'})
        instances = parsed['vrf']['default']['address_family']['ipv4']['instance']
        self.assertEqual(set(instances), {'UNDERLAY', '10'})
        self.assertEqual(instances['10'], {'total_neighbors': 0})

    def test_reject_truncated_table(self):
        raw = (FIXTURES / 'golden_output3_output.txt').read_text()
        with self.assertRaises(ValueError):
            ShowIpOspfNeighbors(device=None).parse(output='\n'.join(raw.splitlines()[:-1]))

    def test_reject_unparsed_neighbor_row(self):
        raw = (FIXTURES / 'golden_output1_output.txt').read_text()
        with self.assertRaises(ValueError):
            ShowIpOspfNeighbors(device=None).parse(output=raw.replace('FULL/ -', '???'))

    def test_reject_duplicate_neighbor(self):
        raw = (FIXTURES / 'golden_output1_output.txt').read_text()
        duplicate = raw.replace('neighbors: 1', 'neighbors: 2')
        duplicate += raw.splitlines()[-1] + '\n'
        with self.assertRaises(ValueError):
            ShowIpOspfNeighbors(device=None).parse(output=duplicate)

    def test_reject_missing_header_or_count(self):
        raw = (FIXTURES / 'golden_output1_output.txt').read_text()
        for missing_line in (0, 1):
            with self.subTest(missing_line=missing_line):
                lines = raw.splitlines()
                del lines[missing_line]
                with self.assertRaises(ValueError):
                    ShowIpOspfNeighbors(device=None).parse(output='\n'.join(lines))


if __name__ == '__main__':
    unittest.main()
