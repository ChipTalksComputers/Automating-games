#Make sure that you run this script from MonkeyRunner 
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
import time

#Creating the device
device = Monkeyrunner.wautForConnection()

#The infinite loop
while(1):
    time.sleep(0.075)     #Change the number according to how fast the computer executes the while loop
    device.touch(538, 1761, 'DOWN_AND_UP')     #Make sure the coordinates of the button are same on your device. If it's not, you've got to change it.
