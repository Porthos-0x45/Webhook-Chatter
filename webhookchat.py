from json import *
from base64 import b64decode
from urllib.request import Request, urlopen
import os
from colorama import Fore
import socket
import json
from modules.readreplies import *

with open('config.json') as f:
    config = json.load(f)
    
webhook_url = config.get('webhook')
hookName = config.get('username')
hookAvatar = config.get('avatar_url')

pc_username = Fore.GREEN + socket.gethostname()
_PREFIX = Fore.GREEN + "px1l" + Fore.WHITE + ":" + pc_username

def getheaders(token=None, content_type="application/json"):
	headers = {
		"Content-Type": content_type,
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
	}
	return headers

def send(message):
	webhook = {
		"content": message,
		"username": hookName,
		"avatar_url": hookAvatar
	}
	try:
		urlopen(Request(webhook_url, data=dumps(webhook).encode(), headers=getheaders()))
	except:
		pass

def help():
	print ("Helping...")
	print ("Commands: chat, purge")
	print ("To execute this commands type run")
	main()

def replies():
	pass

def chat():
	chat = True
	while chat:
		user = str(input(_PREFIX + Fore.WHITE + ":" + Fore.GREEN + "chat" + Fore.WHITE + "> "))
		if user == "exit":
			chat = False
			main()
		elif user == "help":
			print (Fore.GREEN + "Just type your message and done. To exit type 'exit'")
		elif user == "replies":
			replies()
		elif user == "run":
			print(Fore.YELLOW + "Every message now will be sent: ")
			run = True
			while run:
				user = str(input(_PREFIX + Fore.WHITE + ":" + Fore.GREEN + "chat" + Fore.WHITE + ":" + Fore.YELLOW + "run" + Fore.WHITE + "> "))
				if user == "stop":
					print (Fore.RED + '[+]', Fore.WHITE + 'Stopping...')
					run = False
				else:
					send(user)
		else:	
			send(user)

def purge():
	pass

def main():
	user = str(input(_PREFIX + Fore.WHITE + "> "))

	if user == "chat":
		chat()
	elif user == "purge":
		purge()
	elif user == "help":
		help()
	elif user == "exit":
		print(Fore.GREEN + '[+]', Fore.WHITE + 'Exiting... Bye')
		exit()
	else:
		print("Incorrect command try using help!")
		main()

if __name__ == '__main__':
	os.system('clear')
	main()