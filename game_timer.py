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

#Motivational strings:
#Consider adding a list of strings of responses to prompt the user to stop playing
class GameTimer:
    """
    Messages reminders to stop playing after long periods of time.
    Use +playtime to view your current game playtime.
    Use +free to stop GameTimer reminders. (Only use this if you truly have nothing to do!)
    Use +busy to turn reminders back on.
    """
    def __init__(self, bot):
        self.bot = bot
        self.gamer = discord.User
        self.start_time = 0
        self.ptime = 0 #keeps count of playtime
        self.toggle = 'busy'

    async def on_member_update(self, before, after):
        """
        Event listener that waits for a member to change status to 'Playing.'
        Will then wait to message user reminders not to play too long.
        """

        self.gamer = after
        if after.game != None:
            await self.bot.send_message(after,"You have started playing {}".format(after.game))
            await self.bot.send_message(after,"I'll let you know when to take a break.")
        self.start_time = time.time()

        #Begins timers.
        h=0
        t=3600 #t=30 for testing (30s intervals)
        while after.game != None:
            h += 1
            if self.toggle == 'free':
                break
            await asyncio.sleep(t)
            await self.bot.send_message(after, after.mention + " You've been playing for {} hour(s).".format(h))
            if h == 1: #One hour reminder.
                await self.bot.send_message(after, after.mention + " Consider taking a break soon.")
            if h == 2: #Two hours reminder.
                await self.bot.send_message(after, after.mention + " You should give your body a rest. Don't you have things to do?")
            if h == 3: #Three hours reminder.
                await self.bot.send_message(after, after.mention + " That should be enough play time. Time to be productive!")
            if h > 3: #Past three hours
                t=600 #Change to 10 min reminders.
                await self.bot.send_message(after, after.mention + " It's been way too long! You should stop playing!")


    @commands.command(description = 'Tells user current playtime.')
    async def playtime(self):
        """
        Reports current playtime.
        """
        self.ptime = time.time() - self.start_time
        h = int(self.ptime/3600) #hours
        m = int(self.ptime/60) #minutes
        s = int((self.ptime%3600)%60) #seconds
        try:
            if self.gamer.game != None:
                await self.bot.say("You've been playing {} for: {}h {}m {}s.".
                    format(self.gamer.game,h,m,s))
            elif self.gamer.game == None:
                await self.bot.say("You haven't been playing anything for: {}h {}m {}s.".
                    format(h,m,s))
        except:
            print("No status change detected. Please restart the game.")

    @commands.command()
    async def free(self):
        """
        Lets the bot know you are free to game without reminders.
        """
        self.toggle = 'free'

    @commands.command()
    async def busy(self):
        """
        Lets the bot know you are busy again.
        """
        self.toggle = 'busy'

def setup(bot):
    bot.add_cog(GameTimer(bot))
