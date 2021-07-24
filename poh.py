from .. import loader
from asyncio import sleep
@loader.tds
class HeartsMod(loader.Module):
	strings = {"name": "Heartpoh"}
	@loader.owner
	async def pohertcmd(self, message):
		for _ in range(3):
			for heart in ['❤️' ,'🧡' ,'💛' ,'💚' ,'💙' ,'💜' ,'🖤' ,'🤍' ,'🤎' ,'❣' ,'💕' ,'💞' ,'💓','💗' ,'💖','💘' ,'💝' ,'💟']:
				await message.edit(heart)
				await sleep(0.01)
