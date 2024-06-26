from numpy import *
from itertools import pairwise
import json
from urllib.request import Request, urlopen
import pandas as pd
import random


def get_data_from_api(ticker):
    req = Request(
        url='https://api.gurufocus.com/public/user/50e22a65250e1766d8807bf4b5326447:92ec970347a4143ea9d377fe833dd658/stock/'
            + ticker + '/financials',
        headers={'User-Agent': 'Mozilla/5.0'}
    )

    content = urlopen(req).read()
    data = json.loads(content.decode('utf8'))
    return data

def calc_avg(list, year):
    last_years_data = list[-year:-1]
    last_years_numbers = convert_list_of_strings_to_numbers(last_years_data)
    return average(last_years_numbers)


def get_last_year_item(list):
    return float(list[-1])


def convert_list_of_strings_to_numbers(list):
    numbers_list = []
    for e in list:
        num = float(e)
        numbers_list.append(num)
    return numbers_list

def calc_avg_growth_rate(list, year):
    last_years_data = list[-year-2:-1]
    last_years_numbers = convert_list_of_strings_to_numbers(last_years_data)
    yoy_growth = []
    for num, next_num in pairwise(last_years_numbers):
        yoy_gr = (next_num - num)/abs(num)
        yoy_growth.append(yoy_gr)
    return average(yoy_growth) * 100


def create_ttm_quarters_analysis_dict(data_list):
    data_list_numbers = convert_list_of_strings_to_numbers(data_list)
    yoy_change = ((data_list_numbers[-1] - data_list_numbers[0]) / abs(data_list_numbers[0])) * 100
    q1q2_change = ((data_list_numbers[2] - data_list_numbers[1]) / abs(data_list_numbers[1])) * 100
    q2q3_change = ((data_list_numbers[3] - data_list_numbers[2]) / abs(data_list_numbers[2])) * 100
    q3q4_change = ((data_list_numbers[4] - data_list_numbers[3]) / abs(data_list_numbers[3])) * 100

    raw_data = [yoy_change, q1q2_change, q2q3_change, q3q4_change]

    data_dict = {'year over year change': yoy_change,
                 'q1 to q2 change': q1q2_change,
                 'q2 to q3 change': q2q3_change,
                 'q3 to q4 change': q3q4_change}
    return raw_data


def export_table_to_excel(first_cell_value, column_names, row_names, table_data):
    # Create a DataFrame from the table data
    df = pd.DataFrame(table_data)

    # Create an Excel writer using pandas
    writer = pd.ExcelWriter('table_data.xlsx', engine='xlsxwriter')
    workbook = writer.book
    worksheet = workbook.add_worksheet('Sheet1')

    # Write the first cell value to the Excel file
    worksheet.write(0, 0, first_cell_value)

    # Write the column names to the Excel file
    for col_idx, col_name in enumerate(column_names):
        worksheet.write(1, col_idx+1, col_name)

    # Write the row names and table data to the Excel file
    for row_idx, row_name in enumerate(row_names):
        worksheet.write(row_idx + 2, 0, row_name)
        for col_idx, col_name in enumerate(column_names):
            worksheet.write(row_idx + 2, col_idx + 1, df.loc[row_idx, col_name])

    # Save the Excel file
    writer.save()


def export_to_excel_a(dataframe, file_path):
    dataframe.to_excel(file_path)


def export_to_excel(dataframes, file_path):
    with pd.ExcelWriter(file_path) as writer:
        for i, dataframe in enumerate(dataframes, start=1):
            dataframe.to_excel(writer, sheet_name="Sheet1", startrow=(i-1)*6)


def generate_number_by_dictionary_dist(dictionary):
    dict_items = list(dictionary.items())
    num = random.randint(0, 100)
    for item in dict_items:
        if num < item[1]:
            return random.randint(item[0][0], item[0][1])
    return 0


def export_to_excel_financial_analysis(data):
    # Concatenate the dictionaries into a single dictionary
    merged_dict = {}
    for d in data:
        merged_dict.update(d)

    # Create a DataFrame from the merged dictionary
    df = pd.DataFrame.from_dict(merged_dict, orient='index')

    # Create a Pandas Excel writer using XlsxWriter as the engine
    writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')

    # Write the DataFrame to the Excel file
    df.to_excel(writer, index=True, header=False)

    # Customize the worksheet
    workbook = writer.book
    worksheet = writer.sheets['Sheet1']

    # Save the Excel file
    writer.save()

    print("Data exported to 'data.xlsx' successfully.")
