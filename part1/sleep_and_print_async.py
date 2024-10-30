import asyncio
import time


async def p1():
    for i in range(10):
        print(i+1)
        await asyncio.sleep(0.5)


async def main():
    tasks = [p1() , p1()]
    await asyncio.gather(*tasks)
    



if __name__ == "__main__":
    process_start = time.time()
    asyncio.run(main())
    process_end = time.time()
    print("🛠️  Process Time : " + str(process_end - process_start))