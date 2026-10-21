#!/bin/bash 

read -p "enter first number : " a
read -p "enter second number : " b
echo "addition $((a+b))"
echo "sub : $((a-b))"
echo "multi : $((a*b))"
if [ $b -eq 0 ]; then 
	echo " not divide by zero"
else 
	echo " divide: $((a/b))"
fi 


