import asyncio
import random

async def fake_task(name: str):
    await asyncio.sleep(random.uniform(0.5, 1.5))
    return {"task": name, "status": "done", "result": random.randint(1, 100)}
