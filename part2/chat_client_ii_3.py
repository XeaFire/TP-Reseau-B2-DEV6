import socket
import sys
import asyncio
import aioconsole

# On définit la destination de la connexion
host = '10.33.49.148'  # IP du serveur
port = 14447           # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur



async def receive(reader,writer):
    while True:
        data = await reader.read(1024)
        print(data.decode())


async def input(reader,writer):
    while True:
        clientmessage = await aioconsole.ainput()
        msg = clientmessage.encode("utf-8")
        writer.write(msg)
        await writer.drain()

async def main():
    try :
        reader, writer = await asyncio.open_connection(host, port)
    except socket.error as msg:
        print(f"Erreur de connexion avec le serveur : {msg}")
        sys.exit(1)

    # note : la double parenthèse n'est pas une erreur : on envoie un tuple à la fonction connect()

    print(f"Connecté avec succès au serveur {host} sur le port {port}")

    



    # On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
    data = await reader.read(1024)
    if not data :
        sys.exit(1)
    # On libère le socket TCP

    # Affichage de la réponse reçue du serveur
    print(data.decode())
    tasks = [receive() , input()]
    await asyncio.gather(*tasks)

asyncio.run(main())