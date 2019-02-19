import urllib
import json

soccer_league = 'uefa-champions-league' #'england-premier-league'
soccer_url = 'https://www.bovada.lv/services/sports/event/v2/events/A/description/soccer/' + soccer_league + '?marketFilterId=def&preMatchOnly=true&lang=en'
file_handler = urllib.urlopen(soccer_url)
content = file_handler.read()
json_content = json.loads(content)
required_content = json_content[0]
all_bets_list = []
for event in required_content['events']:
    temp_bet_info  = {}
    temp_bet_info['title'] = event['description']
    outcomes = event['displayGroups'][0]['markets'][1]['outcomes']
    temp_bet_info['team_1'] = outcomes[0]['description']
    temp_bet_info['team_2'] = outcomes[1]['description']
    temp_bet_info['win_odds_team_1'] = outcomes[0]['price']['american']
    temp_bet_info['win_odds_team_2'] = outcomes[1]['price']['american']
    temp_bet_info['draw_odds'] = outcomes[2]['price']['american']
    print (temp_bet_info)
    all_bets_list.append(temp_bet_info)




