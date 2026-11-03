"""Regression coverage for blank numeric columns in EVPN/MVPN tables."""
import runpy
from pathlib import Path
import unittest

from genie.libs.parser.nxos.show_bgp import (
    ShowBgpL2vpnEvpn, ShowBgpIpMvpn, ShowBgpIpMvpnRouteType,
)
from genie.metaparser.util.exceptions import SchemaEmptyParserError


FIXTURES = Path(__file__).resolve().parents[1] / 'src/genie/libs/parser/nxos/tests'


class TestBgpPathColumns(unittest.TestCase):
    def raw(self, cls=ShowBgpL2vpnEvpn):
        return (FIXTURES / cls.__name__ / 'cli/equal/golden_path_columns_output.txt').read_text()

    def paths(self, parsed):
        families = parsed['instance']['default']['vrf']['default']['address_family']
        return next(iter(next(iter(next(iter(families.values()))['rd'].values()))['prefix'].values()))['path']

    def test_golden_fixtures(self):
        for cls in (ShowBgpL2vpnEvpn, ShowBgpIpMvpn, ShowBgpIpMvpnRouteType):
            with self.subTest(parser=cls.__name__):
                expected = runpy.run_path(str(FIXTURES / cls.__name__ /
                    'cli/equal/golden_path_columns_expected.py'))['expected_output']
                self.assertEqual(cls(device=None).parse(output=self.raw(cls)), expected)

    def test_column_combinations(self):
        cases = [
            ('', '', '0', '65003 65002', 'i'),
            ('', '100', '0', '65003', 'i'),
            ('20', '', '0', '65003 65002', 'e'),
            ('20', '100', '32768', '', '?'),
            ('0', '100', '0', '{65003 65002}', 'i'),
            ('4294967295', '4294967295', '65535', '65003 65003 65002', 'i'),
        ]
        for cls in (ShowBgpL2vpnEvpn, ShowBgpIpMvpn, ShowBgpIpMvpnRouteType):
            for metric, localpref, weight, aspath, origin in cases:
                with self.subTest(parser=cls.__name__, values=(metric, localpref, weight, aspath)):
                    row = (' ' * 22 + f'{"10.10.0.1":<15}{metric:>11}'
                           f'{localpref:>11}{weight:>11} ' +
                           (aspath + ' ' if aspath else '') + origin)
                    lines = self.raw(cls).splitlines()
                    lines[-1] = row
                    path = self.paths(cls(device=None).parse(output='\n'.join(lines)))[1]
                    self.assertEqual(path['weight'], weight)
                    self.assertEqual(path['origin'], origin)
                    for key, value in [('metric', metric), ('localpref', localpref), ('path', aspath)]:
                        if value:
                            self.assertEqual(path[key], value)
                        else:
                            self.assertNotIn(key, path)

    def test_multiple_paths(self):
        raw = self.raw()
        second = raw.splitlines()[-1]
        second = '* e' + second[3:]
        paths = self.paths(ShowBgpL2vpnEvpn(device=None).parse(output=raw + second + '\n'))
        self.assertEqual(len(paths), 2)
        self.assertEqual(paths[2]['path'], '65003 65002')
        self.assertEqual(paths[2]['weight'], '0')

    def test_headerless_legacy_output(self):
        lines = self.raw().splitlines()
        lines = [line for line in lines if 'Next Hop' not in line]
        lines[-1] = '                      10.10.0.1                 20        100          0 i'
        path = self.paths(ShowBgpL2vpnEvpn(device=None).parse(output='\n'.join(lines)))[1]
        self.assertEqual(path['localpref'], '100')
        self.assertEqual(path['weight'], '0')

    def test_empty_output(self):
        for cls in (ShowBgpL2vpnEvpn, ShowBgpIpMvpn, ShowBgpIpMvpnRouteType):
            with self.subTest(parser=cls.__name__):
                with self.assertRaises(SchemaEmptyParserError):
                    cls(device=None).parse(output='')

    def test_reject_missing_origin(self):
        raw = self.raw().rstrip().removesuffix(' i')
        with self.assertRaises(ValueError):
            ShowBgpL2vpnEvpn(device=None).parse(output=raw)


if __name__ == '__main__':
    unittest.main()
