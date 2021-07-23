from telethon import events
import asyncio
import os
import sys
strings = {'name': 'YojikPOH'}

@poh(events.NewMessage(pattern=r"\.yoj", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit(" 🔘🔘🔘🔘\n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n")
    await asyncio.sleep(0.5)
    await event.edit("🚘🚘🚘🚘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n")
    await asyncio.sleep(0.5)
    await event.edit("🔘🔘🔘🔘 \n🚘🚘🚘🚘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n")
    await asyncio.sleep(0.5)
    await event.edit("🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🚘🚘🚘🚘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n")
    await asyncio.sleep(0.5)
    await event.edit("🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🚘🚘🚘🚘 \n🔘🔘🔘🔘 \n")
    await asyncio.sleep(0.5)
    await event.edit("🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🚘🚘🚘🚘 \n")
    await asyncio.sleep(1)
    await event.edit("🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🚘🚘🚘🚘 \n")
    await asyncio.sleep(0.5)
    await event.edit("🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🦔🦔🦔🦔 \n🚘🚘🚘🚘 \n")
    await asyncio.sleep(0.5)
    await event.edit("🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🔘🔘🔘🔘 \n🖕🖕🖕🖕 \n")
    await asyncio.sleep(0.5)
    await event.edit("А МЫ ЕЖЯ СПИЗДИЛИ ЕДИМ КАТАЦА, ААААА ЁЖИК:)")