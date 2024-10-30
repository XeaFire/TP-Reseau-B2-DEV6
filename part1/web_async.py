import time
import sys
import re
import aiohttp
import asyncio
import aiofiles
import os

if os.name == 'nt':
    tempfolder = 'C:/tmp/web_page/'
else:
    tempfolder = '/tmp/web_page/'


def check_arg():
    if len(sys.argv) < 2:
        print("ERROR : Need un site mon frère")
    else:
        if re.match(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', sys.argv[1]):
            return True
        else:
            print("ERROR : Site non valide ratio")
            return False

async def get_content(url : str):
    try :
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                content = await resp.read()
    except Exception as e:
        print(f"ERROR Y'a une erreur : {e}")
        return None

    return content


async def write_content(content, file : str):
    async with aiofiles.open(file + "/ben.txt", "w") as f:
        await f.write(str(content))
        await f.flush()

async def main():
    if check_arg():
        url = sys.argv[1]
        content = await get_content(url)
        
        if content: await write_content(content, tempfolder)
        


if __name__ == "__main__":
    process_start = time.time()
    asyncio.run(main())
    process_end = time.time()
    print("🛠️  Process Time : " + str(process_end - process_start))
