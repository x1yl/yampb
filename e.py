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

















  ##@bot.hybrid_group(fallback="get")
##async def help(ctx):
##    await ctx.reply(f"Showing tag: {name}")
##
##
##@help.command()
##async def rockpaperscissors(ctx):
##    await ctx.reply(f"Created tag: {name}")


@bot.command(pass_context=True)
@bot.event
async def help(ctx):
    contents = [
        discord.Embed(
            title="Utilities commands",
            description=f"""
text 1    
""",
            colour=0xF00C0C,
        ),
        discord.Embed(
            title="Moderation commands",
            description=f"""
text 2
""",
            colour=0xF00C0C,
        ),
        discord.Embed(
            title="Fun commands",
            description=f"""
text 3
""",
            colour=0xF00C0C,
        ),
        discord.Embed(
            title="Coding commands",
            description=f"""
text 4
""",
            colour=0xF00C0C,
        ),
        discord.Embed(
            title="Bot's info | ID: 856643485340139580",
            description="""
text 5
""",
            colour=0xF00C0C,
        ),
    ]
    pages = 5
    cur_page = 1
    message = await ctx.send(embed=contents[cur_page - 1])

    await message.add_reaction("◀️")
    await message.add_reaction("▶️")

    def check(reaction, user):
        return user == ctx.author and str(reaction.emoji) in ["◀️", "▶️"]

    while True:
        try:
            reaction, user = await bot.wait_for("reaction_add", check=check)

            if str(reaction.emoji) == "▶️" and cur_page != pages:
                cur_page += 1
                await message.edit(embed=contents[cur_page - 1])
                await message.remove_reaction(reaction, user)

            elif str(reaction.emoji) == "◀️" and cur_page > 1:
                cur_page -= 1
                await message.edit(embed=contents[cur_page - 1])
                await message.remove_reaction(reaction, user)

            else:
                await message.remove_reaction(reaction, user)

        except:
            break