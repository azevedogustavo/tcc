#! /bin/bash

#This iscrit is to run on docker

apt update
apt install git make gcc git zlib1g-dev -y

git clone https://github.com/axboe/fio.git

cd ./fio

./configure

make -j8

