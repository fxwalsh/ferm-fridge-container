#!/bin/bash

echo "Compile and upload Arduino Script"
arduino-cli compile --fqbn arduino:avr:uno ferm_controller
arduino-cli upload -p /dev/ttyACM0 --fqbn arduino:avr:uno ferm_controller

echo "Start python Blynk script"
cd /app/pyBlynk
pip3 install -r deps.txt
python3 ferm_fridge.py
