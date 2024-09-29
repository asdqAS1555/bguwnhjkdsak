import requests,secrets
co= secrets.token_hex(8)*2
from user_agent import generate_user_agent
from colorama import Fore
mprorr=requests.session()
import sys as mp
import time as mpp
def slow(mpr):
	for mppp in mpr + "\n":
		mp.stdout.write(mppp)
		mp.stdout.flush()
		mpp.sleep(0.5 / 120)
slow("""
=====================================
|  __  __ _____                     |
| |  \/  |  __ \                    |
| | \  / | |__) | __ ___            |
| | |\/| |  ___/ '__/ _ \           |
| | |  | | |   | | | (_) |          |
| |_|  |_|_|   |_|  \___/           |
=====================================
| My Channel: @xx4gs Tele: @xx6gs   |
=====================================
""")
mpro= "[MPro url-sql] >> "
slow("\n [1]-url list === [2]-url")
mproxx= input("[MPro 1or2] >> ")
def mproscan():
	if mproxx == '1':
		mprolist= 'MPro-url-sqli.txt'
		mprolist1= open(mprolist, 'r')
		while True:
			mproli = mprolist1.readline().split('\n')[0]
			urlmp= mproli
			if "MohammedPro" in urlmp:
				slow("\n=====================================")
				mmppp=input("Links Expired Exit Enter : ")
				print(mmppp)
				slow("\n=====================================")
				exit()
			else:
				mprour= urlmp+"'"
				head= {
					'Cookie':co,
					'User-Agent':generate_user_agent(),
				}
				mproreq= mprorr.get(url=mprour, headers=head).text
				if "mysql" in mproreq:
					print(f'[{Fore.GREEN}MPro Found >>{Fore.WHITE}] ', mprour)
					with open('MPro-sql-Found.txt', 'a') as mpp:
						mpp.write(mpro+mprour+'\n')
				elif "MySQL" in mproreq:
					print(f'[{Fore.GREEN}MPro Found >>{Fore.WHITE}] ', mprour)
					with open('MPro-sql-Found.txt', 'a') as mpp:
						mpp.write(mpro+mprour+'\n')
				else:
					print(f'[{Fore.RED}MPro Not Found >>{Fore.WHITE}] ', mprour)
			
	elif mproxx == '2':
		mprou= input("[MPro Enter url] >>  ")
		mprou1= "'"
		urlmpro= mprou+mprou1
		mprorq= requests.get(url=urlmpro).text
		if "mysql" in mprorq:
			print(f'[{Fore.GREEN}MPro Found >>{Fore.WHITE}] ', urlmpro)
			with open('MPro-sql-Found.txt', 'a') as mp:
				mp.write(mpro+urlmpro+'\n')
		elif "MySQL" in mprorq:
			print(f'[{Fore.GREEN}MPro Found >>{Fore.WHITE}] ', urlmpro)
			with open('MPro-sql-Found.txt', 'a') as mp:
				mp.write(mpro+urlmpro+'\n')
		else:
			print(f'[{Fore.RED}MPro Not Found >>{Fore.WHITE}] ', mprourl2)
mproscan()