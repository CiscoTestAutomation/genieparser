from genie.testbed import load
testbed = load('testbed.yaml')

device = testbed.devices['Switch']

device.connect()
print(device)
output = device.parse('show device-tracking features')

print(output)