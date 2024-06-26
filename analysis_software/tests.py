import pandas as pd
from utils_functions import *
import numpy
import random

#TODO
#tests improvment and organization


# Example usage:
first_cell_value = "Example Table"
column_names = ["Column A", "Column B", "Column C"]
row_names = ["Row 1", "Row 2", "Row 3"]
table_data = [
    {"Column A": "Value A1", "Column B": "Value B1", "Column C": "Value C1"},
    {"Column A": "Value A2", "Column B": "Value B2", "Column C": "Value C2"},
    {"Column A": "Value A3", "Column B": "Value B3", "Column C": "Value C3"}
]


export_table_to_excel(first_cell_value, column_names, row_names, table_data)

#working with data frame
raw_data = {
            'a': [42, 39, 86],
            'b': [52, 41, 79],
            'c': [62, 37, 84]
            }
df = pd.DataFrame(raw_data,
                  index=pd.Index(['metric_a', 'metric_b', 'metric_c']),
                  columns=pd.Index(['a', 'b', 'c'], name='aaa'))

print(df)

d = {(1, 3): 30,
     (4, 6): 70,
     (7, 9): 100}
generate_number_by_dictionary_dist(d)


# Example usage
dict1 = {'A': 1, 'B': 2}
dict2 = {'AA': 11, 'BB': 22}
dict3 = {'AAA': 1, 'BBBB': 222}

data = [dict1, dict2, dict3]

export_to_excel_financial_analysis(data)
