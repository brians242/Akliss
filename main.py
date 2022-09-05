from itertools import count
import discord
from discord.ext import commands
import random
from bs4 import BeautifulSoup
import csv
from selenium import webdriver
import json
import datetime


"""

val = input("Enter what amazon product you are looking for: ")

def get_url(search):
    template = ("https://amazon.com/s?k={}&ref=nb_sb_noss_1")
    search = search.replace(" ", "+")   
    return template.format(search)

url = get_url(val)
print(url)

"""


description = "A bot mainly focused on amazon_searches with a few extra tools."
intents = discord.Intents.default()
intents.members = True
intents.message_content = True
counter = 0

def get_prefix(bot, message):
    global counter
    with open("prefixes.json", "r") as i:
        prefixes = json.load(i)
    
    counter += 1
    return prefixes[str(message.guild.id)]

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
async def change_prefix(ctx, prefix):
    with open("prefixes.json", "r") as i:
        prefixes = json.load(i)
        
    prefixes[str(ctx.guild.id)] = prefix
    
    with open("prefixes.json", "w") as i:
        json.dump(prefixes, i, indent = 4)

@bot.command()
async def search(ctx):
    val = input("Enter what amazon product you are looking for: ")
    template = ("https://amazon.com/s?k={}&ref=nb_sb_noss_1")
    template.replace(" ", "+")
    return template.format()
    

@bot.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round (bot.latency * 1000)} ms")

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
    msg = "```amazon_searcher: the main function of the bot, takes your search result and your values for how important 4 categories are to find the best option for you. \nhelp: returns all of the commands and what they do. \nchange_prefix: changes the prefix to use the bot with. \nping: returns the ping to the server. \nusage: returns how many times you've used any bot commands (including help and usage). \nusage_reset: resets the usage command. \nroll: rolls a NdN dice and gives a random roll result.```"
            
    await ctx.send(msg)

bot.run("MTAxNjI3MDQ2MDc1NDg1Mzk2OQ.GZ6anh.IUXmcDynLXtmzY1kNY9fdYfMnDzrsCh_yeynHo")

# Token = MTAxNjI3MDQ2MDc1NDg1Mzk2OQ.GZ6anh.IUXmcDynLXtmzY1kNY9fdYfMnDzrsCh_yeynHo
