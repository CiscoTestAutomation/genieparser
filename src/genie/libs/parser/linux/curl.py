
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, ListOf


class CurlMinusVSchema(MetaParser):
    schema = {
        'version': str,
        'platform': str,
        'libraries': ListOf({
            'name': str,
            'version': str,
            Optional('extra'): str
        }),
        'release_date': str,
        'protocols': list,
        'features': list
    }


class CurlMinusV(CurlMinusVSchema):

    cli_command = ['curl -V']

    def cli(self, command, output=None):

        if output is None:
            out = self.device.execute(command)
        else:
            out = output

        # curl 8.7.1 (x86_64-apple-darwin24.0) libcurl/8.7.1 (SecureTransport) LibreSSL/3.3.6 zlib/1.2.12 nghttp2/1.64.0
        # curl 7.85.0 (x86_64-iosxe-linux-gnu) libcurl/7.85.0 OpenSSL/1.1.1u-fips zlib/1.2.13 c-ares/1.18.1 libidn2/2.3.3 libssh2/1.10.0 nghttp2/1.49.0
        p1 = re.compile(r'^curl (?P<version>\S+) \((?P<platform>\S+)\) (?P<libraries>((\S+/\S+) ?(\(.*?\) +)?)*)')

        # Release-Date: 2022-08-31
        p2 = re.compile(r'^Release-Date:\s+(?P<release_date>\S+)')

        # Protocols: file ftp ftps http https scp sftp tftp
        p3 = re.compile(r'^Protocols:\s+(?P<protocols>(\w+ ?)+)')

        # Features: alt-svc AsynchDNS HSTS HTTP2 HTTPS-proxy IDN IPv6 Largefile libz NTLM SSL threadsafe TLS-SRP UnixSockets
        p4 = re.compile(r'^Features:\s+(?P<features>(\S+ ?)+)')

        curl_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # curl 7.85.0 (x86_64-iosxe-linux-gnu) libcurl/7.85.0 OpenSSL/1.1.1u-fips zlib/1.2.13 c-ares/1.18.1 libidn2/2.3.3 libssh2/1.10.0 nghttp2/1.49.0
            m1 = p1.match(line)
            if m1:
                curl_dict['version'] = m1.groupdict()['version']
                curl_dict['platform'] = m1.groupdict()['platform']
                curl_dict['libraries'] = []
                for item in m1.groupdict()['libraries'].split():
                    info = {}
                    if '/' in item:
                        name, version = item.split('/')
                        info['name'] = name
                        info['version'] = version
                        curl_dict['libraries'].append(info)
                    else:
                        item = item.strip('()')
                        curl_dict['libraries'][-1].update({'extra': item})
                continue

            # Release-Date: 2022-08-31
            m2 = p2.match(line)
            if m2:
                curl_dict['release_date'] = m2.groupdict()['release_date']
                continue

            # Protocols: file ftp ftps http https scp sftp tftp
            m3 = p3.match(line)
            if m3:
                curl_dict['protocols'] = m3.groupdict()['protocols'].split()
                continue

            # Features: alt-svc AsynchDNS HSTS HTTP2 HTTPS-proxy IDN IPv6 Largefile libz NTLM SSL threadsafe TLS-SRP UnixSockets
            m4 = p4.match(line)
            if m4:
                curl_dict['features'] = m4.groupdict()['features'].split()
                continue

        return curl_dict
