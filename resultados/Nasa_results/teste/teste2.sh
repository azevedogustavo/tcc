#! /bin/bash


yourfilenames=`ls ./*.result`
for eachfile in $yourfilenames
do
   cat $eachfile | grep "Time in"
done



#yourfilenames=$(ls ./*.result)
#for eachfile in $yourfilenames
#do
#	echo eachfile 
#done
