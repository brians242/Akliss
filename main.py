import discord
from discord.ext import commands
import random
import json
import cv2 as cv
import os

# Not completed 
description = "A bot that aims to use take a video and send images back with OpenCV and basic commands."
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
counter = 0
file_type = ""
frame_limit = []
default_pref = ";"

def get_prefix(bot, message):
    global counter
    with open("prefixes.json", "r") as i:
        prefixes = json.load(i)
    
    counter += 1
    if str(message.guild.id) in prefixes:
        return prefixes[str(message.guild.id)]
    else:
        prefixes[str(message.guild.id)] = default_pref
        with open('prefixes.json', 'w') as i:
            json.dump(prefixes, i, indent=4)
        return default_pref

bot = commands.Bot(command_prefix = get_prefix, case_sensitive = True, description = description, intents = intents, help_command = None)


@bot.event
async def on_ready():
    print(f"We have logged in as: {bot.user} (ID: {bot.user.id})")
    print("------")

@bot.event
async def on_guild_join(guild):
    with open("prefixes.json", "r") as i:
        prefixes = json.load(i)
    
    prefixes[str(guild.id)] = ";"
    
    with open("prefixes.json", "w") as i:
        json.dump(prefixes, i, indent = 4)
        
@bot.event
async def on_guild_remove(guild):
    with open("prefixes.json", "r") as i:
        prefixes = json.load(i)
    
    prefixes.pop(str(guild.id))
    
    with open("prefixes.json", "w") as i:
        json.dump(prefixes, i, indent = 4)

@bot.command()
async def check_prefix(ctx):
    with open("prefixes.json", "r") as i:
        prefixes = json.load(i)
    
    await ctx.send(f"your current prefix is {prefixes[str(ctx.guild.id)]}")

@bot.command()
async def change_prefix(ctx, prefix):
    with open("prefixes.json", "r") as i:
        prefixes = json.load(i)
        
    prefixes[str(ctx.guild.id)] = prefix
    
    with open("prefixes.json", "w") as i:
        json.dump(prefixes, i, indent = 4)
    await ctx.send(f"your current server prefix is: {prefix}")

@bot.command()
async def frame(ctx):
    
    count = 0
    path = (f"insert path here/Akliss/images/frame{count}.jpg")
    for i in path:
        with open(path, "rb") as f:
            picture = discord.File(f)
            await ctx.send(file=picture)
    
@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! Latency is {round (bot.latency * 1000)} ms")

@bot.command()
async def usage(ctx):
    if counter <= 1:
        await ctx.send(f"{counter} command has been used since the last reset.")
    elif counter < 0:
        await ctx.send("Error! Make sure to check your code!")
    else:
        await ctx.send(f"{counter} commands have been used since the last reset.")
    
@bot.command()
async def usage_reset(ctx):
    global counter
    await ctx.send(f"Reseting counter! {counter} is now at 0.")
    counter = 0

@bot.command()
async def roll(ctx, dice):
    try:
        rolls, limit = map(int, dice.split("d"))
    except Exception:
        await ctx.send("format has to be in NdN!")
        return
        
    
    result = ", ".join(str(random.randint(1, limit)) for i in range(rolls))
    await ctx.send(result)

@bot.command()
async def help(ctx):
    embed = discord.Embed(
        title = "Help",
        description = "These are all the commands that this bot has: \n\nframe: the main function of the bot, takes your video that you inserted and splits it into frames and gives you all the frames back. \n\nhelp: returns all of the commands and what they do. \n\ncheck_prefix: checks the prefix value (default should be ;), you've found it when it responds with: your current prefix is (your prefix. \n\nchange_prefix: changes the prefix to use the bot with. \n\nping: returns the ping to the server. \n\nusage: returns how many times you've used any bot commands (including help and usage). \n\nusage_reset: resets the usage command. \n\nroll: rolls a NdN dice and gives a random roll result.",
        color = discord.Color.blue()     
    )
    embed.set_image(url="https://echamicrobiology.com/app/uploads/2016/05/question-mark-character.jpg")
    embed.set_footer(text = "If you have additional questions, create an issue in the github repo")
    
    embed.set_author(
        name = "Karatumn",
        icon_url = "https://cdn.discordapp.com/avatars/312997978639958026/99ec2a8e69c5a8ba7f0ea85efe88bb57.webp?size=240",
    )
    
    await ctx.send(embed=embed)
    
bot.run("enter token here")