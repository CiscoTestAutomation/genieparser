""" show_krt.py

JunOs parsers for the following show commands:
    * show version detail
    * show version detail no-forwarding
    * show version invoke-on all-routing-engines
"""

import re

from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, ListOf)


class ShowVersionDetailSchema(MetaParser):

    """ schema = {
    Optional("@xmlns:junos"): str,
    "software-information": {
        Optional("cli"): {
            "display-version": str
        },
        "host-name": str,
        "junos-version": str,
        "output": "list",
        "package-information": [
            {
                "comment": str,
                "name": str
            }
        ],
        "product-model": str,
        "product-name": str,
        "version-information": [
            {
                "build-date": str,
                "build-number": str,
                "builder": str,
                "component": str,
                "major": str,
                "minor": str,
                "release": str,
                "release-category": str,
                "spin": str
            }
        ]
    }
} """

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        "software-information": {
            Optional("cli"): {
                Optional("display-version"): str
            },
            "host-name": str,
            "junos-version": str,
            "output": list,
            "package-information": ListOf({
                "comment": str,
                "name": str
            }),
            "product-model": str,
            Optional("product-name"): str,
            "version-information": ListOf({
                "build-date": str,
                Optional("build-number"): str,
                "builder": str,
                "component": str,
                Optional("major"): str,
                Optional("minor"): str,
                "release": str,
                Optional("release-category"): str,
                Optional("spin"): str
            })
        }
    }


class ShowVersionDetail(ShowVersionDetailSchema):
    """ Parser for:
    * show version detail
    """
    cli_command = 'show version detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #Hostname: sr_hktGDS201
        p1 = re.compile(r'^Hostname: +(?P<host_name>\S+)$')

        #Model: vmx
        p2 = re.compile(r'^Model: +(?P<product_model>\S+)$')

        #Junos: 19.2R1.8
        p3 = re.compile(r'^Junos: +(?P<junos_version>\S+)$')

        #JLAUNCHD release 19.2R1.8 built by builder on 2019-06-21 17:47:00 UTC
        p4 = re.compile(r'^(?P<output>\AJLAUNCHD+[\S\s]+)$')

        #smartd 6.4 2015-06-04 r4109 [FreeBSD JNPR-11.0-20190517.f0321c3_buil amd64] Junos Build
        p5 = re.compile(r'^(?P<output>\Asmartd+[\S\s]+)$')

        #Copyright (C) 2002-15, Bruce Allen, Christian Franke, www.smartmontools.org
        p6 = re.compile(r'^(?P<output>\ACopyright+[\S\s]+)$')

        #JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]
        p7 = re.compile(r'^(?P<comment>JUNOS[\S\s]+)$')

        #KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built
        p8 = re.compile(r'^(?P<comment>KERNEL[\S\s]+)$')

        #MGD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:49 UTC
        #COMMIT-SYNCD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:46 UTC
        p9 = re.compile(r'^(?P<component>[\w\s\-]+)release +(?P<release>\S+) +built +by +(?P<builder>\S+) +on +(?P<build_date>[\S\s]+)$')

        package_map = {"JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]":"os-kernel",
                            "JUNOS OS libs [20190517.f0321c3_builder_stable_11]":"os-libs",
                            "JUNOS OS runtime [20190517.f0321c3_builder_stable_11]":"os-runtime",
                            "JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]":"zoneinfo",
                            "JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]":"netstack",
                            "JUNOS libs [20190621.152752_builder_junos_192_r1]":"junos-libs",
                            "JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]":"os-libs-compat32",
                            "JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]":"os-compat32",
                            "JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]":"junos-libs-compat32",
                            "JUNOS runtime [20190621.152752_builder_junos_192_r1]":"junos-runtime",
                            "JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]":"vmguest",
                            "JUNOS sflow mx [20190621.152752_builder_junos_192_r1]":"sflow-platform",
                            "JUNOS py extensions [20190621.152752_builder_junos_192_r1]":"py-extensions",
                            "JUNOS py base [20190621.152752_builder_junos_192_r1]":"py-base",
                            "JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]":"os-vmguest",
                            "JUNOS OS crypto [20190517.f0321c3_builder_stable_11]":"os-crypto",
                            "JUNOS na telemetry [19.2R1.8]":"na-telemetry",
                            "JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]":"junos-libs-compat32-platform",
                            "JUNOS mx runtime [20190621.152752_builder_junos_192_r1]":"junos-runtime-platform",
                            "JUNOS common platform support [20190621.152752_builder_junos_192_r1]":"junos-platform",
                            "JUNOS Openconfig [19.2R1.8]":"junos-openconfig",
                            "JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]":"junos-net-platform",
                            "JUNOS modules [20190621.152752_builder_junos_192_r1]":"junos-modules",
                            "JUNOS mx modules [20190621.152752_builder_junos_192_r1]":"junos-modules-platform",
                            "JUNOS mx libs [20190621.152752_builder_junos_192_r1]":"junos-libs-platform",
                            "JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]":"junos-jsqlsync",
                            "JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]":"junos-dp-crypto-support-platform",
                            "JUNOS daemons [20190621.152752_builder_junos_192_r1]":"junos-daemons",
                            "JUNOS mx daemons [20190621.152752_builder_junos_192_r1]":"junos-daemons-platform",
                            "JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]":"junos-appidd",
                            "JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]":"jsim-wrlinux",
                            "JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]":"jsim-pfe-vmx",
                            "JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]":"jservices-urlf",
                            "JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]":"jservices-traffic-dird",
                            "JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]":"jservices-telemetry",
                            "JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]":"jservices-tcp-log",
                            "JUNOS Services SSL [20190621.152752_builder_junos_192_r1]":"jservices-ssl",
                            "JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]":"jservices-softwire",
                            "JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]":"jservices-sfw",
                            "JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]":"jservices-rtcom",
                            "JUNOS Services RPM [20190621.152752_builder_junos_192_r1]":"jservices-rpm",
                            "JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]":"jservices-pcef",
                            "JUNOS Services NAT [20190621.152752_builder_junos_192_r1]":"jservices-nat",
                            "JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]":"jservices-mss",
                            "JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]":"jservices-mobile",
                            "JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]":"jservices-lrf",
                            "JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]":"jservices-llpdf",
                            "JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]":"jservices-jflow",
                            "JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]":"jservices-jdpi",
                            "JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]":"jservices-ipsec",
                            "JUNOS Services IDS [20190621.152752_builder_junos_192_r1]":"jservices-ids",
                            "JUNOS IDP Services [20190621.152752_builder_junos_192_r1]":"jservices-idp",
                            "JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]":"jservices-hcm",
                            "JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]":"jservices-fwdd",
                            "JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]":"jservices-crypto-base",
                            "JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]":"jservices-cpcd",
                            "JUNOS Services COS [20190621.152752_builder_junos_192_r1]":"jservices-cos",
                            "JUNOS AppId Services [20190621.152752_builder_junos_192_r1]":"jservices-appid",
                            "JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]":"jservices-alg",
                            "JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]":"jservices-aacl",
                            "JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]":"jsd-jet-1",
                            "JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]":"jmrt-base-x86-64",
                            "JUNOS J-Insight [20190621.152752_builder_junos_192_r1]":"jinsight",
                            "JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]":"jdocs",
                            "JUNOS jail runtime [20190517.f0321c3_builder_stable_11]":"jail-runtime",
                            "KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built":"KERNEL"
                }

        for line in out.splitlines():
            line = line.strip()

            # Hostname: sr_hktGDS201
            m = p1.match(line)
            if m:
                software_info_first_entry = ret_dict.setdefault("software-information", {})
                group = m.groupdict()
                package_list = []
                version_info_list = []
                software_info_first_entry['host-name'] = group['host_name']
                continue

            # Model: vmx
            m = p2.match(line)
            if m:
                group = m.groupdict()
                software_info_first_entry['product-model'] = group['product_model']
                software_info_first_entry['product-name'] = group['product_model']
                continue

            # Junos: 19.2R1.8
            m = p3.match(line)
            if m:
                group = m.groupdict()
                software_info_first_entry['junos-version'] = group['junos_version']
                continue

            # JLAUNCHD release 19.2R1.8 built by builder on 2019-06-21 17:47:00 UTC
            m = p4.match(line)
            if m:
                group = m.groupdict()
                output_list = []
                output_list.append(group['output'])
                continue

            # smartd 6.4 2015-06-04 r4109 [FreeBSD JNPR-11.0-20190517.f0321c3_buil amd64] Junos Build
            m = p5.match(line)
            if m:
                group = m.groupdict()
                output_list.append(group['output'])
                continue

            # Copyright (C) 2002-15, Bruce Allen, Christian Franke, www.smartmontools.org
            m = p6.match(line)
            if m:
                group = m.groupdict()
                output_list.append(group['output'])
                software_info_first_entry["output"] = output_list

                continue


            #JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["comment"] = group["comment"]
                entry_dict["name"] = package_map[group["comment"]]
                package_list.append(entry_dict)
                continue

            #KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built
            m = p8.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["comment"] = group["comment"]
                entry_dict["name"] = package_map[group["comment"]]
                package_list.append(entry_dict)
                software_info_first_entry["package-information"] = package_list

                continue

            #MGD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:49 UTC
            #COMMIT-SYNCD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:46 UTC
            m = p9.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["build-date"] = group["build_date"]
                entry_dict["builder"] = group["builder"]
                entry_dict["component"] = group["component"]
                entry_dict["release"] = group["release"]
                version_info_list.append(entry_dict)
                if(group["component"].strip() == "vlans-ng-actions-dd"):
                    software_info_first_entry["version-information"] = version_info_list
                continue

        return ret_dict


class ShowVersionDetailNoForwarding(ShowVersionDetail):
    """ Parser for:
            - show version detail no-forwarding
    """

    cli_command = 'show version detail no-forwarding'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)


class ShowVersionInvokeOnAllRoutingEnginesSchema(MetaParser):

    """ schema = {
    Optional("@xmlns:junos"): str,
    "multi-routing-engine-results": {
        "multi-routing-engine-item": {
            "re-name": str,
            "software-information": {
                "host-name": str,
                "junos-version": str,
                "package-information": [
                    {
                        "comment": str,
                        "name": str
                    }
                ],
                "product-model": str,
                "product-name": str
            }
        }
    }
} """

    # Main Schema
    schema = {
    Optional("@xmlns:junos"): str,
    "multi-routing-engine-results": {
        "multi-routing-engine-item": {
            "re-name": str,
            "software-information": {
                "host-name": str,
                "junos-version": str,
                "package-information": ListOf({
                        "comment": str,
                        "name": str
                }),
                "product-model": str,
                Optional("product-name"): str
                }
            }
        }
    }


class ShowVersionInvokeOnAllRoutingEngines(ShowVersionInvokeOnAllRoutingEnginesSchema):
    """ Parser for:
    * show version invoke-on all-routing-engines
    """
    cli_command = 'show version invoke-on all-routing-engines'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #re0:
        p0 = re.compile(r'^(?P<re_name>\Are0+)+:$')

        #Hostname: sr_hktGDS201
        p1 = re.compile(r'^Hostname: +(?P<host_name>\S+)$')

        #Model: vmx
        p2 = re.compile(r'^Model: +(?P<product_model>\S+)$')

        #Junos: 19.2R1.8
        p3 = re.compile(r'^Junos: +(?P<junos_version>\S+)$')

        #JLAUNCHD release 19.2R1.8 built by builder on 2019-06-21 17:47:00 UTC
        p4 = re.compile(r'^(?P<output>\AJLAUNCHD+[\S\s]+)$')

        #smartd 6.4 2015-06-04 r4109 [FreeBSD JNPR-11.0-20190517.f0321c3_buil amd64] Junos Build
        p5 = re.compile(r'^(?P<output>\Asmartd+[\S\s]+)$')

        #Copyright (C) 2002-15, Bruce Allen, Christian Franke, www.smartmontools.org
        p6 = re.compile(r'^(?P<output>\ACopyright+[\S\s]+)$')

        #JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]
        p7 = re.compile(r'^(?P<comment>JUNOS[\S\s]+)$')

        #KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built
        p8 = re.compile(r'^(?P<comment>KERNEL[\S\s]+)$')

        #MGD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:49 UTC
        #COMMIT-SYNCD release 20190606.224121_builder.r1033375 built by builder on 2019-06-06 22:58:46 UTC
        p9 = re.compile(r'^(?P<component>[\w\s\-]+)release +(?P<release>\S+) +built +by +(?P<builder>\S+) +on +(?P<build_date>[\S\s]+)$')

        package_map = {"JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]":"os-kernel",
                            "JUNOS OS libs [20190517.f0321c3_builder_stable_11]":"os-libs",
                            "JUNOS OS runtime [20190517.f0321c3_builder_stable_11]":"os-runtime",
                            "JUNOS OS time zone information [20190517.f0321c3_builder_stable_11]":"zoneinfo",
                            "JUNOS network stack and utilities [20190621.152752_builder_junos_192_r1]":"netstack",
                            "JUNOS libs [20190621.152752_builder_junos_192_r1]":"junos-libs",
                            "JUNOS OS libs compat32 [20190517.f0321c3_builder_stable_11]":"os-libs-compat32",
                            "JUNOS OS 32-bit compatibility [20190517.f0321c3_builder_stable_11]":"os-compat32",
                            "JUNOS libs compat32 [20190621.152752_builder_junos_192_r1]":"junos-libs-compat32",
                            "JUNOS runtime [20190621.152752_builder_junos_192_r1]":"junos-runtime",
                            "JUNOS Packet Forwarding Engine Simulation Package [20190621.152752_builder_junos_192_r1]":"vmguest",
                            "JUNOS sflow mx [20190621.152752_builder_junos_192_r1]":"sflow-platform",
                            "JUNOS py extensions [20190621.152752_builder_junos_192_r1]":"py-extensions",
                            "JUNOS py base [20190621.152752_builder_junos_192_r1]":"py-base",
                            "JUNOS OS vmguest [20190517.f0321c3_builder_stable_11]":"os-vmguest",
                            "JUNOS OS crypto [20190517.f0321c3_builder_stable_11]":"os-crypto",
                            "JUNOS na telemetry [19.2R1.8]":"na-telemetry",
                            "JUNOS mx libs compat32 [20190621.152752_builder_junos_192_r1]":"junos-libs-compat32-platform",
                            "JUNOS mx runtime [20190621.152752_builder_junos_192_r1]":"junos-runtime-platform",
                            "JUNOS common platform support [20190621.152752_builder_junos_192_r1]":"junos-platform",
                            "JUNOS Openconfig [19.2R1.8]":"junos-openconfig",
                            "JUNOS mtx network modules [20190621.152752_builder_junos_192_r1]":"junos-net-platform",
                            "JUNOS modules [20190621.152752_builder_junos_192_r1]":"junos-modules",
                            "JUNOS mx modules [20190621.152752_builder_junos_192_r1]":"junos-modules-platform",
                            "JUNOS mx libs [20190621.152752_builder_junos_192_r1]":"junos-libs-platform",
                            "JUNOS SQL Sync Daemon [20190621.152752_builder_junos_192_r1]":"junos-jsqlsync",
                            "JUNOS mtx Data Plane Crypto Support [20190621.152752_builder_junos_192_r1]":"junos-dp-crypto-support-platform",
                            "JUNOS daemons [20190621.152752_builder_junos_192_r1]":"junos-daemons",
                            "JUNOS mx daemons [20190621.152752_builder_junos_192_r1]":"junos-daemons-platform",
                            "JUNOS -MX appidd application-identification daemon [20190621.152752_builder_junos_192_r1]":"junos-appidd",
                            "JUNOS Simulation Linux Package [20190621.152752_builder_junos_192_r1]":"jsim-wrlinux",
                            "JUNOS Simulation Package [20190621.152752_builder_junos_192_r1]":"jsim-pfe-vmx",
                            "JUNOS Services URL Filter package [20190621.152752_builder_junos_192_r1]":"jservices-urlf",
                            "JUNOS Services TLB Service PIC package [20190621.152752_builder_junos_192_r1]":"jservices-traffic-dird",
                            "JUNOS Services Telemetry [20190621.152752_builder_junos_192_r1]":"jservices-telemetry",
                            "JUNOS Services TCP-LOG [20190621.152752_builder_junos_192_r1]":"jservices-tcp-log",
                            "JUNOS Services SSL [20190621.152752_builder_junos_192_r1]":"jservices-ssl",
                            "JUNOS Services SOFTWIRE [20190621.152752_builder_junos_192_r1]":"jservices-softwire",
                            "JUNOS Services Stateful Firewall [20190621.152752_builder_junos_192_r1]":"jservices-sfw",
                            "JUNOS Services RTCOM [20190621.152752_builder_junos_192_r1]":"jservices-rtcom",
                            "JUNOS Services RPM [20190621.152752_builder_junos_192_r1]":"jservices-rpm",
                            "JUNOS Services PCEF package [20190621.152752_builder_junos_192_r1]":"jservices-pcef",
                            "JUNOS Services NAT [20190621.152752_builder_junos_192_r1]":"jservices-nat",
                            "JUNOS Services Mobile Subscriber Service Container package [20190621.152752_builder_junos_192_r1]":"jservices-mss",
                            "JUNOS Services MobileNext Software package [20190621.152752_builder_junos_192_r1]":"jservices-mobile",
                            "JUNOS Services Logging Report Framework package [20190621.152752_builder_junos_192_r1]":"jservices-lrf",
                            "JUNOS Services LL-PDF Container package [20190621.152752_builder_junos_192_r1]":"jservices-llpdf",
                            "JUNOS Services Jflow Container package [20190621.152752_builder_junos_192_r1]":"jservices-jflow",
                            "JUNOS Services Deep Packet Inspection package [20190621.152752_builder_junos_192_r1]":"jservices-jdpi",
                            "JUNOS Services IPSec [20190621.152752_builder_junos_192_r1]":"jservices-ipsec",
                            "JUNOS Services IDS [20190621.152752_builder_junos_192_r1]":"jservices-ids",
                            "JUNOS IDP Services [20190621.152752_builder_junos_192_r1]":"jservices-idp",
                            "JUNOS Services HTTP Content Management package [20190621.152752_builder_junos_192_r1]":"jservices-hcm",
                            "JUNOS Services Flowd MS-MPC Software package [20190621.152752_builder_junos_192_r1]":"jservices-fwdd",
                            "JUNOS Services Crypto [20190621.152752_builder_junos_192_r1]":"jservices-crypto-base",
                            "JUNOS Services Captive Portal and Content Delivery Container package [20190621.152752_builder_junos_192_r1]":"jservices-cpcd",
                            "JUNOS Services COS [20190621.152752_builder_junos_192_r1]":"jservices-cos",
                            "JUNOS AppId Services [20190621.152752_builder_junos_192_r1]":"jservices-appid",
                            "JUNOS Services Application Level Gateways [20190621.152752_builder_junos_192_r1]":"jservices-alg",
                            "JUNOS Services AACL Container package [20190621.152752_builder_junos_192_r1]":"jservices-aacl",
                            "JUNOS Extension Toolkit [20190621.152752_builder_junos_192_r1]":"jsd-jet-1",
                            "JUNOS Juniper Malware Removal Tool (JMRT) [1.0.0+20190621.152752_builder_junos_192_r1]":"jmrt-base-x86-64",
                            "JUNOS J-Insight [20190621.152752_builder_junos_192_r1]":"jinsight",
                            "JUNOS Online Documentation [20190621.152752_builder_junos_192_r1]":"jdocs",
                            "JUNOS jail runtime [20190517.f0321c3_builder_stable_11]":"jail-runtime",
                            "KERNEL JNPR-11.0-20190517.f0321c3_builder_stable_11 #0 r356482+f0321c3e9c9(HEAD) built":"KERNEL"
                }

        for line in out.splitlines():
            line = line.strip()

            #re0:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                multi_routing_engine_item_entry = ret_dict.setdefault("multi-routing-engine-results", {}).\
                                            setdefault("multi-routing-engine-item", {})
                software_information_entry = multi_routing_engine_item_entry.setdefault("software-information", {})
                multi_routing_engine_item_entry['re-name'] = group['re_name']
                continue

            # Hostname: sr_hktGDS201
            m = p1.match(line)
            if m:
                group = m.groupdict()
                package_list = []
                software_information_entry['host-name'] = group['host_name']
                continue

            # Model: vmx
            m = p2.match(line)
            if m:
                group = m.groupdict()
                software_information_entry['product-model'] = group['product_model']
                software_information_entry['product-name'] = group['product_model']
                continue

            # Junos: 19.2R1.8
            m = p3.match(line)
            if m:
                group = m.groupdict()
                software_information_entry['junos-version'] = group['junos_version']
                continue


            #JUNOS OS Kernel 64-bit  [20190517.f0321c3_builder_stable_11]
            m = p7.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["comment"] = group["comment"]
                entry_dict["name"] = package_map[group["comment"]]
                package_list.append(entry_dict)

                if(group["comment"].strip() == "JUNOS jail runtime [20190517.f0321c3_builder_stable_11]"):
                    software_information_entry["package-information"] = package_list
                continue

        return ret_dict