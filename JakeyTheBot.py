import discord
from discord.ext import commands
from discord.ext.commands import bot
import random
import time

bot = commands.Bot(command_prefix='#')

bot.remove_command("help")

USER_TOKEN = 'PUT THE TOKEN HERE'

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------')

@bot.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Latency is {:.2f}ms'.format(duration))
    await ctx.message.delete()

@bot.command(pass_context=True)
async def dmall(ctx, content):
    for members in bot.get_all_members():
        try:
            await members.send(content)
            await time.sleep(20)
            await ctx.message.delete()
        except:
            continue





bot.run(USER_TOKEN, bot=False)