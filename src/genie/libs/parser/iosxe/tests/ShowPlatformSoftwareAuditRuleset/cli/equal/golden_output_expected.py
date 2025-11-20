expected_output = {
    "rulesets": [
        {
            "name": "user_group_config_files",
            "rules": [
                "-a exit,always -F arch=b64 -F path=/etc/passwd -F perm=wa -k user_group_config_files",
                "-a exit,always -F arch=b64 -F path=/etc/shadow -F perm=wa -k user_group_config_files",
                "-a exit,always -F arch=b64 -F path=/etc/group -F perm=wa -k user_group_config_files"
            ]
        },
        {
            "name": "user_privilege_mgmt",
            "rules": [
                "-a always,exit -F arch=b64 -S setuid,setresuid,setreuid,setfsuid,setgid,setresgid,setregid,setfsgid -F key=user_privilege_mgmt",
                "-a always,exit -F arch=b32 -S setgid32,setuid32,setresuid32,setfsuid32,setresgid32,setregid32,setfsgid32,setreuid32 -F key=user_privilege_mgmt"
            ]
        },
        {
            "name": "dns_client_files",
            "rules": [
                "-a exit,always -F arch=b64 -F path=/etc/hosts -F perm=wa -k dns_client_files",
                "-a exit,always -F arch=b64 -F path=/etc/resolv.conf -F perm=wa -k dns_client_files",
                "-a exit,always -F arch=b64 -F path=/var/run/resolv.conf -F perm=wa -k dns_client_files"
            ]
        },
        {
            "name": "kernel_module_mgmt",
            "rules": [
                "-a exit,always -F arch=b64 -F path=/sbin/insmod -F perm=x -k kernel_module_mgmt",
                "-a exit,always -F arch=b64 -F path=/sbin/rmmod -F perm=x -k kernel_module_mgmt",
                "-a exit,always -F arch=b64 -F path=/sbin/modprobe -F perm=x -k kernel_module_mgmt",
                "-a exit,always -F arch=b64 -F path=/bin/kmod -F perm=x -k kernel_module_mgmt"
            ]
        },
        {
            "name": "system_software",
            "rules": [
                "-a exit,always -F arch=b64 -F dir=/bin -F perm=wa -k system_software",
                "-a exit,always -F arch=b64 -F dir=/sbin -F perm=wa -k system_software",
                "-a exit,always -F arch=b64 -F dir=/usr/bin -F perm=wa -k system_software",
                "-a exit,always -F arch=b64 -F dir=/usr/sbin -F perm=wa -k system_software"
            ]
        }
    ]
}