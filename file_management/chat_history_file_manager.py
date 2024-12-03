import json
import aiofiles


async def read_history()->list[dict]:
    async with aiofiles.open('files/history.json', mode='r') as f:
        contents = await f.read()
        data = json.loads(contents)
    return data

async def write_history(data:list[dict]):
    async with aiofiles.open('files/history.json', mode='w') as f:
        await f.write(json.dumps(data))
