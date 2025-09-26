"""starOS implementation of show_ntp_status.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowNtpStatusSchema(MetaParser):
    """Schema for show ntp status"""

    schema = {
        'ntp': {
            Any(): {
                'peer_mode': str,
                'leap': str,
                'stratum': str,
                'precision': str,
                'root_dist': str,
                'root_disper': str,
                'ref_time': str,
                'sys_flags': str,
                'jitter': str,
                'stability': str,
                'brcast_delay': str,
                'authdelay': str,
                'pll_offset': str,
                'pll_freq': str,
                'max_error': str,
                'estim_error': str,
                'status': str,
                'pll_time_cst': str,
                'pll_prec': str,
                'precision': str,
                'freq_tol': str,
                'offset': str,
                'freq': str,
                'poll_adj': str,
                'wtcdog_timer': str            
            },
        }     
    }


class ShowNtpStatusTable(ShowNtpStatusSchema):
    """Parser for show ntp status"""

    cli_command = 'show ntp status'

    """
[local]LABO-ASR5K> show ntp status 
Monday July 11 17:21:01 ART 2022
system peer:          10.93.11.40
system peer mode:     client
leap indicator:       00
stratum:              3
precision:            -21
root distance:        0.01794 s
root dispersion:      0.05183 s
reference ID:         [10.93.11.40]
reference time:       e677026f.63c9832c  Mon, Jul 11 2022 17:11:27.389
system flags:         auth monitor ntp kernel 
jitter:               0.000137 s
stability:            0.037 ppm
broadcastdelay:       -0.049988 s
authdelay:            0.000000 s
pll offset:           0.000158703 s
pll frequency:        -70.051 ppm
maximum error:        0.000339204 s
estimated error:      1.35e-07 s
status:               6001  pll nano mode=fll
pll time constant:    10
precision:            1e-09 s
frequency tolerance:  500 ppm
offset:               0.000183 s
frequency:            -70.051 ppm
poll adjust:          30
watchdog timer:       574 s
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ntp_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^(system peer:\s+(?P<peer>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}))')
        p1 = re.compile(r'^(system peer mode:\s+(?P<peer_mode>\w+))')
        p2 = re.compile(r'^(leap indicator:\s+(?P<leap>\d+))')
        p3 = re.compile(r'^(stratum:\s+(?P<stratum>\d+))')
        p4 = re.compile(r'^(precision:\s+(?P<precision>(([|-])\d+)))')
        p5 = re.compile(r'^(root distance:\s+(?P<root_dist>\d+.\d+\ss))')
        p6 = re.compile(r'^(root dispersion:\s+(?P<root_disper>\d+.\d+\ss))')
        p7 = re.compile(r'^(reference time:\s+.+\s\s(?P<ref_time>.+))')
        p8 = re.compile(r'^(system flags:\s+(?P<sys_flags>.+))')
        p9 = re.compile(r'^(jitter:\s+(?P<jitter>\d+.\d+\ss))')
        p10 = re.compile(r'^(stability:\s+(?P<stability>\d+.\d+\sppm))')
        p11 = re.compile(r'^(broadcastdelay:\s+(?P<brcast_delay>[|-]\d+.\d+\ss))')
        p12 = re.compile(r'^(authdelay:\s+(?P<authdelay>\d+.\d+\ss))')
        p13 = re.compile(r'^(pll offset:\s+(?P<pll_offset>\d+.\d+\ss))')
        p14 = re.compile(r'^(pll frequency:\s+(?P<pll_freq>[|-]\d+.\d+\sppm))')
        p15 = re.compile(r'^(maximum error:\s+(?P<max_error>\d+.\d+\ss))')
        p16 = re.compile(r'^(estimated error:\s+(?P<estim_error>\d+.\d+e-\d+\ss))')
        p17 = re.compile(r'^(status:\s+(?P<status>\d+.+))')
        p18 = re.compile(r'^(pll time constant:\s+(?P<pll_time_cst>\d+))')
        p19 = re.compile(r'^(precision:\s+(?P<pll_prec>\d+e-\d+\ss))')
        p20 = re.compile(r'^(frequency tolerance:\s+(?P<freq_tol>\d+\sppm))')
        p21 = re.compile(r'^(offset:\s+(?P<offset>\d+.\d+\ss))')
        p22 = re.compile(r'^(frequency:\s+(?P<freq>[|-]\d+.\d+\sppm))')
        p23 = re.compile(r'^(poll adjust:\s+(?P<poll_adj>\d+))')
        p24 = re.compile(r'^(watchdog timer:\s+(?P<wtcdog_timer>\d+\ss))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            #system peer:          10.93.11.40
            if m:
                if 'ntp' not in ntp_dict:
                    result_dict = ntp_dict.setdefault('ntp',{})
                peer = m.groupdict()['peer']
                result_dict[peer] = {}
                continue

            m = p1.match(line)
            #system peer mode:     client
            if m:
                peer_mode = m.groupdict()['peer_mode']
                result_dict[peer]['peer_mode'] = peer_mode
                continue

            m = p2.match(line)
            #leap indicator:       00
            if m:
                leap = m.groupdict()['leap']
                result_dict[peer]['leap'] = leap
                continue

            m = p3.match(line)
            #stratum:              3
            if m:
                stratum = m.groupdict()['stratum']
                result_dict[peer]['stratum'] = stratum
                continue
            
            m = p4.match(line)
            #precision:            -21
            if m:
                precision = m.groupdict()['precision']
                result_dict[peer]['precision'] = precision
                continue

            m = p5.match(line)
            #root distance:        0.01794 s
            if m:
                root_dist = m.groupdict()['root_dist']
                result_dict[peer]['root_dist'] = root_dist
                continue

            m = p6.match(line)
            #root dispersion:      0.05183 s
            if m:
                root_disper = m.groupdict()['root_disper']
                result_dict[peer]['root_disper'] = root_disper
                continue

            m = p7.match(line)
            #reference time:       e677026f.63c9832c  Mon, Jul 11 2022 17:11:27.389
            if m:
                ref_time = m.groupdict()['ref_time']
                result_dict[peer]['ref_time'] = ref_time
                continue

            m = p8.match(line)
            #system flags:         auth monitor ntp kernel 
            if m:
                sys_flags = m.groupdict()['sys_flags']
                result_dict[peer]['sys_flags'] = sys_flags
                continue

            m = p9.match(line)
            #jitter:               0.000137 s
            if m:
                jitter = m.groupdict()['jitter']
                result_dict[peer]['jitter'] = jitter
                continue

            m = p10.match(line)
            #stability:            0.037 ppm
            if m:
                stability = m.groupdict()['stability']
                result_dict[peer]['stability'] = stability
                continue

            m = p11.match(line)
            #broadcastdelay:       -0.049988 s
            if m:
                brcast_delay = m.groupdict()['brcast_delay']
                result_dict[peer]['brcast_delay'] = brcast_delay
                continue

            m = p12.match(line)
            #broadcastdelay:       -0.049988 s
            if m:
                authdelay = m.groupdict()['authdelay']
                result_dict[peer]['authdelay'] = authdelay
                continue

            m = p13.match(line)
            #pll offset:           0.000158703 s
            if m:
                pll_offset = m.groupdict()['pll_offset']
                result_dict[peer]['pll_offset'] = pll_offset
                continue

            m = p14.match(line)
            #pll frequency:        -70.051 ppm
            if m:
                pll_freq = m.groupdict()['pll_freq']
                result_dict[peer]['pll_freq'] = pll_freq
                continue
     
            m = p15.match(line)
            #maximum error:        0.000339204 s
            if m:
                max_error = m.groupdict()['max_error']
                result_dict[peer]['max_error'] = max_error
                continue

            m = p16.match(line)
            #estimated error:      1.35e-07 s
            if m:
                estim_error = m.groupdict()['estim_error']
                result_dict[peer]['estim_error'] = estim_error
                continue

            m = p17.match(line)
            #status:               6001  pll nano mode=fll
            if m:
                status = m.groupdict()['status']
                result_dict[peer]['status'] = status
                continue

            m = p18.match(line)
            #pll time constant:    10
            if m:
                pll_time_cst = m.groupdict()['pll_time_cst']
                result_dict[peer]['pll_time_cst'] = pll_time_cst
                continue

            m = p19.match(line)
            #precision:            1e-09 s
            if m:
                pll_prec = m.groupdict()['pll_prec']
                result_dict[peer]['pll_prec'] = pll_prec
                continue

            m = p20.match(line)
            #frequency tolerance:  500 ppm
            if m:
                freq_tol = m.groupdict()['freq_tol']
                result_dict[peer]['freq_tol'] = freq_tol
                continue

            m = p21.match(line)
            #offset:               0.000183 s
            if m:
                offset = m.groupdict()['offset']
                result_dict[peer]['offset'] = offset
                continue

            m = p22.match(line)
            #frequency:            -70.051 ppm
            if m:
                freq = m.groupdict()['freq']
                result_dict[peer]['freq'] = freq
                continue

            m = p23.match(line)
            #poll adjust:          30
            if m:
                poll_adj = m.groupdict()['poll_adj']
                result_dict[peer]['poll_adj'] = poll_adj
                continue

            m = p24.match(line)
            #watchdog timer:       574 s
            if m:
                wtcdog_timer = m.groupdict()['wtcdog_timer']
                result_dict[peer]['wtcdog_timer'] = wtcdog_timer
                continue

        return ntp_dict

