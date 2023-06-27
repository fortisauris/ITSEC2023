#!/bin/bash

while true; do
    nmcli dev wifi list >> wifi_list.txt
    sleep 300  # zaspi na 300 sekund
done