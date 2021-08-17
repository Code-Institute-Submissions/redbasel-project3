FEATURES
Following will explain each individual feature offered by the program and its intended use and benefit for the relevant parties.

*Health Terminal*
This project is called “Health terminal” and is based on python. The reason behind the name, users of this application will be able to access records of fitness clients to review and evaluate their data that is located in a google sheet.

[bild av hela terminalen I heroku]

**USER STORIES**
USER STORY #1
This user is interested in all of the data available on a particular client. What they need is a method for them to be able to clearly see all the data available and what it represents. 
When this user utilizes the application via the termina they will be greeted, presented with clients available and features at their disposal. Using feature 1 and specifying which client record they wish to access they will be presented with a table with clear distinction between rows and columns as well as clear column titles so that they know what the data represents. 

USER STORY #2 
This user is interested in the progress of the client and wants it in a quantifiable and clear way. Thus they need a feature that is precise both in measuring the change and also where the change has taken place. 
When this user utilizes the application via the terminal they will be greeted, presented with clients available and features at their disposal. Using feature 2 and specifying the client they wish to access they are presented with the percentage change in each category. 


USER STORY #3
This user would like to have a qualitative understanding of the clients progress instead of quantitative. Someone who wishes to quickly understand what the overall health level of the client was and their overall health level today. 
 When this user utilizes the application via the terminal they will be greeted, presented with clients available and features at their disposal. Using feature 3 and specifying the client, the application will calculate the BMI of the initial value sand the final values. Then it will take the BMI values and check it against the different ranges as specified by the health board. The user is then presented with which range the client was in and in which range they are enow in. for example, “ (client name) was in the obese range” followed by “(client name) is now in the normal range”


Existing features
1.	Overview of all the available clients’ which records can be accessed, the function will print out the names individually of all the available worksheets inside the google sheet we are referring to. This is beneficial to the user as they will now which clients records are accessible and can be used with the tools. This feature is made possible by the tool_menu() function that fetches the worksheets and prints the title of the worksheets using a for loop. 
![Image showcasing the feature of available clients](docs/images/f1abc.png)
2.	A tool menu which displays the available tools for the user to utilize. The functions allow for the data to be displayed and manipulated.  Firstly, the user is asked which tool they wish to utilize and secondly which client you wish to utilize that tool. This feature uses print statements to present the options and its part of the tool_menu() function. It also features an input element, and based on the input (between 1-3) it will execute the relevant function. If the user enters something else than specified, they will be shown a error message that states “invalid choice. Enter between 1-3” 
![tool menu showcasing to the user the different tools available](docs/images/f2tm.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
3.	Tool menu option#1. This function takes into account the chosen clients health measurements. It will take the first submitted record and compare it against the last submitted record and present the percentage change. This tells the user the change over time for the chosen client. It will also detail how the measurements have changed for each of the categories. This feature is delivered using the health_measurements() function that takes the first and last value of the first four columns and calculates the percentage change. Then using an f” statements it prints out the percentage change for each category. Then as seen the user Is prompted with a selection regarding if they wish to continue utilizing the application. 
![print of client “jenny”’s data and her measurements](docs/images/op1.PNG)
4.	Tool menu option #2 this function will calculate the clients past and present BMI, inform the user of how the past BMI score was to be interpreted and how the clients BMI fare today. This feature is using the bmi_check() function which uses the data available to calculate the bmi, then the value is checked against intervals to see in which range the patient is in. Then the function will print a statement based on which range they belong to. It also checks which range the patient belonged to in the start of their journey. 
![print of client jennys BMI qualitative data](docs/images/op2.PNG)
5.	Tool menu option #3 The third option shows all of the available data for the client from the worksheet. The third feature utilises the all_data_client() function which uses the pprint statement in order to present the table for the user in a more friendly manner. 
![print of all the available data of client jenny](docs/images/op3.PNG)
6.	After a menu option has been utilized the program will ask the user whether they wish to continue. This is made possible using the run_again() function. If the user types yes then the tool_menu() function will run again and if they press no they will be shown a message “Thank you for using….” If they were to enter the answer incorrectly or using upper space they will be asked to enter yes or no more clearly. 
7.	When the user inputs a invalid input, the user will be prompted to try again. 


**TESTING**
The app is run via the terminal and has been tested using both chrome and firefox on desktop, using gitpod and heroku. It is running as expected in the gitpod terminal. When testing it was discovered that heroku to does not adequately run a function that is placed under a print statemetn. Due to this had to alter the code to take this in consideration and add a statemetn targeting heroku users without affeccting otehr users too much. To simply press enter to continue. this does trigger the error message, however. The error message was altered so that it is unobtrusive to the user experience, and more of a general instruction. 



Validator Testing
 PEP8 using www.onlinepep8checker.com
 Pylint using terminal

Possible improvements
It was attempted but not fully succeded to pass the variable between functions as list. So this is a possible improvement that would make the code fully PEP8 compliant. It was attempted to break up the return at the commas, manually and using a python formater but to no avail. It wa also attempted to return all the variables as part of a list and then pass that list on to the functions.

**DEPLOYMENT**
Deployed ot heroku at
https://healthterminal.herokuapp.com/

**CREDITS**
BMI forumla and information
https://www.nhlbi.nih.gov/health/educational/lose_wt/BMI/bmi-m.htm

Gspread documentation
https://docs.gspread.org/en/latest/user-guide.html

Python quickstart for the Sheets API
https://developers.google.com/sheets/api/quickstart/python

Pylint documentation
http://pylint.pycqa.org/en/latest/

Content

The data used for the worksheet is based on client data but the names are made up. In order to have realistic data without comprimizing the integrity of the client. They have also been asked if its okay to use their data without their identity. Additonal resources have been used, these include pip3, gspread and pprint

Packages
pip3 #in order to install the packages.
gspread # to access the google sheets and manipulate.
pprint # to better print tables inthe terminal to provide a better user experience. 


Media
There is no real media used in this project, the only media si the screenshots in this very readme file, which ive take myself. 
