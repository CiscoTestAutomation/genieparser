# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_l2route
from genie.libs.parser.iosxr.show_logging import ShowLogging


# ===========================================
#  Unit test for 'show logging'
# ===========================================
class TestShowLogging(unittest.TestCase):
    """Unit test for 'show logging'"""
    maxDiff = None

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    expected_output = {
        "syslog_logging": {
            "enabled": {
                "counters": {
                    "flushes": 0,
                    "messages_dropped": 0,
                    "overruns": 0
                }
            }
    },
        "logging": {
            "buffer": {
                "level": "debugging",
                "messages_logged": 114
            },
            "console": {
                "status": "Disabled"
            },
            "monitor": {
                "level": "debugging",
                "messages_logged": 0
            },
            "trap": {
                "level": "informational",
                "messages_logged": 0
            }
        },
        "log_buffer_bytes": 2097152,
        "logs": [
            "RP/0/RP0/CPU0:Sep 25 23:24:28.852 UTC: spp[113]: Initialized socket RX node",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.852 UTC: spp[113]: Initialized socket TX node",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.852 UTC: spp[113]: Registered socket plugin",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.929 UTC: spp[113]: Initialized punt classification node",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.929 UTC: spp[113]: Initialized client inject node",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.930 UTC: spp[113]: Registered XRv9k SPP plugin",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9920 (Punt/Inject crucial)",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9921 (Punt/Inject high)",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9922 (Punt/Inject medium)",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9923 (Punt/Inject low)",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.939 UTC: spp[113]: Opened raw socket on eth0 (Management)",
            "RP/0/RP0/CPU0:Sep 25 23:24:28.939 UTC: spp[113]: Successfully initialized socket devices",
            "RP/0/RP0/CPU0:Sep 25 23:24:29.114 UTC: syslogd[342]: %SECURITY-XR_SSL-6-INFO : XR SSL info: Setting fips register",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Pakman memory region 0x10000000 .. 0x18000000, size 128Mb (32 scale)",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 64000 particle of size 256",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 32000 particle of size 512",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 16000 particle of size 768",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 8000 particle of size 1648",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 3200 particle of size 2560",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 3200 particle of size 4608",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 960 particle of size 6240",
            "RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 1600 particle of size 512",
            "RP/0/RP0/CPU0:Sep 25 23:24:48.161 UTC: netio[202]: FINT (IFH 00000010) interface specification received",
            "RP/0/RP0/CPU0:Sep 25 23:24:48.161 UTC: netio[202]: Attached to IFH 00000010 IDB (FINT0_RP0_CPU0)",
            "RP/0/RP0/CPU0:Sep 25 23:24:51.562 UTC: fib_mgr[364]: RC for sysdb_bind wrt \"/cfg/gl/pdcef/lba/hash/fields/mpls/\" is 0x0",
            "RP/0/RP0/CPU0:Sep 25 23:24:51.564 UTC: fib_mgr[364]: RC for sysdb_register_notification wrt \"mpls_entropy-label\" is 0x0",
            "RP/0/RP0/CPU0:Sep 25 23:24:51.566 UTC: fib_mgr[364]: RC for sysdb_register_verification wrt \"mpls_entropy-label\" is 0x0",
            "RP/0/RP0/CPU0:Sep 25 23:24:51.572 UTC: fib_mgr[364]: ss_fib_plat_cfg_hash_fields_ipv6_flow_label_register - sysdb_bind for /cfg/gl/pdcef/lba/hash/fields/ipv6/ succeeded. rc: 0x0",
            "RP/0/RP0/CPU0:Sep 25 23:24:54.958 UTC: iedged[409]: debug_register per_flow successful",
            "RP/0/RP0/CPU0:Sep 25 23:24:55.044 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:24:55.044 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:24:57.134 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:24:57.625 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:25:02.828 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:25:04.832 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:25:09.253 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:25:09.253 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:25:10.057 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:25:10.057 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:25:11.091 UTC: ipsub_ma[169]: debug_register per_flow successful",
            "RP/0/RP0/CPU0:Sep 25 23:25:18.815 UTC: pppoe_ma[217]: debug_register per_flow successful",
            "RP/0/RP0/CPU0:Sep 25 23:25:19.020 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:25:19.020 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:25:20.470 UTC: cepki[363]: %SECURITY-PKI-6-LOG_INFO_DETAIL : FIPS POST Successful for  cepki",
            "RP/0/RP0/CPU0:Sep 25 23:25:22.669 UTC: PPP-MA[406]: debug_register per_flow successful",
            "0/RP0/ADMIN0:Sep 25 23:25:25.856 UTC: wd_diskmon[3204]: %INFRA-WD_DISKMON_SYSADMIN-4-DISK_WARN : Sysadmin: Device: /var/log Usage %: 84 , State: MINOR, MINOR Threshold %: 80",
            "RP/0/RP0/CPU0:Sep 25 23:25:28.866 UTC: ipsec_mp[385]: %SECURITY-IMP-6-PROC_READY : Process ipsec_mp is ready",
            "RP/0/RP0/CPU0:Sep 25 23:25:29.370 UTC: pim6[1254]: %ROUTING-IPV4_PIM-5-HA_NOTICE : NSR not ready",
            "RP/0/RP0/CPU0:Sep 25 23:25:30.045 UTC: cepki[363]: %SECURITY-CEPKI-6-KEY_INFO : One or more host keypairs exist. Not auto-generating keypairs.",
            "RP/0/RP0/CPU0:Sep 25 23:25:31.533 UTC: kim[213]: %INFRA-KIM-6-LOG_INFO : XR statistics will be pushed into the Linux kernel at 1 second intervals",
            "RP/0/RP0/CPU0:Sep 25 23:25:32.821 UTC: smartlicserver[186]: SMART_LIC-6-EXPORT_CONTROLLED:Usage of export controlled features is not allowed",
            "RP/0/RP0/CPU0:Sep 25 23:25:34.886 UTC: smartlicserver[186]: SMART_LIC-6-AGENT_READY:Smart Agent for Licensing is initialized",
            "RP/0/RP0/CPU0:Sep 25 23:25:34.886 UTC: smartlicserver[186]: SMART_LIC-6-AGENT_ENABLED:Smart Agent for Licensing is enabled",
            "RP/0/RP0/CPU0:Sep 25 23:25:34.995 UTC: smartlicserver[186]: SMART_LIC-6-EXPORT_CONTROLLED:Usage of export controlled features is not allowed",
            "RP/0/RP0/CPU0:Sep 25 23:25:35.161 UTC: plat_sl_client[344]: %LICENSE-PLAT_CLIENT-6-STATE_CHANGE : Licensing platform state changing from UNKNOWN to UNREGISTERED",
            "RP/0/RP0/CPU0:Sep 25 23:25:43.320 UTC: pim[1253]: %ROUTING-IPV4_PIM-5-HA_NOTICE : NSR not ready",
            "RP/0/RP0/CPU0:Sep 25 23:25:48.725 UTC: syslog_dev[119]: attestation_agent[1273] PID-4484: attestation_agent: no process found",
            "RP/0/RP0/CPU0:Sep 25 23:26:02.458 UTC: ospfv3[1046]: %ROUTING-OSPFv3-5-HA_NOTICE_START : Starting OSPFv3",
            "RP/0/RP0/CPU0:Sep 25 23:26:03.920 UTC: ospfv3[1046]: %ROUTING-OSPFv3-5-HA_NOTICE : Process 1: OSPFv3 process initialization complete",
            "RP/0/RP0/CPU0:Sep 25 23:26:04.009 UTC: ospfv3[1046]: %ROUTING-OSPFv3-5-HA_NOTICE : Process 1: Signaled PROC_AVAILABLE",
            "RP/0/RP0/CPU0:Sep 25 23:26:04.166 UTC: ospf[1027]: %ROUTING-OSPF-5-HA_NOTICE_START : Starting OSPF",
            "RP/0/RP0/CPU0:Sep 25 23:26:04.614 UTC: isis[1012]: %ROUTING-ISIS-5-NSR_PM_ROLE_CHG : ISIS NSR PM role change, reg-type 0, HA-role: , 1",
            "RP/0/RP0/CPU0:Sep 25 23:26:04.809 UTC: isis[1011]: %ROUTING-ISIS-5-NSR_PM_ROLE_CHG : ISIS NSR PM role change, reg-type 0, HA-role: , 1",
            "RP/0/RP0/CPU0:Sep 25 23:26:06.241 UTC: isis[1012]: %ROUTING-ISIS-6-INFO_STARTUP_START : Cold controlled start beginning",
            "RP/0/RP0/CPU0:Sep 25 23:26:06.246 UTC: ospf[1027]: %ROUTING-OSPF-6-HA_INFO : Process 1: OSPF process initialization complete",
            "RP/0/RP0/CPU0:Sep 25 23:26:06.443 UTC: ospf[1027]: %ROUTING-OSPF-5-HA_NOTICE : Process 1: Signaled PROC_AVAILABLE",
            "RP/0/RP0/CPU0:Sep 25 23:26:06.543 UTC: isis[1011]: %ROUTING-ISIS-6-INFO_STARTUP_START : Cold controlled start beginning",
            "0/RP0/ADMIN0:Sep 25 23:26:10.603 UTC: aaad[3149]: %MGBL-AAAD-7-DEBUG :  Not allowing to sync from XR VM to Admin VM after first user creation.",
            "RP/0/RP0/CPU0:Sep 25 23:26:14.008 UTC: emsd[1114]: %MGBL-EMS-6-EMSD_SERVICE_START : emsd service start",
            "RP/0/RP0/CPU0:Sep 25 23:26:14.008 UTC: emsd[1114]: gRPC is secure with TLS",
            "RP/0/RP0/CPU0:Sep 25 23:26:15.539 UTC: bpm[1093]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : bpm-active:(bgp-bpm-active)inst-id 0, Service Published",
            "RP/0/RP0/CPU0:Sep 25 23:26:15.803 UTC: exec[67271]: %MGBL-exec-3-LOGIN_AUTHEN : Login Authentication failed. Exiting...",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.762 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.762 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.764 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.764 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:26:17.764 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].",
            "RP/0/RP0/CPU0:Sep 25 23:26:18.198 UTC: ifmgr[189]: %PKT_INFRA-LINK-3-UPDOWN : Interface MgmtEth0/RP0/CPU0/0, changed state to Down",
            "RP/0/RP0/CPU0:Sep 25 23:26:18.198 UTC: ifmgr[189]: %PKT_INFRA-LINEPROTO-5-UPDOWN : Line protocol on Interface MgmtEth0/RP0/CPU0/0, changed state to Down",
            "RP/0/RP0/CPU0:Sep 25 23:26:18.202 UTC: cfgmgr-rp[247]: %MGBL-CONFIG-6-OIR_RESTORE : Configuration for node '0/RP0/CPU0' has been restored.",
            "RP/0/RP0/CPU0:Sep 25 23:26:18.276 UTC: ifmgr[189]: %PKT_INFRA-LINK-3-UPDOWN : Interface MgmtEth0/RP0/CPU0/0, changed state to Up",
            "RP/0/RP0/CPU0:Sep 25 23:26:18.278 UTC: ifmgr[189]: %PKT_INFRA-LINEPROTO-5-UPDOWN : Line protocol on Interface MgmtEth0/RP0/CPU0/0, changed state to Up",
            "RP/0/RP0/CPU0:Sep 25 23:26:18.594 UTC: smartlicserver[186]: SMART_LIC-6-EXPORT_CONTROLLED:Usage of export controlled features is not allowed",
            "RP/0/RP0/CPU0:Sep 25 23:26:19.268 UTC: bpm[1093]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : bpm-default:(A)inst-id 0, Connection Open",
            "RP/0/RP0/CPU0:Sep 25 23:26:19.674 UTC: bgp[1078]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : default, process instance 1:(A)inst-id 0, Connection Establised",
            "RP/0/RP0/CPU0:Sep 25 23:26:19.822 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:19.822 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:19.822 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].",
            "RP/0/RP0/CPU0:Sep 25 23:26:20.264 UTC: bgp[1078]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : default:(A)inst-id 0, Initial Config Done",
            "RP/0/RP0/CPU0:Sep 25 23:26:22.016 UTC: isis[1011]: %ROUTING-ISIS-6-INFO_STARTUP_FINISH : Cold controlled start completed",
            "RP/0/RP0/CPU0:Sep 25 23:26:23.522 UTC: isis[1012]: %ROUTING-ISIS-6-INFO_STARTUP_FINISH : Cold controlled start completed",
            "RP/0/RP0/CPU0:Sep 25 23:26:46.668 UTC: syslog_dev[119]: ztp[133] PID-4191: ZTP will now run in the background.",
            "RP/0/RP0/CPU0:Sep 25 23:26:46.668 UTC: syslog_dev[119]: ztp[133] PID-4191: ZTP might bring up the interfaces if they are in shutdown state.",
            "RP/0/RP0/CPU0:Sep 25 23:26:46.668 UTC: syslog_dev[119]: ztp[133] PID-4191: Please use \"show logging\" or look at /var/log/ztp.log to check progress.",
            "RP/0/RP0/CPU0:Sep 25 23:26:46.790 UTC: ZTP[67506]: %OS-SYSLOG-6-LOG_INFO : ZTP running in background",
            "RP/0/RP0/CPU0:Sep 25 23:27:17.623 UTC: exec[67679]: %SECURITY-LOGIN-6-AUTHEN_SUCCESS : Successfully authenticated user 'admin' from 'console' on 'con0_RP0_CPU0'",
            "RP/0/RP0/CPU0:Sep 25 23:27:22.691 UTC: config[67726]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000024' to view the changes.",
            "RP/0/RP0/CPU0:Sep 25 23:27:22.997 UTC: config[67726]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin",
            "0/RP0/ADMIN0:Sep 25 23:27:53.784 UTC: dumper[3156]: %INFRA-CALVADOS_DUMPER-6-HOST_COPY_SUCCESS : Copied host file /misc/scratch/core/default-sdr--1.20200925-232222.core.RP.lxcdump.tar.lz4 to 0/RP0:/misc/disk1",
            "0/RP0/ADMIN0:Sep 25 23:27:53.892 UTC: dumper[3156]: %INFRA-CALVADOS_DUMPER-6-HOST_REMV_SUCCESS : Deleted HostOS file /misc/scratch/core/default-sdr--1.20200925-232222.core.RP.lxcdump.tar.lz4",
            "RP/0/RP0/CPU0:Sep 25 23:28:57.463 UTC: config[68848]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000025' to view the changes.",
            "RP/0/RP0/CPU0:Sep 25 23:28:57.781 UTC: config[68848]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin",
            "RP/0/RP0/CPU0:Sep 25 23:30:54.216 UTC: config[69226]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000026' to view the changes.",
            "RP/0/RP0/CPU0:Sep 25 23:30:54.587 UTC: config[69226]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin",
            "RP/0/RP0/CPU0:Sep 25 23:31:34.897 UTC: config[69352]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000027' to view the changes.",
            "RP/0/RP0/CPU0:Sep 25 23:31:35.276 UTC: config[69352]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin",
            "RP/0/RP0/CPU0:Sep 25 23:32:59.081 UTC: config[69570]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000028' to view the changes.",
            "RP/0/RP0/CPU0:Sep 25 23:32:59.395 UTC: config[69570]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin",
            "RP/0/RP0/CPU0:Sep 25 23:34:19.268 UTC: config[65700]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000029' to view the changes.",
            "RP/0/RP0/CPU0:Sep 25 23:34:19.600 UTC: config[65700]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin",
            "RP/0/RP0/CPU0:R2_xr#"
        ]
    }
    device_output = {'execute.return_value': '''
        show logging
        Fri Sep 25 23:34:26.169 UTC
        Syslog logging: enabled (0 messages dropped, 0 flushes, 0 overruns)
            Console logging: Disabled
            Monitor logging: level debugging, 0 messages logged
            Trap logging: level informational, 0 messages logged
            Buffer logging: level debugging, 114 messages logged

        Log Buffer (2097152 bytes):

        RP/0/RP0/CPU0:Sep 25 23:24:28.852 UTC: spp[113]: Initialized socket RX node
        RP/0/RP0/CPU0:Sep 25 23:24:28.852 UTC: spp[113]: Initialized socket TX node
        RP/0/RP0/CPU0:Sep 25 23:24:28.852 UTC: spp[113]: Registered socket plugin
        RP/0/RP0/CPU0:Sep 25 23:24:28.929 UTC: spp[113]: Initialized punt classification node
        RP/0/RP0/CPU0:Sep 25 23:24:28.929 UTC: spp[113]: Initialized client inject node
        RP/0/RP0/CPU0:Sep 25 23:24:28.930 UTC: spp[113]: Registered XRv9k SPP plugin
        RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9920 (Punt/Inject crucial)
        RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9921 (Punt/Inject high)
        RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9922 (Punt/Inject medium)
        RP/0/RP0/CPU0:Sep 25 23:24:28.932 UTC: spp[113]: Opened UDP socket at 172.16.4.1:9923 (Punt/Inject low)
        RP/0/RP0/CPU0:Sep 25 23:24:28.939 UTC: spp[113]: Opened raw socket on eth0 (Management)
        RP/0/RP0/CPU0:Sep 25 23:24:28.939 UTC: spp[113]: Successfully initialized socket devices
        RP/0/RP0/CPU0:Sep 25 23:24:29.114 UTC: syslogd[342]: %SECURITY-XR_SSL-6-INFO : XR SSL info: Setting fips register
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Pakman memory region 0x10000000 .. 0x18000000, size 128Mb (32 scale)
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 64000 particle of size 256
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 32000 particle of size 512
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 16000 particle of size 768
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 8000 particle of size 1648
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 3200 particle of size 2560
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 3200 particle of size 4608
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 960 particle of size 6240
        RP/0/RP0/CPU0:Sep 25 23:24:31.124 UTC: platform_packet_partner[173]: Creating 1600 particle of size 512
        RP/0/RP0/CPU0:Sep 25 23:24:48.161 UTC: netio[202]: FINT (IFH 00000010) interface specification received
        RP/0/RP0/CPU0:Sep 25 23:24:48.161 UTC: netio[202]: Attached to IFH 00000010 IDB (FINT0_RP0_CPU0)
        RP/0/RP0/CPU0:Sep 25 23:24:51.562 UTC: fib_mgr[364]: RC for sysdb_bind wrt "/cfg/gl/pdcef/lba/hash/fields/mpls/" is 0x0
        RP/0/RP0/CPU0:Sep 25 23:24:51.564 UTC: fib_mgr[364]: RC for sysdb_register_notification wrt "mpls_entropy-label" is 0x0
        RP/0/RP0/CPU0:Sep 25 23:24:51.566 UTC: fib_mgr[364]: RC for sysdb_register_verification wrt "mpls_entropy-label" is 0x0
        RP/0/RP0/CPU0:Sep 25 23:24:51.572 UTC: fib_mgr[364]: ss_fib_plat_cfg_hash_fields_ipv6_flow_label_register - sysdb_bind for /cfg/gl/pdcef/lba/hash/fields/ipv6/ succeeded. rc: 0x0
        RP/0/RP0/CPU0:Sep 25 23:24:54.958 UTC: iedged[409]: debug_register per_flow successful
        RP/0/RP0/CPU0:Sep 25 23:24:55.044 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:24:55.044 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:24:57.134 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:24:57.625 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:25:02.828 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:25:04.832 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:25:09.253 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:25:09.253 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:25:10.057 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:25:10.057 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:25:11.091 UTC: ipsub_ma[169]: debug_register per_flow successful
        RP/0/RP0/CPU0:Sep 25 23:25:18.815 UTC: pppoe_ma[217]: debug_register per_flow successful
        RP/0/RP0/CPU0:Sep 25 23:25:19.020 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V4 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:25:19.020 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:25:20.470 UTC: cepki[363]: %SECURITY-PKI-6-LOG_INFO_DETAIL : FIPS POST Successful for  cepki
        RP/0/RP0/CPU0:Sep 25 23:25:22.669 UTC: PPP-MA[406]: debug_register per_flow successful
        0/RP0/ADMIN0:Sep 25 23:25:25.856 UTC: wd_diskmon[3204]: %INFRA-WD_DISKMON_SYSADMIN-4-DISK_WARN : Sysadmin: Device: /var/log Usage %: 84 , State: MINOR, MINOR Threshold %: 80
        RP/0/RP0/CPU0:Sep 25 23:25:28.866 UTC: ipsec_mp[385]: %SECURITY-IMP-6-PROC_READY : Process ipsec_mp is ready
        RP/0/RP0/CPU0:Sep 25 23:25:29.370 UTC: pim6[1254]: %ROUTING-IPV4_PIM-5-HA_NOTICE : NSR not ready
        RP/0/RP0/CPU0:Sep 25 23:25:30.045 UTC: cepki[363]: %SECURITY-CEPKI-6-KEY_INFO : One or more host keypairs exist. Not auto-generating keypairs.
        RP/0/RP0/CPU0:Sep 25 23:25:31.533 UTC: kim[213]: %INFRA-KIM-6-LOG_INFO : XR statistics will be pushed into the Linux kernel at 1 second intervals
        RP/0/RP0/CPU0:Sep 25 23:25:32.821 UTC: smartlicserver[186]: SMART_LIC-6-EXPORT_CONTROLLED:Usage of export controlled features is not allowed
        RP/0/RP0/CPU0:Sep 25 23:25:34.886 UTC: smartlicserver[186]: SMART_LIC-6-AGENT_READY:Smart Agent for Licensing is initialized
        RP/0/RP0/CPU0:Sep 25 23:25:34.886 UTC: smartlicserver[186]: SMART_LIC-6-AGENT_ENABLED:Smart Agent for Licensing is enabled
        RP/0/RP0/CPU0:Sep 25 23:25:34.995 UTC: smartlicserver[186]: SMART_LIC-6-EXPORT_CONTROLLED:Usage of export controlled features is not allowed
        RP/0/RP0/CPU0:Sep 25 23:25:35.161 UTC: plat_sl_client[344]: %LICENSE-PLAT_CLIENT-6-STATE_CHANGE : Licensing platform state changing from UNKNOWN to UNREGISTERED
        RP/0/RP0/CPU0:Sep 25 23:25:43.320 UTC: pim[1253]: %ROUTING-IPV4_PIM-5-HA_NOTICE : NSR not ready
        RP/0/RP0/CPU0:Sep 25 23:25:48.725 UTC: syslog_dev[119]: attestation_agent[1273] PID-4484: attestation_agent: no process found
        RP/0/RP0/CPU0:Sep 25 23:26:02.458 UTC: ospfv3[1046]: %ROUTING-OSPFv3-5-HA_NOTICE_START : Starting OSPFv3
        RP/0/RP0/CPU0:Sep 25 23:26:03.920 UTC: ospfv3[1046]: %ROUTING-OSPFv3-5-HA_NOTICE : Process 1: OSPFv3 process initialization complete
        RP/0/RP0/CPU0:Sep 25 23:26:04.009 UTC: ospfv3[1046]: %ROUTING-OSPFv3-5-HA_NOTICE : Process 1: Signaled PROC_AVAILABLE
        RP/0/RP0/CPU0:Sep 25 23:26:04.166 UTC: ospf[1027]: %ROUTING-OSPF-5-HA_NOTICE_START : Starting OSPF
        RP/0/RP0/CPU0:Sep 25 23:26:04.614 UTC: isis[1012]: %ROUTING-ISIS-5-NSR_PM_ROLE_CHG : ISIS NSR PM role change, reg-type 0, HA-role: , 1
        RP/0/RP0/CPU0:Sep 25 23:26:04.809 UTC: isis[1011]: %ROUTING-ISIS-5-NSR_PM_ROLE_CHG : ISIS NSR PM role change, reg-type 0, HA-role: , 1
        RP/0/RP0/CPU0:Sep 25 23:26:06.241 UTC: isis[1012]: %ROUTING-ISIS-6-INFO_STARTUP_START : Cold controlled start beginning
        RP/0/RP0/CPU0:Sep 25 23:26:06.246 UTC: ospf[1027]: %ROUTING-OSPF-6-HA_INFO : Process 1: OSPF process initialization complete
        RP/0/RP0/CPU0:Sep 25 23:26:06.443 UTC: ospf[1027]: %ROUTING-OSPF-5-HA_NOTICE : Process 1: Signaled PROC_AVAILABLE
        RP/0/RP0/CPU0:Sep 25 23:26:06.543 UTC: isis[1011]: %ROUTING-ISIS-6-INFO_STARTUP_START : Cold controlled start beginning
        0/RP0/ADMIN0:Sep 25 23:26:10.603 UTC: aaad[3149]: %MGBL-AAAD-7-DEBUG :  Not allowing to sync from XR VM to Admin VM after first user creation.
        RP/0/RP0/CPU0:Sep 25 23:26:14.008 UTC: emsd[1114]: %MGBL-EMS-6-EMSD_SERVICE_START : emsd service start
        RP/0/RP0/CPU0:Sep 25 23:26:14.008 UTC: emsd[1114]: gRPC is secure with TLS
        RP/0/RP0/CPU0:Sep 25 23:26:15.539 UTC: bpm[1093]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : bpm-active:(bgp-bpm-active)inst-id 0, Service Published
        RP/0/RP0/CPU0:Sep 25 23:26:15.803 UTC: exec[67271]: %MGBL-exec-3-LOGIN_AUTHEN : Login Authentication failed. Exiting...
        RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:17.761 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:17.762 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V4 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:17.762 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:17.764 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:26:17.764 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:26:17.764 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is not ready. Reason: [V6 Subscriber infra process(es) is unavailable].
        RP/0/RP0/CPU0:Sep 25 23:26:18.198 UTC: ifmgr[189]: %PKT_INFRA-LINK-3-UPDOWN : Interface MgmtEth0/RP0/CPU0/0, changed state to Down
        RP/0/RP0/CPU0:Sep 25 23:26:18.198 UTC: ifmgr[189]: %PKT_INFRA-LINEPROTO-5-UPDOWN : Line protocol on Interface MgmtEth0/RP0/CPU0/0, changed state to Down
        RP/0/RP0/CPU0:Sep 25 23:26:18.202 UTC: cfgmgr-rp[247]: %MGBL-CONFIG-6-OIR_RESTORE : Configuration for node '0/RP0/CPU0' has been restored.
        RP/0/RP0/CPU0:Sep 25 23:26:18.276 UTC: ifmgr[189]: %PKT_INFRA-LINK-3-UPDOWN : Interface MgmtEth0/RP0/CPU0/0, changed state to Up
        RP/0/RP0/CPU0:Sep 25 23:26:18.278 UTC: ifmgr[189]: %PKT_INFRA-LINEPROTO-5-UPDOWN : Line protocol on Interface MgmtEth0/RP0/CPU0/0, changed state to Up
        RP/0/RP0/CPU0:Sep 25 23:26:18.594 UTC: smartlicserver[186]: SMART_LIC-6-EXPORT_CONTROLLED:Usage of export controlled features is not allowed
        RP/0/RP0/CPU0:Sep 25 23:26:19.268 UTC: bpm[1093]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : bpm-default:(A)inst-id 0, Connection Open
        RP/0/RP0/CPU0:Sep 25 23:26:19.674 UTC: bgp[1078]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : default, process instance 1:(A)inst-id 0, Connection Establised
        RP/0/RP0/CPU0:Sep 25 23:26:19.822 UTC: pppoe_ma[217]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:19.822 UTC: ipsub_ma[169]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:19.822 UTC: iedged[409]: %SUBSCRIBER-SUB_UTIL-5-SESSION_THROTTLE : Subscriber Infra is ready. Reason: [V6 Subscriber infra process(es) is available].
        RP/0/RP0/CPU0:Sep 25 23:26:20.264 UTC: bgp[1078]: %ROUTING-BGP-5-ASYNC_IPC_STATUS : default:(A)inst-id 0, Initial Config Done
        RP/0/RP0/CPU0:Sep 25 23:26:22.016 UTC: isis[1011]: %ROUTING-ISIS-6-INFO_STARTUP_FINISH : Cold controlled start completed
        RP/0/RP0/CPU0:Sep 25 23:26:23.522 UTC: isis[1012]: %ROUTING-ISIS-6-INFO_STARTUP_FINISH : Cold controlled start completed
        RP/0/RP0/CPU0:Sep 25 23:26:46.668 UTC: syslog_dev[119]: ztp[133] PID-4191: ZTP will now run in the background.
        RP/0/RP0/CPU0:Sep 25 23:26:46.668 UTC: syslog_dev[119]: ztp[133] PID-4191: ZTP might bring up the interfaces if they are in shutdown state.
        RP/0/RP0/CPU0:Sep 25 23:26:46.668 UTC: syslog_dev[119]: ztp[133] PID-4191: Please use "show logging" or look at /var/log/ztp.log to check progress.
        RP/0/RP0/CPU0:Sep 25 23:26:46.790 UTC: ZTP[67506]: %OS-SYSLOG-6-LOG_INFO : ZTP running in background
        RP/0/RP0/CPU0:Sep 25 23:27:17.623 UTC: exec[67679]: %SECURITY-LOGIN-6-AUTHEN_SUCCESS : Successfully authenticated user 'admin' from 'console' on 'con0_RP0_CPU0'
        RP/0/RP0/CPU0:Sep 25 23:27:22.691 UTC: config[67726]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000024' to view the changes.
        RP/0/RP0/CPU0:Sep 25 23:27:22.997 UTC: config[67726]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin
        0/RP0/ADMIN0:Sep 25 23:27:53.784 UTC: dumper[3156]: %INFRA-CALVADOS_DUMPER-6-HOST_COPY_SUCCESS : Copied host file /misc/scratch/core/default-sdr--1.20200925-232222.core.RP.lxcdump.tar.lz4 to 0/RP0:/misc/disk1
        0/RP0/ADMIN0:Sep 25 23:27:53.892 UTC: dumper[3156]: %INFRA-CALVADOS_DUMPER-6-HOST_REMV_SUCCESS : Deleted HostOS file /misc/scratch/core/default-sdr--1.20200925-232222.core.RP.lxcdump.tar.lz4
        RP/0/RP0/CPU0:Sep 25 23:28:57.463 UTC: config[68848]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000025' to view the changes.
        RP/0/RP0/CPU0:Sep 25 23:28:57.781 UTC: config[68848]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin
        RP/0/RP0/CPU0:Sep 25 23:30:54.216 UTC: config[69226]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000026' to view the changes.
        RP/0/RP0/CPU0:Sep 25 23:30:54.587 UTC: config[69226]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin
        RP/0/RP0/CPU0:Sep 25 23:31:34.897 UTC: config[69352]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000027' to view the changes.
        RP/0/RP0/CPU0:Sep 25 23:31:35.276 UTC: config[69352]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin
        RP/0/RP0/CPU0:Sep 25 23:32:59.081 UTC: config[69570]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000028' to view the changes.
        RP/0/RP0/CPU0:Sep 25 23:32:59.395 UTC: config[69570]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin
        RP/0/RP0/CPU0:Sep 25 23:34:19.268 UTC: config[65700]: %MGBL-CONFIG-6-DB_COMMIT : Configuration committed by user 'admin'. Use 'show configuration commit changes 1000000029' to view the changes.
        RP/0/RP0/CPU0:Sep 25 23:34:19.600 UTC: config[65700]: %MGBL-SYS-5-CONFIG_I : Configured from console by admin
        RP/0/RP0/CPU0:R2_xr#
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLogging(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.device_output)
        obj = ShowLogging(device=self.device)

        parsed_output = obj.parse()

        self.assertEqual(parsed_output, self.expected_output)

if __name__ == '__main__':
    unittest.main()
