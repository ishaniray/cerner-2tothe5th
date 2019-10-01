#!/bin/bash/

# cerner_2^5_2019

# This script greets the user "Good Morning" / "Good Afternoon" / "Good Evening" based on what time of the day it is.
# On Ubuntu, the following is appended to the /home/username/.bashrc file: source /path/to/script.sh
# Doing the above ensures the script is executed every time the user opens the Terminal.

hour=$(date +%H)
user=$(whoami)

if [ $hour -ge 18 ] ; then
	echo "Good evening, $user!"
elif [ $hour -ge 12 ] ; then
	echo "Good afternoon, $user!"
else
	echo "Good morning, $user!"
fi
