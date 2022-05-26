import commands.gambit as gambit
import discord, os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for !help'))

@bot.command()
async def gp(ctx, tokens=None):
    try:
        if not tokens:
            await ctx.send("Proper usage: !gp tokens")
        else:
            await ctx.send(embed=gambit.profit(int(tokens)))
    except Exception as e:
        print(e)
        await ctx.send("An error occurred. Contact the developer.")

@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title='Gambot Commands', description='!gp tokens'))

bot.run(os.environ.get('BOT_TOKEN'))