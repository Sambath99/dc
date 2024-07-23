import discord
import asyncio

async def change_status(bot):
    while True:
        await bot.change_presence(status=discord.Status.online)
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.offline)
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.dnd)
        await asyncio.sleep(5)
        await bot.change_presence(status=discord.Status.idle)
        await asyncio.sleep(5)
