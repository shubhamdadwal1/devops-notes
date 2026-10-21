#!/bin/bash
read -p 'enter the number ;' num
if [ "$num" -gt 0 ]; then
	echo 'postive'
elif [ "$num" -lt 0 ]; then
	echo 'negative'
else
	echo 'not enter zero'
fi
