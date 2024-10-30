import socket
import sys
import asyncio

# On définit la destination de la connexion
host = '10.33.49.148'  # IP du serveur
port = 14447           # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur






async def main():
    try :
        reader, writer = await asyncio.open_connection(host, port)
    except socket.error as msg:
        print(f"Erreur de connexion avec le serveur : {msg}")
        sys.exit(1)

    # note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

    print(f"Connecté avec succès au serveur {host} sur le port {port}")
    # Envoi de data bidon

    clientmessage =input("Que veux-tu envoyer au serveur : ")

    msg = clientmessage.encode("utf-8")
    writer.write(msg)
    await writer.drain()



    # On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
    data = await reader.read(1024)
    if not data :
        sys.exit(1)
    # On libère le socket TCP
    s.close()

    # Affichage de la réponse reçue du serveur
    print(data.decode())

    sys.exit(0)

asyncio.run(main())