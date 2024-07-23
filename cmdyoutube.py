import requests
import discord
from io import BytesIO
from y2mate_api import Handler

async def fetch_youtube_metadata(ctx, youtube_url):
    api = Handler(youtube_url)
    metadata_list = []
    
    for audio_metadata in api.run(format="mp3"):
        dlink = audio_metadata.get("dlink")  # Get the value of "dlink"
        title = audio_metadata.get("title")  # Get the value of "title"
        
        if dlink:
            response = requests.get(dlink)  # Download the MP3 file from dlink
            if response.status_code == 200:
                # Create BytesIO object from response.content
                audio_file = BytesIO(response.content)
                
                # Determine the filename using title or default to "audio.mp3"
                filename = f"{title}.mp3" if title else "audio.mp3"
                
                # Send the file as an attachment with the determined filename
                await ctx.send(file=discord.File(audio_file, filename=filename))
            else:
                await ctx.send("Failed to fetch MP3 file.")
        else:
            await ctx.send("No download link found.")
