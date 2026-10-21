#!/bin/bash

#read -p "enter the number : " num 
#if [ $((num%2)) -ne 0 ]; then 
#	echo $num 
#fi

echo " today : $(date +"%d-%B-%Y")"


echo " tomorow : $(date -d "tomorrow" +"%d-%B-%y")"
echo "yesterday : $(date -d "yesterday" +"%d-%B-%y") "
