import asyncio
async def work():
    print("Working...")
    await asyncio.sleep(2)
    print("Done")
async def main():
    task = asyncio.create_task(work())
    await task
asyncio.run(main())
