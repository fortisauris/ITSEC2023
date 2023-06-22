# honeypot.py

import asyncio
import time

async def handle_connection(reader, writer):
	peername = writer.get_extra_info('peername')
	while True:
		data = await reader.read(1024)  # nacita byty
		if not data:
			break  # tak nic vrat sa do cyklu
		print(time.time(), peername, data.decode())   # zobraz na obrazovku
		writer.close()

async def main():
    server = await asyncio.start_server(handle_connection, '0.0.0.0', 23) # FTP port 
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())

