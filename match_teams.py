# match team against another team but never against itself.
def match_teams(teams):
    print('Home Team <== Vs ==> Away Team')
    for home_team in teams:
        for away_team in teams:
            if home_team != away_team:
                print(home_team, '<== vs ==>',away_team)
            else:
                continue
            
match_teams(['Lions','Black-Star','Dragons', 'Wolves', 'Pandas', 'Unicorns','Black4Real'])
