from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
 strings = {"name": "loxoleg"}
 @loader.owner
 async def oglohcmd(self, message):
  for _ in range(1):
   for heart in ['это' ,'это Олег' ,'это Олег и' 
,'это Олег и он' ,'это Олег и он сдохнет' ,'это Олег и он сдохнет со','это Олег и он сдохнет со своими'
,'это Олег и он сдохнет со своими коровами в одиночестве нахуй',']:
    await message.edit(heart)
    await sleep(0.5)
