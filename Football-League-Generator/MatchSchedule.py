#!/usr/bin/env python3

"""
Author: 
    Aurel Nicolae

Purpose:
    Defines the MatchSchedule class's methods.
"""

import copy
import random
from typing import List


class MatchSchedule:
    
    SCHED_HEADERS = ['event', 'match', 'host_team', 'guest_team']
    # GOAL_LIMIT = 11
    
    def __init__(self, teams_list: List):
        self.teams = teams_list
        self.original_teams = copy.deepcopy(self.teams)
        if len(self.teams) % 2 != 0:
            self.teams.append('_dummy')
            self.addedDummy = True
        else:
            self.addedDummy = False
        random.shuffle(self.teams)
        self.schedule = []
        self.flat_schedule = []
        # self.scores = None

    def circ_shift(self):
        first_team = self.teams.pop(0)
        self.teams.append(first_team)
    
    def circ_shift_fix_first(self):
        second_team = self.teams.pop(1)
        self.teams.append(second_team)
    
    def create_event(self):
        L = len(self.teams) # Length
        H = L // 2 # Half way
        return [[self.teams[i], self.teams[(L - 1) - i]] for i in range(H) 
                if '_dummy' not in [self.teams[i], self.teams[(L - 1) - i]]]
    
    def create_schedule(self):
        for _ in range(len(self.teams) - 1):
            event = self.create_event()
            self.schedule.append(event)
            self.circ_shift_fix_first()
    
    def mirror_schedule(self):
        mirror_sched = []
        for event in self.schedule:
            mirror_event = []
            for match in event:
                mirror_event.append([match[1], match[0]])
            mirror_sched.append(mirror_event)      
        self.schedule += mirror_sched
    
    def print_schedule(self):
        for event in self.schedule:
            for match in event:
                print(f"{match[0]} vs {match[1]}")
        
    def flatten_schedule(self):
        event_num = 0
        match_num = 0
        for event in self.schedule:
            event_num += 1
            for match in event:
                match_num += 1
                self.flat_schedule.append([event_num, match_num, *match])


if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Running file {os.path.basename(__file__)}")
    print()
