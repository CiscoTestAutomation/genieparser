# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ====================================================
#  Schema for show radius statistics 
# ====================================================
class ShowRadiusStatisticsSchema(MetaParser):
    """
    Schema for show radius statistics 
    """

    schema = {
        Optional('maximum_inq_length'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('maximum_waitq_length'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('maximum_doneq_length'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('total_responses_seen'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('packets_with_responses'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('packets_without_responses'): {
            'auth': str,
            'acct': str,
            'both': str},
        'access_rejects': {
            'auth': str
            },
        'access_accepts': {
            'auth': str
            },
        Optional('average_response_delay'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('maximum_response_delay'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('number_of_radius_timeouts'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_started'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_created'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_create_failed'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_stopped'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_stop_failed'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_outstanding'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_added'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_add_failed'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_jitterred'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('radius_timers_jitter_failed'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('duplicate_id_detects'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('buffer_allocation_failures'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('maximum_buffer_size'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('malformed_responses'): {
            'auth': str,
            'acct': str,
            'both': str},
        Optional('bad_authenticators'): {
            'auth': str,
            'acct': str,
            'both': str},
        'unknown_responses': {
            'auth': str,
            'acct': str,
            'both': str},

        'source_port_range': str,
        'last_used_source_port': list,

        'elapsed_time_since_counters_last_cleared': str,

        Optional('radius_latency_distribution'): {
            '<= 2ms': {'auth': str, 'acct': str},
            '3-5ms': {'auth': str, 'acct': str},
            '5-10ms': {'auth': str, 'acct': str},
            '10-20ms': {'auth': str, 'acct': str},
            '20-50ms': {'auth': str, 'acct': str},
            '50-100m': {'auth': str, 'acct': str},
            '>100ms': {'auth': str, 'acct': str}
        },
        Optional('current_inq_length'): str,
        Optional('current_doneq_length'): str
    }


# ====================================================
#  Parser for show radius statistics 
# ====================================================
class ShowRadiusStatistics(ShowRadiusStatisticsSchema):
    """
    Parser for show radius statistics 
    Args:
        device (`obj`): Device object.
        output (Optional): Output of show radius statistics command
    Returns:
        Dictionary with the keys mentioned in schema class
    """

    def cli(self, output=None):
        # Cli command 
        cmd = 'show radius statistics'

        #----------------------------------------------------------------
        # Maximum inQ length:             NA         NA         0
        # Maximum waitQ length:           NA         NA         2
        # Maximum doneQ length:           NA         NA         0
        # Total responses seen:           0          0          0
        # Packets with responses:         0          0          0
        # Packets without responses:      4          0          4
        # Radius Timers Started:         20          0         20
        # Radius Timers Created:         20          0         20
        # Radius Timers Stopped:         20          0         20
        # Radius Timers Outstanding:      0          0          0
        # Radius Timers Added:           20          0         20
        # Radius Timers Jitterred:        0          0          0
        # Duplicate ID detects:           0          0          0
        # Buffer Allocation Failures:     0          0          0
        #----------------------------------------------------------------
        p1 = re.compile(r'(^\w+\s+\w+\s+\w+)\s*:\s+(?P<auth>\w+)\s+(?P<acct>\w+)\s+(?P<both>\w+)\s*')
        
        # Access Rejects           :          0
        p2 = re.compile(r'(^Access\s+Rejects)\s+:\s+(?P<auth>\w+)\s*')
        
        #Access Accepts           :          0
        p3 = re.compile(r'(^Access\s+Accepts)\s+:\s+(?P<auth>\w+)\s*')

        #----------------------------------------------------------------
        # Number of Radius timeouts:         20          0         20
        # Radius Timers Create Failed:        0          0          0
        # Radius Timers Stop Failed:          0          0          0
        # Radius Timers Add Failed:           0          0          0
        # Radius Timers Jitter Failed:        0          0          0
        #----------------------------------------------------------------
        p4 = re.compile(r'(^\w+\s+\w+\s+\w+\s+\w+)\s*:\s+(?P<auth>\w+)\s+(?P<acct>\w+)\s+(?P<both>\w+)\s*')

        #----------------------------------------------------------------
        # Average response delay(ms):          0          0          0
        # Maximum response delay(ms):          0          0          0
        # Maximum Buffer Size (bytes):        310          0        310
        #----------------------------------------------------------------
        p5 = re.compile(r'(^\w+\s+\w+\s+\w+)\s*[(]\w+[)]\s*:\s+(?P<auth>\w+)\s+(?P<acct>\w+)\s+(?P<both>\w+)\s*')

        #----------------------------------------------------------------
        # Malformed Responses        :          0          0          0
        # Bad Authenticators         :          0          0          0
        # Unknown Responses          :          0          0          0
        #----------------------------------------------------------------
        p6 = re.compile(r'(^\w+\s+\w+)\s*:\s+(?P<auth>\w+)\s+(?P<acct>\w+)\s+(?P<both>\w+)\s*')

        # Source Port Range: (2 ports only)
        p7 = re.compile(r'(^Source\s+Port\s+Range)\s*:\s*([(]\w+\s+\w+\s+\w+\s*[)])')

        #1645 - 1646
        p8 = re.compile(r'(\w+)\s*-\s*(\w+)')

        # Last used Source Port/Identifier:
        p9 = re.compile(r'(^Last\s+used\s+Source\s+Port)[/]Identifier\s*:')

        # 1645/0
        p10 = re.compile(r'(\d+)\s*[/]\s*(\d+)')

        # Elapsed time since counters last cleared: 1d11h15m
        p11 = re.compile(r'(^Elapsed\s+time\s+since\s+counters\s+last\s+cleared)\s*:\s*(\w+)')

        # Radius Latency Distribution:
        p12 = re.compile(r'(^Radius\s+Latency\s+Distribution)\s*:')

        # <= 2ms :          0          0
        p13 = re.compile(r'(<=\s*\w+)\s*:\s*(?P<auth>\w+)\s*(?P<acct>\w+)')

        #----------------------------------------------------------------
        # 3-5ms  :          0          0
        # 5-10ms :          0          0
        # 10-20ms:          0          0
        # 20-50ms:          0          0
        # 50-100m:          0          0
        #----------------------------------------------------------------
        p14 = re.compile(r'(\d+\s*[-]\s*\w+)\s*:\s*(?P<auth>\w+)\s*(?P<acct>\w+)')
        
        # >100ms :          0          0
        p15 = re.compile(r'(>\s*\w+)\s*:\s*(?P<auth>\w+)\s*(?P<acct>\w+)')

        # Current inQ length  : 0
        p16 = re.compile(r'(^Current\s+inQ\s+length)\s*:\s*(\d+)')

        # Current doneQ length: 0
        p17 = re.compile(r'(^Current\s+doneQ\s+length)\s*:\s*(\d+)')

        ret_dict = {}

        try:

            if output is None:
                out = self.device.execute(cmd)
            else:
                out = output

            istr = iter(out.splitlines())
            for line in istr:
                line = line.strip()

                
                mo = p1.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.groupdict())

                mo = p2.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.groupdict())

                mo = p3.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.groupdict())

                mo = p4.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.groupdict())

                mo = p5.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.groupdict())

                mo = p6.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.groupdict())

                # Source Port Range: (2 ports only)
                # 1645 - 1646
                mo = p7.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, '')
                    try:
                        next_line = next(istr)
                        res = p8.match(next_line.strip())
                        if res:
                            ret_dict[key_string] = res.group()
                    except StopIteration as e:
                        continue

                # Last used Source Port/Identifier:
                # 1645/0
                # 1646/0
                mo = p9.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, '')
                    try:
                        last_used_source_port = []
                        for i in range(2):
                            next_line = next(istr)
                            res = p10.match(next_line.strip())
                            if res:
                                last_used_source_port.append(res.group())
                            else:
                                break
                        ret_dict[key_string] = last_used_source_port
                    except StopIteration as e:
                        continue

                mo = p11.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.group(2))

                # Radius Latency Distribution:
                # <= 2ms :          0          0
                # 3-5ms  :          0          0
                # 5-10ms :          0          0
                # 10-20ms:          0          0
                # 20-50ms:          0          0
                # 50-100m:          0          0
                # >100ms :          0          0
                mo = p12.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    radius_latency = ret_dict.setdefault(key_string, {})
                    next_line = next(istr)
                    res = p13.match(next_line.strip())
                    if res:
                        radius_latency.setdefault(res.group(1), res.groupdict())
                        for i in range(6):
                            next_line = next(istr)
                            res = p14.match(next_line.strip())
                            if res:
                                radius_latency.setdefault(res.group(1), res.groupdict())
                            elif p16.match(line):
                                break
                        res = p15.match(next_line.strip())
                        if res:
                            radius_latency.setdefault(res.group(1), res.groupdict())

                mo = p16.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.group(2))

                mo = p17.match(line)
                if mo:
                    key_string = (re.sub(r'\s+', '_', mo.group(1))).lower()
                    ret_dict.setdefault(key_string, mo.group(2))

        except Exception as error:
            logger.info('error {} occurred while executing the command'.format(error))

        import pprint
        pprint.pprint(ret_dict)

        return ret_dict


# ====================================================
#  Schema for show radius server-group all
# ====================================================
class ShowRadiusServerGroupAllSchema(MetaParser):
    """
    Schema for show radius server-group all
    """

    schema = {
        Any(): {
            "sharecount": str,
            "sg_unconfigured": str,
            "type": str,
            "memlocks": str,
            Any(): {
                "authen": str,
                "author": str,
                "acct": str,
                "server_auto_test_enabled": str,
                "keywrap_enabled": str,
            },
        },
    }


# ====================================================
#  Parser for show radius server-group all
# ====================================================
class ShowRadiusServerGroupAll(ShowRadiusServerGroupAllSchema):
    """
    Parser for show radius server-group all
    """

    def cli(self, output=None):
        # Cli command 
        cmd = 'show radius server-group all'

        # Server group radius
        p1 = re.compile(r'(^Server\s+group)\s+(.*)')
        
        # Sharecount = 1  sg_unconfigured = FALSE
        p2 = re.compile(r'(^Sharecount)\s*\=\s*(?P<sharecount>\d+)\s+(sg_unconfigured)\s*\=\s*(?P<sg_unconfigured>\D+)')
        
        # Type = standard  Memlocks = 1
        p3 = re.compile(r'(^Type)\s*\=\s*(?P<type>\w+)\s+(Memlocks)\s*\=\s*(?P<memlocks>\d+)')
        
        # 'Server(121.0.0.1:1812,1813,data-rad) Transactions:' |
        # 'Server(44AA::1:1812,1813,ipv6-rad) Transactions:'
        p4 = re.compile(r'(^Server)\s*[(](((\d+\.){3}\d+)|(\w+::\d+))\:\d+\,\d+\,\w+\-(\w+)[)]\s+(Transactions)')
        
        # Authen: 0   Author: 0       Acct: 0
        p5 = re.compile(r'(^Authen)\s*\:\s*(?P<authen>\d+)\s+(Author)\s*\:\s*(?P<author>\d+)\s+(Acct)\s*\:\s*(?P<acct>\d+)\s*')
        
        # Server_auto_test_enabled: FALSE
        p6 = re.compile(r'(^Server_auto_test_enabled)\s*\:\s*(?P<server_auto_test_enabled>\D+)\s*')
        
        # Keywrap enabled: FALSE
        p7 = re.compile(r'(^Keywrap\s+enabled)\s*\:\s*(?P<keywrap_enabled>\D+)\s*')

        ret_dict = {}
        server_grp = {}
        server_trans = {}

        try:
            if output is None:
                out = self.device.execute(cmd)
            else:
                out = output

            for line in out.splitlines():
                line = line.strip()
                
                res = p1.match(line)
                if res:
                    server_grp = ret_dict.setdefault(res.group(2), {})

                res = p2.match(line)
                if res:
                    server_grp.update(res.groupdict())

                res = p3.match(line)
                if res:
                    server_grp.update(res.groupdict())

                res = p4.match(line)
                if res:
                    key_string = (re.sub(r'\s+', '_', res.group())).lower()
                    server_trans = server_grp.setdefault(key_string, {})
                
                res = p5.match(line)
                if res:
                    server_trans.update(res.groupdict())
                    
                res = p6.match(line)
                if res:
                    server_trans.update(res.groupdict())


                res = p7.match(line)
                if res:
                    server_trans.update(res.groupdict())
                
        except Exception as error:
            logger.info('error {} occurred while executing the command'.format(error))

        return ret_dict
