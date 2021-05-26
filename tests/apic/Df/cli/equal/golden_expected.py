expected_output = {
    "directory": {
        "/bin": {
            "available": 26637041664,
            "filesystem": "/dev/mapper/vg_ifc0-boot",
            "mounted_on": "/bin",
            "total": 42141548544,
            "use_percentage": 34,
            "used": 13340246016
        },
        "/data/techsupport": {
            "available": 39721684992,
            "filesystem": "/dev/mapper/vg_ifc0-techsupport",
            "mounted_on": "/data/techsupport",
            "total": 42141450240,
            "use_percentage": 1,
            "used": 255504384
        },
        "/data2": {
            "available": 45798060032,
            "filesystem": "/dev/mapper/vg_ifc0-data2",
            "mounted_on": "/data2",
            "total": 68563689472,
            "use_percentage": 30,
            "used": 19259191296
        },
        "/data2/third-party/nomad/data/alloc/047a0365-93a3-a452-cfd9-24a556594476/moss/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/047a0365-93a3-a452-cfd9-24a556594476/moss/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/data2/third-party/nomad/data/alloc/4ff974a9-b3b2-ef30-c8c6-17f1380b24d2/kafka/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/4ff974a9-b3b2-ef30-c8c6-17f1380b24d2/kafka/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/data2/third-party/nomad/data/alloc/623ade6f-94a6-ce85-c0ca-3abc781771c2/ksm/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/623ade6f-94a6-ce85-c0ca-3abc781771c2/ksm/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/data2/third-party/nomad/data/alloc/6c97f156-6997-358a-80e7-1d6cd81beb3d/hms/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/6c97f156-6997-358a-80e7-1d6cd81beb3d/hms/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/data2/third-party/nomad/data/alloc/75e3d4f6-1d43-dc01-0244-96eea0d48978/statsq/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/75e3d4f6-1d43-dc01-0244-96eea0d48978/statsq/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/data2/third-party/nomad/data/alloc/89f6f22f-3f6e-0057-b324-a8008af16a9e/dc/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/89f6f22f-3f6e-0057-b324-a8008af16a9e/dc/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/data2/third-party/nomad/data/alloc/8c9a3ab0-19c4-610b-85f6-5cb63e071e1a/es/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/8c9a3ab0-19c4-610b-85f6-5cb63e071e1a/es/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/data2/third-party/nomad/data/alloc/97d95dd6-39c1-bedb-1cab-2aaf8633ea80/zk/secrets": {
            "available": 1048576,
            "filesystem": "tmpfs",
            "mounted_on": "/data2/third-party/nomad/data/alloc/97d95dd6-39c1-bedb-1cab-2aaf8633ea80/zk/secrets",
            "total": 1048576,
            "use_percentage": 0,
            "used": 0
        },
        "/dev": {
            "available": 33557979136,
            "filesystem": "devtmpfs",
            "mounted_on": "/dev",
            "total": 33557979136,
            "use_percentage": 0,
            "used": 0
        },
        "/dev/shm": {
            "available": 4114776064,
            "filesystem": "tmpfs",
            "mounted_on": "/dev/shm",
            "total": 4294967296,
            "use_percentage": 5,
            "used": 180191232
        },
        "/firmware": {
            "available": 37752147968,
            "filesystem": "/dev/mapper/vg_ifc0-firmware",
            "mounted_on": "/firmware",
            "total": 42141450240,
            "use_percentage": 6,
            "used": 2225041408
        },
        "/home": {
            "available": 32866426880,
            "filesystem": "/dev/mapper/vg_ifc0-scratch",
            "mounted_on": "/home",
            "total": 42141450240,
            "use_percentage": 18,
            "used": 7110762496
        },
        "/sys/fs/cgroup": {
            "available": 33572356096,
            "filesystem": "tmpfs",
            "mounted_on": "/sys/fs/cgroup",
            "total": 33572356096,
            "use_percentage": 0,
            "used": 0
        },
        "/tmp": {
            "available": 17179807744,
            "filesystem": "tmpfs",
            "mounted_on": "/tmp",
            "total": 17179869184,
            "use_percentage": 1,
            "used": 61440
        },
        "/tmp/bootflash": {
            "available": 51081216,
            "filesystem": "/dev/sdc1",
            "mounted_on": "/tmp/bootflash",
            "total": 56726528,
            "use_percentage": 3,
            "used": 1242112
        },
        "/var/log/dme": {
            "available": 88317472768,
            "filesystem": "/dev/mapper/vg_ifc0_ssd-data",
            "mounted_on": "/var/log/dme",
            "total": 93457219584,
            "use_percentage": 1,
            "used": 368726016
        },
        "/var/log/dme/core": {
            "available": 49954611200,
            "filesystem": "/dev/mapper/vg_ifc0-dmecores",
            "mounted_on": "/var/log/dme/core",
            "total": 52710309888,
            "use_percentage": 1,
            "used": 54566912
        },
        "/var/log/dme/log": {
            "available": 1523101696,
            "filesystem": "tmpfs",
            "mounted_on": "/var/log/dme/log",
            "total": 2147483648,
            "use_percentage": 30,
            "used": 624381952
        },
        "/var/log/dme/oldlog": {
            "available": 35257298944,
            "filesystem": "/dev/mapper/vg_ifc0-logs",
            "mounted_on": "/var/log/dme/oldlog",
            "total": 42141450240,
            "use_percentage": 12,
            "used": 4719890432
        },
        "/var/run/utmp": {
            "available": 33568755712,
            "filesystem": "tmpfs",
            "mounted_on": "/var/run/utmp",
            "total": 33572356096,
            "use_percentage": 1,
            "used": 3600384
        }
    }
}
