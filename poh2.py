from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Heartpoh"}
	@loader.owner
	async def pohertcmd(self, message):
		for _ in range(3):
			for heart in ['โค๏ธ' ,'๐งก' ,'๐' ,'๐' ,'๐' ,'๐' ,'๐ค' ,'๐ค' ,'๐ค' ,'โฃ' ,'๐' ,'๐' ,'๐','๐' ,'๐','๐' ,'๐' ,'๐']:
				await message.edit(heart)
				await sleep(1.0)
