from .. import loader
from asyncio import sleep 

def register(cb):
 cb(starMod()) 
 
class starMod(loader.Module):
 """Звездопад"""
 strings = {'name': 'starspoh'}
        
 async def starcmd(self, message):
  """Используй .star"""
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n\n\n\n\n\n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n       ⭐     ⭐     ⭐     ⭐   ⭐\n\n\n\n\n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n    ⭐    ⭐     ⭐     ⭐     ⭐   ⭐\n ⭐    ⭐    ⭐    ⭐    ⭐    ⭐       \n\n\n\n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit(' ☁☁☁☁☁☁☁☁☁☁☁\n   ⭐    ⭐     ⭐     ⭐     ⭐   ⭐\n⭐   ⭐    ⭐    ⭐    ⭐    ⭐       \n    ⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n\n\n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n    ⭐   ⭐     ⭐     ⭐     ⭐   ⭐\n⭐    ⭐     ⭐     ⭐     ⭐   ⭐       \n    ⭐     ⭐     ⭐     ⭐   ⭐    ⭐     \n⭐     ⭐     ⭐     ⭐   ⭐    ⭐    \n\n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n    ⭐    ⭐     ⭐    ⭐     ⭐  ⭐\n⭐    ⭐    ⭐    ⭐    ⭐    ⭐       \n    ⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n  ⭐      ⭐    ⭐  ⭐      ⭐  ⭐ \n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍') 
  await sleep(1.25)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n\n⭐️    ⭐️    ⭐    ⭐    ⭐    ⭐       \n    ⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n  ⭐      ⭐    ⭐  ⭐      ⭐  ⭐  \n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n\n\n    ⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n  ⭐      ⭐    ⭐  ⭐      ⭐  ⭐ \n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n\n\n\n⭐    ⭐    ⭐    ⭐    ⭐    ⭐     \n  ⭐      ⭐    ⭐  ⭐      ⭐  ⭐ \🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
  await sleep(0.75)
  await message.edit('☁☁☁☁☁☁☁☁☁☁☁\n\n\n\n\n  💫💫💫💫💫💫💫💫💫💫💫 \n🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍🌍')
