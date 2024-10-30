import asyncio



async def handle_packet(reader, writer):
    data = await reader.read(100)
    message = data.decode()
    addr = writer.get_extra_info('peername')

    print(f"Received {message!r} from {addr!r}")

    print(f"Send: {message!r}")
    servermessage = f"Hello {addr[0]}:{addr[1]}".encode("utf-8")
    writer.write(servermessage)
    await writer.drain()

    print("Close the connection")
    writer.close()
    await writer.wait_closed()
    return



async def main():
    server = await asyncio.start_server(handle_packet, '10.33.49.148', 14447)

    addr = server.sockets[0].getsockname()
    print(f"Serveur en écoute sur {addr}")

    async with server:
        await server.serve_forever()    
asyncio.run(main())