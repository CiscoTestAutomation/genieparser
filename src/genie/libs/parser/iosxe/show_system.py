"""show_system.py

"""
# Python
import re
import logging
import xml.etree.ElementTree as ET
from xml.dom import minidom
from genie.libs.parser.utils.common import Common

log = logging.getLogger(__name__)

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (
    Schema,
    Any,
    Optional,
    Or,
    And,
    Default,
    Use,
)


class ShowClockSchema(MetaParser):
    """Schema for show clock"""

    schema = {
        "timezone": str,
        "day": str,
        "day_of_week": str,
        "month": str,
        "year": str,
        "time": str,
    }


class ShowClock(ShowClockSchema):
    """Parser for show clock"""

    cli_command = "show clock"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # 05:26:38.035 EST Wed JAN 4 2019
        # *05:26:38.035 EST Wed JAN 4 2019
        p1 = re.compile(
            r"^\*?(?P<time>[\d\:\.]+) +(?P<timezone>\w+)"
            " +(?P<day_of_week>\w+) +(?P<month>\w+) +"
            "(?P<day>\d+) +(?P<year>\d+)$"
        )

        for line in out.splitlines():
            line = line.strip()

            # 18:56:04.554 EST Mon Oct 17 2016
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k: str(v) for k, v in group.items()})
                continue

        return ret_dict


class ShowSystemIntegrityAllMeasurementNonceSchema(MetaParser):
    """Schema for show system integrity all measurement nonce <nonce>"""

    schema = {
        "bay": str,
        "fru": str,
        "node": str,
        "chassis": str,
        "slot": {
            int: {
                "platform": str,
                "boot_hashes": {Any(): str},
                "os": {
                    "version": str,
                    "hashes": {
                        Any(): str,
                    },
                },
                "registers": {"PCR0": str, "PCR8": str},
                "signature": {"version": int, "value": str},
            },
        },
    }


class ShowSystemIntegrityAllMeasurementNonce(ShowSystemIntegrityAllMeasurementNonceSchema):
    """Parser for show system integrity all measurement nonce <nonce>"""

    cli_command = "show system integrity all measurement nonce {nonce}"

    def cli(self, nonce="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(nonce=nonce))

        # initial return dictionary
        ret_dict = {}
        # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
        p1 = re.compile(
            r"^LOCATION FRU=+(?P<fru>\S+) +SLOT=+(?P<slot>\d+) +BAY=+(?P<bay>\d+) +CHASSIS=+(?P<chassis>\S+) +NODE=+(?P<node>\d+)$"
        )
        # Platform: C9410R
        p2 = re.compile(r"^Platform: +(?P<platform>\S+)$")
        # MA1004R06.1604052017: 6243F41868F21144E7D5CE30683
        # 17.8.1r[FC1]: 48E0DD991BCD6274B842A42C0F9DEDCD8809E6187928F0
        p3 = re.compile("^(?P<boot_hash>[\(\)\[\]\.\:A-Z0-9a-z]+)\s(?P<value>[0-9A-F]+)$")
        # Version: BLD_POLARIS_DEV_LATEST_20220313_143357
        p4 = re.compile(r"^Version: +(?P<version>.*\_\S+)$")
        # cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20220313_143357.SSA.bin: 452997E880E6CEF
        # cat9k-wlc.BLD_POLARIS_DEV_LATEST_20220313_143357.SSA.pkg: 9456F1B1CFB3A25C9
        # cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20220313_143357.0.NODEFECT.SSA.smu.bin: 9D7CC2C73A688FAF294C4BB90CAA6FDB26B9B
        p5 = re.compile("^(?P<hashes>(.*bin)|(.*pkg))\:\s(?P<value>\S+)$")
        # PCR0: 6DEC62AF32505978BD553E7
        p6 = re.compile("^PCR0: +(?P<pcr0>([0-9A-F])+)$")
        # PCR8: 6DEC62AF32505978BD553E7
        p7 = re.compile("^PCR8: +(?P<pcr8>([0-9A-F])+)$")
        # Version: 1
        p8 = re.compile(r"^Version: +(?P<version>\d)$")
        # 922D10C26D9DFF33278B4EBD9935A968DD5641C51EF496251
        p9 = re.compile(r"^(?P<value>([0-9A-F])+)$")
        for line in output.splitlines():
            line = line.strip()

            # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
            m = p1.match(line)
            if m:
                count = 0
                group = m.groupdict()
                tmp = int(group["slot"])
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                ret_dict.update({"fru": group["fru"]})
                ret_dict.update({"chassis": group["chassis"]})
                ret_dict.update({"bay": group["bay"]})
                ret_dict.update({"node": group["node"]})
                continue

            # Platform: C9410R
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                device.update({"platform": group["platform"]})
                continue

            # MA1004R06.1604052017: 6243F41868F21144E7D5CE30683
            # 17.8.1r[FC1]: 48E0DD991BCD6274B842A42C0F9DEDCD8809E6187928F0
            m = p3.match(line)
            if m:
                if count <= 1:
                    slot = ret_dict.setdefault("slot", {})
                    device = slot.setdefault(tmp, {})
                    boot_hashes = device.setdefault("boot_hashes", {})
                    group = m.groupdict({})
                    boot_hashes.update({group["boot_hash"][:-1]: group["value"]})
                    count += 1
                    continue

            # Version: BLD_POLARIS_DEV_LATEST_20220313_143357
            m = p4.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                os = device.setdefault("os", {})
                os.update({"version": group["version"]})
                continue

            # cat9k_iosxe.BLD_POLARIS_DEV_LATEST_20220313_143357.SSA.bin: 452997E880E6CEF
            m = p5.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                os = device.setdefault("os", {})
                hashes = os.setdefault("hashes", {})
                hashes.update({group["hashes"]: group["value"]})
                continue

            # PCR0: 6DEC62AF32505978BD553E7
            m = p6.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                reg = device.setdefault("registers", {})
                reg.update({"PCR0": group["pcr0"]})
                continue

            # PCR8: 6DEC62AF32505978BD553E7
            m = p7.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                reg = device.setdefault("registers", {})
                reg.update({"PCR8": group["pcr8"]})
                continue

            # Version: 1
            m = p8.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"version": int(group["version"])})
                continue

            # Value: 922D10C26D9DFF33278B4EBD9935A968DD5641C51EF496251
            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"value": group["value"]})
                continue
        return ret_dict

    def yang(self, nonce="", output=None):
        if not output:
            output = self.device.get(filter=('xpath', f'/system-integrity-oper-data/location/integrity[nonce={nonce}][request="choice-measurement"]')).data_xml
        log.info(minidom.parseString(output).toprettyxml())
        root = ET.fromstring(output)
        system_integrity_oper_data = Common.retrieve_xml_child(root=root, key='system-integrity-oper-data')
        ret_dict = {}
        name = None
        version = None
        for parent in system_integrity_oper_data:
            for child in parent:
                if child.tag.endswith('slot'):
                    slot = int(child.text)
                    slot_dict = ret_dict.setdefault('slot', {})
                    slot_id = slot_dict.setdefault(slot, {})
                elif child.tag.endswith('fru'):
                    ret_dict.update({'fru': child.text})
                elif child.tag.endswith('chassis'):
                    ret_dict.update({'chassis': child.text})
                elif child.tag.endswith('bay'):
                    ret_dict.update({'bay': child.text})
                elif child.tag.endswith('node'):
                    ret_dict.update({'node': child.text})
                elif child.tag.endswith('integrity'):
                    for sub_child in child:
                        if sub_child.tag.endswith('measurement'):
                            for sub_child1 in sub_child:
                                if sub_child1.tag.endswith('boot-loader'):
                                    for sub_child2 in sub_child1:
                                        boot_hash_dict = slot_id.setdefault('boot_hashes',{})
                                        if sub_child2.tag.endswith('version'):
                                            version = sub_child2.text
                                        elif version and sub_child2.tag.endswith('hash'):
                                            boot_hash_dict.update({version: sub_child2.text})
                                elif sub_child1.tag.endswith('platform'):
                                    slot_id.update({'platform': sub_child1.text})
                                elif sub_child1.tag.endswith('operating-system'):
                                    for sub_child2 in sub_child1:
                                        os_dict = slot_id.setdefault('os', {})
                                        if sub_child2.tag.endswith('version'):
                                            os_dict.update({'version': sub_child2.text})
                                        elif sub_child2.tag.endswith('package-integrity'):
                                            for sub_child3 in sub_child2:
                                                os_dict1 = slot_id.setdefault('os', {}). \
                                                                setdefault('hashes', {})
                                                if sub_child3.tag.endswith('name'):
                                                    name = sub_child3.text
                                                elif name and sub_child3.tag.endswith('hash'):
                                                    os_dict1.update({name: sub_child3.text})
                                elif sub_child1.tag.endswith('register'):
                                    for sub_child2 in sub_child1:
                                        regs_dict = slot_id.setdefault('registers', {})
                                        if sub_child2.tag.endswith('index'):
                                            name = 'PCR{}'.format(sub_child2.text)
                                        elif sub_child2.tag.endswith('pcr-content'):
                                            regs_dict.update({name: sub_child2.text})
                                            name = None
                                elif sub_child1.tag.endswith('signature'):
                                    for sub_child2 in sub_child1:
                                        sign_dict = slot_id.setdefault('signature', {})
                                        if sub_child2.tag.endswith('signature'):
                                            sign_dict.update({'value': sub_child2.text})
                                        elif sub_child2.tag.endswith('version'):
                                            sign_dict.update({'version': int(sub_child2.text)})
        return ret_dict


class ShowSystemIntegrityAllComplianceNonceSchema(MetaParser):
    """Schema for show system integrity all compliance nonce <nonce>"""

    schema = {
        "bay": str,
        "fru": str,
        "node": str,
        "chassis": str,
        "slot": {
            int: {
                "compliance": {
                    "secure_boot": str,
                    "tam_service": str,
                    "ldwm_envelope": str,
                    "num_btlstage": int,
                    "bivlen": int,
                    "register_pcr0_disabled": str,
                    "register_pcr8_disabled": str,
                },
                "signature": {"version": int, "value": str},
            },
        },
    }


class ShowSystemIntegrityAllComplianceNonce(ShowSystemIntegrityAllComplianceNonceSchema):
    """Parser for Show system integrity all compliance nonce <nonce>"""

    cli_command = "show system integrity all compliance nonce {nonce}"

    def cli(self, nonce="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(nonce=nonce))

        # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
        p1 = re.compile(
            r"^LOCATION FRU=+(?P<fru>\S+) +SLOT=+(?P<slot>\d+) +BAY=+(?P<bay>\d+) +CHASSIS=+(?P<chassis>\S+) +NODE=+(?P<node>\d+)$"
        )
        # secure_boot: true
        p2 = re.compile(r"^secure_boot: +(?P<secure_boot>\S+)$")
        # tam_service: hardware
        p3 = re.compile(r"^tam_service: +(?P<tam_service>\S+)$")
        # ldwm_envelope: false
        p4 = re.compile(r"^ldwm_envelope: +(?P<ldwm_envelope>\S+)$")
        # num_btlstage: 2
        p5 = re.compile(r"^num_btlstage: +(?P<num_btlstage>\S+)$")
        # bivlen: 64
        p6 = re.compile(r"^bivlen: +(?P<bivlen>\S+)$")
        # register.pcr0.disabled: false
        p7 = re.compile(r"^register.pcr0.disabled: +(?P<pcr0>\S+)$")
        # register.pcr8.disabled: false
        p8 = re.compile(r"^register.pcr8.disabled: +(?P<pcr8>\S+)$")
        # Version: 1
        p9 = re.compile(r"^Version: +(?P<version>\d)$")
        # Value: AA2B82869BD48E0CFFAF75133E14AE891F5592E61C8C3
        p10 = re.compile(r"^(?P<value>([0-9A-F])+)$")
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=-1 NODE=0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tmp = int(group["slot"])
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                ret_dict.update({"fru": group["fru"]})
                ret_dict.update({"chassis": group["chassis"]})
                ret_dict.update({"bay": group["bay"]})
                ret_dict.update({"node": group["node"]})
                continue

            # secure_boot: true
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"secure_boot": group["secure_boot"]})
                continue

            # tam_service: hardware
            m = p3.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"tam_service": group["tam_service"]})
                continue

            # ldwm_envelope: false
            m = p4.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update(
                    {"ldwm_envelope": group["ldwm_envelope"]}
                )
                continue

            # num_btlstage: 2
            m = p5.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"num_btlstage": int(group["num_btlstage"])})
                continue

            # bivlen: 64
            m = p6.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update({"bivlen": int(group["bivlen"])})
                continue

            # register.pcr0.disabled: false
            m = p7.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update(
                    {"register_pcr0_disabled": group["pcr0"]}
                )
                continue

            # register.pcr8.disabled: false
            m = p8.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("compliance", {})
                slot[tmp]["compliance"].update(
                    {"register_pcr8_disabled": group["pcr8"]}
                )
                continue

            # Version: 1
            m = p9.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("signature", {})
                slot[tmp]["signature"].update({"version": int(group["version"])})
                continue

            # Value: AA2B82869BD48E0CFFAF75133E14AE891F5592E61C8C3
            m = p10.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                slot[tmp].setdefault("signature", {})
                slot[tmp]["signature"].update({"value": group["value"]})
                continue
        return ret_dict
    

class ShowSystemIntegrityAllTrustChainNonceSchema(MetaParser):
    """Schema for system integrity all trust_chain nonce <nonce>"""

    schema = {
        "bay": str,
        "fru": str,
        "node": str,
        "chassis": str,
        "slot": {
            int: {
                "crca_certificate": str,
                "cmca_certificate": str,
                "sudi_certificate": str,
                "signature": {"version": int, "value": str},
            },
        },
    }


class ShowSystemIntegrityAllTrustChainNonce(ShowSystemIntegrityAllTrustChainNonceSchema):
    """Parser for system integrity all trust_chain nonce <nonce>"""

    cli_command = "show system integrity all trust_chain nonce {nonce}"

    def cli(self, nonce="", output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(nonce=nonce))

        # initial return dictionary
        ret_dict = {}

        # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=3 NODE=0
        p1 = re.compile(
            r"^LOCATION FRU=+(?P<fru>\S+) +SLOT=+(?P<slot>\d+) +BAY=+(?P<bay>\d+) +CHASSIS=+(?P<chassis>\S+) +NODE=+(?P<node>\d+)$"
        )
        # Version: 1
        p2 = re.compile(r"^Version: +(?P<version>\d)$")
        #   Value: 9DA0FB31FA0BF959BDE14FEE6E20D6CD837E8108E4D37E9088C67E8CD1E7A7C015C1
        p3 = re.compile("^(?P<value>[A-F0-9]+)$")
        # Certificate Name: CMCA CERTIFICATE
        p4 = re.compile(r"^Certificate Name: +(?P<certificate_name>\S+\s\S+)$")
        # -----BEGIN CERTIFICATE-----
        p5 = re.compile("^\-+BEGIN CERTIFICATE\-+$")
        # -----END CERTIFICATE-----
        p6 = re.compile("^\-+END CERTIFICATE\-+$")
        # MIIDfTCCAmWgAwIBAgIEAfLTJTANBgkqhkiG9w0BAQsFADAnMQ4wDAYDVQQKEwVDaXNjbzEVMBMG
        p7 = re.compile("^([a-zA-Z0-9/+=]+)$")

        certificate_name = ""
        certificate = ""
        begin_certificate = None

        for line in output.splitlines():
            line = line.strip()

            # LOCATION FRU=fru-rp SLOT=0 BAY=0 CHASSIS=3 NODE=0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tmp = int(group["slot"])
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                ret_dict.update({"fru": group["fru"]})
                ret_dict.update({"chassis": group["chassis"]})
                ret_dict.update({"bay": group["bay"]})
                ret_dict.update({"node": group["node"]})
                continue

            # Version: 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"version": int(group["version"])})
                continue

            # Value: 9DA0FB31FA0BF959BDE14FEE6E20D6CD837E8108E4D37E9088C67E8CD1E7A7C015C1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                signature = device.setdefault("signature", {})
                signature.update({"value": group["value"]})
                continue

            # Certificate Name: CMCA CERTIFICATE
            m = p4.match(line)
            if m:
                group = m.groupdict()
                certificate_id = group["certificate_name"]
                continue

            # -----BEGIN CERTIFICATE-----
            m = p5.match(line)
            if m:
                begin_certificate = True
                certificate_name = certificate_id.replace(" ", "_").lower()
                continue

            # -----END CERTIFICATE-----
            m = p6.match(line)
            if m:
                slot = ret_dict.setdefault("slot", {})
                device = slot.setdefault(tmp, {})
                device.update({certificate_name: certificate})
                certificate = ""
                begin_certificate = False
                continue

            # MIIDfTCCAmWgAwIBAgIEAfLTJTANBgkqhkiG9w0BAQsFADAnMQ4wDAYDVQQKEwVDaXNjbzEVMBMG
            m = p7.match(line)
            if m:
                if begin_certificate:
                    certificate = certificate + m.group()
                    continue

        return ret_dict

    def yang(self, nonce="", output=None):
        if not output:
            output = self.device.get(filter=('xpath', f'/system-integrity-oper-data/location/integrity[nonce={nonce}][request="choice-trust-chain"]')).data_xml
        
        log.debug(minidom.parseString(output).toprettyxml())
        
        root = ET.fromstring(output)
        system_integrity_oper_data = Common.retrieve_xml_child(root=root, key='system-integrity-oper-data')
        ret_dict = {}
        name = None
        for parent in system_integrity_oper_data:
            for child in parent:
                if child.tag.endswith('slot'):
                    slot = int(child.text)
                    slot_dict = ret_dict.setdefault('slot', {})
                    slot_id = slot_dict.setdefault(slot, {})
                elif child.tag.endswith('fru'):
                    ret_dict.update({'fru': child.text})
                elif child.tag.endswith('chassis'):
                    ret_dict.update({'chassis': child.text})
                elif child.tag.endswith('bay'):
                    ret_dict.update({'bay': child.text})
                elif child.tag.endswith('node'):
                    ret_dict.update({'node': child.text})
                elif child.tag.endswith('integrity'):
                    for sub_child in child:
                        if sub_child.tag.endswith('trust-chain'):
                            for sub_child1 in sub_child:
                                if sub_child1.tag.endswith('trust-chain'):
                                    for sub_child2 in sub_child1:
                                        if sub_child2.tag.endswith('name'):
                                            name = sub_child2.text.replace(" ","_").lower()
                                        elif name and sub_child2.tag.endswith('value'):
                                            slot_id.update({name: sub_child2.text})
                                            name = None
                                elif sub_child1.tag.endswith('signature'):
                                    for sub_child2 in sub_child1:
                                        sign_dict = slot_id.setdefault('signature',{})
                                        if sub_child2.tag.endswith('signature'):
                                            sign_dict.update({'value': sub_child2.text})
                                        elif sub_child2.tag.endswith('version'):
                                            sign_dict.update({'version': int(sub_child2.text)})
        return ret_dict

