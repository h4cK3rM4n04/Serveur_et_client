import socket

host_ip = "192.168.1.197"
port = 6390

#Création du socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host_ip, port))
socket.listen(1)

#Le script s'arrête jusqu'à une connection
client, ip = socket.accept()
print("le client d'ip", ip, "s'est connecté")

#1000 = nombre de caractère maximum passé par le client
while True:
    requete_client = client.recv(1000)
    #Décoder car elle est en UTF-8
    requete_client = requete_client.decode("utf-8")
    print(requete_client)
    if not requete_client: #Dans le cas ou on perd la connexion
        print("CLOSE")
        break #On casse la boucle

    message = input("===>")
    #encoder en utf-8
    message = message.encode("utf-8")
    client.send(message)

client.close()
socket.close()