from telethon import events
import asyncio
import os
import sys


@borg.on(events.NewMessage(pattern=r"\.yoj", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
       
 
    await event.edit(" ๐๐๐๐\n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(1)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐ฆ๐ฆ๐ฆ๐ฆ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n๐๐๐๐ \n")
    await asyncio.sleep(0.5)
    await event.edit("ะ ะะซ ะะะฏ ะกะะะะะะะ ะะะะ ะะะขะะฆะ, ะะะะะ ะะะะ:)")
