import asyncio
import time
import threading


def blocking_task():
    print('Task starting')
    time.sleep(2)
    thread = threading.current_thread()
    print(f'name={thread.name}, daemon={thread.daemon}')
    print('Task done')


# async def background():
#     while True:
#         print('background task running')
#         await asyncio.sleep(0.5)



async def main():
    # _= asyncio.create_task(background())
    print('Main running the blocking task')
    coro = asyncio.to_thread(blocking_task)
    #task = asyncio.create_task(coro)
    print('Main doing other operations')
    #await asyncio.sleep(2.1)
    await coro

asyncio.run(main())
