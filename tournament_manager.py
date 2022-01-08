from team import Team


def get_number_of_teams():
    num = 0
    while True:
        num = int(input("Enter the number of teams in the tournament: "))
        if num % 2 == 0 and num >= 2:
            break
        else:
            print("The minimum number of teams is 2, try again.")
    return num


def create_teams(number_of_teams):
    teams = []
    for i in range(number_of_teams):
        team_name = ""
        while True:
            team_name = input(f"Enter the name of team #{i+1}: ")
            if len(team_name) >= 2 and len(team_name.split()) <= 2:
                break
            elif len(team_name) >= 2:
                print("Team names must have at least 2 characters, try again.")
            else:
                print("Team names may have at most 2 words, try again.")
        teams.append(Team(team_name))
    return teams


def get_number_games_played(number_of_teams):
    games_played = 0
    while True:
        games_played = int(
            input("Enter the number of games played by each team: "))
        if games_played >= number_of_teams-1:
            break
        else:
            print("Invalid number of games. Each team plays each other at least once in the regular season, try again.")
    return games_played


def set_team_wins(teams, number_of_games):
    for team in teams:
        while True:
            team_wins = int(input(
                f"Enter the number of wins Team {team.name} had: "))
            if team_wins <= number_of_games and team_wins >= 0:
                break
            elif team_wins > number_of_games:
                print(
                    f"The maximum number of wins is {number_of_games}, try again.")
            else:
                print("The minimum number of wins is 0, try again.")


def generate_game_plan(teams, round):
    print(
        f"Generating the games to be played in the {round} of the tournament...")
    teams.sort(key=lambda x: x.wins)
    for i in range(len(teams)//2):
        print(f"Home: {teams[i].name} VS Away: {teams[-i-1].name}")


number_of_teams = get_number_of_teams()
teams = create_teams(number_of_teams)
games_played = get_number_games_played(number_of_teams)
set_team_wins(teams, games_played)
generate_game_plan(teams, "first")
