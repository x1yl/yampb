import discord
from discord.ext import commands

class ping(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    messageID = "992194632874217472"
    if messageID == payload.message_id:
      member = payload.member
      guild = member.guild
      if payload.emoji.name == 'blackpng_bow':
        role = discord.utils.get(guild.roles, name="news")
      elif payload.emoji.name == 'blackpng_butterfly':
        role = discord.utils.get(guild.roles, name="giveaways")
      elif payload.emoji.name == 'blackpng_gaming':
        role = discord.utils.get(guild.roles, name="polls")
      await member.add_roles(role)
  

  @commands.command(pass_context=True)
  async def ping(self, ctx):
    embed = discord.Embed(
      title=";   ping roles   ;",
      description="",
      color=discord.Color.from_rgb(0, 0, 0),
    )
    embed.set_image(url="https://media.discordapp.net/attachments/990405465353621574/992146968669323264/d1d286e18fda97d0a7e53cc96a12337d.jpg?width=329&height=584")
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

def setup(client):
  client.add_cog(ping(client))