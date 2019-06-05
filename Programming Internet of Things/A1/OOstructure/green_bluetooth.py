import bluetooth
import time
import subprocess as sp
import os
from NotificationSender import Sender

class Bluetoothtask:
    def _int__(self):
        pass
    #Get paired device from raspberry Pi    
    def getBluetoothDevice(self):
        p = sp.Popen(["bt-device", "--list"], stdin = sp.PIPE, stdout = sp.PIPE, close_fds = True)
        (stdout, stdin) = (p.stdout, p.stdin)
        data = stdout.readlines() 
        pairedMacaddress = data[1].split()[2]
        macaddres = pairedMacaddress[1:18].decode()
        print(macaddres)
        Bluetoothtask().compareBluetooth(macaddres)

    #Compare paired devices to nearby devices 
    def compareBluetooth(self,macaddres):  
        found = "no"
        while (found != "Yes!"):
            print("Scanning...")
            nearbyDevices = bluetooth.discover_devices()
            for macAddress in nearbyDevices:
                print("Found device with mac-address: " + macAddress)
                if (macaddres == macAddress):
                    Sender().send_notification_via_pushbullet("Your paired device is in the nearby area!", "From Raspberry Pi")

                    found = "Yes!"

def main():
    Bluetoothtask().getBluetoothDevice() 

if __name__ == "__main__":
    main()



              
    