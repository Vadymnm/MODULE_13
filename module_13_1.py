import time
import asyncio

async def start_strongman(name, power):
    print('Силач',name,'начал соревнование.')
    for i in range(1,6):
        await asyncio.sleep(1 / power)
        print('Силач',name,'поднял шар №',i)
    print('Силач', name, 'закончил соревнование.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Вася', 4))
    task2 = asyncio.create_task(start_strongman('Петя', 3))
    task3 = asyncio.create_task(start_strongman('Денис', 5))
    await task1
    await task2
    await task3
    print('Все,  конец!')


start = time.time()
asyncio.run(start_tournament())
finish = time.time()

print(f"Working time = {round(finish - start,3)} sec.")
print('(В исходном варианте время выполнения программы было 3.924сек.)')