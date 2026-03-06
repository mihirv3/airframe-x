import asyncio
import numpy as np


class mock_drone:
    async def connect(self):
        print("start")
        await asyncio.sleep(2)
        print("Connected")


async def altitude():
    while True:
        pitch = np.random.uniform(-90, 90)
        yield pitch
        await asyncio.sleep(0.1)


async def main():
    drone = mock_drone()
    await drone.connect()

    async for data in altitude():
        print("Pitch angle:", data)

asyncio.run(main())
