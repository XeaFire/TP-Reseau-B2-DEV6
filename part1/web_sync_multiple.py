import time
import sys
import re
import requests
import os

if os.name == 'nt':
    tempfolder = 'C:/tmp/web_page/'
else:
    tempfolder = '/tmp/web_page/'


def getUrls(path : str):
    with open(path, 'r') as file:
        urls = file.readlines()
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


def get_content(url : str):
    try :
        content = requests.get(url)
    except Exception as e:
        print(f"ERROR Y'a une erreur : {e}")
        return None

    return content


def write_content(content, file : str):
    f = open(file, "w")
    f.write(str(content.content))
    f.flush()

def main():
    urls = getUrls(sys.argv[1])
    valid_url = check_args(urls)
    if len(sys.argv) < 2:
        print("ERROR : Frro ? il est où ton path de fichier là ???")
        return
    for url in valid_url:
        content = get_content(url)    
        if content: write_content(content,tempfolder + url.split("//")[1] + ".txt" )
        


if __name__ == "__main__":
    process_start = time.time()
    main()
    process_end = time.time()
    print("🛠️  Process Time : " + str(process_end - process_start))
