import time

from .. import loader
from asyncio import sleep
@loader.tds
class timerMod(loader.Module):
	strings = {"name": "timerpoh"}
	@loader.owner
	async def timercmd(self, message):

while true:
i = 0 # секунды
ii = 0 # минуты
iii = # часы
time_user = int(input("введите кол-во секунд: "))
comment = str(input("введите комментарий: "))
for q in range(time_user):
    time.sleep(1)
    i += 1
    print("прошло секунд:", i)
    if(i % 60) == 0
        ii += 1
        ptint("прошло минут:", ii)
    if(i % 3600) == 0:
        iii += 1
        print("прошло часов:", iii)
print("время окончено!")
print("ваш комментарий!")