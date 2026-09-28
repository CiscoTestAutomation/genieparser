"""IOS XE parsers for YANG operational commands."""

import re

from genie.metaparser import MetaParser


# ==============================================================
# Schema for 'show yang sync status'
# ==============================================================
class ShowYangSyncStatusSchema(MetaParser):
    """Schema for ``show yang sync status``."""

    schema = {
        "sync_pending": bool,
        "pending_full_sync": bool,
        "syncing_state": str,
        "sync_trigger": str,
    }


# ==============================================================
# Parser for 'show yang sync status'
# ==============================================================
class ShowYangSyncStatus(ShowYangSyncStatusSchema):
    """Parser for ``show yang sync status``."""

    cli_command = "show yang sync status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        parsed_dict = {}

        # sync pending: false
        p1 = re.compile(
            r"^sync +pending: +(?P<sync_pending>true|false)$",
            re.IGNORECASE,
        )

        # pending full sync: false
        p2 = re.compile(
            r"^pending +full +sync: +(?P<pending_full_sync>true|false)$",
            re.IGNORECASE,
        )

        # syncing state: Not Syncing
        p3 = re.compile(
            r"^syncing +state: +(?P<syncing_state>.+)$",
            re.IGNORECASE,
        )

        # sync trigger: N/A
        p4 = re.compile(
            r"^sync +trigger: +(?P<sync_trigger>.+)$",
            re.IGNORECASE,
        )

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                parsed_dict["sync_pending"] = (
                    match.group("sync_pending").lower() == "true"
                )
                continue

            match = p2.match(line)
            if match:
                parsed_dict["pending_full_sync"] = (
                    match.group("pending_full_sync").lower() == "true"
                )
                continue

            match = p3.match(line)
            if match:
                parsed_dict["syncing_state"] = match.group(
                    "syncing_state"
                ).strip()
                continue

            match = p4.match(line)
            if match:
                parsed_dict["sync_trigger"] = match.group(
                    "sync_trigger"
                ).strip()
                continue

        return parsed_dict
