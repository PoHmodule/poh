from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
 strings = {"name": "lox"}
 @loader.owner
 async def loxcmd(self, message):
  for _ in range(1):
   for heart in ['Олег' ,'олег лох' ,'олег лох под' ,'олег лох под юбкой' ,'олег лох под юбкой сдох']:
    await message.edit(heart)
    await sleep(0.6)
