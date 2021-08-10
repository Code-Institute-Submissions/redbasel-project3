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
#worksheet_list = SHEET.worksheets()
#print('Welcome, here you can find client health data and have health metrics calculated \n Avaialble client worksheets...\n')

# funciton with placeholder for varibale. tell user to pick a worksheet from the list. 
# for loop. for names inside the workshee, take them out and put in new list
# convert from worksheet to string so we can work with it easier.
"""
ws_names = ','.join(str(v) for v in worksheet_list)
for sheet in worksheet_list:
    print(sheet.title)
"""
def to_be_utilized():
    select_worksheet = input('write the name of which client you which client record you wish to access:\n')
    terminal_chosen_worksheet = SHEET.worksheet(select_worksheet)
    chosen_ws_all_values = terminal_chosen_worksheet.get_all_values()
    header_row = chosen_ws_all_values[0]
    start_row = chosen_ws_all_values[1]
    last_row = chosen_ws_all_values[-1]
    start_weight_test = terminal_chosen_worksheet.cell(2, 1)
    weight_start_value = int(chosen_ws_all_values[1][0])
    weight_final_value = int(chosen_ws_all_values[-1][0])
    height_value = int(chosen_ws_all_values[-1][-2])
    start_bmi = (((weight_start_value) / ((height_value) * (height_value))) * 10000)
    final_bmi = (((weight_final_value) / ((height_value) * (height_value))) * 10000)
    percentage_change_test_bmi = int(((int(final_bmi)) - (int(start_bmi)))/(int(start_bmi)) * 100)
    return select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi

"""
def funb():
    select_worksheet= to_be_utilized()
    pp(select_worksheet)
"""





"""
select_worksheet = input('write the name of which client you which client record you wish to access:\n')
terminal_chosen_worksheet = SHEET.worksheet(select_worksheet)
chosen_ws_all_values = terminal_chosen_worksheet.get_all_values()
#pp(chosen_ws_all_values)
header_row = chosen_ws_all_values[0]
start_row = chosen_ws_all_values[1]
last_row = chosen_ws_all_values[-1]
start_weight_test = terminal_chosen_worksheet.cell(2, 1)
"""
#function that calculates the percentage change in the cleints health data over time, comparing the first measurement with the last. 
def health_measurements():
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
    for x in range(4):
        percentage_change_test = int(((int(last_row[x])) - (int(start_row[x])))/(int(start_row[x])) * 100)
        header_row_x = header_row[x]
        print(f"the percentage change in {header_row_x} is {percentage_change_test}%")

"""
weight_start_value = int(chosen_ws_all_values[1][0])
weight_final_value = int(chosen_ws_all_values[-1][0])
height_value = int(chosen_ws_all_values[-1][-2])

start_bmi = (((weight_start_value) / ((height_value) * (height_value))) * 10000)
final_bmi = (((weight_final_value) / ((height_value) * (height_value))) * 10000)
percentage_change_test_bmi = int(((int(final_bmi)) - (int(start_bmi)))/(int(start_bmi)) * 100)
"""
"""

def bmi_check():
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
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
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
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
"""
# this function calcualtes the bmi of the client. firstly their initial bmi value and secondly their final bmi vlaue. and it outputs to the client in which bmi range they were and which they are presently in.
def bmi_check():
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
    if 18.5 > start_bmi:
        print (f"{select_worksheet} were in the underweight range")
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
    elif 18.5 <= start_bmi <= 24.9:
        print(f"{select_worksheet} were in the healthy weight range")
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
    elif 25 <= start_bmi <= 29.9:
        print(f"{select_worksheet} were in the overweight range")
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
    elif 30 <= start_bmi <= 39.9:
        print(f"{select_worksheet} were in the obese range")
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
    else:
        print(f"{select_worksheet} should've seen a physician")

# this function prints the table of the client which the first row filled with the titles 
def allDataClient():
    select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
    pp(chosen_ws_all_values)

# this is the menu that the user will interact with initially and then return to again to continue using the other functions available. 
def toolMenu():
    print("\nWelcome to the tool menu, these tools are at your disposal")
    print("1: Analyze the clients percentage change of their body measurements")
    print("2: Analyze the clients past and present BMI data")
    print("3: Show all the data avaialable")
    print('available clients:')
    worksheet_list = SHEET.worksheets()
    ws_names = ','.join(str(v) for v in worksheet_list)
    for sheet in worksheet_list:
        print(sheet.title)
    selection = int(input("Please enter your selection, between 1-3:\n"))
    if selection==1:
        health_measurements()
        runAgain()
    elif selection==2:
        #print(f"{select_worksheet} BMI was:{start_bmi} and now it is {final_bmi}")
        bmi_check()
        runAgain()
    elif selection==3:
        allDataClient()
        runAgain()
    else:
        print("invalid choice. enter between 1-3")
        toolMenu()
# this function main task is once tooMenu finishes, ask if the user is finished or wish to utilize the menu once more
def runAgain():
    answer = input('Do you wish to continue using the program, type "yes" in that case otherwise "no"')
    if answer== 'yes':
        toolMenu()
    elif answer == 'no':
        print('Thank you for using the tool, hopefully it could assist you')
    else:
        print('Invalid input, please type again "yes" or "no"')
        runAgain()


"""

# fucniton 1 will be accesing the worksheeet and picking a client
# funcitn 2 will use that return value of which client was chosen and ask the user which ccalcualton o be made
# funciton 2/3 will do just that
# function 4 asking to restart the code, y/n  prompt

"""
def main():
   # worksheet_list = SHEET.worksheets()
    #ws_names = ','.join(str(v) for v in worksheet_list)
    #for sheet in worksheet_list:
        #print(sheet.title)
    #select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi = to_be_utilized()
    toolMenu()
    #return select_worksheet, terminal_chosen_worksheet, chosen_ws_all_values, header_row, start_row, last_row, start_weight_test, weight_final_value, height_value, start_bmi, final_bmi, percentage_change_test_bmi
    


main()