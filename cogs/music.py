import discord
from discord import player
from discord.ext import commands
from discord.ext.commands.core import command
from discord.player import FFmpegAudio
import youtube_dl
import os
import DiscordUtilsMod


music = DiscordUtilsMod.Music()


class Music(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.DJ_id = 892408470870057030

    @commands.command()
    async def join (self , ctx):
        if ctx.author.voice is None:
            await ctx.send("You Are Not In Any Voice Channel!!!")
        voice_channel=ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def leave(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        await player.stop()
        await ctx.voice_client.disconnect()
        await ctx.send("The bot left the  voice channel.")


    @commands.command()
    async def play(self , ctx ,url):
        player = music.get_player(guild_id=ctx.guild.id)
        if not player :
            player = music.create_player(ctx, ffmpeg_error_betterfix=True)
        if not ctx.voice_client.is_playing():
            await player.queue(url , search= True)
            song= await player.play()
            await ctx.send (f' I Have Started Playing --{song.name}')
        else:
            song= await player.queue(url, search =True)
            await ctx.send(f"{','.join([song.name for song in player.current_queue()])}")

    @commands.command()
    async def skip(self , ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        data = await player.skip(force=True)
        if len(data) == 2:
           await ctx.send(f"Skipped from {data[0].name} to {data[2].name}")
        else:
            await ctx.send(f"Skipped {data[0].name}")

    @commands.command()
    async def queue(self,ctx,url):
        player = music.get_player(guild_id=ctx.guild.id)
        await ctx.send(f"{', '.join([song.name for song in player.current_queue()])}")

    @commands.command()
    async def pause(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.pause()
        await ctx.send(f"DJ Paused The song {song.name}")

    @commands.command()
    async def resume(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.resume()
        await ctx.send(f"DJ Resumed The song {song.name}")
    @commands.command()
    async def stop(self,ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.stop()
        await ctx.send(f"DJ stoped The song {song.name}")

    @commands.command()
    async def loop(self, ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.toggle_song_loop()
        if song.is_looping:
            return await ctx.send(f'{song.name} is looping ')
        else:
            return await ctx.send(f'{song.name} is not looping ')

    @commands.command()
    async def nowplaying(self , ctx):
        player = music.get_player(guild_id=ctx.guild.id)
        song= player.now_playing()
        await ctx.send(song.name)

    @commands.command()
    async def volume(self,ctx , vol):
        player = music.get_player(guild_id=ctx.guild.id)
        song, volume = await player.change_volume(float(vol) / 100) # volume should be a float between 0 to 1
        await ctx.send(f"Changed volume for {song.name} to {volume*100}%")

    @commands.command()
    async def remove(self ,ctx, index):
        player = music.get_player(guild_id=ctx.guild.id)
        song = await player.remove_from_queue(int(index))
        await ctx.send(f"Removed {song.name} from queue")


def setup(client):
    client.add_cog(Music(client))
    print(">>> music load ho gaya hai load ho gaya !!!!!!!!!")
