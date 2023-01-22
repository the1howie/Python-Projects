#!/usr/bin/env python3

"""
Author: 
    Aurel Nicolae

Purpose:
    Defines the FilterMatches class's methods.
    Provides the ability to filter by one team and report statistics for the selected team.
"""

# import copy
# import random
import pandas as pd
# import numpy as np
# import xlwings as xw
import ipywidgets as widget
# from typing import List
from MatchSchedule import *
from KeepScore import *
from LeagueTable import *
import matplotlib.pyplot as plt


class FilterMatches:
    
    def __init__(self, match_scores: KeepScore, match_schedule: MatchSchedule):
        self.match_scores = match_scores
        self.match_schedule = match_schedule
        self.selected_team = ""

    @staticmethod
    def color_result(val):
        return f'background-color: red;' if val < 0 else f'background-color: green;' if val > 0 else None
    
    def get_filtered_team_matches(self, filter_on_team):
        filter_mask = (self.match_scores.scores['host_team'] == filter_on_team) | (self.match_scores.scores['guest_team'] == filter_on_team)
        filtered_matches = copy.deepcopy(self.match_scores.scores.loc[filter_mask])
        filtered_matches.reset_index(drop=True, inplace=True)
        new_col = filter_on_team + '_WDL'
        filtered_matches[new_col] = None

        for m in range(filtered_matches.shape[0]):
            if filtered_matches.at[m, 'host_team'] == filter_on_team:
                score1, score2 = 'host_score', 'guest_score'
            else:
                score1, score2  = 'guest_score', 'host_score'

            if filtered_matches.at[m, score1] > filtered_matches.at[m, score2]:
                filtered_matches.at[m, new_col] = 1 # Win
            elif filtered_matches.at[m, score1] == filtered_matches.at[m, score2]:
                filtered_matches.at[m, new_col] = 0 # Draw
            else:
                filtered_matches.at[m, new_col] = -1 # Loss
        
        return filtered_matches
    
    def get_goals_for_and_against(self, filtered_matches, filter_on_team):
        goals_for = [] # goals scores by the selected team
        goals_against = [] # goals conceeded by the selected team

        for row in range(filtered_matches.shape[0]):
            # print(filtered_matches.iloc[row,])
            if filtered_matches.at[row, 'host_team'] == filter_on_team:
                goals_for.append(filtered_matches.at[row, 'host_score'])
                goals_against.append(filtered_matches.at[row, 'guest_score'])
            else:
                goals_for.append(filtered_matches.at[row, 'guest_score'])
                goals_against.append(filtered_matches.at[row, 'host_score'])
        
        return goals_for, goals_against


if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Running file {os.path.basename(__file__)}")
    print()
