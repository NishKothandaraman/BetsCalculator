import urllib
import json
import pprint
import parlay_calculator as parlay_calc

soccer_league = 'england-premier-league' #uefa-champions-league' #'england-premier-league'
soccer_url = 'https://www.bovada.lv/services/sports/event/v2/events/A/description/soccer/' + soccer_league + '?marketFilterId=def&preMatchOnly=true&lang=en'
file_handler = urllib.urlopen(soccer_url)
content = file_handler.read()
json_content = json.loads(content)
required_content = json_content[0]
all_bets_list = []
for event in required_content['events']:
    temp_bet_info  = {}
    outcomes = event['displayGroups'][0]['markets'][1]['outcomes']
    temp_bet_info['teams'] = []
    temp_bet_info['teams'].append(outcomes[0]['description'])
    temp_bet_info['teams'].append(outcomes[1]['description'])
    temp_bet_info['teams'].append(event['description'])
    temp_bet_info['odds'] = []
    # Pre process EVEN to 100
    if (outcomes[0]['price']['american'] == 'EVEN'):
        outcomes[0]['price']['american'] = '+100'
    if (outcomes[1]['price']['american'] == 'EVEN'):
        outcomes[1]['price']['american'] = '+100'
    if (outcomes[2]['price']['american'] == 'EVEN'):
        outcomes[2]['price']['american'] = '+100'
    temp_bet_info['odds'].append(outcomes[0]['price']['american'])
    temp_bet_info['odds'].append(outcomes[1]['price']['american'])
    temp_bet_info['odds'].append(outcomes[2]['price']['american'])
    temp_bet_info['result'] = []
    temp_bet_info['result'].append('Win')
    temp_bet_info['result'].append('Win')
    temp_bet_info['result'].append('Draw')
    #print (temp_bet_info)
    all_bets_list.append(temp_bet_info)

# change from '3' matches to n matches
print_result = parlay_calc.parlay_calculator(all_bets_list[:3])
pp = pprint.PrettyPrinter(indent=4)
