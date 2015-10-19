#!/usr/bin/python
#  dreyercito
# Checks if a bluetooth device is close by

import objc
import sys
objc.loadBundle('IOBluetooth', globals(), bundle_path=u'/System/Library/Frameworks/IOBluetooth.framework')

if(len(sys.argv)<=1):
    print "Use: %s mac_address"%sys.argv[0]
    sys.exit(-1)

device = IOBluetoothDevice.deviceWithAddressString_(sys.argv[1])  

if(device.isConnected()):
    print "ConnectedPaired"
    sys.exit(0)

if(device.openConnection_withPageTimeout_authenticationRequired_(None,5000,False)):
    print "Connected"
    sys.exit(0)

else:
    print "Not Connected"
    sys.exit(1)
