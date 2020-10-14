#!/usr/bin/env python
import  subprocess

subprocess.call('ifconfig wlan0 down',shell=True)
subprocess.call('ifconfig wlan0 hw ether 11:22:44:55:66:77',shell=True)
subprocess.call('ifconfig wlan0 up',shell=True)