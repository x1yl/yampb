import os
import random
import typing

import discord
from discord import  app_commands
from discord.ext import commands
from discord.ext.commands import MissingPermissions, has_permissions
from discord.ui import view
from discord.utils import get
import discordmongo
import motor.motor_asyncio
from config import *


async def get_prefix(bot, message):
    if not message.guild:
        return commands.when_mentioned_or(bot.DEFAULT_PREFIX)(bot, message)

    try:
        data = await bot.prefixes.find(message.guild.id)
        if not data or "prefix" not in data:
            return commands.when_mentioned_or(bot.DEFAULT_PREFIX)(bot, message)
        return commands.when_mentioned_or(data["prefix"])(bot, message)
    except:
        return commands.when_mentioned_or(bot.DEFAULT_PREFIX)(bot, message)


class Bot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(command_prefix=get_prefix, intents=intents)

    async def setup_hook(self):
        await self.tree.sync()
        print(f"Synced slash commands for {self.user}.")


bot = Bot()
bot.DEFAULT_PREFIX = "!"


@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.dnd,
        activity=discord.Activity(type=discord.ActivityType.listening, name="!help"),
    )
    print(
        f"------------------------\nLogged in as {bot.user}\n------------------------"
    )


@bot.event
async def on_guild_join(ctx, guild):
    await ctx.send(
        f"Hello! My name is YAMPB(yet another multipurpose bot). I support slash commands and prefixed commands. Learn about my commands by using {prefix}help or /help."
    )
    print(f"{bot.user} just joined {guild.id}")


@bot.hybrid_command(
    name="prefix",
    with_app_command=True,
    description="Replies with prefix",
)
async def prefix(ctx: commands.Context):
    prefix = await bot.prefixes.find(ctx.guild.id)
    if prefix is None:
        await ctx.reply(f"The server prefix is {bot.DEFAULT_PREFIX}")
    else:
        await ctx.reply(f'The server prefix is {prefix["prefix"]}')


@bot.hybrid_command(
    name="changeprefix",
    with_app_command=True,
    description="Changes server prefix (manage guild required)",
)
@commands.has_guild_permissions(manage_guild=True)
async def changeprefix(ctx: commands.Context, prefix=None):
    if prefix is None:
        return await ctx.reply("A prefix is required!")

    data = await bot.prefixes.find(ctx.guild.id)
    if data is None or "prefix" not in data:
        data = {"_id": ctx.guild.id, "prefix": prefix}
    data["prefix"] = prefix
    await bot.prefixes.upsert(data)
    await ctx.reply(f"I have changed the server's prefix to {prefix}")


@bot.hybrid_command(
    name="ping", with_app_command=True, description="Replies with client latency"
)
async def ping(ctx: commands.Context):
    latency = round(bot.latency, 5)
    await ctx.defer(ephemeral=True)
    await ctx.reply(f"Pong! The client latency is {latency} :ping_pong:")


@bot.hybrid_command(
    name="activedev",
    with_app_command=True,
    description="Use this for active dev badge",
    pass_context=True,
)
##@app_commands.guilds(discord.Object(id = 942802471615606895))
@commands.is_owner()
async def ActiveDev(
    ctx: commands.Context,
):
    await ctx.reply(
        "\n".join(
            [
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
            ]
        ),
        ephemeral=False,
    )


@bot.hybrid_command(
    name="rockpaperscissors",
    with_app_command=True,
    description="Play rock paper scissors with me!",
    pass_context=True,
)
##@app_commands.guilds(discord.Object(id = 942802471615606895))
async def RockPaperScissors(ctx: commands.Context, choice: str):
    RockPaperScissorRandom = random.randint(1, 3)
    if RockPaperScissorRandom == 1:
        RockPaperScissorBotChoice = "rock"
    elif RockPaperScissorRandom == 2:
        RockPaperScissorBotChoice = "paper"
    elif RockPaperScissorRandom == 3:
        RockPaperScissorBotChoice = "scissor"
    if RockPaperScissorBotChoice == choice:
        await ctx.reply(f"Draw! I chose {choice}, try again.")
    else:
        if (RockPaperScissorBotChoice == "rock") and (choice == "paper"):
            await ctx.reply(
                f"I choose {RockPaperScissorBotChoice}, gg you win <a:8922_Letter_W:945766211436818525>!"
            )
        elif (RockPaperScissorBotChoice == "rock") and (choice == "scissor"):
            await ctx.reply(
                f"I choose {RockPaperScissorBotChoice}, you lose <a:6141_Letter_L:945766211520708738>"
            )
        elif (RockPaperScissorBotChoice == "paper") and (choice == "scissor"):
            await ctx.reply(
                f"I choose {RockPaperScissorBotChoice}, gg you win <a:8922_Letter_W:945766211436818525>!"
            )
        elif (RockPaperScissorBotChoice == "paper") and (choice == "rock"):
            await ctx.reply(
                f"I choose {RockPaperScissorBotChoice}, you lose <a:6141_Letter_L:945766211520708738>"
            )
        elif (RockPaperScissorBotChoice == "scissor") and (choice == "paper"):
            await ctx.reply(
                f"I choose {RockPaperScissorBotChoice}, you lose <a:6141_Letter_L:945766211520708738>"
            )
        elif (RockPaperScissorBotChoice == "scissor") and (choice == "rock"):
            await ctx.reply(
                f"I choose {RockPaperScissorBotChoice}, gg you win <a:8922_Letter_W:945766211436818525>!"
            )


@RockPaperScissors.autocomplete("choice")
async def RockPaperScissors_autocompletion(
    ctx: commands.Context, current: str
) -> typing.List[app_commands.Choice[str]]:
    data = []
    for choice in ["rock", "paper", "scissor"]:
        if current.lower() in choice.lower():
            data.append(app_commands.Choice(name=choice, value=choice))
    return data


@bot.hybrid_command(name="kick", with_app_command=True, description="Kick a user")
@has_permissions(administrator=True, kick_members=True)
async def kick(ctx: commands.Context, member: discord.Member, *, reason=None):
    if reason == None:
        reason = f"No reason was provided"
    await ctx.guild.kick(member, reason=reason)
    await ctx.defer(ephemeral=True)
    await ctx.reply(f"User {member.mention} has been kicked", delete_after=5)


@kick.error
async def kickerror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.defer(ephemeral=True)
        await ctx.reply(
            "You need Kick Members or Administrator permission to use this command!"
        )
    else:
        await ctx.reply(
            "I can't banned this user!",
            ephemeral=True,
        )


@bot.hybrid_command(name="ban", with_app_command=True, description="Ban a user")
@has_permissions(ban_members=True, administrator=True)
async def ban(ctx: commands.Context, member: discord.Member, *, reason=None):
    if reason == None:
        reason = f"No reason was provided"
    await ctx.guild.ban(member, reason=reason)
    await ctx.defer(ephemeral=True)
    await ctx.reply(f"User {member.mention} has been banned", delete_after=5)


@ban.error
async def banerror(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.defer(ephemeral=True)
        await ctx.reply(
            "You need Ban Members or Administrator permission to use this command!"
        )
    else:
        await ctx.reply(
            "I can't banned this user!",
            ephemeral=True,
        )


@bot.hybrid_command(
    name="banlist", with_app_command=True, description="See a list of banned users"
)
@commands.has_permissions(ban_members=True, administrator=True)
async def banlist(ctx: commands.Context):
    bannedlistdescription = []
    async for entry in ctx.guild.bans():
        bannedlistdescription.append(
            f"**Banned User:**\n{entry.user.mention} ({entry.user.id})\n\n**Reason for Ban:**\n{entry.reason}\n\n"
        )
        print(entry.user, entry.reason)
    bannedlist = discord.Embed(
        title="Banned Users!",
        description=f"{''.join(bannedlistdescription)}",
    )
    await ctx.defer(ephemeral=True)
    await ctx.reply(embed=bannedlist)


@bot.hybrid_command(name="unban", with_app_command=True, description="Unban a user")
@commands.has_permissions(ban_members=True, administrator=True)
async def unban(ctx: commands.Context, id, reason=None):
    user = await bot.fetch_user(id)
    await ctx.guild.unban(user)
    await ctx.defer(ephemeral=True)
    if reason == None:
        reason = "No reason was provided"
    await ctx.reply(f"{user.mention} was unbanned")
    link = await ctx.channel.create_invite(
        reason=f"Sent to unbanned user {user}", max_uses=1
    )
    unbannedInvite = discord.Embed(
        title=f"You have been unbanned from {ctx.message.guild.name} (id: {ctx.message.guild.id})!",
        description=f"Click [here]({link}) to join back.\n\n**Reason**\n{reason}\n**Action by**\n{ctx.author}",
    )
    await user.send(embed=unbannedInvite)


@bot.hybrid_group(fallback="get")
async def helps(ctx, name):
    user = await bot.fetch_user(ctx.author.id)
    await user.send()


@helps.command()
async def moderation(ctx, name):
    await ctx.reply(f"Created tag: {name}")


if __name__ == "__main__":
    bot.mongo = motor.motor_asyncio.AsyncIOMotorClient(mongo_url)
    bot.db = bot.mongo[db_name]
    bot.prefixes = discordmongo.Mongo(connection_url=bot.db, dbname=collection_name)

bot.run(token)
