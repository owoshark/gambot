import requests, discord, os

#email: ""
#password: ""
#recaptchaToken: ""

def profit(num):

    games_list = ['Basketball', 'Ice Hockey', 'Baseball']
    auth_token = os.environ.get('AUTH_TOKEN')
    headers = {'Authorization': auth_token}

    response = requests.get(
        'https://api-production.gambitrewards.com/api/v1/matches/', headers=headers)

    #webhook = discord.Webhook.from_url('', adapter=discord.RequestsWebhookAdapter())

    match_ids = []
    for match in response.json()['items']:
        if match['sport_category']['sport']['name'] in games_list:
            match_ids.append(match['id'])

    if not match_ids:
        return discord.Embed(description='No current games.', color=242424)

    x = 0
    y = 0
    odds1 = 0
    odds2 = 0
    tokens = num
    profit = 0
    max_profit = 0
    bets1 = []
    bets2 = []
    profits = []
    profit_ids = []
    profit_names = []
    profit_odds1 = []
    profit_odds2 = []

    for id in match_ids:
        response2 = requests.get(
            'https://api-production.gambitrewards.com/api/v1/matches/' + id, headers=headers)
        for bet in response2.json()['item']['bet_types_matches']:
            if bet['bet_type']['label'] == 'Pick the Winner':
                odds1 = bet['match_lines'][0]['payout']
                odds2 = bet['match_lines'][1]['payout']
                x = tokens / (1+odds1/odds2)
                y = tokens / (1+odds2/odds1)
                profit = (odds1*x - tokens*.9) / (tokens*.9)
                if profit >= max_profit:
                    max_profit = profit
                    bets1.append(x)
                    bets2.append(y)
                    profits.append(profit)
                    profit_ids.append(id)
                    profit_names.append(response2.json()['item']['name'])
                    profit_odds1.append(odds1)
                    profit_odds2.append(odds2)

    embed = discord.Embed(title='Gambit Profit', color=242424)

    for i in reversed(range(len(profit_ids))):
        embed.add_field(
            name='Game ' + str(len(profit_ids)-i), value='[{}](https://app.gambitrewards.com/match/{})'.format(profit_names[i], profit_ids[i]), inline=False)
        embed.add_field(name='Odds 1', value=str(profit_odds1[i]))
        embed.add_field(name='Odds 2', value=str(profit_odds2[i]))
        embed.add_field(name='Profit', value=format(profits[i], '.2%'))
        embed.add_field(name='Bet 1', value=str(round(bets1[i])))
        embed.add_field(name='Bet 2', value=str(round(bets2[i])))
        embed.add_field(name='Tokens', value=tokens)

    embed.set_footer(text='Swagit donations accepted @phillter')
    #webhook.send(embed=embed, content='<@&{}>'.format('526067036145844235'))
    #print('Best hedge is '+profit_name+' at '+str(profit_odds1)+'/'+str(profit_odds2) +
    #      ' '+format(max_profit, '.2%')+'\nhttps://app.gambitrewards.com/match/'+profit_id)
    return embed

#profit(20000)