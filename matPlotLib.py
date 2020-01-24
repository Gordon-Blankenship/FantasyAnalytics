import pandas as pd
from matplotlib import pyplot as plt
import csv

currentWeek = 5
week = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
scores = [145, 142, 186, 163, 123, 154, 123, 124, 152, 125, 124, 124, 162]
teamNum = 0

teams = open('Teams.csv')
teamsReader = pd.read_csv('Teams.csv')

names = teamsReader.__getattr__('Team Name:')

noShows = teamsReader[names == 'NoShows']
struggle = teamsReader[names == 'Struggle Bus']
leapers = teamsReader[names == 'Leambeau Leapers']
wurst = teamsReader[names == 'Wurst on the Field']
luv = teamsReader[names == 'Luv the Pack']
wookies = teamsReader[names == 'Wilshire Wookies']
titleTown = teamsReader[names == 'TitleTown USA']
lions = teamsReader[names == 'Fitchburg Lionstars']
line = teamsReader[names == 'WI Large_Line']
bobRoss = teamsReader[names == 'Iowa Happy Trees']

allTeams = [noShows, struggle, leapers, wurst, luv,
            wookies, titleTown, lions, line, bobRoss]

plt.plot(week, scores)
plt.show()