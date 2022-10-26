#! /bin/bash


yourfilenames=`ls ./*.result`
for eachfile in $yourfilenames
do
   
   echo $eachfile | cut -d"/" -f2 >> saida
   cat $eachfile | grep "Time in" >> saida

done



