import asyncio

host = '5.5.5.1'
port = 14447

global CLIENTS
CLIENTS = {}

async def sendAll(message, writeradrr):
    for addr in CLIENTS:
        writer = CLIENTS[addr]["w"]
        servermessage = f"{CLIENTS[addr]["username"]} : {message}".encode("utf-8")
        writer.write(servermessage)
        print("message send")
    return

async def handle_packet(reader, writer):
    addr = writer.get_extra_info('peername')
    CLIENTS[addr] = {}
    CLIENTS[addr]["r"] = reader
    CLIENTS[addr]["w"] = writer
    servermessage = f"Hello {addr[0]}:{addr[1]}".encode("utf-8")
    writer.write(servermessage)
    await writer.drain()
    
    while True:
        data = await reader.read(100)
        message = data.decode()
        if not data:
            await asyncio.sleep(0.05)
        print(f"Message received from {addr[0]!r}:{addr[1]!r} :{message!r}")
        if CLIENTS[addr]["username"] == '':
            CLIENTS[addr]["username"] = message.decode("utf-8")
        else:
            await sendAll(message, addr)
       
        await writer.drain()
        if data == b'': # Gestion de la déco relou le loup
            print("Close the connection")
            writer.close()
            await writer.wait_closed()
            return

    # Je laisse ça là ça peut toujours me servir
   

async def main():
    server = await asyncio.start_server(handle_packet, host, port)

    addr = server.sockets[0].getsockname()
    print(f"Serveur en écoute sur {addr}")

    async with server:
        await server.serve_forever()    


if __name__ == "__main__":
    asyncio.run(main())