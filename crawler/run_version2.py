import asyncio
import random
import time

async def worker(no):
    print(f'strat worker {no}')
    await asyncio.sleep(random.randint(1,5))
    print(f'done worker {no}')



def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait([worker(i) for i in range(1,10)]))
    loop.close()

if __name__ == '__main__':
    t1 = time.time()
    main()
    t2 = time.time()
    print(f'elsped {t2-t1}')