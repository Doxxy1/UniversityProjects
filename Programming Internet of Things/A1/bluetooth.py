import bluetooth
import time
import subprocess as sp
import os

p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
(stdout, stdin) = (p.stdout, p.stdin)

data = stdout.readlines() 
pairedMacaddress = data[1].split()[2]
macaddres = pairedMacaddress[1:18].decode()
print(macaddres)

while True:
    print("Scanning...")
    nearbyDevices = bluetooth.discover_devices()

    for macAddress in nearbyDevices:
        print("Found device with mac-address: " + macAddress)
        if (macaddres == macAddress):
            print("yes")
       
                
        
      
