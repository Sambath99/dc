import discord
from discord.ext import commands

async def list_users(ctx):
    guild = ctx.guild
    members = guild.members
    member_count = len(members)

    # Create an embed
    embed = discord.Embed(title=f"User List ({member_count} members)", color=discord.Color.blue())
    
    member_names = "\n".join([member.name for member in members])
    embed.add_field(name="Members", value=member_names, inline=False)
    
    await ctx.send(embed=embed)
