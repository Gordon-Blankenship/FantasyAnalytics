from matplotlib import pyplot as plt
import csv
import numpy as np


def plot_teams(current_week):
    current_week = int(current_week)

    plt.style.use('classic')

    weeks = []

    for num in range(1, current_week):
        weeks.append(num)

    teams = open('Teams.csv')
    teams_reader = csv.reader(teams)
    teams_data = list(teams_reader)

    no_shows = [float(i) for i in teams_data[1][1:current_week]]
    struggle = [float(i) for i in teams_data[2][1:current_week]]
    leapers = [float(i) for i in teams_data[3][1:current_week]]
    wurst = [float(i) for i in teams_data[4][1:current_week]]
    luv = [float(i) for i in teams_data[5][1:current_week]]
    wookies = [float(i) for i in teams_data[6][1:current_week]]
    titletown = [float(i) for i in teams_data[7][1:current_week]]
    lions = [float(i) for i in teams_data[8][1:current_week]]
    line = [float(i) for i in teams_data[9][1:current_week]]
    bob_ross = [float(i) for i in teams_data[10][1:current_week]]

    names = [no_shows, struggle, leapers, wurst, luv, wookies,
        titletown, lions, line, bob_ross]

    for i in names:
        plt.plot(weeks, i, marker='.')

    plt.title('Lambeau League 2019')
    plt.xlabel('Week #')
    plt.ylabel('Points Scored')
    plt.legend(['NoShows', 'Struggle Bus', 'Lambeau Ls', 'WurstOTF', 'Luv the Pack',
                'Wilshire Wookies', 'TitleTown', 'Lionstars', 'Large_Line', 'Happy Trees'],
                fontsize=('xx-small'))
    plt.grid(True)

    plt.show()
    teams.close()


def current_totals():
    plt.style.use('classic')

    amount_of_teams = []
    for i in range(1, 10):
        amount_of_teams.append(i)

    teams_arranged = np.arange(len(amount_of_teams))

    teams = open('Teams.csv')
    teams_reader = csv.reader(teams)
    teams_data = list(teams_reader)

    no_shows = [float(i) for i in teams_data[1][14:]]
    struggle = [float(i) for i in teams_data[2][14:]]
    leapers = [float(i) for i in teams_data[3][14:]]
    wurst = [float(i) for i in teams_data[4][14:]]
    luv = [float(i) for i in teams_data[5][14:]]
    wookies = [float(i) for i in teams_data[6][14:]]
    titletown = [float(i) for i in teams_data[7][14:]]
    lions = [float(i) for i in teams_data[8][14:]]
    line = [float(i) for i in teams_data[9][14:]]
    bob_ross = [float(i) for i in teams_data[10][14:]]

    names = [no_shows, struggle, leapers, wurst, luv, wookies,
             titletown, lions, line, bob_ross]

    team_name = 0
    for name in names:
        plt.bar(team_name, name, width=.5)
        team_name += 1

    plt.xticks(ticks=teams_arranged, labels='')
    plt.title('Lambeau League Total Points by Team')
    plt.xlabel('Teams')
    plt.ylabel('Points Scored this season')
    plt.grid(True)
    plt.legend(['NoShows', 'Struggle Bus', 'Lambeau Ls', 'WurstOTF', 'Luv the Pack',
                'Wilshire Wookies', 'TitleTown', 'Lionstars', 'Large_Line', 'Happy Trees'],
               loc='upper left', fontsize=('xx-small'))
    plt.show()