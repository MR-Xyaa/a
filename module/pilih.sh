#!/bin/sh
read -p "root@MR-Xyaa~#" bro
if [ $bro = 1 ] || [ $bro = 1 ]
then
clear
figlet "MR-Xyaa" | lolcat
pkg update && pkg upgrade

pkg install python python2 python3

pip install requests mechanize

pip2 install requests mechanize

pkg install git

pkg install ruby

pkg install curl

gem install lolcat

pip2 install php

pkg install figlet

pkg install wget

pkg install nano

pkg install bash

pkg install cowsay

apt update && apt upgrade -y

pkg install bash

pkg install pv -y

pkg install wget -y

pkg install git -y

echo"Selesai"
fi

if [ $bro = 2 ] || [ $bro = 2 ]
then
clear
figlet "MR-Xyaa" | lolcat
git clone https://github.com/MR-Xyaa/Oh-My-Zsh
cd Oh-My--Zsh
git pull
sh oh-my-zsh
fi

if [ $bro = 3 ] || [ $bro = 3 ]
then
clear
figlet "MR-Xyaa" | lolcat
git clone https://github.com/MR-Xyaa/MTK
cd MTK
git pull
sh mtk.sh
fi

if [ $bro = 4 ] || [ $bro = 4 ]
then
clear
figlet "MR-Xyaa" | lolcat
git clone https://github.com/MR-Xyaa/dmbf
cd dmbf
git pull
python dmbf.py
fi


if [ $bro = 6 ] || [ $bro = 6 ]
then
clear
figlet "MR-Xyaa" | lolcat
git clone https://github.com/MR-Xyaa/pribadi
cd pribadi
git pull
sh aprillia.sh
fi

if [ $bro = 5 ] || [ $bro = 5 ]
then
clear
figlet "MR-Xyaa" | lolcat
git clone https://github.com/MR-Xyaa/belajar
cd belajar
git pull
sh bljar.sh
fi


if [ $bro = 00 ] || [ $bro = 00 ]
then
echo "\033[32;1mMR-Xyaa"
echo "\033[33;1mWe Security"
echo " We Not Friends"
echo "We Are Family"
echo "Hacking Is Not Criminal"
echo "Ketika Sebuah Hayalan Tidak tercapai"
echo "Maka Terus lah BerJuang Dan Berusaha"
echo "\033[32;1mKarna Suatu Hari Nanti Kamu akan Mendapatkannya"
exit
fi
