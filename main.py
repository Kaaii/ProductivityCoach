import discord
from discord.ext import commands
import asyncio

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')


bot.run('NDA0Mzk2ODAxMzY2NDI1NjAw.DUVPeA.gLHVx50KQ8_diEIWNfncUt7ebCw')
