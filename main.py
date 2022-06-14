import commands.gambit as gambit
import discord, os
from json.decoder import JSONDecodeError
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for !help'))

@bot.command()
async def gp(ctx, tokens=None):
    try:
        isinstance(int(tokens), int)
        await ctx.send(embed=gambit.profit(int(tokens)))
    except JSONDecodeError as e:
        print(e)
        await ctx.send("Token expired. <@191787373292421120>")
    except TypeError as e:
        print(e)
        await ctx.send("Proper usage: !gp #OfTokens")     
    except ValueError as e:
        print(e)
        await ctx.send("Proper usage: !gp #OfTokens")
    except Exception as e:
        print(e)
        await ctx.send("An error occurred: {}\nContact the developer.".format(e))

@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title='Gambot Commands', description='!gp tokens'))

bot.run(os.environ.get('BOT_TOKEN'))