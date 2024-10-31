import asyncio
import re

host = '5.5.5.1'
port = 14447

global CLIENTS
CLIENTS = {}

async def joinEvent(writeradrr):
        for addr in CLIENTS:
            writer = CLIENTS[addr]["w"]
            servermessage = f"{CLIENTS[writeradrr]["username"]} a rejoint la chatroom".encode("utf-8")
            writer.write(servermessage)
        return


async def leaveEvent(writeradrr):
    for addr in CLIENTS:
        writer = CLIENTS[addr]["w"]
        if CLIENTS[writeradrr]["username"] == '':
            CLIENTS[writeradrr]["username"] = CLIENTS[addr]["w"]
        servermessage = f"{CLIENTS[writeradrr]["username"]} a quitté la chatroom".encode("utf-8")
        writer.write(servermessage)
    return
    

async def sendAll(message, writeradrr):
    for addr in CLIENTS:
        writer = CLIENTS[addr]["w"]
        servermessage = f"{CLIENTS[writeradrr]["username"]} : {message}".encode("utf-8")
        writer.write(servermessage)
    return

async def handle_packet(reader, writer):
    addr = writer.get_extra_info('peername')
    CLIENTS[addr] = {}
    CLIENTS[addr]["r"] = reader
    CLIENTS[addr]["w"] = writer
    CLIENTS[addr]["username"] = ''
    servermessage = f"Hello {addr[0]}:{addr[1]}".encode("utf-8")
    writer.write(servermessage)
    await writer.drain()
    
    
    while True:
        data = await reader.read(100)
        message = data.decode('utf-8')
        if not data:
            await asyncio.sleep(0.05)
        print(f"Message received from {addr[0]!r}:{addr[1]!r} :{message!r}")
        if data == b'': # Gestion de la déco relou le loup
            await leaveEvent(addr)
            writer.close()
            await writer.wait_closed()
            return
        if CLIENTS[addr]["username"] == '':
            if re.match(r'^[a-z0-9_-]{3,15}$', message):
                CLIENTS[addr]["username"] = message
                await joinEvent(addr)
        else:
            await sendAll(message, addr)
       
        await writer.drain()
        
    # Je laisse ça là ça peut toujours me servir
   

async def main():
    server = await asyncio.start_server(handle_packet, host, port)

    addr = server.sockets[0].getsockname()
    print(f"Serveur en écoute sur {addr}")

    async with server:
        await server.serve_forever()    


if __name__ == "__main__":
    asyncio.run(main())