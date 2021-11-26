from riotwatcher import LolWatcher, ApiError
import pandas as pd
import csv

def get_information(my_matches, watcher, start, end, filename):
    participants = []
    # fetch last match detail
    for i in my_matches[start: end]:
        try:
            match_detail = watcher.match.by_id(region='EUROPE', match_id = i)
            participants_row = {}
            # generate match information
            participants_row['gameId'] = match_detail['info']['gameId']
            participants_row['gameDuration'] = match_detail['info']['gameDuration']
            participants_row['gameVersion'] = match_detail['info']['gameVersion']
            participants_row['platformId'] = match_detail['info']['platformId']
            participants_row['season'] = match_detail['info']['mapId']
            # essential resources information
            if match_detail['info']['teams'][0]['win'] == True:
                participants_row['winner'] = 1
            else:
                participants_row['winner'] = 2

            # the first baron
            if match_detail['info']['teams'][0]['objectives']['baron']['first'] == True:
                participants_row['1st_baron'] = 1
            elif match_detail['info']['teams'][1]['objectives']['baron']['first'] == True:
                participants_row['1st_baron'] = 2
            else:
                participants_row['1st_baron'] = 0

            # the first dragon    
            if match_detail['info']['teams'][0]['objectives']['dragon']['first'] == True:
                participants_row['1st_dragon'] = 1
            elif match_detail['info']['teams'][1]['objectives']['dragon']['first'] == True:
                participants_row['1st_dragon'] = 2
            else:
                participants_row['1st_dragon'] = 0

            # the first inhibitor
            if match_detail['info']['teams'][0]['objectives']['inhibitor']['first'] == True:
                participants_row['1st_inhibitor'] = 1
            elif match_detail['info']['teams'][1]['objectives']['inhibitor']['first'] == True:
                participants_row['1st_inhibitor'] = 2
            else:
                participants_row['1st_inhibitor'] = 0

            # the first riftHerald 
            if match_detail['info']['teams'][0]['objectives']['riftHerald']['first'] == True:
                participants_row['1st_riftHerald'] = 1
            elif match_detail['info']['teams'][1]['objectives']['riftHerald']['first'] == True:
                participants_row['1st_riftHerald'] = 2
            else:
                participants_row['1st_riftHerald'] = 0

            # the first tower   
            if match_detail['info']['teams'][0]['objectives']['tower']['first'] == True:
                participants_row['1st_tower'] = 1
            elif match_detail['info']['teams'][1]['objectives']['tower']['first'] == True:
                participants_row['1st_tower'] = 2
            else:
                participants_row['1st_tower'] = 0

            # Team 1 information
            participants_row['t1_baron_kills'] = match_detail['info']['teams'][0]['objectives']['baron']['kills'] 
            participants_row['t1_champ_kills'] = match_detail['info']['teams'][0]['objectives']['champion']['kills'] 
            participants_row['t1_dragon_kills'] = match_detail['info']['teams'][0]['objectives']['dragon']['kills'] 
            participants_row['t1_inhibitor_kills'] = match_detail['info']['teams'][0]['objectives']['inhibitor']['kills']
            participants_row['t1_riftHerald_kills'] = match_detail['info']['teams'][0]['objectives']['riftHerald']['kills'] 
            participants_row['t1_tower_kills'] = match_detail['info']['teams'][0]['objectives']['tower']['kills'] 
            
            participants_row['t1_team_assists'] = match_detail['info']['participants'][0]['assists'] + match_detail['info']['participants'][1]['assists'] + match_detail['info']['participants'][2]['assists'] + match_detail['info']['participants'][3]['assists'] + match_detail['info']['participants'][4]['assists']
            participants_row['t1_team_gold_earn'] = match_detail['info']['participants'][0]['goldEarned'] + match_detail['info']['participants'][1]['goldEarned'] + match_detail['info']['participants'][2]['goldEarned'] + match_detail['info']['participants'][3]['goldEarned'] + match_detail['info']['participants'][4]['goldEarned']
            participants_row['t1_team_gold_spen'] = match_detail['info']['participants'][0]['goldSpent'] + match_detail['info']['participants'][1]['goldSpent'] + match_detail['info']['participants'][2]['goldSpent'] + match_detail['info']['participants'][3]['goldSpent'] + match_detail['info']['participants'][4]['goldSpent']
            
            if match_detail['info']['teams'][1]['objectives']['champion']['kills'] != 0:
                participants_row['t1_team_kda'] = (participants_row['t1_champ_kills'] + participants_row['t1_team_assists']) / match_detail['info']['teams'][1]['objectives']['champion']['kills']
            else:
                participants_row['t1_team_kda'] = participants_row['t1_champ_kills'] + participants_row['t1_team_assists']        


            # Team 2 information
            participants_row['t2_baron_kills'] = match_detail['info']['teams'][1]['objectives']['baron']['kills'] 
            participants_row['t2_champ_kills'] = match_detail['info']['teams'][1]['objectives']['champion']['kills'] 
            participants_row['t2_dragon_kills'] = match_detail['info']['teams'][1]['objectives']['dragon']['kills'] 
            participants_row['t2_inhibitor_kills'] = match_detail['info']['teams'][1]['objectives']['inhibitor']['kills']
            participants_row['t2_riftHerald_kills'] = match_detail['info']['teams'][1]['objectives']['riftHerald']['kills'] 
            participants_row['t2_tower_kills'] = match_detail['info']['teams'][1]['objectives']['tower']['kills']

            participants_row['t2_team_assists'] = match_detail['info']['participants'][5]['assists'] + match_detail['info']['participants'][6]['assists'] + match_detail['info']['participants'][7]['assists'] + match_detail['info']['participants'][8]['assists'] + match_detail['info']['participants'][9]['assists']
            participants_row['t2_team_gold_earn'] = match_detail['info']['participants'][5]['goldEarned'] + match_detail['info']['participants'][6]['goldEarned'] + match_detail['info']['participants'][7]['goldEarned'] + match_detail['info']['participants'][8]['goldEarned'] + match_detail['info']['participants'][9]['goldEarned']
            participants_row['t2_team_gold_spen'] = match_detail['info']['participants'][5]['goldSpent'] + match_detail['info']['participants'][6]['goldSpent'] + match_detail['info']['participants'][7]['goldSpent'] + match_detail['info']['participants'][8]['goldSpent'] + match_detail['info']['participants'][9]['goldSpent']

            if match_detail['info']['teams'][0]['objectives']['champion']['kills'] != 0:
                participants_row['t2_team_kda'] = (participants_row['t2_champ_kills'] + participants_row['t2_team_assists']) / match_detail['info']['teams'][0]['objectives']['champion']['kills']
            else:
                participants_row['t2_team_kda'] = participants_row['t2_champ_kills'] + participants_row['t2_team_assists'] 

            participants.append(participants_row)

        except Exception as e:
            pass
        
        continue
    df = pd.DataFrame(participants)
    df.to_csv(filename)
    
    return df   
