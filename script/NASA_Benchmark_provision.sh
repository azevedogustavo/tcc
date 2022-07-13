#! /bin/bash

#Provision Nasa Benchmark in docker
cd /home
apt update; apt install wget vim -y
wget https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/openmpi/4.0.3-0ubuntu1/openmpi_4.0.3.orig.tar.xz
tar -xf openmpi_4.0.3.orig.tar.xz 
apt install gcc g++ -y
apt-get install libcr-dev gcc g++ -y

cd openmpi

cd openmpi-4.0.3/

./configure
apt install openmpi-bin openmpi-dev openmpi-common openmpi-doc libopenmpi-dev -y


apt-get install gfortran -y
./configure
make -j8
make install
cd ..

tar -xvf NPB3.4.2.tar.gz 

cd NPB3.4.2

cd NPB3.4-MPI/

cd bin/

cd ..


cd config/

cp make.def.template make.def


make -j8

sudo apt install ssh
apt install ssh -y
apt install rsh
apt-get install rsh-server rsh-client -y
