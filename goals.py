import discord
import asyncio
from discord.ext import commands
import time
import datetime

class Goals:
    """
    Allows user to create goals and their respective deadlines.
    """
    def __init__(self, bot):
        self.bot = bot
        self.user = discord.User
        self.gdict = {}
        self.next_check = 0 #time until tomorrow's check in hours

    async def check_date(self):
        """
        Checks how long in hours until tomorrow's midnight.
        Checks if date matches any on your goal list or is imminent.
        Sends a reminder.
        """
        now = time.localtime()
        self.next_check = 24 - now.tm_hour
        #print("Next check is {} hours from now.".format(self.next_check))

        #Check if today's date matches a deadline.
        m = now.tm_mon
        d = now.tm_mday
        y = now.tm_year
        date = "{}-{}-{}".format(m,d,y)
        date = datetime.datetime.strftime(datetime.datetime.strptime(date, "%m-%d-%Y"), '%m-%d-%Y')
        #print(date)

        for key in self.gdict:
            #print(key, self.gdict[key])
            if date == self.gdict[key]:
                await self.bot.send_message(self.user, self.user.mention +
                    "Reminder: {} is due!".format(key))

        await asyncio.sleep(self.next_check*3600)
        await self.check_date()

    @commands.group(pass_context=True)
    async def goal(self,ctx):
        """
        Requires a subcommand: [add] or [remove].
        """
        self.user = ctx.message.author
        if ctx.invoked_subcommand is None:
            await self.bot.say("Please specify the subcommand (add or remove).")

    @goal.command(pass_context=True)
    async def add(self,ctx):
        """
        Adds a goal to the goal list.
        Ex: +goal add "Do Something". Prompts for deadline in MM-DD-YYYY format.
        """
        gl = ctx.message.content[len('+goal add'):].strip()
        await self.bot.say("Please enter a deadline in MM-DD-YYYY format.")
        msg = await self.bot.wait_for_message(author = ctx.message.author)
        deadline = msg.content
        try:
            deadline = datetime.datetime.strftime(
                datetime.datetime.strptime(deadline, '%m-%d-%Y'), '%m-%d-%Y')
            self.gdict.update({gl:deadline})
            await self.bot.say("Goal added: {} due {}.".format(gl,deadline))
        except ValueError:
            await self.bot.say("Invalid input, please try adding the goal again.")
        finally:
            await self.check_date()
    @goal.command(pass_context=True)
    async def remove(self, ctx):
        """
        Removes an existing goal from the list.
        """
        gl = ctx.message.content[len('+goal remove'):].strip()
        try:
            del self.gdict[gl]
            await self.bot.say("Goal has been removed.")
        except KeyError:
            await self.bot.say("That goal wasn't found, try again.")


    @commands.command(pass_context=True)
    async def todo(self,ctx):
        """
        Shows current list of set goals.
        """
        await self.bot.say("These are your goals: ")
        for g in self.gdict:
            await self.bot.say("- {} due {}.".format(g, self.gdict[g]))


def setup(bot):
    bot.add_cog(Goals(bot))
