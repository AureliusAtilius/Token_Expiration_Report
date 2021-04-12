import sys, csv
from datetime import *


# Take file name as a command line argument
fileName = sys.argv[1]

# Get today's date using datetime.today()
today = datetime.today()

sortedDates={}
# Open file
with open(fileName) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        # Iterate through each row:
        for row in csv_reader:        
                # Check whether or not Token is active
                if row["Account Enabled"]== "Yes":
                        # Check whether date is after Today's date by converting date string using datetime.strptime("2019-10-22", "%Y-%m-%d")
                        date = datetime.strptime(row["Token Expiration Date"], "%Y-%m-%d")
                        if today<date:
                                
                                # Store user name and expiration date
                                if date not in sortedDates:
                                        sortedDates[date] = []
                                        sortedDates[date].append(row["First Name"]+" "+row["Last Name"])
                                else:
                                      sortedDates[date].append(row["First Name"]+" "+row["Last Name"])  
#TODO: Print user names sorted by expiration dates:
        #<DATE>
                #<USER>
                #<USER>
                #<USER>
        #<DATE>
                #<USER>
                #<USER>
