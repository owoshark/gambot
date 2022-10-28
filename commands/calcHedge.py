import requests
import discord
import os


def calcHedge(odds1, odds2, tokens):
    x = tokens / (1+odds1/odds2)
    y = tokens / (1+odds2/odds1)
    profit = (odds1*x - tokens*.95) / (tokens*.95)
    embed = discord.Embed(color=242424)
    embed.add_field(name='Odds 1', value=str(odds1))
    embed.add_field(name='Odds 2', value=str(odds2))
    embed.add_field(name='Profit', value=format(profit, '.2%'))
    embed.add_field(name='Bet 1', value=str(round(x)))
    embed.add_field(name='Bet 2', value=str(round(y)))
    embed.add_field(name='Tokens', value=tokens)
    return embed
