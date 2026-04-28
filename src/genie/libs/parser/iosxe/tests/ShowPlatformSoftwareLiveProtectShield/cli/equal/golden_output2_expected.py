expected_output = {
    "shield": {
        "cve-2026-40010-v01": {
            "mode": "monitoring",
            "enforcing_hits": 0,
            "monitoring_hits": 12,
            "total_hits": 12,
        },
        "cve-2026-40010-v02": {
            "mode": "enforcement",
            "enforcing_hits": 100,
            "monitoring_hits": 0,
            "total_hits": 100,
        },
        "cve-2026-40010-v03": {
            "mode": "monitoring",
            "enforcing_hits": 1,
            "monitoring_hits": 1,
            "total_hits": 2,
        },
    }
}
