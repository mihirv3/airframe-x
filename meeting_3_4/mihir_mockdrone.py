import numpy as np
import asyncio

class MockDrone:

    async def connect(self):
        print("begin")
        await asyncio.sleep(2)
        print("Connected")

    async def attitude_data(self):
        while True:
            pitch_val = (np.random.randint(-90, 90))
            yield pitch_val
            await asyncio.sleep(0.02)

async def main():
    drone = MockDrone()
    await drone.connect()
    async for data in drone.attitude_data():
        print("Pitch angle:", data) 

if __name__ == "__main__":
    asyncio.run(main())
