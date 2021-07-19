# we need gspread in order to access the sheet.
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint as pp
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


#

#jenny = SHEET.worksheet('jenny')

#jenny_data = jenny.get_all_values()

#print(jenny_data)

#print(SHEET['sheets'])

# in order to fetch the worksheet sinsde the sheet as list we use this below. 
worksheet_list = SHEET.worksheets()

#pp is for multiplelien lists
#print(worksheet_list)
print('Welcome, here you can find client health data and have health metrics calculated \n Avaialble client worksheets...\n')
#pp(worksheet_list)


# funciton with placeholder for varibale. tell user to pick a worksheet from the list. 
# for loop. for names inside the workshee, take them out and put in new list


# in list worksheet_list, create seprate vlaue s for strings inside '' push to new list. 


#str_worksheet = ''.join([worksheet_list])

#print(str_worksheet)
# convert from worksheet to string so we can work with it easier.
ws_names = ','.join(str(v) for v in worksheet_list)


#print(ws_names)

#print(ws_names)

for sheet in worksheet_list:
    print(sheet.title)


select_worksheet = input('write the name of which client you which client record you wish to access:\n')
terminal_chosen_worksheet = SHEET.worksheet(select_worksheet)
chosen_ws_all_values = terminal_chosen_worksheet.get_all_values()
print(chosen_ws_all_values)


#print(ws_names.split(' '))

#sp_test = 

