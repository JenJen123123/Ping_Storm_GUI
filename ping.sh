#!/bin/bash

echo "ping.sh started"

sites=("google.com" "facebook.com" "tiktok.com")
count=1

for site in "${sites[@]}"; do
    echo "Pinging $site..."
    rtt=$(ping -c $count $site | grep "rtt min/avg/max/mdev")

    if [ -n "$rtt" ]; then
        values=$(echo "$rtt" | cut -d '=' -f 2 | tr -d ' ms')
        IFS='/' read -r min avg max mdev <<< "$values"
        echo "$site → Min: $min | Avg: $avg | Max: $max | Mdev: $mdev"
    else
        echo "$site → ping failed"
    fi
done

echo "ping.sh finished"
