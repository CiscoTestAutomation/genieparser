expected_output = {
    'ssh': {
        'enabled': True,
        'version': '2.0',
        'authentication_methods': ['publickey', 'keyboard-interactive', 'password'],
        'authentication_publickey_algorithms': [
            'ecdsa-sha2-nistp256',
            'ecdsa-sha2-nistp384', 
            'ecdsa-sha2-nistp521',
            'ssh-ed25519',
            'x509v3-ecdsa-sha2-nistp256',
            'x509v3-ecdsa-sha2-nistp384',
            'x509v3-ecdsa-sha2-nistp521',
            'rsa-sha2-256',
            'rsa-sha2-512',
            'x509v3-rsa2048-sha256',
            'sk-ecdsa-sha2-nistp256@openssh.com',
            'sk-ssh-ed25519@openssh.com'
        ],
        'hostkey_algorithms': [
            'ecdsa-sha2-nistp256',
            'ecdsa-sha2-nistp384',
            'ecdsa-sha2-nistp521',
            'rsa-sha2-512',
            'rsa-sha2-256'
        ],
        'encryption_algorithms': [
            'chacha20-poly1305@openssh.com',
            'aes128-gcm@openssh.com',
            'aes256-gcm@openssh.com',
            'aes128-gcm',
            'aes256-gcm',
            'aes128-ctr',
            'aes192-ctr',
            'aes256-ctr'
        ],
        'mac_algorithms': [
            'hmac-sha2-256-etm@openssh.com',
            'hmac-sha2-512-etm@openssh.com',
            'hmac-sha2-256',
            'hmac-sha2-512'
        ],
        'kex_algorithms': [
            'curve25519-sha256',
            'curve25519-sha256@libssh.org',
            'ecdh-sha2-nistp256',
            'ecdh-sha2-nistp384',
            'ecdh-sha2-nistp521',
            'diffie-hellman-group14-sha256',
            'diffie-hellman-group16-sha512'
        ],
        'authentication_timeout': 120,
        'authentication_retries': 3,
        'min_dh_key_size': 2048,
        'rsa_key': {
            'present': True,
            'modulus_size': 2048,
            'key_data': 'ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD5TMNzWY5Fb5PPGuisS9wqAivpkpzmGMULxTr5Sk7+ ivkeNpbbp4QI9oUNUdNalAlgwvxahPapm1c9Gl+ebTRxoCHHxlVM7TirlgdCdr5Lfnw9m2YkmwEew/q8 mm0GwglclzY5bNPO5UNFDhsz3EOYERy9LB0e36cLaM2Jnzp8NILznOybZGV7D1yyo5GUeEqk8m1b7wMi oncV+lcbXi94lMSVDlFuIcsKlnHFiemwrvEcfYW0rFQa0OyBcB+qMxCdvXlAP6j7TlHkxgqnwH0yOxcf oaQifKJlTJuGQmJGYvRptyKAaQuBMhgJsOX/YEbcJR2Z3QpdoQyZ0ModcoSB'
        },
        'ecdsa_key': {
            'present': True,
            'key_size': 256,
            'key_data': 'ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBPOMQIhOr INuYleNhhIQfy1sJf1j3EZq45tqIHSHxHVur0z8yumlk60+hZTL6DtQG9MAA38JJd+4grH8ZlH4clc='
        }
    }
}