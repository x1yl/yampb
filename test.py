import json
import os
import random
import time
import typing

import discord
from discord import Client, Color, Intents, Interaction, app_commands
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions
from discord.utils import get

from config import *

def get_prefix(prefix):
    return str(prefix)
    
class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix = get_prefix(prefix), intents = intents)
    async def setup_hook(self):
        await self.tree.sync(guild = discord.Object(id = 942802471615606895))
        print(f"Synced slash commands for {self.user}.")

    async def on_command_error(self, ctx, error):
        await ctx.reply(error, ephemeral = True)

bot = Bot()

@bot.event
async def on_guild_join(guild, ctx): 
    me = ctx.message.server.me
    username = await bot.fetch_user(1041060008495939766)
    await bot.change_nickname(me, {username})

@bot.hybrid_command(name = "changeprefix", with_app_command = True, description = "Changes server prefix (manage server required)")
@app_commands.guilds(discord.Object(id = 942802471615606895))
@commands.has_guild_permissions(manage_messages = True)
async def changeprefix(ctx: commands.Context, prefixes: str):
    global prefix
    del prefix
    prefix = "".join(prefixes)
    await ctx.reply(f"Server Prefix Changed to {prefix}", ephemeral = True)


@bot.hybrid_command(name = "ping", with_app_command = True, description = "Replies with client latency")
@app_commands.guilds(discord.Object(id = 942802471615606895))
@commands.has_permissions(administrator = True)
async def ping(ctx: commands.Context):
    await ctx.defer(ephemeral = True)
    await ctx.reply(f"The client latency is {bot.latency} :ping_pong:")

@bot.hybrid_command(name = "activedev", with_app_command = True, description = "Use this for active dev badge", pass_context = True)
@app_commands.guilds(discord.Object(id = 942802471615606895))
@commands.is_owner()
async def ActiveDev(ctx: commands.Context,):
    print(f"> {ctx.author} used the command.")
    await ctx.reply("\n".join([
        f"Hello <@{ctx.author.id}>, learn more about the badge below",
        "",
        "__**Where's my badge?**__",
        "Wait 24 hrs",
        "",
        "__**It's been 24 hours, now how do I get the badge?**__",
        "Go to <https://discord.com/developers/active-developer> and fill out the 'form' there.",
        "",
        "__**Active Developer Badge Updates**__",
        "Updates regarding the Active Developer badge can be found at <https://discord.gg/discord-developers> - in the <#1040380406299644064>.",
    ]), ephemeral = False)


@bot.hybrid_command(name = "rockpaperscissors", with_app_command = True, description = "Play rock paper scissors with me!", pass_context = True)
@app_commands.guilds(discord.Object(id = 942802471615606895))
async def RockPaperScissors(ctx: commands.Context, choice: str):
    RockPaperScissorRandom=random.randint(1,3)
    if RockPaperScissorRandom == 1:
        RockPaperScissorBotChoice = "rock"
    elif RockPaperScissorRandom == 2:
        RockPaperScissorBotChoice = "paper"
    elif RockPaperScissorRandom == 3:
        RockPaperScissorBotChoice = "scissor"
    if RockPaperScissorBotChoice == choice:
        await ctx.reply(f"Draw! I chose {choice}, try again.")
    else:
      if ((RockPaperScissorBotChoice == "rock") and (choice == "paper")):
          await ctx.reply(f"I choose {RockPaperScissorBotChoice}, gg you win <a:8922_Letter_W:945766211436818525>!")
      elif ((RockPaperScissorBotChoice == "rock") and (choice == "scissor")):
          await ctx.reply(f"I choose {RockPaperScissorBotChoice}, you lose <a:6141_Letter_L:945766211520708738>")
      elif ((RockPaperScissorBotChoice == "paper") and (choice == "scissor")):
          await ctx.reply(f"I choose {RockPaperScissorBotChoice}, gg you win <a:8922_Letter_W:945766211436818525>!")
      elif ((RockPaperScissorBotChoice == "paper") and (choice == "rock")):
          await ctx.reply(f"I choose {RockPaperScissorBotChoice}, you lose <a:6141_Letter_L:945766211520708738>")
      elif ((RockPaperScissorBotChoice == "scissor") and (choice == "paper")):
          await ctx.reply(f"I choose {RockPaperScissorBotChoice}, you lose <a:6141_Letter_L:945766211520708738>")
      elif ((RockPaperScissorBotChoice == "scissor") and (choice == "rock")):
          await ctx.reply(f"I choose {RockPaperScissorBotChoice}, gg you win <a:8922_Letter_W:945766211436818525>!")

@RockPaperScissors.autocomplete("choice")
async def RockPaperScissors_autocompletion(ctx: commands.Context, current: str) -> typing.List[app_commands.Choice[str]]:
    data = []
    for choice in ['rock', 'paper', 'scissor']:
        if current.lower() in choice.lower():
            data.append(app_commands.Choice(name=choice, value=choice))
    return data
bot.run(token)
