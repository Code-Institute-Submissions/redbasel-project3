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



# in order to fetch the worksheet sinsde the sheet as list we use this below. 
worksheet_list = SHEET.worksheets()
print('Welcome, here you can find client health data and have health metrics calculated \n Avaialble client worksheets...\n')


# funciton with placeholder for varibale. tell user to pick a worksheet from the list. 
# for loop. for names inside the workshee, take them out and put in new list
# convert from worksheet to string so we can work with it easier.
ws_names = ','.join(str(v) for v in worksheet_list)
for sheet in worksheet_list:
    print(sheet.title)

select_worksheet = input('write the name of which client you which client record you wish to access:\n')
terminal_chosen_worksheet = SHEET.worksheet(select_worksheet)
chosen_ws_all_values = terminal_chosen_worksheet.get_all_values()
#pp(chosen_ws_all_values)
header_row = chosen_ws_all_values[0]
start_row = chosen_ws_all_values[1]
last_row = chosen_ws_all_values[-1]
start_weight_test = terminal_chosen_worksheet.cell(2, 1)


def health_measurements():
    for x in range(4):
        percentage_change_test = int(((int(last_row[x])) - (int(start_row[x])))/(int(start_row[x])) * 100)
        header_row_x = header_row[x]
        print(f"the percentage change in {header_row_x} is {percentage_change_test}%")


weight_start_value = int(chosen_ws_all_values[1][0])
weight_final_value = int(chosen_ws_all_values[-1][0])
height_value = int(chosen_ws_all_values[-1][-2])

start_bmi = (((weight_start_value) / ((height_value) * (height_value))) * 10000)
final_bmi = (((weight_final_value) / ((height_value) * (height_value))) * 10000)
percentage_change_test_bmi = int(((int(final_bmi)) - (int(start_bmi)))/(int(start_bmi)) * 100)

def bmi_check():
    if 18.5 > start_bmi:
        print (f"{select_worksheet} were in the underweight range")
    elif 18.5 <= start_bmi <= 24.9:
        print(f"{select_worksheet} were in the healthy weight range")
    elif 25 <= start_bmi <= 29.9:
        print(f"{select_worksheet} were in the overweight range")
    elif 30 <= start_bmi <= 39.9:
        print(f"{select_worksheet} were in the obese range")
    else:
        print(f"{select_worksheet} should've seen a physician")

def bmi_check_final():
    if 18.5 > final_bmi:
        print (f"{select_worksheet} is now in the underweight range")
    elif 18.5 <= final_bmi <= 24.9:
        print(f"{select_worksheet} is now in the healthy weight range")
    elif 25 <= final_bmi <= 29.9:
        print(f"{select_worksheet} is now in the overweight range")
    elif 30 <= final_bmi <= 39.9:
        print(f"{select_worksheet} is now in the obese range")
    else:
        print(f"{select_worksheet} should see a physician")


def toolMenu():
    print("\nWelcome to the tool menu, these tools are at your disposal")
    print("1: Analyze the clients percentage change of their body measurements")
    print("2: Analyze the clients past and present BMI data")
    print("3: Show all the data avaialable")
    print("4: Re-run the program")
    selection = int(input("Please enter your selection, between 1-3:\n"))
    if selection==1:
        health_measurements()
        toolMenu()
    elif selection==2:
        print(f"{select_worksheet} BMI was:{start_bmi} and now it is {final_bmi}")
        bmi_check()
        bmi_check_final()
        toolMenu()
    elif selection==3:
        pp(chosen_ws_all_values)
        toolMenu()
    elif selection==4:
        
    else:
        print("invalid choice. enter between 1-3")
        toolMenu()

toolMenu()



"""

# fucniton 1 will be accesing the worksheeet and picking a client
# funcitn 2 will use that return value of which client was chosen and ask the user which ccalcualton o be made
# funciton 2/3 will do just that
# function 4 asking to restart the code, y/n  prompt



"""
