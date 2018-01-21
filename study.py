import discord
import asyncio
from discord.ext import commands
import time

"""
Study session timing using the traditional Pomodoro technique.
"""
class Study:
    """
    Pomodoro timer.
    25 minute sessions with 5 minute breaks in between.
    After the fourth session, a 15 minute break is introduced.
    """
    def __init__(self, bot):
        self.bot = bot
        self.start_time = 0
        self.end_time = 0
        self.checks = 0
        self.session = 'study'

    @commands.cooldown(1, 1500, commands.BucketType.user)
    @commands.command(pass_context=True,
        description='Sets a Pomodoro timer.')
    async def timer(self):
        #Checks type of session to start
        if self.session == 'study':
            t = 1
        elif self.session == 'break':
            t = 5
        elif self.session == 'long break':
            t = 15
        else: #Ends sessions
            return None

        self.start_time = time.time()
        h = time.localtime(self.start_time).tm_hour
        m = time.localtime(self.start_time).tm_min
        if m < 10: #Convert single digit to two digit
            m = '0{}'.format(m)
        self.end_time = time.time() + t*60

        await self.bot.say("Timer has begun. You have {} minutes.".format(t))
        await self.bot.say("Current time is: {}:{} PST.".format(h,m))

        while time.time() < self.end_time:
            await asyncio.sleep(10)

        if time.time() > self.end_time and t == 1:
            self.checks += 1
            if self.checks%4 == 0:
                self.session = 'long break'
            else:
                self.session = 'break'
            h=time.localtime(time.time()).tm_hour
            m=time.localtime(time.time()).tm_min
            await self.bot.say("Time's up!")
            await self.bot.say("Type ready when you are ready for your break.")
        elif time.time() > self.end_time and t != 1:
            self.session = 'study'
            await self.bot.say("Break's over!")
            await self.bot.say("Type ready when you are ready for the next session.")

        def check(msg):
            return self.msg.content.startswith('ready')

        msg = await self.bot.wait_for_message(check = check)
        if msg.content.startswith('ready'):
            await self.timer()



    @commands.command(description='Check time remaining.')
    async def time_left(self):
        time_left = self.end_time - time.time()
        m = int(time_left/60)
        s = int(time_left%60)
        if m < 10: #Convert single digit to two digit
            m = '0{}'.format(m)
        await self.bot.say("Time remaining: {}:{} (min:sec).".format(m,s))


    @commands.command(description='Ends Pomodoro sessions.')
    async def end(self):
        await self.bot.say("Ending current session. You completed {} sessions!".format(self.checks))
        await self.timer('C')


def setup(bot):
    bot.add_cog(Study(bot))
