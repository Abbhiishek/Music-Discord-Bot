#importing databases we need for the projects
import discord
from discord.errors import ClientException
from discord.ext import commands
from discord.ext import tasks
import os
from decouple import config
from discord.enums import UserFlags
from discord.flags import Intents
import random
import json
from datetime import datetime
from discord.user import ClientUser
import requests
import asyncio
from random import choice



#adding our client (our bot , i am using client as bot)
#setting up Intents

intents = discord.Intents.default()
intents.members = True

#senpai variables
senpai_id = 888414036662833164
client = commands.Bot(command_prefix=commands.when_mentioned_or( '.', 'Dj'), case_insensitive=True, intents=intents)
client.remove_command("help")

print(">>>> The Master Is Logging To The Server... \n >>>Please wait for the connections to stablish...<<<<")

#Loads all the cogs in the cogs folder 
def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            client.load_extension(f"cogs.{file[:-3]}")

@client.command()
@commands.is_owner()
async def r(ctx):
  for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            client.load_extension(f"cogs.{file[:-3]}")
            await ctx.send(">>DJ  reloaded cogs")
        else:
            await ctx.send("SOME ERROR OCCURED !")

 #creating a task that change the activity status of the bot every 5 seconds so that it show different information evry 5 second. 

@tasks.loop(seconds=4)
async def switchpresence():
    await client.wait_until_ready()
    sm = [f"{len(client.guilds)} Servers!", f"{len(client.users)} Users!","Made by Abhishek Kushwaha"]
    ast = random.choice(sm)
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"senpai & {ast}"))

# loading all the information on the terminal when the bot goes online 

@client.event
async def on_ready():
    load_cogs()
    print(f">> Logged in as : {client.user.name} \n>> ID : {client.user.id}")
    print(f">> Total  Active Servers : {len(client.guilds)}")
    print('>> music is Onwork.')
    print(">> Data loaded.")
               
#do stuffs

@client.command()
async def status(ctx):
            
            async with ctx.channel.typing():
                embed = discord.Embed(title="Dj.io", description="These are the config of Dj.io",timestamp=datetime.utcnow(),
                                  color=discord.Colour.red())
                embed.add_field(name="version" , value=" 1.01.02", inline=True)
                embed.add_field(name="created by", value='<@752362202945683480>',inline=True)
                embed.add_field(name="Total servers", value=f"{len(client.guilds)} Servers!",inline=True)
                embed.add_field(name="Total User ", value= f"{len(client.users)} Users!",inline=True)
                
                embed.set_image(url="https://c.tenor.com/RGhPDvXANBQAAAAd/discord.gif")
                await ctx.send(embed=embed)

token = config("TOKEN")
switchpresence.start()
client.run(token)
#starting the loop for the switch_presence
#rumming the client in the server


