import requests
from colorama import Fore
from googlesearch import *
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
def mpro_google():
	urlmp = input("[MPro dork] >> ")
	slow("\n=====================================")
	stmpro= input("[MPro number of url] >> ")
	slow("\n=====================================")
	for mpro in search(urlmp,stop=int(stmpro)):
		print(Fore.BLUE+'-|===============[MohammedPro]===============|-'+Fore.WHITE)
		print(mpro)
		with open('MPro-url-sqli.txt', 'a') as mprroo:
			mprroo.write(mpro+'\n')
	else:
		
		slow("\n=====================================")
		slow("""
	|▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔|
	|     [===== My Accounts =====]      |
	|         Telegram:@xx4gs            |
	|         Instagram:@xx4gs           |
	|      [===== Welcome =====]         |
	|                                    |
	 ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔
	""")
		slow("\n=====================================")
		exit()
mpro_google()