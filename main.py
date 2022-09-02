import commands.gambit as gambit
import commands.games as games
import discord, os, asyncio
from datetime import time, datetime
from json.decoder import JSONDecodeError
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name='for !help'))
bot.remove_command('help')

async def main():
    async with bot:
        send_games.start()
        await bot.start(os.environ.get('BOT_TOKEN'))

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
async def list(ctx):
    if (ctx.author.id == 191787373292421120):
        try:
            await ctx.send(embed=games.get_games())
            await ctx.message.delete(delay=1.0)
        except JSONDecodeError as e:
            print(e)
            await ctx.send("Token expired. <@191787373292421120>")
        except Exception as e:
            print(e)
            await ctx.send("An error occurred: {}\nContact the developer.".format(e))

@bot.command()
async def help(ctx):
    await ctx.send(embed=discord.Embed(title='Gambot Commands', description='!gp tokens'))

t = time(14, 45, 0) #UTC to 745AM PST
@tasks.loop(time=t)
async def send_games():
    channel = bot.get_channel(1005585267345854636)
    await channel.send(games.get_games())

@send_games.before_loop
async def before_send_games():
    await bot.wait_until_ready()

asyncio.run(main())
