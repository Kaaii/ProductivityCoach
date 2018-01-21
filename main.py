import discord
from discord.ext import commands
import asyncio
import sys
import traceback

command_prefix = '+'
bot = commands.Bot(command_prefix)

extensions = ["study", "game_timer"]

if __name__ == '__main__':
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('----------')

#Raises an error to console, and messages user command is on cooldown.
@bot.event
async def on_command_error(error, ctx):
    #Cooldown error. Tells you how much time in s left on cooldown.
    if isinstance(error, commands.CommandOnCooldown):
        await bot.send_message(ctx.message.channel, content='This command is still on cooldown. (%.2fs remaining)' % error.retry_after)
    raise error

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    #DM start with user
    if bot.user.mentioned_in(message):
        await bot.send_message(message.author,
            'What would you like to do? Type +help for a list of commands.')

    #Close the bot connection completely. Remove or add permission check to avoid abrupt closures.
    if message.content.startswith('bye!') and message.author.id == '271513843555893248':
        await bot.close()



bot.run('NDA0Mzk2ODAxMzY2NDI1NjAw.DUW_Pg.hz289-r8DkwwCYN4FuyNnGfiR8U')
