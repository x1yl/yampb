import discord
from discord.ext import commands

class admin(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.command (pass_context = True)
  @commands.has_permissions (manage_roles = True)
  async def addRole(self, ctx, user: discord.Member, *, role: discord.Role):
    if role in user.roles:
      await ctx.send(f"{user.mention} already has the role, {role}")
    else:
      await user.add_roles(role)
      await ctx.send(f"Added {role} to {user.mention}")

def setup(client):
  client.add_cog(admin(client))