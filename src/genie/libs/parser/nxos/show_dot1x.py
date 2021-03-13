# -*- coding: utf-8 -*-
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

#   ============================================    #
#                    Statistics                     #
#   ============================================    #

# Schema class
class ShowDot1xAllStatisticsSchema(MetaParser):
    # string here not needed
    ''' Schema for: 
            show dot1x all statistics
    '''
    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'statistics': {
                    'txreq': int,
                    'rxlogoff': int,
                    'rxtotal': int,
                    'txtotal': int,
                    'rxversion': int,
                    'lastrxsrcmac': str,
                    Optional('rxlenerr'): int,
                    Optional('txreq'): int,
                    Optional('txreqid'): int,
                    Optional('rxstart'): int,
                    Optional('rxlogoff'): int,
                    Optional('rxresp'): int,
                    Optional('rxrespid'): int,
                    Optional('txreqid'): int,
                    Optional('rxinvalid'): int,
                },
            }
        }
    }

# Parser class
class ShowDot1xAllStatistics(ShowDot1xAllStatisticsSchema):
    '''Parser for:
            show dot1x all statistics
    '''

    cli_command = 'show dot1x all statistics'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        p1 = re.compile(r'((^[Dd]ot1x)\s+)?' +
                        '(([Aa]uthenticator)\s+)?' +
                        '(([Pp])ort\s+)?(([Ss]tatistics)\s+)?' +
                        '((for)\s+)?(?P<interface>(\w*)\d+(\/)(\d+))$\s*')



        p2 = re.compile(r'(\w+) *\= *(\d+)+ *')

        p3 = re.compile(r'^([Rr]x[Vv]ersion) \= *(?P<rxversion>\d+)' +
                        '   ([Ll]ast[Rr]x[Ss]rc[Mm][Aa][Cc]) = (?P<lastrxsrcmac>\w+:\w+:\w+:\w+:\w+:\w+)$')



        for line in out.splitlines():
            line = line.strip()

            # Dot1x Authenticator Port Statistics for Ethernet1/1
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                ret_dict.setdefault("interfaces", {}).setdefault(interface, {}).setdefault(
                    'interface', interface)
                ret_dict.setdefault("interfaces", {}).setdefault(interface, {}).setdefault(
                    'statistics', {})
                stats = ret_dict.setdefault("interfaces", {}).setdefault(interface, {}).setdefault(
                    'statistics', {})
                continue

            # RxVersion = 0   LastRxSrcMAC = 00: 00: 00: 00: 00: 00
            m = p3.match(line)
            if m:
                stats.update({'rxversion': int(m.groupdict()['rxversion'])})
                stats.update({'lastrxsrcmac': m.groupdict()['lastrxsrcmac']})
                continue

            # RxStart = 0     RxLogoff = 0    RxResp = 0      RxRespID = 0
            # RxInvalid = 0   RxLenErr = 0    RxTotal = 0
            # TxReq = 0       TxReqID = 0     TxTotal = 3
            m = p2.findall(line)
            if m:
                for item in m:
                    stats.update({item[0].lower(): int(item[1])})
                continue

        return ret_dict

#   ============================================    #
#                     Summary                       #
#   ============================================    #

# Schema class
class ShowDot1xAllSummarySchema(MetaParser):
    ''' Schema for:
            show dot1x all summary
    '''
    schema = {
        'interfaces': {
            Any(): {
                'interface': str,
                'clients': {
                Any() : {
                        'client': str,
                        'pae': str,
                        'status': str,
                    }
                }
            }
        }
    }

# Parser class
class ShowDot1xAllSummary(ShowDot1xAllSummarySchema):
    '''Parser for:
            show dot1x all summary
    '''
    cli_command = 'show dot1x all summary'

    def cli(self, output = None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        p1 = re.compile(r'^(?P<intf>((\w+\d+)(\/\d+)*)) + +(?P<pae>\w+) + +' +
                        '(?P<client>(\w+\:\w+\:\w+\:\w+\:\w+\:\w+)|\w+) + +(?P<status>\w+)$')

        for line in out.splitlines():
            line = line.strip()

            # Ethernet1/1    AUTH                none      AUTHORIZED
            # Ethernet102/1/6    AUTH   0E:BE:EF:FF:3F:3F      AUTHORIZED
            m = p1.match(line)
            if m:
                intf = m.groupdict()['intf']
                if 'interfaces' not in ret_dict:
                    interfaces_dict = ret_dict.setdefault('interfaces', {})
                interfaces_dict.setdefault(intf, {}).setdefault('interface', intf)
                clients = interfaces_dict.setdefault(intf, {}).setdefault('clients', {})

                client_mac = m.groupdict()['client']
                client_dict = clients.setdefault(client_mac, {})
                client_dict.setdefault('client', client_mac)
                client_dict.update({'pae': m.groupdict()['pae']})
                client_dict.update({'status': m.groupdict()['status']})
                continue

        return ret_dict


#   ============================================    #
#                     Details                       #
#   ============================================    #

# Schema class
class ShowDot1xAllDetailsSchema(MetaParser):
    '''Schema for:
            show dot1x all details
    '''
    schema = {
        Optional('system_auth_control'): bool,
        Optional('version'): int,
        Optional ('interfaces'): {
            Any() : {
                'pae': str,
                'interface': str,
                Optional ('credentials') : str,
                Optional ('max_reauth_req'): int,
                Optional ('max_req'): int,
                Optional ('max_start'): int,
                Optional ('port_control'): str,
                Optional ('control_direction'): str,
                Optional ('host_mode'): str,
                Optional ('re_authentication'): bool,
                Optional ('re_auth_max'): int,
                Optional ('mac-auth-bypass'): bool,
                Optional('port_status') : str,
                Optional ('timeout'): {
                    Optional ('auth_period'): int,
                    Optional ('held_period'): int,
                    Optional ('quiet_period'): int,
                    Optional ('ratelimit_period'): int,
                    Optional ('server_timeout'): int,
                    Optional ('start_period'): int,
                    Optional ('supp_timeout'): int,
                    Optional ('tx_period'): int,
                    Optional('re_auth_period'): int,
                    Optional ('time_to_next_reauth'): int,
                },
                Optional ('authenticator'): {
                    'eap': {
                        'profile': str,
                    },
                },
                Optional ('supplicant'): {
                    'eap': {
                        'profile': str,
                    },
                },
                Optional('clients') : {
                    Any() : {
                        Optional('client'): str,
                        Optional('eap_method'): str,
                        Optional('auth_method'): str, 
                        Optional('session'): {
                            Optional('reauth_action'): str,
                            Optional('auth_by') : str,
                            Optional('session_id'): str,
                            Optional('auth_sm_state'): str,
                            Optional('auth_bend_sm_state'): str,
                        }
                    }
                }
            }
        }
    }

# Parser class
class ShowDot1xAllDetails(ShowDot1xAllDetailsSchema):
    '''Parser for:
            show dot1x all details
    '''

    cli_command = 'show dot1x all details'

    def cli(self, output=None):
        if output is None:  # if no input as second arg
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}
        eap_method = ''
        # Sysauthcontrol Enabled
        p1 = re.compile(r'^Sysauthcontrol +(?P<SysControl>\w+)$')
        
        # Dot1x Protocol Version 2
        p2 = re.compile(r'^Dot1x +Protocol +Version +(?P<version>\d+)$')
        
        # Dot1x Info for Ethernet1/2
        p3 = re.compile(r'^Dot1x +Info +for +(?P<intf>\w+\d+\/\d+)$')
        
        # EAP Method                = (13)
        # PAE = AUTHENTICATOR
        # MaxReq = 3
        # PortControl = AUTO
        # ReAuthentication = Enabled
        # Port Status = AUTHORIZED
        # HostMode = SINGLE HOST
        # ReAuthMax = 2
        # Mac-Auth-Bypass = Disabled
        # QuietPeriod = 60
        # RateLimitPeriod = 0
        # ServerTimeout = 30
        # SuppTimeout = 30
        # TxPeriod = 30
        # TimeToNextReauth = 17
        # ReAuthPeriod = 60
        # Supplicant = 54:BE:EF:FF:E5:E5
        # Authentication Method = EAP
        # ReAuthAction = Reauthenticate
        # Authenticated By = Remote Server
        # Auth SM State = AUTHENTICATED
        # Auth BEND SM State = IDLE
        p4 = re.compile(r'^(?P<key>[\-\s\w]+) +\= +(?P<value>(((\w)|(\())+((:\w+)|(\s\w+)|(.\w+))*)+(\))?)$')

        for line in out.splitlines():
            line = line.strip()

            # Sysauthcontrol Enabled
            m = p1.match(line)
            if m:
                sysControl = m.groupdict()['SysControl']
                bool = True if sysControl.lower() == 'enabled' else False
                ret_dict.setdefault("system_auth_control", bool)
                continue

            # Dot1x Protocol Version 2
            m = p2.match(line)
            if m:
                version = m.groupdict()['version']
                ret_dict.setdefault("version", int(version))
                continue
            
            # Dot1x Info for Ethernet1/2
            # Dot1x Info for Ethernet1/1
            m = p3.match(line)
            if m:
                intf = m.groupdict()['intf']
                ret_dict.setdefault("interfaces", {}).setdefault(intf, {}).setdefault('interface', intf)
                intf_dict = ret_dict.setdefault("interfaces", {}).setdefault(intf, {})
                continue

            m = p4.match(line)
            if m:
                value = m.groupdict()
                key = value['key'].strip()
                val = value['value'].lower()

                # PAE = AUTHENTICATOR
                if key.lower() == 'pae':
                    intf_dict.setdefault(key.lower(), val)

                elif key.lower() == 'credentials':
                    intf_dict.setdefault(key.lower(), val)

                elif key.lower() == 'maxreauthreq':
                    intf_dict.setdefault('max_reauth_req', int(val))
                
                # MaxReq = 3
                # MaxReq = 2
                elif key.lower() == 'maxreq':
                    intf_dict.setdefault('max_req', int(val))

                elif key.lower() == 'maxstart':
                    intf_dict.setdefault('max_start', int(val))

                # PortControl = AUTO
                # PortControl = FORCE_AUTH
                elif key.lower() == 'portcontrol':
                    intf_dict.setdefault('port_control', val)
                
                elif key.lower() == 'controldirection':
                    intf_dict.setdefault('control_direction', val)
                
                # ReAuthentication = Enabled
                # ReAuthentication = Disabled
                elif key.lower() == 'reauthentication':
                    bool = True if val == 'enabled' else False
                    intf_dict.setdefault('re_authentication', bool)

                # Port Status = AUTHORIZED
                elif key.lower() == 'port status':
                    intf_dict.setdefault('port_status', val)
                
                # HostMode = SINGLE HOST
                elif key.lower() == 'hostmode':
                    intf_dict.setdefault('host_mode', val)
                
                # ReAuthMax = 2
                elif key.lower() == 'reauthmax':
                    intf_dict.setdefault('re_auth_max', int(val))
                
                # Mac-Auth-Bypass = Disabled
                elif key.lower() == 'mac-auth-bypass':
                    bool = True if val == 'enabled' else False
                    intf_dict.setdefault('mac-auth-bypass', bool)

            ### Timeout ###

                elif key.lower() == 'authperiod':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('auth_period', int(val))
                
                elif key.lower() == 'held_period':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('held_period', int(val))
                
                # QuietPeriod = 60
                elif key.lower() == 'quietperiod':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('quiet_period', int(val))
                
                # RateLimitPeriod = 0
                elif key.lower() == 'ratelimitperiod':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('ratelimit_period', int(val))
                
                # ServerTimeout = 30
                elif key.lower() == 'servertimeout':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('server_timeout', int(val))

                elif key.lower() == 'startperiod':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('start_period', int(val))
                
                # SuppTimeout = 30
                elif key.lower() == 'supptimeout':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('supp_timeout', int(val))

                # TxPeriod = 30
                elif key.lower() == 'txperiod':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('tx_period', int(val))
                
                # ReAuthPeriod = 60
                elif key.lower() == 'reauthperiod':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('re_auth_period', int(val))
                
                # TimeToNextReauth = 17
                elif key.lower() == 'timetonextreauth':
                    if 'timeout' not in intf_dict:
                        timeout = intf_dict.setdefault('timeout', {})
                    timeout.setdefault('time_to_next_reauth', int(val))

            ### Clients ###

                # Supplicant = 54:BE:EF:FF:E5:E5
                elif key.lower() == 'supplicant':
                    client_dict = intf_dict.setdefault('clients', {}).setdefault(val, {})
                    client_dict['client'] = val
                    if eap_method:
                        client_dict['eap_method'] = eap_method
                    
                # EAP Method                = (13)
                elif key.lower() == 'eap method':
                    eap_method = val

                # Authentication Method = EAP
                elif key.lower() == 'authentication method':
                    client_dict.setdefault('auth_method', val)

            ### Session ###  
                # ReAuthAction = Reauthenticate
                elif key.lower() == 'reauthaction':
                    # if 'session' not in intf_dict: 
                    session_dict = client_dict.setdefault('session', {})
                    session_dict.setdefault('reauth_action', val)

                # Authenticated By = Remote Server
                elif key.lower() == 'authenticated by':
                    session_dict = client_dict.setdefault('session', {})
                    session_dict.setdefault('auth_by', val)

                elif key.lower() == 'session id':
                    session_dict = client_dict.setdefault('session', {})
                    session_dict.setdefault('session_id', val)

                # Auth SM State = AUTHENTICATED
                elif key.lower() == 'auth sm state':
                    session_dict = client_dict.setdefault('session', {})
                    session_dict.setdefault('auth_sm_state', val)

                # Auth BEND SM State = IDLE
                elif key.lower() == 'auth bend sm state':
                    session_dict = client_dict.setdefault('session', {})
                    session_dict.setdefault('auth_bend_sm_state', val)
            
        return ret_dict