#!/usr/bin/env python3

"""
Author: 
    Aurel Nicolae

Purpose:
    Defines the KeepScore class's methods.
"""

import random
import pandas as pd
from MatchSchedule import *


class KeepScore:
    
    GOAL_LIMIT = 11
    
    def __init__(self, schedule: MatchSchedule):
        self.schedule = schedule
        self.scores = None
        
    def config_match_scores(self):
        if not self.schedule.flat_schedule:
            self.schedule.flatten_schedule()
        self.scores = pd.DataFrame(self.schedule.flat_schedule, columns=MatchSchedule.SCHED_HEADERS)
        self.scores['host_score'] = None 
        self.scores['guest_score'] = None
    
    def keep_score(self, match, host_score, guest_score):
        try:
            self.scores.loc[self.scores["match"] == match, ["host_score", "guest_score"]] = \
                [int(host_score), int(guest_score)]
        except Exception as e:
            print(e)
    
    @classmethod
    def random_match_score(cls):
        return int(random.random() * random.randint(0, cls.GOAL_LIMIT))
    
    def generate_random_match_scores(self):
        for match in range(1, self.scores.shape[0] + 1):
            self.keep_score(match, 
                            KeepScore.random_match_score(), 
                            KeepScore.random_match_score())
    

if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Running file {os.path.basename(__file__)}")
    print()
