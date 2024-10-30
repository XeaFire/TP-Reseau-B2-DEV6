import time

def p1():
    for i in range(10):
        print(i+1)
        time.sleep(0.5)


def main():
    
    p1()
    p1()
    



if __name__ == "__main__":
    process_start = time.time()
    main()
    process_end = time.time()
    print("🛠️  Process Time : " + str(process_end - process_start))
