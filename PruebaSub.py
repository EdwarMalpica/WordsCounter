import asyncio
import subprocess
import time
import os

initial_time = time.time()

async def subprocess_sleep():
    process = subprocess.Popen(['sleep','0.1']) #Crea un subproceso hijo
    print(f'The process ID: {process.pid} \n Started sleep at {time.time() - initial_time:.1f}')
    await asyncio.sleep(1)

async def main():
    await asyncio.gather(subprocess_sleep())

if __name__ == "__main__":
    asyncio.run(main())




subprocess_sleep()