# we need gspread in order to access the sheet.
# pprint is to better present the tables to the users
from pprint import pprint
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



def to_be_utilized():
    """
    this function fetches and manipulates the values,
    from the selected client to be used with the tools i.e. our functions
    """
    try:
        result = {}
        select_worksheet = input('Name of the client you wish to access:\n').lower()
        result['select_worksheet'] = select_worksheet
        terminal_chosen_worksheet = SHEET.worksheet(select_worksheet)
        result['terminal_chosen_worksheet'] = terminal_chosen_worksheet
        chosen_ws_all_values = terminal_chosen_worksheet.get_all_values()
        result['chosen_ws_all_values'] = chosen_ws_all_values
        header_row = chosen_ws_all_values[0]
        result['header_row'] = header_row
        start_row = chosen_ws_all_values[1]
        result['start_row'] = start_row
        last_row = chosen_ws_all_values[-1]
        result['last_row'] = last_row
        start_weight_test = terminal_chosen_worksheet.cell(2, 1)
        result['start_weight_test'] = start_weight_test
        weight_start_value = int(chosen_ws_all_values[1][0])
        result['weight_start_value'] = weight_start_value
        weight_final_value = int(chosen_ws_all_values[-1][0])
        result['weight_final_value'] = int(chosen_ws_all_values[-1][0])
        height_value = int(chosen_ws_all_values[-1][-2])
        result['height_value'] = height_value
        start_bmi = (((weight_start_value) / ((height_value) * (height_value))) * 10000)
        result['start_bmi'] = start_bmi
        final_bmi = (((weight_final_value) / ((height_value) * (height_value))) * 10000)
        result['final_bmi'] = final_bmi
        percentage_change_test_bmi = int(((int(final_bmi)) - (int(start_bmi)))/(int(start_bmi)) * 100)
        result['percentage_change_test_bmi'] = percentage_change_test_bmi
        return result
    except gspread.WorksheetNotFound:
        print("Please enter the client name exactly as presented to you")
        print("Restarting the application")
        main()




def health_measurements():
    """
    for loop that calculates the percentage change of client data over time,
    comparing the first measurement with the last.
    """
    result = to_be_utilized()
    last_row = result['start_row']
    start_row = result['last_row']
    header_row = result['header_row']
    for x in range(4):
        percentage_change_test = int(((int(last_row[x])) - (int(start_row[x])))/(int(start_row[x])) * 100)
        header_row_x = header_row[x]
        print(f"the change in {header_row_x} is {percentage_change_test}%")




def bmi_check():
    """
    this function calcualtes the bmi of the client.
    Firstly their initial bmi value.
    Secondly, their final bmi vlaue.
    Lastly, it outputs to the client in which bmi range they were,
    and which they are presently in.
    """
    result = to_be_utilized()
    start_bmi = result['start_bmi']
    final_bmi = result['final_bmi']
    select_worksheet = result['select_worksheet']
    if start_bmi < 18.5:
        bmi_interval_past = "underweight"
        if final_bmi < 18.5:
            bmi_interval_present = "underweight"
        elif 18.5 <= final_bmi <= 24.9:
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            bmi_interval_present = "obese"
        else:
            bmi_interval_present = "beyond obese"
    elif 18.5 <= start_bmi <= 24.9:
        bmi_interval_past = "healthy"
        if final_bmi < 18.5:
            bmi_interval_present = "underweight"
        elif 18.5 <= final_bmi <= 24.9:
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            bmi_interval_present = "obese"
        else:
            bmi_interval_present = "beyond obese"
    elif 25 <= start_bmi <= 29.9:
        bmi_interval_past = "overweight"
        if final_bmi < 18.5:
            bmi_interval_present = "underweight"
        elif 18.5 <= final_bmi <= 24.9:
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            bmi_interval_present = "obese"
        else:
            bmi_interval_present = "beyond obese"
    elif 30 <= start_bmi <= 39.9:
        bmi_interval_past = "obese"
        if final_bmi < 18.5:
            bmi_interval_present = "underweight"
        elif 18.5 <= final_bmi <= 24.9:
            bmi_interval_present = "healthy"
        elif 25 <= final_bmi <= 29.9:
            bmi_interval_present = "overweight"
        elif 30 <= final_bmi <= 39.9:
            bmi_interval_present = "obese"
        else:
            bmi_interval_present = "beyond obese"
    else:
        bmi_interval_past = "beyond obese"
    print(f"\n{select_worksheet} was in the {bmi_interval_past} range,")
    print(f"now {select_worksheet} is in the {bmi_interval_present} range. \n")




def all_data_client():
    """
    This function prints the table of the client,
    of which the first row is filled with the titles
    """
    result = to_be_utilized()
    chosen_ws_all_values = result['chosen_ws_all_values']
    pprint(chosen_ws_all_values)



def tool_menu():
    """
    This is the menu that the user will interact with initially,
    then return to again to continue using the other functions available.
    """
    print("\nWelcome to the tool menu, these tools are at your disposal")
    print("1: Analyze the clients percentage change in body measurements")
    print("2: Analyze the clients past and present BMI data")
    print("3: Show all the data available")
    worksheet_list = SHEET.worksheets()
    ws_names = ','.join(str(v) for v in worksheet_list)
    try:
        selection = int(input("Please enter your selection, between 1-3:\n"))
        if selection == 1:
            print('Available clients:')
            for sheet in worksheet_list:
                print(sheet.title)
            health_measurements()
            run_again()
        elif selection == 2:
            print('Available clients:')
            for sheet in worksheet_list:
                print(sheet.title)
            bmi_check()
            run_again()
        elif selection == 3:
            print('Available clients:')
            for sheet in worksheet_list:
                print(sheet.title)
            all_data_client()
            run_again()
        else:
            print("invalid choice. enter between 1-3")
            tool_menu()
    except ValueError:
        print("Please, enter a valid selection, make sure its an integer")
        run_again()



def run_again():
    """
    This function main task is once tool_menu finishes,
    ask if the user is finished or wish to utilize the menu once more
    """
    answer = input('To continue, type "yes" otherwise "no". \n').lower()
    if answer == 'yes':
        tool_menu()
    elif answer == 'no':
        print('Thank you for using the tool, hopefully it could assist you.')
        exit()
    else:
        print(" Don't use uppercase or integers.")
        run_again()



def main():
    """
    this is the function that starts the application,
    doing it this way makes it possible to add elements in the future
    """
    tool_menu()

main()