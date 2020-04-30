import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_version import ShowVersionDetail,\
                                                 ShowVersionDetailNoForarding,\
                                                 ShowVersionInvokeOnAllRoutingEngines

class TestShowVersionDetail(unittest.TestCase):
    """ Unit tests for:
            * show version detail
    """

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
        show version detail
        Hostname: sr_hktGCS001
        Model: vmx
        Junos: 19.2R1.8
        JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]
        JUNOS OS libs [20190517.f0321c3_builder_stable_11]
        JUNOS OS runtime [20190517.f0321c3_builder_stable_11]
        JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]
        JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]
        JUNOS libs [20190621.152752_builder_junos_192_r1]
        JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]
        JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]
        JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]
        JUNOS runtime [20190621.152752_builder_junos_192_r1]
        JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]
        JUNOS sflow mx [20190621.152752_builder_junos_192_r1]
        JUNOS py extensions [20190621.152752_builder_junos_192_r1]
        JUNOS py base [20190621.152752_builder_junos_192_r1]
        JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]
        JUNOS OS crypto [20190517.f0321c3_builder_stable_11]
        JUNOS na telemetry [19.2R1.8]
        JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]
        JUNOS mx runtime [20190621.152752_builder_junos_192_r1]
        JUNOS common platform support [20190621.152752_builder_junos_192_r1]
        JUNOS Openconfig [19.2R1.8]
        JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]
        JUNOS modules [20190621.152752_builder_junos_192_r1]
        JUNOS mx modules [20190621.152752_builder_junos_192_r1]
        JUNOS mx libs [20190621.152752_builder_junos_192_r1]
        JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]
        JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]
        JUNOS daemons [20190621.152752_builder_junos_192_r1]
        JUNOS mx daemons [20190621.152752_builder_junos_192_r1]
        JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]
        JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]
        JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]
        JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]
        JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]
        JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]
        JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]
        JUNOS Services SSL [20190621.152752_builder_junos_192_r1]
        JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]
        JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]
        JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]
        JUNOS Services RPM [20190621.152752_builder_junos_192_r1]
        JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]
        JUNOS Services NAT [20190621.152752_builder_junos_192_r1]
        JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]
        JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]
        JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]
        JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]
        JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]
        JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]
        JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]
        JUNOS Services IDS [20190621.152752_builder_junos_192_r1]
        JUNOS IDP Services [20190621.152752_builder_junos_192_r1]
        JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]
        JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]
        JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]
        JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]
        JUNOS Services COS [20190621.152752_builder_junos_192_r1]
        JUNOS AppId Services [20190621.152752_builder_junos_192_r1]
        JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]
        JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]
        JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]
        JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]
        JUNOS J-Insight [20190621.152752_builder_junos_192_r1]
        JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]
        JUNOS jail runtime [20190517.f0321c3_builder_stable_11]
        KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built
        MGD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:49 UTC
        CLI release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:55:22 UTC
        JLAUNCHD release 19.2R1.8 built by builder on 2019-06-21 17:47:00 UTC
        RPD release 19.2R1.8 built by builder on 2019-06-22 01:02:12 UTC
        CHASSISD release 19.2R1.8 built by builder on 2019-06-21 21:24:54 UTC
        COMMIT-SYNCD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:46 UTC
        BFDD release 19.2R1.8 built by builder on 2019-06-21 20:28:12 UTC
        JNUD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:47 UTC
        DFWD release 19.2R1.8 built by builder on 2019-06-21 20:28:35 UTC
        DCD release 19.2R1.8 built by builder on 2019-06-21 20:27:41 UTC
        SNMPD release 19.2R1.8 built by builder on 2019-06-21 21:03:26 UTC
        ALARM-MGMTD release 19.2R1.8 built by builder on 2019-06-21 21:03:22 UTC
        MIB2D release 19.2R1.8 built by builder on 2019-06-21 21:07:04 UTC
        APSD release 19.2R1.8 built by builder on 2019-06-21 20:28:33 UTC
        VRRPD release 19.2R1.8 built by builder on 2019-06-21 20:30:14 UTC
        ALARMD release 19.2R1.8 built by builder on 2019-06-21 20:56:00 UTC
        PFED release 19.2R1.8 built by builder on 2019-06-21 20:59:01 UTC
        AGENTD release 19.2R1.8 built by builder on 2019-06-21 20:33:19 UTC
        CRAFTD release 19.2R1.8 built by builder on 2019-06-21 20:28:34 UTC
        SAMPLED release 19.2R1.8 built by builder on 2019-06-21 20:34:16 UTC
        SRRD release 19.2R1.8 built by builder on 2019-06-21 20:25:57 UTC
        JFLOWD release 19.2R1.8 built by builder on 2019-06-21 20:25:10 UTC
        ILMID release 19.2R1.8 built by builder on 2019-06-21 20:28:40 UTC
        RMOPD release 19.2R1.8 built by builder on 2019-06-21 20:28:30 UTC
        COSD release 19.2R1.8 built by builder on 2019-06-21 21:00:26 UTC
        FSAD release 19.2R1.8 built by builder on 2019-06-21 20:24:41 UTC
        IRSD release 19.2R1.8 built by builder on 2019-06-21 20:27:00 UTC
        FUD release 19.2R1.8 built by builder on 2019-06-21 20:24:41 UTC
        RTSPD release 19.2R1.8 built by builder on 2019-06-21 18:55:26 UTC
        smartd 6.4 2015-06-04 r4109 [FreeBSD JNPR-11.0-20190517.f0321c3_buil amd64] Junos Build
        Copyright (C) 2002-15, Bruce Allen, Christian Franke, www.smartmontools.org
        KSYNCD release 19.2R1.8 built by builder on 2019-06-21 18:51:23 UTC
        SPD release 19.2R1.8 built by builder on 2019-06-21 20:57:57 UTC
        JL2TPD release 19.2R1.8 built by builder on 2019-06-21 20:33:03 UTC
        JPPPOED release 19.2R1.8 built by builder on 2019-06-21 20:33:03 UTC
        RDD release 19.2R1.8 built by builder on 2019-06-21 20:27:29 UTC
        PPPD release 19.2R1.8 built by builder on 2019-06-21 20:24:45 UTC
        DFCD release 19.2R1.8 built by builder on 2019-06-21 20:28:34 UTC
        LACPD release 19.2R1.8 built by builder on 2019-06-21 20:28:56 UTC
        LFMD release 19.2R1.8 built by builder on 2019-06-21 20:28:57 UTC
        OAMD release 19.2R1.8 built by builder on 2019-06-21 20:29:03 UTC
        TNETD release 19.2R1.8 built by builder on 2019-06-21 17:38:55 UTC
        CFMD release 19.2R1.8 built by builder on 2019-06-21 20:58:51 UTC
        JDHCPD release 19.2R1.8 built by builder on 2019-06-21 20:33:00 UTC
        JSAVALD release 19.2R1.8 built by builder on 2019-06-21 20:26:50 UTC
        PSSD release 19.2R1.8 built by builder on 2019-06-21 20:25:11 UTC
        MSPD release 19.2R1.8 built by builder on 2019-06-21 20:25:11 UTC
        AUTHD release 19.2R1.8 built by builder on 2019-06-21 21:02:00 UTC
        PMOND release 19.2R1.8 built by builder on 2019-06-21 20:39:54 UTC
        AUTOCONFD release 19.2R1.8 built by builder on 2019-06-21 20:32:51 UTC
        BBE-SMGD release 19.2R1.8 built by builder on 2019-06-21 20:59:56 UTC
        JDIAMETERD release 19.2R1.8 built by builder on 2019-06-21 20:33:00 UTC
        BDBREPD release 19.2R1.8 built by builder on 2019-06-21 20:27:25 UTC
        APPIDD release 19.2R1.8 built by builder on 2019-06-21 20:56:15 UTC
        JPPPD release 19.2R1.8 built by builder on 2019-06-21 20:33:48 UTC
        JSSCD release 19.2R1.8 built by builder on 2019-06-21 20:33:50 UTC
        ICCPD release 19.2R1.8 built by builder on 2019-06-21 20:15:11 UTC
        MCLAG-CFGCHKD release 19.2R1.8 built by builder on 2019-06-21 20:58:06 UTC
        SHM-RTSDBD release 19.2R1.8 built by builder on 2019-06-21 20:32:30 UTC
        DATAPATH-TRACED release 19.2R1.8 built by builder on 2019-06-21 20:25:07 UTC
        CPCDD release 19.2R1.8 built by builder on 2019-06-21 20:33:39 UTC
        SMID release 19.2R1.8 built by builder on 2019-06-21 20:56:05 UTC
        SMIHELPERD release 19.2R1.8 built by builder on 2019-06-21 20:29:57 UTC
        JDDOSD release 19.2R1.8 built by builder on 2019-06-21 20:33:45 UTC
        TRANSPORTD release 19.2R1.8 built by builder on 2019-06-21 20:33:09 UTC
        CLKSYNCD release 19.2R1.8 built by builder on 2019-06-21 20:30:16 UTC
        srd release 19.2R1.8 built by builder on 2019-06-21 20:30:01 UTC
        SDK-VMMD release 19.2R1.8 built by builder on 2019-06-21 20:29:56 UTC
        GSTATD release 19.2R1.8 built by builder on 2019-06-21 17:47:03 UTC
        SFLOWD release 19.2R1.8 built by builder on 2019-06-21 20:27:32 UTC
        JKHMD release 19.2R1.8 built by builder on 2019-06-21 20:39:54 UTC
        DOT1XD release 19.2R1.8 built by builder on 2019-06-21 21:20:07 UTC
        ESSMD release 19.2R1.8 built by builder on 2019-06-21 20:27:50 UTC
        VMOND release 19.2R1.8 built by builder on 2019-06-21 20:30:13 UTC
        BBE-MIBD release 19.2R1.8 built by builder on 2019-06-21 20:33:22 UTC
        NET-MONITORD release 19.2R1.8 built by builder on 2019-06-21 20:30:16 UTC
        BBE-STATSD release 19.2R1.8 built by builder on 2019-06-21 20:33:36 UTC
        TRAFFIC-DIRD release 19.2R1.8 built by builder on 2019-06-21 20:30:05 UTC
        JINSIGHTD release 19.2R1.8 built by builder on 2019-06-21 20:14:59 UTC
        TCPFWDD release 19.2R1.8 built by builder on 2019-06-21 20:41:54 UTC
        RDMD release 19.2R1.8 built by builder on 2019-06-21 20:27:30 UTC
        BBE-FWSD release 19.2R1.8 built by builder on 2019-06-21 20:33:22 UTC
        PPMD release 19.2R1.8 built by builder on 2019-06-21 20:28:12 UTC
        LMPD release 19.2R1.8 built by builder on 2019-06-21 18:51:29 UTC
        LRMUXD release 19.2R1.8 built by builder on 2019-06-21 20:26:17 UTC
        PGMD release 19.2R1.8 built by builder on 2019-06-21 20:26:05 UTC
        BFDD release 19.2R1.8 built by builder on 2019-06-21 20:28:12 UTC
        SDXD release 19.2R1.8 built by builder on 2019-06-21 20:25:03 UTC
        AUDITD release 19.2R1.8 built by builder on 2019-06-21 20:55:47 UTC
        L2ALD release 19.2R1.8 built by builder on 2019-06-21 21:10:36 UTC
        EVENTD release 19.2R1.8 built by builder on 2019-06-21 20:32:57 UTC
        L2CPD release 19.2R1.8 built by builder on 2019-06-21 20:55:06 UTC
        ANCPD release 19.2R1.8 built by builder on 2019-06-21 20:28:32 UTC
        MCSNOOPD release 19.2R1.8 built by builder on 2019-06-21 21:09:21 UTC
        MPLSOAMD release 19.2R1.8 built by builder on 2019-06-21 20:26:22 UTC
        WEB-API release 19.2R1.8 built by builder on 2019-06-21 17:38:42 UTC
        JSD release 19.2R1.8 built by builder on 2019-06-21 20:32:49 UTC
        UI-PUBD release 19.2R1.8 built by builder on 2019-06-21 20:32:50 UTC
        MGD-API release 19.2R1.8 built by builder on 2019-06-21 20:15:09 UTC
        PCCD release 19.2R1.8 built by builder on 2019-06-21 20:30:18 UTC
        OVERLAYD release 19.2R1.8 built by builder on 2019-06-21 20:27:28 UTC
        NTAD release 19.2R1.8 built by builder on 2019-06-21 20:25:51 UTC
        SDPD release 19.2R1.8 built by builder on 2019-06-21 21:01:42 UTC
        SPMD release 19.2R1.8 built by builder on 2019-06-21 20:55:12 UTC
        SCPD release 19.2R1.8 built by builder on 2019-06-21 21:01:40 UTC
        VCCPD release 19.2R1.8 built by builder on 2019-06-21 20:55:12 UTC
        JSQLSYNCD release 19.2R1.8 built by builder on 2019-06-21 20:30:42 UTC
        KMD release 19.2R1.8 built by builder on 2019-06-21 20:28:03 UTC
        GKMD release 19.2R1.8 built by builder on 2019-06-21 20:28:01 UTC
        PKID release 19.2R1.8 built by builder on 2019-06-21 20:28:23 UTC
        SENDD release 19.2R1.8 built by builder on 2019-06-21 20:25:04 UTC
        base-actions-dd release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:53:16 UTC
        junos-base-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
        jkernel-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:06 UTC
        aaad-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
        ancpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
        appsecure-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
        aprobe-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
        apsd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
        authd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:08:43 UTC
        autoconfd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
        bfdd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
        cfm-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
        chassis_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
        clksyncd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
        collector-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
        cos_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
        cpcdd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
        dcd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
        demuxd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
        dfcd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
        dot1xd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:30 UTC
        dyn-sess-prof-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
        elmi-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        essmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        forwarding_options_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        fsad-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        gres-test-point-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        httpd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        iccp_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        ilmid-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        jappid-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        jcrypto-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        jcrypto_junos-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
        jddosd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        jdiameterd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
        jdocs-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:55 UTC
        jidpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        jkernel_junos-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
        jpppd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        jroute-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:42 UTC
        jroute_junos-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
        junos-routing-bgp-advanced-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
        junos-routing-bgp-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
        junos-routing-infra-advanced-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
        junos-routing-infra-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:36 UTC
        junos-routing-instance-vrf-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
        junos-routing-isis-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
        junos-routing-ldp-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
        junos-routing-ospf-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
        junos-routing-prpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
        l2ald-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
        lldp-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
        lrf-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
        macsec-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
        mclag_cfgchk_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        mcsnoop-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:51 UTC
        mo-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        mobiled-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        pccd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        ppmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        pppd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        pppoed-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        r2cpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        rdd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        rdmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        repd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        rmpsd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
        scpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        sdpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        services-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
        sflow-service-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:31 UTC
        spmd_common-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
        srd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:42 UTC
        stp-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
        subinfo-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
        tcpfwdd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:42 UTC
        traffic-dird-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
        transportd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
        url-filterd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
        virtualchassis-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
        vlans-ng-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:31 UTC
    '''}

    golden_parsed_output = {
        "software-information": {
            "host-name": "sr_hktGCS001",
            "junos-version": "19.2R1.8",
            "output": [
                "JLAUNCHD release 19.2R1.8 built by builder on 2019-06-21 17:47:00 UTC",
                "smartd 6.4 2015-06-04 r4109 [FreeBSD JNPR-11.0-20190517.f0321c3_buil amd64] Junos Build",
                "Copyright (C) 2002-15, Bruce Allen, Christian Franke, www.smartmontools.org"
            ],
            "package-information": [
                {
                    "comment": "JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]",
                    "name": "os-kernel"
                },
                {
                    "comment": "JUNOS OS libs [20190517.f0321c3_builder_stable_11]",
                    "name": "os-libs"
                },
                {
                    "comment": "JUNOS OS runtime [20190517.f0321c3_builder_stable_11]",
                    "name": "os-runtime"
                },
                {
                    "comment": "JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]",
                    "name": "zoneinfo"
                },
                {
                    "comment": "JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]",
                    "name": "netstack"
                },
                {
                    "comment": "JUNOS libs [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs"
                },
                {
                    "comment": "JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]",
                    "name": "os-libs-compat32"
                },
                {
                    "comment": "JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]",
                    "name": "os-compat32"
                },
                {
                    "comment": "JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs-compat32"
                },
                {
                    "comment": "JUNOS runtime [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-runtime"
                },
                {
                    "comment": "JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]",
                    "name": "vmguest"
                },
                {
                    "comment": "JUNOS sflow mx [20190621.152752_builder_junos_192_r1]",
                    "name": "sflow-platform"
                },
                {
                    "comment": "JUNOS py extensions [20190621.152752_builder_junos_192_r1]",
                    "name": "py-extensions"
                },
                {
                    "comment": "JUNOS py base [20190621.152752_builder_junos_192_r1]",
                    "name": "py-base"
                },
                {
                    "comment": "JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]",
                    "name": "os-vmguest"
                },
                {
                    "comment": "JUNOS OS crypto [20190517.f0321c3_builder_stable_11]",
                    "name": "os-crypto"
                },
                {
                    "comment": "JUNOS na telemetry [19.2R1.8]",
                    "name": "na-telemetry"
                },
                {
                    "comment": "JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs-compat32-platform"
                },
                {
                    "comment": "JUNOS mx runtime [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-runtime-platform"
                },
                {
                    "comment": "JUNOS common platform support [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-platform"
                },
                {
                    "comment": "JUNOS Openconfig [19.2R1.8]",
                    "name": "junos-openconfig"
                },
                {
                    "comment": "JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-net-platform"
                },
                {
                    "comment": "JUNOS modules [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-modules"
                },
                {
                    "comment": "JUNOS mx modules [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-modules-platform"
                },
                {
                    "comment": "JUNOS mx libs [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs-platform"
                },
                {
                    "comment": "JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-jsqlsync"
                },
                {
                    "comment": "JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-dp-crypto-support-platform"
                },
                {
                    "comment": "JUNOS daemons [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-daemons"
                },
                {
                    "comment": "JUNOS mx daemons [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-daemons-platform"
                },
                {
                    "comment": "JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-appidd"
                },
                {
                    "comment": "JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]",
                    "name": "jsim-wrlinux"
                },
                {
                    "comment": "JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]",
                    "name": "jsim-pfe-vmx"
                },
                {
                    "comment": "JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-urlf"
                },
                {
                    "comment": "JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-traffic-dird"
                },
                {
                    "comment": "JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-telemetry"
                },
                {
                    "comment": "JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-tcp-log"
                },
                {
                    "comment": "JUNOS Services SSL [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-ssl"
                },
                {
                    "comment": "JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-softwire"
                },
                {
                    "comment": "JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-sfw"
                },
                {
                    "comment": "JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-rtcom"
                },
                {
                    "comment": "JUNOS Services RPM [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-rpm"
                },
                {
                    "comment": "JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-pcef"
                },
                {
                    "comment": "JUNOS Services NAT [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-nat"
                },
                {
                    "comment": "JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-mss"
                },
                {
                    "comment": "JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-mobile"
                },
                {
                    "comment": "JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-lrf"
                },
                {
                    "comment": "JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-llpdf"
                },
                {
                    "comment": "JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-jflow"
                },
                {
                    "comment": "JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-jdpi"
                },
                {
                    "comment": "JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-ipsec"
                },
                {
                    "comment": "JUNOS Services IDS [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-ids"
                },
                {
                    "comment": "JUNOS IDP Services [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-idp"
                },
                {
                    "comment": "JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-hcm"
                },
                {
                    "comment": "JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-fwdd"
                },
                {
                    "comment": "JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-crypto-base"
                },
                {
                    "comment": "JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-cpcd"
                },
                {
                    "comment": "JUNOS Services COS [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-cos"
                },
                {
                    "comment": "JUNOS AppId Services [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-appid"
                },
                {
                    "comment": "JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-alg"
                },
                {
                    "comment": "JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-aacl"
                },
                {
                    "comment": "JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]",
                    "name": "jsd-jet-1"
                },
                {
                    "comment": "JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]",
                    "name": "jmrt-base-x86-64"
                },
                {
                    "comment": "JUNOS J-Insight [20190621.152752_builder_junos_192_r1]",
                    "name": "jinsight"
                },
                {
                    "comment": "JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]",
                    "name": "jdocs"
                },
                {
                    "comment": "JUNOS jail runtime [20190517.f0321c3_builder_stable_11]",
                    "name": "jail-runtime"
                },
                {
                    "comment": "KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built",
                    "name": "KERNEL"
                }
            ],
            "product-model": "vmx",
            "product-name": "vmx",
            "version-information": [
                {
                    "build-date": "2019-06-06 22:58:49 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MGD ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:55:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CLI ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-22 01:02:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:24:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CHASSISD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:58:46 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "COMMIT-SYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BFDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:58:47 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JNUD ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DFWD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:03:26 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SNMPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:03:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ALARM-MGMTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:07:04 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MIB2D ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "APSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:14 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "VRRPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:56:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ALARMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:59:01 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PFED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:19 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AGENTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CRAFTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:34:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SAMPLED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SRRD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:10 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JFLOWD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ILMID ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RMOPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:00:26 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "COSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:24:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "FSAD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "IRSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:24:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "FUD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 18:55:26 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RTSPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 18:51:23 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "KSYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:57:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JL2TPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JPPPOED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:29 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:24:45 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PPPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DFCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:56 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LACPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LFMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:29:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "OAMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:38:55 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TNETD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:58:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CFMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JDHCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSAVALD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:11 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PSSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:11 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MSPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:02:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AUTHD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:39:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PMOND ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AUTOCONFD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:59:56 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-SMGD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JDIAMETERD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:25 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BDBREPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:56:15 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "APPIDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:48 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JPPPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSSCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:15:11 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ICCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:58:06 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MCLAG-CFGCHKD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SHM-RTSDBD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:07 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DATAPATH-TRACED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CPCDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:56:05 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SMID ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:29:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SMIHELPERD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:45 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JDDOSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:09 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TRANSPORTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CLKSYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:01 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "srd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:29:56 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SDK-VMMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:47:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "GSTATD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SFLOWD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:39:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JKHMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:20:07 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DOT1XD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ESSMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:13 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "VMOND ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-MIBD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "NET-MONITORD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-STATSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:05 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TRAFFIC-DIRD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:14:59 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JINSIGHTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:41:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TCPFWDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RDMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-FWSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PPMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 18:51:29 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LMPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:17 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LRMUXD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:05 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PGMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BFDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SDXD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:47 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AUDITD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:10:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "L2ALD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "EVENTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:06 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "L2CPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ANCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:09:21 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MCSNOOPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MPLSOAMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:38:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "WEB-API ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:49 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "UI-PUBD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:15:09 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MGD-API ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:18 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PCCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:28 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "OVERLAYD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "NTAD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:01:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SDPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SPMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:01:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "VCCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSQLSYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "KMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:01 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "GKMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:23 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PKID ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:04 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SENDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:53:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "base-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-base-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:06 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jkernel-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "aaad-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ancpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "appsecure-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "aprobe-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "apsd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:08:43 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "authd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "autoconfd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "bfdd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "cfm-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "chassis_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "clksyncd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "collector-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "cos_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "cpcdd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dcd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "demuxd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dfcd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dot1xd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dyn-sess-prof-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "elmi-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "essmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "forwarding_options_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "fsad-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "gres-test-point-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "httpd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "iccp_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ilmid-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jappid-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jcrypto-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jcrypto_junos-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jddosd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jdiameterd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:55 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jdocs-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jidpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jkernel_junos-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jpppd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jroute-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jroute_junos-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-bgp-advanced-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-bgp-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-infra-advanced-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-infra-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-instance-vrf-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-isis-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-ldp-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-ospf-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-prpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "l2ald-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "lldp-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "lrf-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "macsec-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mclag_cfgchk_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mcsnoop-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mo-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mobiled-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "pccd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ppmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "pppd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "pppoed-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "r2cpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "rdd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "rdmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "repd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "rmpsd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "scpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "sdpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "services-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:31 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "sflow-service-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "spmd_common-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "srd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "stp-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "subinfo-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "tcpfwdd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "traffic-dird-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "transportd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "url-filterd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "virtualchassis-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:31 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "vlans-ng-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                }
            ]
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVersionDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVersionDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowVersionDetailNoForwarding(unittest.TestCase):
    """ Unit tests for:
            * show version detail no-forwarding
    """

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    show version detail no-forwarding | no-more 
    Hostname: sr_hktGCS001
    Model: vmx
    Junos: 19.2R1.8
    JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]
    JUNOS OS libs [20190517.f0321c3_builder_stable_11]
    JUNOS OS runtime [20190517.f0321c3_builder_stable_11]
    JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]
    JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]
    JUNOS libs [20190621.152752_builder_junos_192_r1]
    JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]
    JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]
    JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]
    JUNOS runtime [20190621.152752_builder_junos_192_r1]
    JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]
    JUNOS sflow mx [20190621.152752_builder_junos_192_r1]
    JUNOS py extensions [20190621.152752_builder_junos_192_r1]
    JUNOS py base [20190621.152752_builder_junos_192_r1]
    JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]
    JUNOS OS crypto [20190517.f0321c3_builder_stable_11]
    JUNOS na telemetry [19.2R1.8]
    JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]
    JUNOS mx runtime [20190621.152752_builder_junos_192_r1]
    JUNOS common platform support [20190621.152752_builder_junos_192_r1]
    JUNOS Openconfig [19.2R1.8]
    JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]
    JUNOS modules [20190621.152752_builder_junos_192_r1]
    JUNOS mx modules [20190621.152752_builder_junos_192_r1]
    JUNOS mx libs [20190621.152752_builder_junos_192_r1]
    JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]
    JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]
    JUNOS daemons [20190621.152752_builder_junos_192_r1]
    JUNOS mx daemons [20190621.152752_builder_junos_192_r1]
    JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]
    JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]
    JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]
    JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]
    JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]
    JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]
    JUNOS Services SSL [20190621.152752_builder_junos_192_r1]
    JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]
    JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]
    JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]
    JUNOS Services RPM [20190621.152752_builder_junos_192_r1]
    JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]
    JUNOS Services NAT [20190621.152752_builder_junos_192_r1]
    JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]
    JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]
    JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]
    JUNOS Services IDS [20190621.152752_builder_junos_192_r1]
    JUNOS IDP Services [20190621.152752_builder_junos_192_r1]
    JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]
    JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services COS [20190621.152752_builder_junos_192_r1]
    JUNOS AppId Services [20190621.152752_builder_junos_192_r1]
    JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]
    JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]
    JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]
    JUNOS J-Insight [20190621.152752_builder_junos_192_r1]
    JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]
    JUNOS jail runtime [20190517.f0321c3_builder_stable_11]
    KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built
    MGD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:49 UTC
    CLI release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:55:22 UTC
    JLAUNCHD release 19.2R1.8 built by builder on 2019-06-21 17:47:00 UTC
    RPD release 19.2R1.8 built by builder on 2019-06-22 01:02:12 UTC
    CHASSISD release 19.2R1.8 built by builder on 2019-06-21 21:24:54 UTC
    COMMIT-SYNCD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:46 UTC
    BFDD release 19.2R1.8 built by builder on 2019-06-21 20:28:12 UTC
    JNUD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:47 UTC
    DFWD release 19.2R1.8 built by builder on 2019-06-21 20:28:35 UTC
    DCD release 19.2R1.8 built by builder on 2019-06-21 20:27:41 UTC
    SNMPD release 19.2R1.8 built by builder on 2019-06-21 21:03:26 UTC
    ALARM-MGMTD release 19.2R1.8 built by builder on 2019-06-21 21:03:22 UTC
    MIB2D release 19.2R1.8 built by builder on 2019-06-21 21:07:04 UTC
    APSD release 19.2R1.8 built by builder on 2019-06-21 20:28:33 UTC
    VRRPD release 19.2R1.8 built by builder on 2019-06-21 20:30:14 UTC
    ALARMD release 19.2R1.8 built by builder on 2019-06-21 20:56:00 UTC
    PFED release 19.2R1.8 built by builder on 2019-06-21 20:59:01 UTC
    AGENTD release 19.2R1.8 built by builder on 2019-06-21 20:33:19 UTC
    CRAFTD release 19.2R1.8 built by builder on 2019-06-21 20:28:34 UTC
    SAMPLED release 19.2R1.8 built by builder on 2019-06-21 20:34:16 UTC
    SRRD release 19.2R1.8 built by builder on 2019-06-21 20:25:57 UTC
    JFLOWD release 19.2R1.8 built by builder on 2019-06-21 20:25:10 UTC
    ILMID release 19.2R1.8 built by builder on 2019-06-21 20:28:40 UTC
    RMOPD release 19.2R1.8 built by builder on 2019-06-21 20:28:30 UTC
    COSD release 19.2R1.8 built by builder on 2019-06-21 21:00:26 UTC
    FSAD release 19.2R1.8 built by builder on 2019-06-21 20:24:41 UTC
    IRSD release 19.2R1.8 built by builder on 2019-06-21 20:27:00 UTC
    FUD release 19.2R1.8 built by builder on 2019-06-21 20:24:41 UTC
    RTSPD release 19.2R1.8 built by builder on 2019-06-21 18:55:26 UTC
    smartd 6.4 2015-06-04 r4109 [FreeBSD JNPR-11.0-20190517.f0321c3_buil amd64] Junos Build
    Copyright (C) 2002-15, Bruce Allen, Christian Franke, www.smartmontools.org
    KSYNCD release 19.2R1.8 built by builder on 2019-06-21 18:51:23 UTC
    SPD release 19.2R1.8 built by builder on 2019-06-21 20:57:57 UTC
    JL2TPD release 19.2R1.8 built by builder on 2019-06-21 20:33:03 UTC
    JPPPOED release 19.2R1.8 built by builder on 2019-06-21 20:33:03 UTC
    RDD release 19.2R1.8 built by builder on 2019-06-21 20:27:29 UTC
    PPPD release 19.2R1.8 built by builder on 2019-06-21 20:24:45 UTC
    DFCD release 19.2R1.8 built by builder on 2019-06-21 20:28:34 UTC
    LACPD release 19.2R1.8 built by builder on 2019-06-21 20:28:56 UTC
    LFMD release 19.2R1.8 built by builder on 2019-06-21 20:28:57 UTC
    OAMD release 19.2R1.8 built by builder on 2019-06-21 20:29:03 UTC
    TNETD release 19.2R1.8 built by builder on 2019-06-21 17:38:55 UTC
    CFMD release 19.2R1.8 built by builder on 2019-06-21 20:58:51 UTC
    JDHCPD release 19.2R1.8 built by builder on 2019-06-21 20:33:00 UTC
    JSAVALD release 19.2R1.8 built by builder on 2019-06-21 20:26:50 UTC
    PSSD release 19.2R1.8 built by builder on 2019-06-21 20:25:11 UTC
    MSPD release 19.2R1.8 built by builder on 2019-06-21 20:25:11 UTC
    AUTHD release 19.2R1.8 built by builder on 2019-06-21 21:02:00 UTC
    PMOND release 19.2R1.8 built by builder on 2019-06-21 20:39:54 UTC
    AUTOCONFD release 19.2R1.8 built by builder on 2019-06-21 20:32:51 UTC
    BBE-SMGD release 19.2R1.8 built by builder on 2019-06-21 20:59:56 UTC
    JDIAMETERD release 19.2R1.8 built by builder on 2019-06-21 20:33:00 UTC
    BDBREPD release 19.2R1.8 built by builder on 2019-06-21 20:27:25 UTC
    APPIDD release 19.2R1.8 built by builder on 2019-06-21 20:56:15 UTC
    JPPPD release 19.2R1.8 built by builder on 2019-06-21 20:33:48 UTC
    JSSCD release 19.2R1.8 built by builder on 2019-06-21 20:33:50 UTC
    ICCPD release 19.2R1.8 built by builder on 2019-06-21 20:15:11 UTC
    MCLAG-CFGCHKD release 19.2R1.8 built by builder on 2019-06-21 20:58:06 UTC
    SHM-RTSDBD release 19.2R1.8 built by builder on 2019-06-21 20:32:30 UTC
    DATAPATH-TRACED release 19.2R1.8 built by builder on 2019-06-21 20:25:07 UTC
    CPCDD release 19.2R1.8 built by builder on 2019-06-21 20:33:39 UTC
    SMID release 19.2R1.8 built by builder on 2019-06-21 20:56:05 UTC
    SMIHELPERD release 19.2R1.8 built by builder on 2019-06-21 20:29:57 UTC
    JDDOSD release 19.2R1.8 built by builder on 2019-06-21 20:33:45 UTC
    TRANSPORTD release 19.2R1.8 built by builder on 2019-06-21 20:33:09 UTC
    CLKSYNCD release 19.2R1.8 built by builder on 2019-06-21 20:30:16 UTC
    srd release 19.2R1.8 built by builder on 2019-06-21 20:30:01 UTC
    SDK-VMMD release 19.2R1.8 built by builder on 2019-06-21 20:29:56 UTC
    GSTATD release 19.2R1.8 built by builder on 2019-06-21 17:47:03 UTC
    SFLOWD release 19.2R1.8 built by builder on 2019-06-21 20:27:32 UTC
    JKHMD release 19.2R1.8 built by builder on 2019-06-21 20:39:54 UTC
    DOT1XD release 19.2R1.8 built by builder on 2019-06-21 21:20:07 UTC
    ESSMD release 19.2R1.8 built by builder on 2019-06-21 20:27:50 UTC
    VMOND release 19.2R1.8 built by builder on 2019-06-21 20:30:13 UTC
    BBE-MIBD release 19.2R1.8 built by builder on 2019-06-21 20:33:22 UTC
    NET-MONITORD release 19.2R1.8 built by builder on 2019-06-21 20:30:16 UTC
    BBE-STATSD release 19.2R1.8 built by builder on 2019-06-21 20:33:36 UTC
    TRAFFIC-DIRD release 19.2R1.8 built by builder on 2019-06-21 20:30:05 UTC
    JINSIGHTD release 19.2R1.8 built by builder on 2019-06-21 20:14:59 UTC
    TCPFWDD release 19.2R1.8 built by builder on 2019-06-21 20:41:54 UTC
    RDMD release 19.2R1.8 built by builder on 2019-06-21 20:27:30 UTC
    BBE-FWSD release 19.2R1.8 built by builder on 2019-06-21 20:33:22 UTC
    PPMD release 19.2R1.8 built by builder on 2019-06-21 20:28:12 UTC
    LMPD release 19.2R1.8 built by builder on 2019-06-21 18:51:29 UTC
    LRMUXD release 19.2R1.8 built by builder on 2019-06-21 20:26:17 UTC
    PGMD release 19.2R1.8 built by builder on 2019-06-21 20:26:05 UTC
    BFDD release 19.2R1.8 built by builder on 2019-06-21 20:28:12 UTC
    SDXD release 19.2R1.8 built by builder on 2019-06-21 20:25:03 UTC
    AUDITD release 19.2R1.8 built by builder on 2019-06-21 20:55:47 UTC
    L2ALD release 19.2R1.8 built by builder on 2019-06-21 21:10:36 UTC
    EVENTD release 19.2R1.8 built by builder on 2019-06-21 20:32:57 UTC
    L2CPD release 19.2R1.8 built by builder on 2019-06-21 20:55:06 UTC
    ANCPD release 19.2R1.8 built by builder on 2019-06-21 20:28:32 UTC
    MCSNOOPD release 19.2R1.8 built by builder on 2019-06-21 21:09:21 UTC
    MPLSOAMD release 19.2R1.8 built by builder on 2019-06-21 20:26:22 UTC
    WEB-API release 19.2R1.8 built by builder on 2019-06-21 17:38:42 UTC
    JSD release 19.2R1.8 built by builder on 2019-06-21 20:32:49 UTC
    UI-PUBD release 19.2R1.8 built by builder on 2019-06-21 20:32:50 UTC
    MGD-API release 19.2R1.8 built by builder on 2019-06-21 20:15:09 UTC
    PCCD release 19.2R1.8 built by builder on 2019-06-21 20:30:18 UTC
    OVERLAYD release 19.2R1.8 built by builder on 2019-06-21 20:27:28 UTC
    NTAD release 19.2R1.8 built by builder on 2019-06-21 20:25:51 UTC
    SDPD release 19.2R1.8 built by builder on 2019-06-21 21:01:42 UTC
    SPMD release 19.2R1.8 built by builder on 2019-06-21 20:55:12 UTC
    SCPD release 19.2R1.8 built by builder on 2019-06-21 21:01:40 UTC
    VCCPD release 19.2R1.8 built by builder on 2019-06-21 20:55:12 UTC
    JSQLSYNCD release 19.2R1.8 built by builder on 2019-06-21 20:30:42 UTC
    KMD release 19.2R1.8 built by builder on 2019-06-21 20:28:03 UTC
    GKMD release 19.2R1.8 built by builder on 2019-06-21 20:28:01 UTC
    PKID release 19.2R1.8 built by builder on 2019-06-21 20:28:23 UTC
    SENDD release 19.2R1.8 built by builder on 2019-06-21 20:25:04 UTC
    base-actions-dd release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:53:16 UTC
    junos-base-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
    jkernel-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:06 UTC
    aaad-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
    ancpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
    appsecure-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
    aprobe-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
    apsd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
    authd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:08:43 UTC
    autoconfd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
    bfdd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
    cfm-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:33 UTC
    chassis_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
    clksyncd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
    collector-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
    cos_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
    cpcdd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
    dcd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
    demuxd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
    dfcd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
    dot1xd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:30 UTC
    dyn-sess-prof-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:34 UTC
    elmi-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    essmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    forwarding_options_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    fsad-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    gres-test-point-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    httpd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    iccp_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    ilmid-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    jappid-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    jcrypto-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    jcrypto_junos-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
    jddosd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    jdiameterd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:35 UTC
    jdocs-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:55 UTC
    jidpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    jkernel_junos-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
    jpppd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    jroute-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:42 UTC
    jroute_junos-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
    junos-routing-bgp-advanced-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
    junos-routing-bgp-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
    junos-routing-infra-advanced-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
    junos-routing-infra-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:36 UTC
    junos-routing-instance-vrf-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
    junos-routing-isis-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
    junos-routing-ldp-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
    junos-routing-ospf-basic-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:40 UTC
    junos-routing-prpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:39 UTC
    l2ald-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
    lldp-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
    lrf-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:36 UTC
    macsec-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:32 UTC
    mclag_cfgchk_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    mcsnoop-actions-dd release 19.2R1.8 built by builder on 2019-06-21 17:09:51 UTC
    mo-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    mobiled-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    pccd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    ppmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    pppd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    pppoed-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    r2cpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    rdd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    rdmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    repd_cmd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    rmpsd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:41 UTC
    scpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    sdpd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    services-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:37 UTC
    sflow-service-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:31 UTC
    spmd_common-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
    srd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:42 UTC
    stp-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
    subinfo-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
    tcpfwdd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:42 UTC
    traffic-dird-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
    transportd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
    url-filterd-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
    virtualchassis-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:38 UTC
    vlans-ng-actions-dd release 19.2R1.8 built by builder on 2019-06-21 16:07:31 UTC
        
    '''}

    golden_parsed_output = {
        "software-information": {
            "host-name": "sr_hktGCS001",
            "junos-version": "19.2R1.8",
            "output": [
                "JLAUNCHD release 19.2R1.8 built by builder on 2019-06-21 17:47:00 UTC",
                "smartd 6.4 2015-06-04 r4109 [FreeBSD JNPR-11.0-20190517.f0321c3_buil amd64] Junos Build",
                "Copyright (C) 2002-15, Bruce Allen, Christian Franke, www.smartmontools.org"
            ],
            "package-information": [
                {
                    "comment": "JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]",
                    "name": "os-kernel"
                },
                {
                    "comment": "JUNOS OS libs [20190517.f0321c3_builder_stable_11]",
                    "name": "os-libs"
                },
                {
                    "comment": "JUNOS OS runtime [20190517.f0321c3_builder_stable_11]",
                    "name": "os-runtime"
                },
                {
                    "comment": "JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]",
                    "name": "zoneinfo"
                },
                {
                    "comment": "JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]",
                    "name": "netstack"
                },
                {
                    "comment": "JUNOS libs [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs"
                },
                {
                    "comment": "JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]",
                    "name": "os-libs-compat32"
                },
                {
                    "comment": "JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]",
                    "name": "os-compat32"
                },
                {
                    "comment": "JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs-compat32"
                },
                {
                    "comment": "JUNOS runtime [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-runtime"
                },
                {
                    "comment": "JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]",
                    "name": "vmguest"
                },
                {
                    "comment": "JUNOS sflow mx [20190621.152752_builder_junos_192_r1]",
                    "name": "sflow-platform"
                },
                {
                    "comment": "JUNOS py extensions [20190621.152752_builder_junos_192_r1]",
                    "name": "py-extensions"
                },
                {
                    "comment": "JUNOS py base [20190621.152752_builder_junos_192_r1]",
                    "name": "py-base"
                },
                {
                    "comment": "JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]",
                    "name": "os-vmguest"
                },
                {
                    "comment": "JUNOS OS crypto [20190517.f0321c3_builder_stable_11]",
                    "name": "os-crypto"
                },
                {
                    "comment": "JUNOS na telemetry [19.2R1.8]",
                    "name": "na-telemetry"
                },
                {
                    "comment": "JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs-compat32-platform"
                },
                {
                    "comment": "JUNOS mx runtime [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-runtime-platform"
                },
                {
                    "comment": "JUNOS common platform support [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-platform"
                },
                {
                    "comment": "JUNOS Openconfig [19.2R1.8]",
                    "name": "junos-openconfig"
                },
                {
                    "comment": "JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-net-platform"
                },
                {
                    "comment": "JUNOS modules [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-modules"
                },
                {
                    "comment": "JUNOS mx modules [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-modules-platform"
                },
                {
                    "comment": "JUNOS mx libs [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-libs-platform"
                },
                {
                    "comment": "JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-jsqlsync"
                },
                {
                    "comment": "JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-dp-crypto-support-platform"
                },
                {
                    "comment": "JUNOS daemons [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-daemons"
                },
                {
                    "comment": "JUNOS mx daemons [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-daemons-platform"
                },
                {
                    "comment": "JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]",
                    "name": "junos-appidd"
                },
                {
                    "comment": "JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]",
                    "name": "jsim-wrlinux"
                },
                {
                    "comment": "JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]",
                    "name": "jsim-pfe-vmx"
                },
                {
                    "comment": "JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-urlf"
                },
                {
                    "comment": "JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-traffic-dird"
                },
                {
                    "comment": "JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-telemetry"
                },
                {
                    "comment": "JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-tcp-log"
                },
                {
                    "comment": "JUNOS Services SSL [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-ssl"
                },
                {
                    "comment": "JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-softwire"
                },
                {
                    "comment": "JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-sfw"
                },
                {
                    "comment": "JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-rtcom"
                },
                {
                    "comment": "JUNOS Services RPM [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-rpm"
                },
                {
                    "comment": "JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-pcef"
                },
                {
                    "comment": "JUNOS Services NAT [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-nat"
                },
                {
                    "comment": "JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-mss"
                },
                {
                    "comment": "JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-mobile"
                },
                {
                    "comment": "JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-lrf"
                },
                {
                    "comment": "JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-llpdf"
                },
                {
                    "comment": "JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-jflow"
                },
                {
                    "comment": "JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-jdpi"
                },
                {
                    "comment": "JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-ipsec"
                },
                {
                    "comment": "JUNOS Services IDS [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-ids"
                },
                {
                    "comment": "JUNOS IDP Services [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-idp"
                },
                {
                    "comment": "JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-hcm"
                },
                {
                    "comment": "JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-fwdd"
                },
                {
                    "comment": "JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-crypto-base"
                },
                {
                    "comment": "JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-cpcd"
                },
                {
                    "comment": "JUNOS Services COS [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-cos"
                },
                {
                    "comment": "JUNOS AppId Services [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-appid"
                },
                {
                    "comment": "JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-alg"
                },
                {
                    "comment": "JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]",
                    "name": "jservices-aacl"
                },
                {
                    "comment": "JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]",
                    "name": "jsd-jet-1"
                },
                {
                    "comment": "JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]",
                    "name": "jmrt-base-x86-64"
                },
                {
                    "comment": "JUNOS J-Insight [20190621.152752_builder_junos_192_r1]",
                    "name": "jinsight"
                },
                {
                    "comment": "JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]",
                    "name": "jdocs"
                },
                {
                    "comment": "JUNOS jail runtime [20190517.f0321c3_builder_stable_11]",
                    "name": "jail-runtime"
                },
                {
                    "comment": "KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built",
                    "name": "KERNEL"
                }
            ],
            "product-model": "vmx",
            "product-name": "vmx",
            "version-information": [
                {
                    "build-date": "2019-06-06 22:58:49 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MGD ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:55:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CLI ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-22 01:02:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:24:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CHASSISD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:58:46 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "COMMIT-SYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BFDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:58:47 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JNUD ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DFWD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:03:26 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SNMPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:03:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ALARM-MGMTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:07:04 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MIB2D ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "APSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:14 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "VRRPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:56:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ALARMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:59:01 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PFED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:19 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AGENTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CRAFTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:34:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SAMPLED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SRRD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:10 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JFLOWD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ILMID ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RMOPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:00:26 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "COSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:24:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "FSAD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "IRSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:24:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "FUD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 18:55:26 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RTSPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 18:51:23 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "KSYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:57:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JL2TPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JPPPOED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:29 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:24:45 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PPPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DFCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:56 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LACPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LFMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:29:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "OAMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:38:55 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TNETD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:58:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CFMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JDHCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSAVALD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:11 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PSSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:11 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MSPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:02:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AUTHD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:39:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PMOND ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AUTOCONFD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:59:56 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-SMGD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:00 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JDIAMETERD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:25 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BDBREPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:56:15 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "APPIDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:48 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JPPPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSSCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:15:11 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ICCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:58:06 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MCLAG-CFGCHKD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SHM-RTSDBD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:07 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DATAPATH-TRACED ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CPCDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:56:05 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SMID ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:29:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SMIHELPERD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:45 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JDDOSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:09 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TRANSPORTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "CLKSYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:01 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "srd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:29:56 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SDK-VMMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:47:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "GSTATD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SFLOWD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:39:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JKHMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:20:07 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "DOT1XD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ESSMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:13 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "VMOND ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-MIBD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "NET-MONITORD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-STATSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:05 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TRAFFIC-DIRD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:14:59 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JINSIGHTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:41:54 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "TCPFWDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "RDMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:33:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BBE-FWSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PPMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 18:51:29 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LMPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:17 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "LRMUXD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:05 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PGMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "BFDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SDXD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:47 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "AUDITD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:10:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "L2ALD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:57 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "EVENTD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:06 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "L2CPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ANCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:09:21 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MCSNOOPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:26:22 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MPLSOAMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:38:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "WEB-API ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:49 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:32:50 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "UI-PUBD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:15:09 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "MGD-API ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:18 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PCCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:27:28 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "OVERLAYD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "NTAD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:01:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SDPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SPMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 21:01:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:55:12 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "VCCPD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:30:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "JSQLSYNCD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:03 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "KMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:01 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "GKMD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:28:23 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "PKID ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 20:25:04 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "SENDD ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-06 22:53:16 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "base-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "20190606.224121_builder.r1033375",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-base-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:06 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jkernel-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "aaad-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ancpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "appsecure-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "aprobe-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "apsd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:08:43 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "authd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "autoconfd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "bfdd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:33 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "cfm-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "chassis_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "clksyncd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "collector-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "cos_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "cpcdd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dcd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "demuxd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dfcd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:30 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dot1xd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:34 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "dyn-sess-prof-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "elmi-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "essmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "forwarding_options_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "fsad-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "gres-test-point-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "httpd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "iccp_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ilmid-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jappid-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jcrypto-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jcrypto_junos-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jddosd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:35 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jdiameterd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:55 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jdocs-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jidpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jkernel_junos-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jpppd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jroute-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "jroute_junos-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-bgp-advanced-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-bgp-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-infra-advanced-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-infra-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-instance-vrf-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-isis-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-ldp-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:40 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-ospf-basic-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:39 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "junos-routing-prpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "l2ald-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "lldp-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:36 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "lrf-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:32 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "macsec-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mclag_cfgchk_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 17:09:51 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mcsnoop-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mo-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "mobiled-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "pccd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "ppmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "pppd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "pppoed-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "r2cpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "rdd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "rdmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "repd_cmd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:41 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "rmpsd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "scpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "sdpd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:37 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "services-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:31 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "sflow-service-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "spmd_common-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "srd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "stp-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "subinfo-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:42 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "tcpfwdd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "traffic-dird-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "transportd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "url-filterd-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:38 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "virtualchassis-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                },
                {
                    "build-date": "2019-06-21 16:07:31 UTC",
                    "build-number": "1",
                    "builder": "builder",
                    "component": "vlans-ng-actions-dd ",
                    "major": "19",
                    "minor": "2",
                    "release": "19.2R1.8",
                    "release-category": "R",
                    "spin": "8"
                }
            ]
        }
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVersionDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVersionDetail(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


class TestShowVersionInvokeOnAllRoutingEngines(unittest.TestCase):
    """ Unit tests for:
            * show version invoke-on all-routing-engines
    """

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''
    show version invoke-on all-routing-engines | no-more 
    re0:
    --------------------------------------------------------------------------
    Hostname: sr_hktGCS001
    Model: vmx
    Junos: 19.2R1.8
    JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]
    JUNOS OS libs [20190517.f0321c3_builder_stable_11]
    JUNOS OS runtime [20190517.f0321c3_builder_stable_11]
    JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]
    JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]
    JUNOS libs [20190621.152752_builder_junos_192_r1]
    JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]
    JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]
    JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]
    JUNOS runtime [20190621.152752_builder_junos_192_r1]
    JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]
    JUNOS sflow mx [20190621.152752_builder_junos_192_r1]
    JUNOS py extensions [20190621.152752_builder_junos_192_r1]
    JUNOS py base [20190621.152752_builder_junos_192_r1]
    JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]
    JUNOS OS crypto [20190517.f0321c3_builder_stable_11]
    JUNOS na telemetry [19.2R1.8]
    JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]
    JUNOS mx runtime [20190621.152752_builder_junos_192_r1]
    JUNOS common platform support [20190621.152752_builder_junos_192_r1]
    JUNOS Openconfig [19.2R1.8]
    JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]
    JUNOS modules [20190621.152752_builder_junos_192_r1]
    JUNOS mx modules [20190621.152752_builder_junos_192_r1]
    JUNOS mx libs [20190621.152752_builder_junos_192_r1]
    JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]
    JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]
    JUNOS daemons [20190621.152752_builder_junos_192_r1]
    JUNOS mx daemons [20190621.152752_builder_junos_192_r1]
    JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]
    JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]
    JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]
    JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]
    JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]
    JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]
    JUNOS Services SSL [20190621.152752_builder_junos_192_r1]
    JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]
    JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]
    JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]
    JUNOS Services RPM [20190621.152752_builder_junos_192_r1]
    JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]
    JUNOS Services NAT [20190621.152752_builder_junos_192_r1]
    JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]
    JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]
    JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]
    JUNOS Services IDS [20190621.152752_builder_junos_192_r1]
    JUNOS IDP Services [20190621.152752_builder_junos_192_r1]
    JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]
    JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]
    JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Services COS [20190621.152752_builder_junos_192_r1]
    JUNOS AppId Services [20190621.152752_builder_junos_192_r1]
    JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]
    JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]
    JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]
    JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]
    JUNOS J-Insight [20190621.152752_builder_junos_192_r1]
    JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]
    JUNOS jail runtime [20190517.f0321c3_builder_stable_11]
    
        
    '''}

    golden_parsed_output = {
        "multi-routing-engine-results": {
            "multi-routing-engine-item": {
                "re-name": "re0",
                "software-information": {
                    "host-name": "sr_hktGCS001",
                    "junos-version": "19.2R1.8",
                    "package-information": [
                        {
                            "comment": "JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]",
                            "name": "os-kernel"
                        },
                        {
                            "comment": "JUNOS OS libs [20190517.f0321c3_builder_stable_11]",
                            "name": "os-libs"
                        },
                        {
                            "comment": "JUNOS OS runtime [20190517.f0321c3_builder_stable_11]",
                            "name": "os-runtime"
                        },
                        {
                            "comment": "JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]",
                            "name": "zoneinfo"
                        },
                        {
                            "comment": "JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]",
                            "name": "netstack"
                        },
                        {
                            "comment": "JUNOS libs [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-libs"
                        },
                        {
                            "comment": "JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]",
                            "name": "os-libs-compat32"
                        },
                        {
                            "comment": "JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]",
                            "name": "os-compat32"
                        },
                        {
                            "comment": "JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-libs-compat32"
                        },
                        {
                            "comment": "JUNOS runtime [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-runtime"
                        },
                        {
                            "comment": "JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]",
                            "name": "vmguest"
                        },
                        {
                            "comment": "JUNOS sflow mx [20190621.152752_builder_junos_192_r1]",
                            "name": "sflow-platform"
                        },
                        {
                            "comment": "JUNOS py extensions [20190621.152752_builder_junos_192_r1]",
                            "name": "py-extensions"
                        },
                        {
                            "comment": "JUNOS py base [20190621.152752_builder_junos_192_r1]",
                            "name": "py-base"
                        },
                        {
                            "comment": "JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]",
                            "name": "os-vmguest"
                        },
                        {
                            "comment": "JUNOS OS crypto [20190517.f0321c3_builder_stable_11]",
                            "name": "os-crypto"
                        },
                        {
                            "comment": "JUNOS na telemetry [19.2R1.8]",
                            "name": "na-telemetry"
                        },
                        {
                            "comment": "JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-libs-compat32-platform"
                        },
                        {
                            "comment": "JUNOS mx runtime [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-runtime-platform"
                        },
                        {
                            "comment": "JUNOS common platform support [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-platform"
                        },
                        {
                            "comment": "JUNOS Openconfig [19.2R1.8]",
                            "name": "junos-openconfig"
                        },
                        {
                            "comment": "JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-net-platform"
                        },
                        {
                            "comment": "JUNOS modules [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-modules"
                        },
                        {
                            "comment": "JUNOS mx modules [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-modules-platform"
                        },
                        {
                            "comment": "JUNOS mx libs [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-libs-platform"
                        },
                        {
                            "comment": "JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-jsqlsync"
                        },
                        {
                            "comment": "JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-dp-crypto-support-platform"
                        },
                        {
                            "comment": "JUNOS daemons [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-daemons"
                        },
                        {
                            "comment": "JUNOS mx daemons [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-daemons-platform"
                        },
                        {
                            "comment": "JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]",
                            "name": "junos-appidd"
                        },
                        {
                            "comment": "JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]",
                            "name": "jsim-wrlinux"
                        },
                        {
                            "comment": "JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]",
                            "name": "jsim-pfe-vmx"
                        },
                        {
                            "comment": "JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-urlf"
                        },
                        {
                            "comment": "JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-traffic-dird"
                        },
                        {
                            "comment": "JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-telemetry"
                        },
                        {
                            "comment": "JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-tcp-log"
                        },
                        {
                            "comment": "JUNOS Services SSL [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-ssl"
                        },
                        {
                            "comment": "JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-softwire"
                        },
                        {
                            "comment": "JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-sfw"
                        },
                        {
                            "comment": "JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-rtcom"
                        },
                        {
                            "comment": "JUNOS Services RPM [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-rpm"
                        },
                        {
                            "comment": "JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-pcef"
                        },
                        {
                            "comment": "JUNOS Services NAT [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-nat"
                        },
                        {
                            "comment": "JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-mss"
                        },
                        {
                            "comment": "JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-mobile"
                        },
                        {
                            "comment": "JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-lrf"
                        },
                        {
                            "comment": "JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-llpdf"
                        },
                        {
                            "comment": "JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-jflow"
                        },
                        {
                            "comment": "JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-jdpi"
                        },
                        {
                            "comment": "JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-ipsec"
                        },
                        {
                            "comment": "JUNOS Services IDS [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-ids"
                        },
                        {
                            "comment": "JUNOS IDP Services [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-idp"
                        },
                        {
                            "comment": "JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-hcm"
                        },
                        {
                            "comment": "JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-fwdd"
                        },
                        {
                            "comment": "JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-crypto-base"
                        },
                        {
                            "comment": "JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-cpcd"
                        },
                        {
                            "comment": "JUNOS Services COS [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-cos"
                        },
                        {
                            "comment": "JUNOS AppId Services [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-appid"
                        },
                        {
                            "comment": "JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-alg"
                        },
                        {
                            "comment": "JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]",
                            "name": "jservices-aacl"
                        },
                        {
                            "comment": "JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]",
                            "name": "jsd-jet-1"
                        },
                        {
                            "comment": "JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]",
                            "name": "jmrt-base-x86-64"
                        },
                        {
                            "comment": "JUNOS J-Insight [20190621.152752_builder_junos_192_r1]",
                            "name": "jinsight"
                        },
                        {
                            "comment": "JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]",
                            "name": "jdocs"
                        },
                        {
                            "comment": "JUNOS jail runtime [20190517.f0321c3_builder_stable_11]",
                            "name": "jail-runtime"
                        }
                    ],
                    "product-model": "vmx",
                    "product-name": "vmx"
                }
            }
        }
        
        
        }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowVersionInvokeOnAllRoutingEngines(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVersionInvokeOnAllRoutingEngines(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
