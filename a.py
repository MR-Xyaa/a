import os, sys
os.system('clear')
from optparse import Option
print("×WELLCOME TO TOOLS MR XYAA:)")
print("×Tekan Enter Untuk Lanjut")
print("×Atau")
print("×CTRL+C Untuk Keluar")
option=int(input("pilih="))



print ("\033[1;32mMasukan UserName&Password Dulu Ya:)")
print ("\033[1;31;1mKalo Gak Tau Kunjungi Github MR-Xyaa")
print ("\033[1;32mhttps://github.com/MR-Xyaa")
username = 'MR'      
password = 'Xyaa'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "\n\033[1;34mHello Welcome To Tools MR-Xyaa", 
			sys.exit()

		else:
			print "\n\033[1;36mSorry Invalid Password !!!\033[00m"
			print "Back Login\n"
			restart()

	else:
		print "\n\033[1;36mSorry Invalid Username !!!\033[00m"
		print "Back Login\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
