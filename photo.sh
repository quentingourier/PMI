#!/bin/sh

echo "preparing..."
sleep 5
while:

        do
                raspistill -ISO 100 -o "screen.png"
		echo "taken, sleeping..."
                sleep 15
        done