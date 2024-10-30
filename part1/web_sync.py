import time
import sys
import re
import requests
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

def get_content(url : str):
    try :
        content = requests.get(url)
    except Exception as e:
        print(f"ERROR Y'a une erreur : {e}")
        return None

    return content


def write_content(content, file : str):
    f = open(file + "/ben.txt", "w")
    f.write(str(content.content))
    f.flush()

def main():
    if check_arg():
        url = sys.argv[1]
        content = get_content(url)
        
        if content: write_content(content,tempfolder)
        


if __name__ == "__main__":
    process_start = time.time()
    main()
    process_end = time.time()
    print("🛠️  Process Time : " + str(process_end - process_start))
