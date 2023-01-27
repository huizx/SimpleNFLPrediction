# NFL Game predictor
# Authors:  Ben Spencer and Tony Hui

TEAMS = ['Cowboys', 'Buccaneers', 'Eagles', 'Falcons', 'Steelers',
 'Bills', 'Jets', 'Panthers', 'Vikings',
  'Bengals', '49ers', 'Lions', 'Jaguars', 'Texans',
   'Seahawks', 'Colts', 'Cardinals', 'Titans',
    'Chargers', 'Commanders', 'Browns', 'Chiefs',
     'Dolphins', 'Patriots', 'Packers', 'Saints',
      'Broncos', 'Giants', 'Bears', 'Rams', 'Raiders', 'Ravens']


def checkTeam(team):
        
    for x in TEAMS:
        if (x == team):
            return True
            break
    
    print("\n")
    print("You have entered an invalid team name please restart the program and try again.")
    quit

def intro():
    print('\n')
    print("This is a program that allows the user to enter 2 teams for a ",  end = '')
    print("potential matchup and return the team that based on our algorithm we think has the higher chance of winning.")
    print('\n')
    print("Please only enter the nicknames for each NFL team. (Ex. Type Bears instead of Chicago)")
    print('\n')

def main():

    intro()

    team1 = input("Please enter the first team name that you want to test. ")
    checkTeam(team1)

    team2 = input("Please enter the second team name that you want to test. ")
    checkTeam(team2)






main()