import discord
from discord.ext import commands
import os
import time
import json
import random
from discord import Color
from discord.utils import get
from discord.ext.commands import has_permissions, MissingPermissions
from config import *

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = prefix, intents=intents)
ourmessage = ""

@client.event
async def on_ready():
  print(f"Logged in as {client.user}")
  print("---------------------------")
@client.event
async def on_message(message):
    if message.content == "!connect4":
      await message.channel.send("How to play \n type the number corresponding to a row", reference=message)
      time.sleep(1)
      await message.channel.send("Proceed?", reference=message)
      if message == "yes":
        await message.channel.send("<:c4_1:1008273636102250558><:c4_2:1008273628346990622><:c4_3:1008273620423938128><:c4_4:1008273612714803310><:c4_5:1008273609275486218><:c4_6:1008273605399953469><:c4_7:1008273603374096474>\n ", reference=message)  
    if message.content == "ping":
        await message.channel.send("pong:ping_pong:", reference=message)
    if message.content == "!rock":
      a=random.randint(1,3)
      print(a)
      if a == 1:
        await message.channel.send("I choose rock, draw. Try again!", reference=message)
      elif a == 2:
        await message.channel.send("I choose paper, you lost <a:6141_Letter_L:945766211520708738>", reference=message)
      elif a == 3:
        await message.channel.send("I choose scissors, gg you win <a:8922_Letter_W:945766211436818525>!", reference=message)
    if message.content == "!paper":
      a=random.randint(1,3)
      print(a)
      if a == 1:
        await message.channel.send("I choose rock, gg you win <a:8922_Letter_W:945766211436818525>!", reference=message)
      elif a == 2:
        await message.channel.send("I choose paper, draw. Try again!", reference=message)
      elif a == 3:
        await message.channel.send("I choose scissors, you lost <a:6141_Letter_L:945766211520708738>", reference=message)
    if message.content == "!scissors":
      a=random.randint(1,3)
      print(a)
      if a == 1:
        await message.channel.send("I choose rock, you lost <a:6141_Letter_L:945766211520708738>", reference=message)
      elif a == 2:
        await message.channel.send("I choose paper, gg you win <a:8922_Letter_W:945766211436818525>!", reference=message)
      elif a == 3:
        await message.channel.send("I choose scissors, draw. Try again!", reference=message)
    if message.content == "!scissor":
      a=random.randint(1,3)
      print(a)
      if a == 1:
        await message.channel.send("I choose rock, you lost <a:6141_Letter_L:945766211520708738>", reference=message)
      elif a == 2:
        await message.channel.send("I choose paper, gg you win <a:8922_Letter_W:945766211436818525>!", reference=message)
      elif a == 3:
        await message.channel.send("I choose scissors, draw. Try again!", reference=message)
@client.event
async def on_raw_reaction_add(payload):
  messageID = '992448354715959407'
  if payload.message_id == 992448354715959407:
    member = payload.member
    guild = member.guild
    if payload.emoji.name == 'blackpng_bow':
      role = discord.utils.get(guild.roles, name="news")
    elif payload.emoji.name == 'blackpng_butterfly':
      role = discord.utils.get(guild.roles, name="giveaways")
    elif payload.emoji.name == 'blackpng_gaming':
      role = discord.utils.get(guild.roles, name="polls")
    await member.add_roles(role)
  elif payload.message_id == 992448372910850078:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'blackpng_guitar':
      role = discord.utils.get(guild.roles, name="dms open")
    elif payload.emoji.name == 'blackpng_heart':
      role = discord.utils.get(guild.roles, name="ask to dm")
    elif payload.emoji.name == 'blackwhitepng_cat':
      role = discord.utils.get(guild.roles, name="dms closed")
    await member.add_roles(role)
  elif payload.message_id == 992448411741720636:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'emoji_13':
      role = discord.utils.get(guild.roles, name="minor")
    elif payload.emoji.name == 'emoji_14':
      role = discord.utils.get(guild.roles, name="adult")
    await member.add_roles(role)
  elif payload.message_id == 992448422261051552:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'emoji_35':
      role = discord.utils.get(guild.roles, name="female")
    elif payload.emoji.name == 'emoji_38':
      role = discord.utils.get(guild.roles, name="male")
    elif payload.emoji.name == 'emoji_41':
      role = discord.utils.get(guild.roles, name="genderfluid")
    await member.add_roles(role)
  elif payload.message_id == 992448433447243826:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'emoji_21':
      role = discord.utils.get(guild.roles, name="﹒uploaders")
    await member.add_roles(role)

    

@client.event
async def on_raw_reaction_remove(payload):
  messageID = '992448354715959407'
  if payload.message_id == 992448354715959407:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'blackpng_bow':
      role = discord.utils.get(guild.roles, name="news")
    elif payload.emoji.name == 'blackpng_butterfly':
      role = discord.utils.get(guild.roles, name="giveaways")
    elif payload.emoji.name == 'blackpng_gaming':
      role = discord.utils.get(guild.roles, name="polls")
    await member.remove_roles(role)
  elif payload.message_id == 992448372910850078:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'blackpng_guitar':
      role = discord.utils.get(guild.roles, name="dms open")
    elif payload.emoji.name == 'blackpng_heart':
      role = discord.utils.get(guild.roles, name="ask to dm")
    elif payload.emoji.name == 'blackwhitepng_cat':
      role = discord.utils.get(guild.roles, name="dms closed")
    await member.remove_roles(role)
  elif payload.message_id == 992448411741720636:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'emoji_13':
      role = discord.utils.get(guild.roles, name="minor")
    elif payload.emoji.name == 'emoji_14':
      role = discord.utils.get(guild.roles, name="adult")
    await member.remove_roles(role)
  elif payload.message_id == 992448422261051552:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'emoji_35':
      role = discord.utils.get(guild.roles, name="female")
    elif payload.emoji.name == 'emoji_38':
      role = discord.utils.get(guild.roles, name="male")
    elif payload.emoji.name == 'emoji_41':
      role = discord.utils.get(guild.roles, name="genderfluid")
    await member.remove_roles(role)
  elif payload.message_id == 992448433447243826:
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if payload.emoji.name == 'emoji_21':
      role = discord.utils.get(guild.roles, name="﹒uploaders")
    await member.remove_roles(role)
  

@client.command(pass_context=True)
@has_permissions(manage_roles = True)  
async def ping(ctx):
  embed = discord.Embed(
    title=";                                   ping roles                                   ;",
    description="",
    color=discord.Color.from_rgb(0, 0, 0),
  )
  embed.set_image(url="https://media.discordapp.net/attachments/990405465353621574/992146968669323264/d1d286e18fda97d0a7e53cc96a12337d.jpg?width=614&height=585")
  await ctx.send(embed=embed)
  embed2 = discord.Embed(
    title="",
    description="<:blackpng_bow:991762673349963806> : `news`\n<:blackpng_butterfly:991762702601027615> : `giveaways`\n<:blackpng_gaming:991762934810279966> : `polls`",
	color=discord.Color.from_rgb(128, 128, 128),
    )
  msg = await ctx.send(embed=embed2)  
  await msg.add_reaction('<:blackpng_bow:991762673349963806>')
  await msg.add_reaction('<:blackpng_butterfly:991762702601027615>')
  await msg.add_reaction('<:blackpng_gaming:991762934810279966>')

@client.command(pass_context=True)
@has_permissions(manage_roles = True)  
async def gender(ctx):
  embed = discord.Embed(
    title=";                                gender roles                                ;",
    description="",
    color=discord.Color.from_rgb(0, 0, 0),
  )
  embed.set_image(url="https://media.discordapp.net/attachments/990405465353621574/992147364154445954/829208e16216e60eb7f7f480add25d00.jpg?width=614&height=585")
  await ctx.send(embed=embed)
  embed2 = discord.Embed(
    title="",
      description="<:emoji_35:991778357358374933> : `female`\n<:emoji_38:991778495443243069> : `male`\n<:emoji_41:991778617057091674> :`genderfluid`",
	color=discord.Color.from_rgb(128, 128, 128),
    )
  msg = await ctx.send(embed=embed2)
  await msg.add_reaction('<:emoji_35:991778357358374933>')
  await msg.add_reaction('<:emoji_38:991778495443243069>')
  await msg.add_reaction('<:emoji_41:991778617057091674>')
  
@client.command(pass_context=True)
@has_permissions(manage_roles = True)  
async def uploaders(ctx):
  embed = discord.Embed(
    title=";                                    uploader                                    ;",
    description="",
    color=discord.Color.from_rgb(0, 0, 0),
  )
  embed.set_image(url="https://media.discordapp.net/attachments/990405465353621574/992147461042884731/1fb748e7353850ce7e78d3ac24dfa850.jpg?width=614&height=585")
  await ctx.send(embed=embed)
  embed2 = discord.Embed(
    title="",
      description="<:emoji_21:991776949179514890> : `uploaders`",
	color=discord.Color.from_rgb(128, 128, 128),
    )
  msg = await ctx.send(embed=embed2)
  await msg.add_reaction('<:emoji_21:991776949179514890>')

  

@client.command(pass_context=True)
@has_permissions(manage_roles = True)  
async def dm(ctx):
  embed = discord.Embed(
    title=";                                    dm roles                                    ;",
    description="",
    color=discord.Color.from_rgb(0, 0, 0),
  )
  embed.set_image(url="https://media.discordapp.net/attachments/990405465353621574/992147104006938734/27530a7552aeef0c70318387e098b2b1.jpg?width=614&height=585")
  await ctx.send(embed=embed)
  embed2 = discord.Embed(
    title="",
      description="<:blackpng_guitar:991763069405503558> : `dms open`\n<:blackpng_heart:991762998341414994> : `ask to dm`\n<:blackwhitepng_cat:991762872201904219> : `dms closed`",
	color=discord.Color.from_rgb(128, 128, 128),
    )
  msg = await ctx.send(embed=embed2)
  await msg.add_reaction('<:blackpng_guitar:991763069405503558>')
  await msg.add_reaction('<:blackpng_heart:991762998341414994>')
  await msg.add_reaction('<:blackwhitepng_cat:991762872201904219>')
  
@client.command(pass_context=True)
@has_permissions(manage_roles = True)  
async def age(ctx):
  embed = discord.Embed(
    title=";                                    age roles                                   ;",
    description="",
    color=discord.Color.from_rgb(0, 0, 0),
  )
  embed.set_image(url="https://media.discordapp.net/attachments/990405465353621574/992147404474302464/20a5a613e068dad10c47b9122fe795a4.jpg?width=614&height=585")
  await ctx.send(embed=embed)
  embed2 = discord.Embed(
    title="",
    description="<:emoji_13:991763442274934855> : `minor`\n<:emoji_14:991763466295726161> : `adult`",
    color=discord.Color.from_rgb(128, 128, 128),
    )
  msg = await ctx.send(embed=embed2)
  await msg.add_reaction('<:emoji_13:991763442274934855>')
  await msg.add_reaction('<:emoji_14:991763466295726161>')


@client.command(pass_context=True)
async def love(ctx, message):
  await message.channel.send("success")
inital_extensions = []

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    inital_extensions.append("cogs." + filename[:-3])

if __name__ == '__main__':
  for extension in inital_extensions:
    client.load_extension(extension)
client.run(token)