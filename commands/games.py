import requests, discord, os
from datetime import time, datetime

#email: ""
#password: ""
#recaptchaToken: ""


def get_games():

    #games_list = ['Basketball', 'Ice Hockey', 'Baseball', 'Esports']
    auth_token = os.environ.get('AUTH_TOKEN')
    headers = {'Authorization': auth_token}

    response = requests.get(
        'https://api-production.gambitrewards.com/api/v1/matches/', headers=headers)

    match_ids = {}
    for match in response.json()['items']:
        match_ids[match['id']] = match['name']

    if not match_ids:
        #return discord.Embed(description='No current games.', color=242424)
        return 'No current games.'

    """field_length = ''
    embed = discord.Embed(title='Games '+ str(datetime.now().date()), color=242424)
    for id in match_ids:
        if len(field_length) < 4096:
            embed.add_field(name='\u200b', value='[{}](https://app.gambitrewards.com/match/{})'.format(match_ids[id], id), inline=False)
            field_length += str(embed.fields)
        else:

    #webhook = discord.SyncWebhook.partial(id, 'token')
    #webhook.send(embed=embed)
    
    return embed"""
    games_str = ''
    games_list = []
    for id in match_ids:
        s = 'https://app.gambitrewards.com/match/{} - {}\n'.format(id, match_ids[id])
        if len(games_str)+len(s) < 2000:
            games_str += s
        else:
            games_list.append(games_str)
            games_str = s

    if not games_list:
        games_list.append(games_str)

    print(games_list)
    return games_list

#get_games()
