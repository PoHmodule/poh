from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
 strings = {"name": "ssikunpoh"}
 @loader.owner
 async def ssakacmd(self, message):
  for _ in range(2):
   for heart in ['я' ,'видел' ,'как' ,'ты' ,'обоссался' ,'вчера']:
    await message.edit(heart)
    await sleep(0.9)
