import discord
from discord import app_commands
from typing import List
from discord.ext import commands

class rock(commands.Cog):

  def __init__(self, client):
    self.client = client

  
  
def setup(client):
  client.add_cog(rock(client))