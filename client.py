import socket

host_ip = "192.168.1.197"
port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((host_ip, port))

while True:
	message = input("===>")
	# Convertir la chaîne de caractères en bytes
	message_bytes = message.encode('utf-8')
	socket.send(message_bytes)
	requete_server = socket.recv(1000)
	#Enlever le code en utf-8
	requete_server = requete_server.decode("utf-8")
	print(requete_server)
