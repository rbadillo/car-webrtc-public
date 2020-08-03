#!/bin/bash

echo "Starting GPS"
/bin/systemctl stop gpsd.socket
/bin/systemctl disable gpsd.socket
/usr/sbin/gpsd /dev/ttyACM0 -F /var/run/gpsd.sock
/usr/bin/python -u /home/pi/Desktop/car_gps.py
