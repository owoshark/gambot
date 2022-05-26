import commands.gambit as gambit
import discord
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for !help'))


@bot.command()
async def gp(ctx, tokens=None):
    if not tokens:
        await ctx.send("Proper usage: !gp tokens")
    else:
        await ctx.send(embed=gambit.profit(tokens))


@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title='Gambot Commands', description='!gp tokens'))

bot.run(os.environ.get('BOT_TOKEN'))
