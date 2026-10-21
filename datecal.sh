#!/bin/bash

echo "today: $(date +"%d-%m-%y")"

echo "tomorrow: $(date -d "tomorrow" +"%d-%m-%y")"


echo "yesterday: $(date -d "yesterday" +"%d-%m-%y")"

echo "time: $(date +"%I:%M:%S %p")"

echo "5day after: $(date -d "-5 day" +"%d-%B-%y")"

echo "date: $(date -d "25 dec 2004" +"%d-%B-%y")"

echo "day: $(date +"%A")"

echo "birth date $(date -d "20 jan 2004" +"%d-%B-%Y")"

echo "time: $(date +"%I:%M:%S %p")"

