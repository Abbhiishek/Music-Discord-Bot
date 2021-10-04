#importing databases we need for the projects
import os
import discord
from discord.ext import clients, tasks
from discord_components import DiscordComponents
import asyncio
import random
from datetime import datetime

#adding our client (our bot , i am using client as bot)
#setting up Intents

intents = discord.Intents.default()
intents.members = True

#senpai variables
senpai_id = 88841403666283316
client = clients.Bot(command_prefix=clients.when_mentioned_or( '?', 'play.'), case_insensitive=True, intents=intents)
client.remove_command("help")

print(">>>> The Master Is Logging To The Server... \n >>>Please wait for the connections to stablish...<<<<")

#Loads all the cogs in the cogs folder 
def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            client.load_extension(f"cogs.{file[:-3]}")

@client.command()
@clients.is_owner()
async def r(ctx):
  for file in os.listdir("./cogs"):
    if file.endswith(".py") and not file.startswith("_"):
      client.reload_extension(f"cogs.{file[:-3]}")
      await ctx.send(">> Senpai reloaded cogs")
    else:
        await ctx.send("SOME ERROR OCCURED !")

 #creating a task that change the activity status of the bot every 5 seconds so that it show different information evry 5 second. 

@tasks.loop(seconds=5)
async def switchpresence():
    await client.wait_until_ready()
    sm = [f"{len(client.guilds)} Servers!", f"{len(client.users)} Users!"]
    ast = random.choice(sm)
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"senpai & {ast}"))

# loading all the information on the terminal when the bot goes online 

@client.event
async def on_ready():
    load_cogs()
    print(f">> Logged in as : {client.user.name} \n>> ID : {client.user.id}")
    print(f">> Total  Active Servers : {len(client.guilds)}")
    print('>> Senpai is Onwork.')
    print(">> Data loaded.")
               
#do stuffs

@client.command()
async def status(ctx):
            
            async with ctx.channel.typing():
                embed = discord.Embed(title="senpai.io", description="These are the config of senpai.io",timestamp=datetime.utcnow(),
                                  color=discord.Colour.red())
                embed.add_field(name="version" , value=" 1.01.02", inline=True)
                embed.add_field(name="created by", value='<@752362202945683480>',inline=True)
                embed.add_field(name="Total servers", value=f"{len(client.guilds)} Servers!",inline=True)
                embed.add_field(name="Total User ", value= f"{len(client.users)} Users!",inline=True)
                
                embed.set_image(url="https://c.tenor.com/RGhPDvXANBQAAAAd/discord.gif")
                await ctx.send(embed=embed)

switchpresence.start()
client.run('ODkyNDA4NDcwODcwMDU3MDMw.YVMeJw.iccZZVYS7-xVzqgQV84YNg8L-_s')
#starting the loop for the switch_presence
#rumming the client in the server

