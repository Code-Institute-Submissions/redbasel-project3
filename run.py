# we need gspread in order to access the sheet.
import gspread
from google.oauth2.service_account import Credentials
# the scope says which apis can be utilized
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
# pointing python to which sheet file we want to access.
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('p3clients')

# import google sheets
# import math
# formulas for BMI and percentage change
# check value of bmi and rate it in differnt category.
# Testing that python is fetching the correct worksheet, tis willbe canged to a function in which the user says which sheet to acces. 
jenny = SHEET.worksheet('jenny')

jenny_data = jenny.get_all_values()

#print(jenny_data)

#print(SHEET['sheets'])

worksheet_list = SHEET.worksheets()

print(worksheet_list)


