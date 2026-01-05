import discord
from discord.ext import commands
from discord import app_commands
import time

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="ping", description="Проверка задержки Nexora Bot")
    async def ping(self, interaction: discord.Interaction):
        start = time.perf_counter()
        await interaction.response.defer()
        end = time.perf_counter()

        embed = discord.Embed(
            title="🟦 Nexora Ping",
            color=0x2F80ED
        )
        embed.add_field(
            name="🟢 Bot latency",
            value=f"`{round((end - start) * 1000)} ms`",
            inline=True
        )
        embed.add_field(
            name="🟣 API latency",
            value=f"`{round(self.bot.latency * 1000)} ms`",
            inline=True
        )
        embed.set_footer(text="Nexora Labs")

        await interaction.followup.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Ping(bot))
