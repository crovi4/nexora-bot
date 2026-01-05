from config import TOKEN
print(f"Токен: {TOKEN!r}")
print(f"Тип токена: {type(TOKEN)}")
print(f"Длина токена: {len(TOKEN)}")
import discord
from discord.ext import commands
import os
import asyncio


intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ {bot.user} запущен")
    await bot.tree.sync()

async def load_cogs():
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            try:
                await bot.load_extension(f"cogs.{file[:-3]}")
                print(f"Загружен модуль: {file}")
            except Exception as e:
                print(f"Ошибка загрузки {file}: {e}")

async def main():
    async with bot:
        await load_cogs()
        await bot.start(TOKEN)

asyncio.run(main())
