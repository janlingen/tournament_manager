import tournament_manager as t

number_of_teams = t.get_number_of_teams()
teams = t.create_teams(number_of_teams)
games_played = t.get_number_games_played(number_of_teams)
t.set_team_wins(teams, games_played)
t.generate_game_plan(teams, "first")
