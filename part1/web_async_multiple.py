import time
import sys
import re
import requests
import aiofiles
import asyncio
import aiohttp
import os

if os.name == 'nt':
    tempfolder = 'C:/tmp/web_page/'
else:
    tempfolder = '/tmp/web_page/'



async def getUrls(path : str):
    async with aiofiles.open(path, "r") as file:
        urls = await file.readlines()
        urls = [url.strip() for url in urls]
        return urls
    


def check_args(urls):
    valdid_url = []
    for url in urls:
        if re.match(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)', url):
            valdid_url.append(url)
        else:
            continue
    return valdid_url


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
    async with aiofiles.open(file, "w") as f:
        await f.write(str(content))
        await f.flush()

async def main():
    urls = await getUrls(sys.argv[1])
    valid_url = check_args(urls)
    if len(sys.argv) < 2:
        print("ERROR : Frro ? il est où ton path de fichier là ???")
        return
    tasks = []
    for url in valid_url:
        tasks.append(get_content(url))  
    contents = await asyncio.gather(*tasks)

    write_tasks = []
    for content in contents:
        write_tasks.append(write_content(content, tempfolder + url.split("//")[1] + ".txt" ))
    await asyncio.gather(*write_tasks)

        


if __name__ == "__main__":
    process_start = time.time()
    asyncio.run(main())
    process_end = time.time()
    print("🛠️  Process Time : " + str(process_end - process_start))
