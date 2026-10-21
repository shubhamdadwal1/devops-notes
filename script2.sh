#!/bin/bash
#echo 'light blub'
##echo ' 1. on '
#echo '2. off'
#read -p "choose one ; " lig
#if [ $lig -eq 1 ]; then
#	echo "LIGHT BLUB ON"
#elif [ $lig -eq 2 ]; then 
#	echo 'LIGHT BLUB OFF'
#else
#	echo "choose right number"
#fi


#for i in {1..10}
#do
#	echo $i
#done


#list=("shubh" "dadwal" "reeta" "devi" )
#for item in "${list[@]}"
#do
#	echo $item
#done


read -p "enter the number : " num
for i in $( seq 0 $num )
do
	if [ $((i%2)) -eq 0 ]; then 
		echo ${i}
	fi
done 

