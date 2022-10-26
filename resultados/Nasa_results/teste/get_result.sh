#! /bin/bash


yourfilenames=`ls ./*.result`
for eachfile in $yourfilenames
do
	sufix=$(echo $eachfile | cut -d"/" -f2)
	name="Time."${sufix}
	cat eachfile | grep "Time in" > saida
done
