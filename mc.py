import discord
from discord.ext import commands
import aiohttp
from datetime import datetime

async def fetch_server_info(server_ip):
    url = f"https://api.mcsrvstat.us/3/{server_ip}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                return await response.json()
            else:
                return None

async def minecraft_server_info(ctx, server_ip):
    server_info = await fetch_server_info(server_ip)

    if server_info is None or 'error' in server_info:
        await ctx.send(f"Could not fetch data for server: {server_ip}. Please check the IP address and try again.")
        return

    # Extracting server information from JSON response
    server_name = server_info.get('hostname', 'Unknown Server')
    server_icon_url = f"https://api.mcsrvstat.us/icon/{server_ip}"
    server_status = server_info.get('online', False)
    server_address = server_info.get('ip', 'Unknown IP')
    server_port = server_info.get('port', 'Unknown Port')
    players_online = server_info.get('players', {}).get('online', 0)
    players_max = server_info.get('players', {}).get('max', 0)
    motd = server_info.get('motd', {}).get('clean', 'No MOTD')
    protocol = server_info.get('version', 'Unknown Version')

    # Determine status emoji and text color
    status_emoji = '🔴' if not server_status else '🟢'
    status_text = 'Offline' if not server_status else 'Online'
    status_color = discord.Color.red() if not server_status else discord.Color.green()

    # Format players count
    players_count = f"{players_online}/{players_max}"

    # Get current time for last update
    current_time = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S UTC')

    # Create an embed
    embed = discord.Embed(title=server_name, color=status_color)
    embed.set_thumbnail(url=server_icon_url)
    embed.add_field(name="Status", value=f"{status_emoji} {status_text}", inline=True)
    embed.add_field(name="Address:Port", value=f"{server_address}:{server_port}", inline=True)
    embed.add_field(name="Players", value=players_count, inline=True)
    embed.add_field(name="MOTD", value=motd, inline=False)
    embed.add_field(name="Protocol", value=protocol, inline=False)
    embed.set_footer(text=f"Last Updated: {current_time}", icon_url=server_icon_url)

    await ctx.send(embed=embed)
