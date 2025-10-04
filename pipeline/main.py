import asyncio
from pipeline.logger import PKLLogger
from pipeline.tasks import fake_task

logger = PKLLogger()

async def run_pipeline():
    tasks = [fake_task(f"task_{i}") for i in range(5)]
    results = await asyncio.gather(*tasks)
    logger.log(results)

if __name__ == "__main__":
    asyncio.run(run_pipeline())
