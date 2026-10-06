"""IOSXE C9250 parsers for the following commands:

* ``show platform hardware fed {mode} qos scheduler sdk interface
  {interface}``
* ``show platform hardware fed {switch} {mode} qos scheduler sdk interface
  {interface}``
* ``show platform hardware fed active qos queue stats interface {interface}``
* ``show platform hardware fed switch {switch_num} qos queue stats interface
  {interface}``
* ``show platform hardware fed active qos queue stats interface {interface}
  clear``
* ``show platform hardware fed switch {switch_num} qos queue stats interface
  {interface} clear``
* ``show platform hardware fed active qos queue config interface {interface}``
* ``show platform hardware fed switch {switch_num} qos queue config interface
  {interface}``
* ``show platform hardware fed {switch} active qos queue stats internal
  port_type punt queue {voq_id}``
* ``show platform hardware fed switch active qos queue stats internal
  port_type punt queue {voq_id}``
* ``show platform hardware fed {switch} {mode} fwd-asic resource tcam
  utilization [asic]``
* ``show platform hardware fed active fwd-asic resource tcam utilization
  [asic]``
* ``show platform hardware fed switch {mode} fwd-asic resource tcam
  utilization [asic]``
* ``show platform software fed switch active acl info db detail``
* ``show platform software fed {switch} {mode} acl info db detail``
* ``show platform software fed {mode} acl info db detail``
* ``show platform software fed {switch} active punt asic-cause brief``
* ``show platform software fed active punt asic-cause brief``
* ``show inventory``

The C9250 uses the same parser implementations as the C9350. The
subclasses below expose those parsers under the C9250 abstraction token.
"""

from genie.libs.parser.iosxe.cat9k.c9350 import (
    show_platform as c9350,
)


class ShowPlatformHardwareFedQosSchedulerSdkInterfaceSchema(
    c9350.ShowPlatformHardwareFedQosSchedulerSdkInterfaceSchema
):
    """Schema for C9250 FED QoS scheduler SDK interface output."""

    pass


class ShowPlatformHardwareFedQosSchedulerSdkInterface(
    c9350.ShowPlatformHardwareFedQosSchedulerSdkInterface
):
    """Parser for C9250 FED QoS scheduler SDK interface commands."""

    pass


class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema(
    c9350.ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema
):
    """Schema for C9250 FED QoS queue interface statistics output."""

    pass


class ShowPlatformHardwareFedSwitchQosQueueStatsInterface(
    c9350.ShowPlatformHardwareFedSwitchQosQueueStatsInterface
):
    """Parser for C9250 FED QoS queue interface statistics commands."""

    pass


class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear(
    c9350.ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear
):
    """Parser for C9250 FED QoS queue statistics clear commands."""

    pass


class ShowPlatformHardwareFedSwitchQosQueueConfigSchema(
    c9350.ShowPlatformHardwareFedSwitchQosQueueConfigSchema
):
    """Schema for C9250 FED QoS queue interface configuration output."""

    pass


class ShowPlatformHardwareFedSwitchQosQueueConfig(
    c9350.ShowPlatformHardwareFedSwitchQosQueueConfig
):
    """Parser for C9250 FED QoS queue interface configuration commands."""

    pass


class ShowPlatformHardwareFedSwitchActiveQosQueueStatsInternalPortTypePuntQueueSchema(
    c9350.ShowPlatformHardwareFedSwitchActiveQosQueueStatsInternalPortTypePuntQueueSchema
):
    """Schema for C9250 internal punt queue statistics output."""

    pass


class ShowPlatformHardwareFedSwitchActiveQosQueueStatsInternalPortTypePuntQueue(
    c9350.ShowPlatformHardwareFedSwitchActiveQosQueueStatsInternalPortTypePuntQueue
):
    """Parser for the C9250 internal punt queue statistics command."""

    pass


class ShowPlatformTcamUtilizationSchema(
    c9350.ShowPlatformTcamUtilizationSchema
):
    """Schema for C9250 FED TCAM resource utilization output."""

    pass


class ShowPlatformTcamUtilization(c9350.ShowPlatformTcamUtilization):
    """Parser for C9250 FED TCAM resource utilization commands."""

    pass


class ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema(
    c9350.ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema
):
    """Schema for C9250 FED ACL database detail output."""

    pass


class ShowPlatformSoftwareFedActiveAclInfoDbDetail(
    c9350.ShowPlatformSoftwareFedActiveAclInfoDbDetail
):
    """Parser for C9250 FED ACL database detail commands."""

    pass


class ShowPlatformSoftwareFedActivePuntAsicCauseBriefSchema(
    c9350.ShowPlatformSoftwareFedActivePuntAsicCauseBriefSchema
):
    """Schema for C9250 FED punt ASIC-cause brief output."""

    pass


class ShowPlatformSoftwareFedActivePuntAsicCauseBrief(
    c9350.ShowPlatformSoftwareFedActivePuntAsicCauseBrief
):
    """Parser for C9250 FED punt ASIC-cause brief commands."""

    pass


class ShowInventorySchema(c9350.ShowInventorySchema):
    """Schema for C9250 ``show inventory`` output."""

    pass


class ShowInventory(c9350.ShowInventory):
    """Parser for the C9250 ``show inventory`` command."""

    pass
