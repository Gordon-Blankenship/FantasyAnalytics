import csv
import tkinter as tk


class Style:
    def __init__(self, name, primary, secondary, tertiary, fourth, background):
        self.name = name
        self.primary = primary
        self.secondary = secondary
        self.tertiary = tertiary
        self.fourth = fourth
        self.background = background

def change_style(team):
    name = ""
    primary = ""
    secondary = ""
    tertiary = ""
    fourth = ""
    background = ""

    if team == "ISU":
        name = "Illinois State"
        primary += "#CE1126"
        secondary += "#F9DD16"
        tertiary += "#000000"
        fourth += "#ffffff"
        background = "redbird.png"
    if team == "LA":
        name = "Rams"
        primary += "#FFCD00"
        secondary += "#002D72"
        tertiary += "#ffffff"
        fourth += "#000000"
        background = "rams.png"
    if team == "IOWA":
        name = "University of Iowa"
        primary += "#000000"
        secondary += "#FFCD00"
        tertiary += "#ffffff"
        fourth += "#000000"
        background = "hawkeye.png"
    if team == "GB":
        name = "Packers"
        primary += "#FFB612"
        secondary += "#203731"
        tertiary += "#ffffff"
        fourth += "#000000"
        background = "packers.png"

    settings_file = open('current_settings.csv', 'w+')
    override = [name, primary, secondary, tertiary, fourth, background]
    settings_writer = csv.writer(settings_file)
    settings_writer.writerow(override)
    settings_file.close()

themes = open('settings.csv')
themes_reader = csv.reader(themes)
themes_list = list(themes_reader)

settings = open('current_settings.csv')
settings_reader = csv.reader(settings)
settings_list = list(settings_reader)

current_style = Style(settings_list[0][0], settings_list[0][1], settings_list[0][2],
                settings_list[0][3], settings_list[0][4], settings_list[0][5])
