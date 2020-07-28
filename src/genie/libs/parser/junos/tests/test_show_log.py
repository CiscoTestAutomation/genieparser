import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_log import ShowLogFilename


class TestShowLogFilename(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show log messages
        Mar  5 00:45:00 sr_hktGCS001 newsyslog[89037]: logfile turned over due to size>1024K
        Mar  5 02:42:53  sr_hktGCS001 sshd[87374]: Received disconnect from 10.1.0.1 port 46480:11: disconnected by user
        Mar  5 02:42:53  sr_hktGCS001 sshd[87374]: Disconnected from 10.1.0.1 port 46480
        Mar  5 02:42:53  sr_hktGCS001 inetd[6841]: /usr/sbin/sshd[87371]: exited, status 255
        Mar  5 14:47:18  sr_hktGCS001 sshd[91368]: Accepted keyboard-interactive/pam for user from 10.1.0.1 port 46494 ssh2
        Mar  5 14:47:45  sr_hktGCS001 mgd[91373]: UI_DBASE_LOGIN_EVENT: User 'user' entering configuration mode
        Mar  5 14:47:45  sr_hktGCS001 mgd[91373]: UI_LOAD_EVENT: User 'user' is performing a 'load override'
        Mar  5 14:47:45  sr_hktGCS001 mgd[91373]: UI_COMMIT: User 'user' requested 'commit' operation (comment: none)
        Mar  5 14:47:47  sr_hktGCS001 mgd[91373]: UI_CHILD_EXITED: Child exited: PID 91546, status 7, command '/usr/sbin/mustd'
        Mar  5 14:47:47  sr_hktGCS001 ffp: "dynamic-profiles": Profiles are being modified
        Mar  5 14:47:47  sr_hktGCS001 rpd[91549]: ted_client reset
        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: JAM:PL: mod info  i2cc4a
        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: JAM:PL: asy info  i2cc4a
        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: JAM:PL: Reg Attribs done for c4a
        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: JAM:PL: vectors_set done for c4a
        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: JAM:PL: ds_prepare done for c4a
        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: CHASSISD_IOCTL_FAILURE: acb_get_fpga_rev: unable to get FPGA revision for Control Board (Inappropriate ioctl for device)
        Mar  5 14:47:48  sr_hktGCS001 agentd[91565]: AGENTD_CONFIG_INFO: Entering configuration read. is_master:0
        Mar  5 14:47:48  sr_hktGCS001 agentd[91565]: AGENTD_SENSOR_INSTALL_SUCCESS: Sensor install success :sensorname: sensor_1000, resname: /junos/events/event[id='CHASSISD_SNMP_TRAP7']/
        Mar  5 14:47:48  sr_hktGCS001 agentd[91565]: AGENTD_SENSOR_INSTALL_SUCCESS: Sensor install success :sensorname: sensor_1003, resname: /components/
        Mar  5 14:47:48  sr_hktGCS001 mobiled: MBG_PKG_BBE_NOT_FOUND: Neither BNG LIC nor JMOBILE package is present, exit mobiled on(single Chassis, MXVC, GNF)
        Mar  5 14:47:49  sr_hktGCS001 ffp: "dynamic-profiles": Profiles are being modified
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92002(disk-monitoring): exec_command
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92003((null)): exec_command
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Alarm clear command: /usr/sbin/cli (PID 92003) started
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: disk-monitoring (PID 92002) started
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92002(disk-monitoring): new process
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92004(mobiled): exec_command
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92005((null)): exec_command
        Mar  5 14:47:49  sr_hktGCS001 mobiled: MBG_PKG_BBE_NOT_FOUND: Neither BNG LIC nor JMOBILE package is present, exit mobiled on(single Chassis, MXVC, GNF)
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Alarm clear command: /usr/sbin/cli (PID 92005) started
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: mobiled (PID 92004) started
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92004(mobiled): new process
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92006(commit-batch): exec_command
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: commit-batch (PID 92006) started
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92006(commit-batch): new process
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: mobiled (PID 92004) exited with status=0 Normal Exit
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92007(mobiled): exec_command
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: mobiled (PID 92007) started
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92007(mobiled): new process
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: commit-batch (PID 92006) exited with status=0 Normal Exit
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: disk-monitoring (PID 92002) exited with status=17
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92008(disk-monitoring): exec_command
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: disk-monitoring (PID 92008) started
        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered PID 92008(disk-monitoring): new process
        Mar  5 14:47:50  sr_hktGCS001 rpd[6904]: ted_client reset
    """
    }

    golden_parsed_output = {
        "file-content": [
            "        show log messages",
            "        Mar  5 00:45:00 sr_hktGCS001 newsyslog[89037]: "
            "logfile turned over due to size>1024K",
            "        Mar  5 02:42:53  sr_hktGCS001 sshd[87374]: Received "
            "disconnect from 10.1.0.1 port 46480:11: disconnected by user",
            "        Mar  5 02:42:53  sr_hktGCS001 sshd[87374]: "
            "Disconnected from 10.1.0.1 port 46480",
            "        Mar  5 02:42:53  sr_hktGCS001 inetd[6841]: "
            "/usr/sbin/sshd[87371]: exited, status 255",
            "        Mar  5 14:47:18  sr_hktGCS001 sshd[91368]: Accepted "
            "keyboard-interactive/pam for user from 10.1.0.1 port 46494 "
            "ssh2",
            "        Mar  5 14:47:45  sr_hktGCS001 mgd[91373]: "
            "UI_DBASE_LOGIN_EVENT: User 'user' entering configuration "
            "mode",
            "        Mar  5 14:47:45  sr_hktGCS001 mgd[91373]: "
            "UI_LOAD_EVENT: User 'user' is performing a 'load override'",
            "        Mar  5 14:47:45  sr_hktGCS001 mgd[91373]: "
            "UI_COMMIT: User 'user' requested 'commit' operation "
            "(comment: none)",
            "        Mar  5 14:47:47  sr_hktGCS001 mgd[91373]: "
            "UI_CHILD_EXITED: Child exited: PID 91546, status 7, command "
            "'/usr/sbin/mustd'",
            "        Mar  5 14:47:47  sr_hktGCS001 ffp: "
            '"dynamic-profiles": Profiles are being modified',
            "        Mar  5 14:47:47  sr_hktGCS001 rpd[91549]: " "ted_client reset",
            "        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: "
            "JAM:PL: mod info  i2cc4a",
            "        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: "
            "JAM:PL: asy info  i2cc4a",
            "        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: "
            "JAM:PL: Reg Attribs done for c4a",
            "        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: "
            "JAM:PL: vectors_set done for c4a",
            "        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: "
            "JAM:PL: ds_prepare done for c4a",
            "        Mar  5 14:47:47  sr_hktGCS001 chassisd[91550]: "
            "CHASSISD_IOCTL_FAILURE: acb_get_fpga_rev: unable to get "
            "FPGA revision for Control Board (Inappropriate ioctl for "
            "device)",
            "        Mar  5 14:47:48  sr_hktGCS001 agentd[91565]: "
            "AGENTD_CONFIG_INFO: Entering configuration read. "
            "is_master:0",
            "        Mar  5 14:47:48  sr_hktGCS001 agentd[91565]: "
            "AGENTD_SENSOR_INSTALL_SUCCESS: Sensor install success "
            ":sensorname: sensor_1000, resname: "
            "/junos/events/event[id='CHASSISD_SNMP_TRAP7']/",
            "        Mar  5 14:47:48  sr_hktGCS001 agentd[91565]: "
            "AGENTD_SENSOR_INSTALL_SUCCESS: Sensor install success "
            ":sensorname: sensor_1003, resname: /components/",
            "        Mar  5 14:47:48  sr_hktGCS001 mobiled: "
            "MBG_PKG_BBE_NOT_FOUND: Neither BNG LIC nor JMOBILE package "
            "is present, exit mobiled on(single Chassis, MXVC, GNF)",
            "        Mar  5 14:47:49  sr_hktGCS001 ffp: "
            '"dynamic-profiles": Profiles are being modified',
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92002(disk-monitoring): exec_command",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92003((null)): exec_command",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Alarm clear "
            "command: /usr/sbin/cli (PID 92003) started",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: "
            "disk-monitoring (PID 92002) started",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92002(disk-monitoring): new process",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92004(mobiled): exec_command",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92005((null)): exec_command",
            "        Mar  5 14:47:49  sr_hktGCS001 mobiled: "
            "MBG_PKG_BBE_NOT_FOUND: Neither BNG LIC nor JMOBILE package "
            "is present, exit mobiled on(single Chassis, MXVC, GNF)",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Alarm clear "
            "command: /usr/sbin/cli (PID 92005) started",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: mobiled "
            "(PID 92004) started",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92004(mobiled): new process",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92006(commit-batch): exec_command",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: "
            "commit-batch (PID 92006) started",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92006(commit-batch): new process",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: mobiled "
            "(PID 92004) exited with status=0 Normal Exit",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92007(mobiled): exec_command",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: mobiled "
            "(PID 92007) started",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92007(mobiled): new process",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: "
            "commit-batch (PID 92006) exited with status=0 Normal Exit",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: "
            "disk-monitoring (PID 92002) exited with status=17",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92008(disk-monitoring): exec_command",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: "
            "disk-monitoring (PID 92008) started",
            "        Mar  5 14:47:49  sr_hktGCS001 jlaunchd: Registered "
            "PID 92008(disk-monitoring): new process",
            "        Mar  5 14:47:50  sr_hktGCS001 rpd[6904]: ted_client " "reset",
            "    ",
        ]
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLogFilename(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLogFilename(device=self.device)
        parsed_output = obj.parse(filename="messages")
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()