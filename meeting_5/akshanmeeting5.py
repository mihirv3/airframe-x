import asyncio
from mavsdk import System
from mavsdk.offboard import PositionNedYaw


async def run_mission():

    drone = System()
    await drone.connect(system_address="udp://:14540")

    print("Connected to drone")

    async for health in drone.telemetry.health():
        if health.is_global_position_ok:
            print("GPS Lock Acquired")
            break

    await drone.action.arm()

    initial = PositionNedYaw(0,0,0,0)
    await drone.offboard.set_position_ned(initial)
    await drone.offboard.start()

    target = PositionNedYaw(5,0,-5,0)
    await drone.offboard.set_position_ned(target)

    # print coordinates while flying
    async for position in drone.telemetry.position_velocity_ned():

        north = position.position.north_m
        east = position.position.east_m
        down = position.position.down_m

        print(f"N: {north:.2f}  E: {east:.2f}  D: {down:.2f}")

        await asyncio.sleep(0.5)

asyncio.run(run_mission())