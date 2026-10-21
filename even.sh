#!/bin/bash 

read -p "enter number :" num
for i in $(seq 1 $num)
do
	if [ $((i%2)) -eq 0 ]; then
		echo "$i is even"
	else
		echo "$i is odd"
	fi
done 

mysql password
NewPassword123!