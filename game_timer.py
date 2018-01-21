import discord
import asyncio
from discord.ext import commands
import time

"""
Watches user entering a game using the status change in Discord.
Alerts the user every hour of the time.
After 2 hours warns user to stop playing.
After 3 hours begins penalizing the user every 10 minutes with point deducations.
"""
class GameTimer:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'playtime')
    async def playtime(self, ctx):
        ptime = 0
        await bot.say("You've been playing for: {}.".format(ptime))

def setup(bot):
    bot.add_cog(GameTimer(bot))
