import socket
from threading import Thread

def Send(socket):
	while True:
		mes = input("")
		mes = mes.encode("utf-8")
		socket.send(mes)

def Recep(socket):
	while True:
		requete_server = socket.recv(1000)
		# Enlever le code en utf-8
		requete_server = requete_server.decode("utf-8")
		print(requete_server)

host_ip = "192.168.1.197"
port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host_ip, port))

envoi = Thread(target = Send, args = [socket])
reception = Thread(target = Recep, args = [socket])

envoi.start()
reception.start()