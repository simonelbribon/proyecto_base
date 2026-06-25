import asyncio

async def handle_publish(payload: dict):
    await asyncio.sleep(0.1)
    print(f"[HANDLER] procesado: {payload}")

