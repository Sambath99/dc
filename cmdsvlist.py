import discord

async def list_channels(ctx):
    guild = ctx.guild
    channels = guild.channels

    # Create an embed
    embed = discord.Embed(title=f"Channel List ({len(channels)} channels)", color=discord.Color.blue())
    
    channel_names = "\n".join([channel.name for channel in channels])
    embed.add_field(name="Channels", value=channel_names, inline=False)
    
    await ctx.send(embed=embed)
