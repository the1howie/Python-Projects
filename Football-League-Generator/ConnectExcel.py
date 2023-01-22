#!/usr/bin/env python3

"""
Author: 
    Aurel Nicolae

Purpose:
    Defines the ConnectExcel class's methods.

Requires: 
    https://pypi.org/project/xlwings/ - pip install xlwings
    
"""

import xlwings as xw
import pandas as pd
# from typing import TypeVar
# DataFrameStr = TypeVar("pandas.core.frame.DataFrame(str)")


class ConnectExcel:
    
    def __init__(self, data_frame: pd.DataFrame):
        self.data = data_frame
    
    def view_results_in_excel(self):
        xw.view(self.data)
    
    def write_curent_scores_to_excel(self):
        pass
    
    def read_input_scores_from_excel(self):
        pass


if __name__ == "__main__":
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Running file {os.path.basename(__file__)}")
    print()
