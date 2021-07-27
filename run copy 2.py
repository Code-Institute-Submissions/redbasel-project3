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

#pp is for multiplelien lists
#print(worksheet_list)
print('Welcome, here you can find client health data and have health metrics calculated \n Avaialble client worksheets...\n')
#pp(worksheet_list)


# funciton with placeholder for varibale. tell user to pick a worksheet from the list. 
# for loop. for names inside the workshee, take them out and put in new list


# in list worksheet_list, create seprate vlaue s for strings inside '' push to new list. 



# convert from worksheet to string so we can work with it easier.
ws_names = ','.join(str(v) for v in worksheet_list)




for sheet in worksheet_list:
    print(sheet.title)


select_worksheet = input('write the name of which client you which client record you wish to access:\n')
terminal_chosen_worksheet = SHEET.worksheet(select_worksheet)
chosen_ws_all_values = terminal_chosen_worksheet.get_all_values()
#pp(chosen_ws_all_values)

# beginner value
header_row = chosen_ws_all_values[0]
start_row = chosen_ws_all_values[1]
last_row = chosen_ws_all_values[-1]


#percentage_change_stats = int(start_row) - int(last_row)


#pp(f"The starting values {start_row}")
#pp(f"The clients final values {last_row}")
#pp(f"The clients percentage change {percentage_change_stats}%")


start_weight_test = terminal_chosen_worksheet.cell(2, 1)
#print(start_weight_test)
#type(start_weight_test)

    
#data1 = get_sales_data()





#print(f"if you wish to access {select_worksheet}'s health statistics please type 'health_stats' and if you wish to analyse the clients BMI please type 'BMI_analyze'\n")



def health_measurements():
    for x in range(4):
        percentage_change_test = int(((int(last_row[x])) - (int(start_row[x])))/(int(start_row[x])) * 100)
        header_row_x = header_row[x]
        print(f"the percentage change in {header_row_x} is {percentage_change_test}%")

#function_to_run = input('Please type which function you wish to run')

#def hihi():
#   (function_to_run)()

#hihi()
#health_measurements()




weight_start_value = int(chosen_ws_all_values[1][0])
weight_final_value = int(chosen_ws_all_values[-1][0])
height_value = int(chosen_ws_all_values[-1][-2])

start_bmi = (((weight_start_value) / ((height_value) * (height_value))) * 10000)
#print(start_bmi)
final_bmi = (((weight_final_value) / ((height_value) * (height_value))) * 10000)
#print(final_bmi)
percentage_change_test_bmi = int(((int(final_bmi)) - (int(start_bmi)))/(int(start_bmi)) * 100)
#print(f"The percentage change in BMI is {percentage_change_test_bmi}%")


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

#print(bmi_check())

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

#print(bmi_check_final())


def toolMenu():
    print("\nWelcome to the tool menu, these tools are at your disposal")
    print("1: Analyze the clients percentage change of their body measurements")
    print("2: Analyze the clients past and present BMI data")
    print("3: Show all the data avaialable")
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
    else:
        print("invalid choice. enter between 1-3")
        toolMenu()

toolMenu()

#print(final_bmi)

"""
below 18.5 – you're in the underweight range
between 18.5 and 24.9 – you're in the healthy weight range
between 25 and 29.9 – you're in the overweight range
between 30 and 39.9 – you're in the obese range

if 18.5 => 
bmi_range = "you're in the underweight range"

"""
"""
def calculate_percentage_change(present_values):

    past_values = chosen_ws_all_values[1]
    present_values = chosen_ws_all_values[-1]

    percentage_data = []
    for x in range(len(chosen_ws_all_values)):
        percentag = chosen_ws_all_values[1] - chosen_ws_all_values[-1]
        percentage_data.append(percentage)
        print(percentage_data)
    return percentage_data

calculate_percentage_change(chosen_ws_all_values)
# s
# would be nice to pair this with row 0 names so would be: thigh_cm : 13%

# stock = sheet worksheet.get all values
# stock_row = specific row of stock 

# new list. row 0 row 1 and row-1

# formula 1 " row 1 worksheet title, row 2 name of measuremnt, row 3 percentage change firs and last data row" 
# print client name, 
# function picker f{function}()
# 

#print(ws_names.split(' '))

#sp_test = 

"""
"""
def calculate_surplus_data(sales_row):
    
    #compare sales with previus day


    print("calcaling surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]
    print(f"stock row: {stock_row}")
    print(f"sales row: {sales_row}")

    surplus_data = []
    for stock, sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    return surplus_data"

stock = sheet worksheet.get all values
stock_row = specific row of stock 
"""

# fucniton 1 will be accesing the worksheeet and picking a client
# funcitn 2 will use that return value of which client was chosen and ask the user which ccalcualton o be made
# funciton 2/3 will do just that
# function 4 asking to restart the code, y/n  prompt