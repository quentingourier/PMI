#!/bin/bash


file="screen.jpg"
raspberry_pi_dir="/home/pi"
laptop_dir="C:\\Users\\quent\\Desktop\\IPSA\\aero5\\PMI"

while true; do
    # Use the ssh command to check if the file exists in the Raspberry Pi directory
    if ssh pi@raspberrypi "test -e $raspberry_pi_dir/$file"
    then
        # If the file exists, use the scp command to copy it from the Raspberry Pi to the laptop
        scp pi@raspberrypi:$raspberry_pi_dir/$file $laptop_dir
        echo "File $file has been copied to $laptop_dir"
        break
    else
        # If the file does not exist, display a message and wait for 10 seconds
        echo "File $file does not exist in $raspberry_pi_dir, waiting..."
        sleep 10
    fi
done
