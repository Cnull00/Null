#!/bin/py

import os,sys

os.system('clear')

def cekip():
 print (f'[!] Mendapatkan IP..')
 re = requests.get('https://api.myip.com').json()
 ip = re['ip']
 print (f'[!] IP kamu : {ip}')

def iOsif():
 print (f'[!] Menginstall tools osif..')
 os.system('pkg update upgrade')
 os.system('pkg install git python2')
 os.system('git clone https://github.com/ciku370/OSIF')
 os.system('cd OSIF')
 os.system('pip2 install -r requirements.txt')
 os.system('python2 osif.py')

def owscan():
 print (f'[!] Tools Ini Buat Informayion Gathering Website Target Kalian [!]')
 os.system('pkg update && pkg upgrade')
 os.system('pkg install php')
 os.system('pkg install git')
 os.system('git clone https://github.com/Gameye98/OWScan')
 os.system('cd OWScan')
 os.system('php owscan.php')

def faceboom():
 print (f'Ini Buat Hack FB Pake WORDLIST...')
 os.system('pkg upgrade')
 os.system('pkg install python')
 os.system('pkg install git')
 os.system('pip install requests')
 os.system('git clone https://github.com/Oseid/FaceBoom')
 os.system('cd FaceBoom')
 os.system('python faceboom.py')

def redhawk():
 print (f'Ini Buat Vulnerability Scanner')
 os.system('pkg upgrade')
 os.system('pkg install git')
 os.system('git clone https://github.com/Tuhinshubhra/RED_HAWK')
 os.system('cd RED_HAWK')
 os.system('php rhawk.php')

def geoip():
 print (f'Ini Tools Buat Ngelacak Lokasi Orang Lewat IP')
 os.system('git clone https://github.com/maldevel/IPGeoLocation')
 os.system('cd IPGeoLocation')
 os.system('python ipgeolocation.py')

def santet():
 print (f'Ini Tools Buat Sosial Engiinering')
 print ('')
 os.system('git clone https://github.com/Gameye98/santet-online')
 os.system('cd santet-online')

def seeker():
 print (f'Ini Tools Sadap WA Dan Lain')
 os.system('git clone https://github.com/thewhiteh4t/seeker')
#tampilan
print ("\033[1;36m===============================================")
os.system("figlet Tools | lolcat")
os.system("figlet Mr.john | lolcat")
os.system("date | lolcat")
print ("\033[0;36mAuthor : HANIF ")
print ("\033[1;36m+++++++++++++++++++++++++++++++++++++++++++++++")
print ("LIST TOOLS HACKING")
print ('\033[1;35m[1] Cek IP')
print ('\033[1;35m[2] Install OSIF')
print ('\033[1;35m[3] OWSCAN')
print ('\033[1;35m[4] FACEBOOM (BRUTEFORCE WITH WORDLIST)')
print ('\033[1;35m[5] REDHAWK')
print ('\033[1;35m[6] IPGEOLOCATION')
print ('\033[1;35m[7] SANTET-ONLINE')
print ('\033[1;35m[8] Seeker')
print ('\033[1;35m[9] KELUAR')
print ("")
print ("")

menu = input('[?] Silahkan pilih menu : ')

if menu == '1':
 cekip()
elif menu == '2':
 iOsif()
elif menu == '3':
 owscan()
elif menu == '4':
 faceboom()
elif menu == '5':
 redhawk()
elif menu == '6':
 geoip()
elif menu == '7':
 santet()
elif menu == '8':
 seeker()
elif menu == '9':
 print ('\033[1;31m[?] Keluar..')
 sys.exit()
else:
 print ('\033[1;32m[?] Perintah tidak diketahui..')
 sys.exit()

#Data warna
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
Birumudaterang='\033[1;36m'
putih='\033[1;37m'
