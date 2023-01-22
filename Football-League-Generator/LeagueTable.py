#!/usr/bin/env python3

"""
Author: 
    Aurel Nicolae

Purpose:
    Defines the LeagueTable class's methods.
"""

import pandas as pd
from MatchSchedule import *
from KeepScore import *
import matplotlib.pyplot as plt


class LeagueTable:
    
    TABLE_FIELD_NAMES = ['MP', 'W', 'D', 'L', 'GF', 'GA', 'GD', 'Pts']
    
    def __init__(self, match_scores: KeepScore):
        self.match_scores = match_scores
        self.league = pd.DataFrame(sorted(self.match_scores.schedule.original_teams), columns=['Team'])
        for field in LeagueTable.TABLE_FIELD_NAMES:
            self.league[field] = 0
    
    def reset_table(self):
        for col in range(1, len(self.league.columns)):
            self.league.iloc[:, col] = 0
    
    def update_table(self):
        self.reset_table() # NB
        
        for i in range(self.match_scores.scores.shape[0]):
            if not all(score is None for score in self.match_scores.scores.loc[i, ["host_score", "guest_score"]]):
                host_team = str(self.match_scores.scores.at[i, "host_team"])
                host_score = int(self.match_scores.scores.at[i, "host_score"])
                guest_team = str(self.match_scores.scores.at[i, "guest_team"])
                guest_score = int(self.match_scores.scores.at[i, "guest_score"])
                
                host_id = int(self.league.loc[self.league['Team'] == host_team].index.values[0])
                guest_id = int(self.league.loc[self.league['Team'] == guest_team].index.values[0])
                            
                self.league.at[host_id, 'MP'] += 1
                self.league.at[guest_id, 'MP'] += 1
                
                self.league.at[host_id, 'GF'] += host_score
                self.league.at[host_id, 'GA'] += guest_score
                self.league.at[host_id, 'GD'] += host_score - guest_score
                
                self.league.at[guest_id, 'GF'] += guest_score
                self.league.at[guest_id, 'GA'] += host_score
                self.league.at[guest_id, 'GD'] += guest_score - host_score 
                
                if host_score > guest_score:
                    self.league.at[host_id, 'W'] += 1
                    self.league.at[guest_id, 'L'] += 1
                    self.league.at[host_id, 'Pts'] += 3
                elif host_score < guest_score:
                    self.league.at[guest_id, 'W'] += 1
                    self.league.at[host_id, 'L'] += 1
                    self.league.at[guest_id, 'Pts'] += 3
                else:
                    self.league.at[host_id, 'D'] += 1
                    self.league.at[guest_id, 'D'] += 1
                    self.league.at[host_id, 'Pts'] += 1
                    self.league.at[guest_id, 'Pts'] += 1

    def sort_table(self):
        self.league.sort_values(by=['Pts', 'GD', 'W', 'D', 'GF', 'GA'], 
                                ascending=[False, False, False, False, False, False], inplace=True)
        self.league.reset_index(drop=True, inplace=True)

    def plot_wins_draw_losses(self):
        ax = self.league.plot.barh(x="Team", y=["W", "D", "L"], stacked=True, color=["g", "k", "r"], rot=0)
        ax.legend(loc="center right", bbox_to_anchor=(1.2, 0.5))
        ax.invert_yaxis()
        plt.title("Wins / Draws / Losses")
        plt.show()
        return ax


if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Running file {os.path.basename(__file__)}")
    print()
