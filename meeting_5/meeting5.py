import asyncio
from mavsdk import System
from mavsdk.offboard import OffboardError, PositionNedYaw

async def run_mission():
    drone = System()
    print("Attempting to connect to the PX4 simulation...")
    await drone.connect(system_address="udpin://0.0.0.0:14540")

    print("Waiting for drone to connect...")
    async for state in drone.core.connection_state():
        if state.is_connected:
            print(f"-- Connected to drone!")
            break

    print("Waiting for drone to have a global positional estimate...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("-- GPS Lock Acquired!")
        break

    print("-- Arming")
    for attempt in range(5):
        try:
            await drone.action.arm()
            print("-- Armed Successfully!")
            break
        except Exception as e:
            print(f"Arming attempt {attempt + 1} failed: {e}. Retrying...")
            await asyncio.sleep(2)

    print("-- Setting initial setpoint")
    initial_position = PositionNedYaw(0.0, 0.0, 0.0, 0.0)
    await drone.offboard.set_position_ned(initial_position)

    try:
        print("-- Starting offboard mode")
        await drone.offboard.start()
    except OffboardError as error:
        print(f"Offboard start failed: {error}. Disarming...")
        await drone.action.disarm()
        return

    print("-- Flying to 5m North, 5m Altitude")
    target_position = PositionNedYaw(5.0, 0.0, -5.0, 0.0)
    await drone.offboard.set_position_ned(target_position)

    print("-- Hovering for 10 seconds...")
    await asyncio.sleep(10)

    print("-- Stopping offboard mode")
    try:
        await drone.offboard.stop()
    except OffboardError as error:
        print(f"Offboard stop failed: {error}")

    print("-- Landing")
    await drone.action.land()

if __name__ == "__main__":
    asyncio.run(run_mission())