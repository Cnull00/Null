#!/bin/sh

#Data warnabash
#perintahnya-printf
hitam='\033[0;30m'
merah='\033[0;31m'
hijau='\033[0;32m'
oren='\033[0;33m'   
biru='\033[0;34m'
ungu='\033[0;35m'   
birumuda='\033[0;36m'
abuterang='\033[0;37m' 
abugelap='\033[1;30m'
merahterang='\033[1;31m'
hijauterang='\033[1;32m'
kuning='\033[1;33m'
biruterang='\033[1;34m'
unguterang='\033[1;35m'
birumudaterang='\033[1;36m'
putih='\033[1;37m'
#awal
figlet __Null__ | lolcat
date | lolcat

sleep 0.1
#page
echo -e "${ungu}Login dulu.."
sleep 1
pass="satu";
read -sp "Password : " word;
if [ $pass == $word ] 
then
sleep 2
 echo -e "${hijau}Login sukses"
	clear 
else
sleep 2
 echo -e  "${merah}Password salah"
	bash tes.sh
fi

#pengulangan
sleep 0.1
figlet __Null__ | lolcat
echo " author :Null " | lolcat
echo " Hacker by :Null " | lolcat
date | lolcat
echo "=========================================" | lolcat
sleep 2
read -p " siapa namamu:" nama
sleep 1
echo  "salken!!" $nama
echo "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" | lolcat
echo
sleep 1
#isiscript
echo
	echo "	   =====Menu===== " | lolcat
	echo "	   [1] install bahan " | lolcat
	echo "	   [2] Hekhekan " | lolcat
	echo "	   [3] deface web " | lolcat
	echo "	   [4] Mr.john " | lolcat
	echo "           [5] keluar " | lolcat
	echo "	   =============== " | lolcat
echo -n "masukan pilihan : " | lolcat
read pil;

if [ $pil = '1' ] || [ $pil = '01' ]
then
	pkg install python && pkg install python2 -y
	bash tes.sh
elif [ $pil = '2' ] || [ $pil = '02' ]
then
	clear 
	bash new.sh
elif [ $pil = '3' ] || [ $pil = '03' ]
then
	echo " Deface " | lolcat
	pip2 install requests
	python2 ngebot.py
elif [ $pil = '4' ] || [ $pil = '04' ]
then
	clear
	python bang.py
elif [ $pil = '5' ] || [ $pil = '05' ]
then
	echo -e "${biru}Terima Kasih "
	exit
fi

