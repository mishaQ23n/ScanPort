# -*- coding: utf-8 -*-
import socket
import colorama
colorama.init()
def fun():
	sock = socket.socket()
	ip = input("Введите IP:")
	ports = int(input("Введите ПОРТ:"))
	try:

		sock.connect((ip,ports))

	except socket.error:
		print("\033[31m[!]ПОРТ ЗАКРЫТ " + str(ports))
	else:
   		print("\033[32m[!]ПОРТ ОТКРЫТ " + str(ports))
def funs():
    ip = input("Введите IP:")
    portis = [20, 21, 22, 23, 42, 43, 53, 67, 69, 80]
    for i in portis:
    	try:
    		sock = socket.socket()
    		sock.settimeout(0.5)
    		sock.connect((ip,i))
    	except socket.error:
    		print("\033[31m[!]ПОРТ ЗАКРЫТ! " + str(i))
    	else:
    		print("\033[32m[!]ПОРТ ОТКРЫТ " + str(i))
priva = [
"""
░██████╗░█████╗░░█████╗░███╗░░██╗██████╗░░█████╗░██████╗░████████╗
\033[34m██╔════╝██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝
╚█████╗░██║░░╚═╝███████║██╔██╗██║██████╔╝██║░░██║██████╔╝░░░██║░░░
░╚═══██╗██║░░██╗██╔══██║██║╚████║██╔═══╝░██║░░██║██╔══██╗░░░██║░░░
██████╔╝╚█████╔╝██║░░██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║░░░██║░░░
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░
 
 \033[31m                          Автор: @chmotie

1) Сканировать отдельный порт
2) Сканировать список портов
"""
]
print(priva[0])
ports = input("->")

if ports == "1":

	fun()

elif ports == "2":

	funs()

else:

	print("\033[31m[!]Выбрана неверная опция!")