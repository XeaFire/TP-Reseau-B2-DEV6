import asyncio



async def handle_packet(reader, writer):
    addr = writer.get_extra_info('peername')
    print(f"Client connecté: {addr}")
    return



async def main():
    server = await asyncio.start_server(handle_packet, '10.33.49.148', 14447)

    addr = server.sockets[0].getsockname()
    print(f"Serveur en écoute sur {addr}")

    async with server:
        await server.serve_forever()    
asyncio.run(main())