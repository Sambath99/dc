import discord
from discord.ext import commands

async def hello(ctx):
    await ctx.send('Hello!')

# Listener for detecting the "hello" message in any chat
async def handle_hello_message(message):
    if message.author.bot:
        return
    if "hello" in message.content.lower():
        await message.channel.send('Welcome to this server!')
