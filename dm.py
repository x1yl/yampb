import discord
from discord.ext import commands

class dm(commands.Cog):

  def __init__(self, client):
    self.client = client
  @commands.command(pass_context=True)
  async def dm(ctx):
    embed = discord.Embed(
      title=";   dm roles   ;",
      description="",
      color=discord.Color.from_rgb(0, 0, 0),
  )
    embed.set_image(url="https://media.discordapp.net/attachments/990405465353621574/992147104006938734/27530a7552aeef0c70318387e098b2b1.jpg?width=614&height=585")
    await ctx.send(embed=embed)
    embed4 = discord.Embed(
      title="",
      description="<:blackpng_guitar:991763069405503558> : `dms open`\n<:blackpng_heart:991762998341414994> : `ask to dm`\n<:blackwhitepng_cat:991762872201904219> : `dms closed`",
	  color=discord.Color.from_rgb(128, 128, 128),
    )
    msg = await ctx.send(embed=embed4)
    await msg.add_reaction('<:blackpng_guitar:991763069405503558>')
    await msg.add_reaction('<:blackpng_heart:991762998341414994>')
    await msg.add_reaction('<:blackwhitepng_cat:991762872201904219>')
  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    messageID = ""
    if messageID == payload.message_id:
      member = payload.member
      guild = member.guild
    if payload.emoji.name == 'blackpng_guitar':
      role = discord.utils.get(guild.roles, name="dms open")
    elif payload.emoji.name == 'blackpng_heart':
      role = discord.utils.get(guild.roles, name="ask to dm")
    elif payload.emoji.name == 'blackwhitepng_cat':
      role = discord.utils.get(guild.roles, name="dms closed")
    await member.add_roles(role)

def setup(client):
  client.add_cog(dm(client))