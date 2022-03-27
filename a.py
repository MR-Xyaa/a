import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils
from optparse import Option
print("Wellcome To Tools MR-Xyaa")
print("Pilih :")
print("1.Lanjut")
print("99.Keluar")
option=int(input("Lanju Apa Keluar : "))


def backtomenu_option():
	print(backtomenu_banner)
	backtomenu = input("santet > ")
	
	if backtomenu == "99":
		restart_program()
	elif backtomenu == "00":
		sys.exit()
	else:
		print("\nERROR: Wrong input")
		time.sleep(2)
		restart_program()
