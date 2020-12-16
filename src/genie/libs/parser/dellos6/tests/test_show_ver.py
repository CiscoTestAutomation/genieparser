# Import our libraries
from genie.conf import Genie


# Create a testbed object for the network
testbed = Genie.init("/mnt/c/sdk/testbed.yml")


for device in testbed.devices:
    # Connect to the device
    testbed.devices[device].connect(alias='mgmt')
    testbed.devices[device].mgmt.execute('enable')
    output = testbed.devices[device].parse(
        "show version")
print(output)
