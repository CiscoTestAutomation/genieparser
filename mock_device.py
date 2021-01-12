import argparse
import code

from pprint import pprint

from genie.conf.base import Device

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # Pass in the XPRESSO job ID
    parser.add_argument(
        "os",
        help="os",
        type=str,
    )

    args = parser.parse_args()

dev = Device(name='aName', os=args.os)
dev.custom.abstraction = {'order':['os']}
output = '''
# show interfaces ae0 extensive 
Physical interface: ae0, Enabled, Physical link is Up	
  Interface index: 192, SNMP ifIndex: 822, Generation: 251	
  Link-level type: Ethernet, MTU: 1514, Speed: 30Gbps, BPDU Error: None, MAC-REWRITE Error: None, Loopback: Disabled, Source filtering: Disabled, Flow control: Disabled	
  Pad to minimum frame size: Disabled	
  Minimum links needed: 1, Minimum bandwidth needed: 1bps	
  '''
import pprint
pprint.pprint(dev.parse("show interfaces ae0 extensive", output=output))
