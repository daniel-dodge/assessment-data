log_file = open("um-server-01.txt")
# Connecting this python file to the data of the server text file and setting it to a variable 

def sales_reports(log_file): #Declaring a function with parameter called log_file
    for line in log_file: # For loop that will loop through the log_file data
        line = line.rstrip() #Removing any whitespace on each line of the data
        day = line[0:3] #Collecting the first 3 string characters starting at index 0 of the line (which would be the day) and setting it to a variable
        if day == "Mon": # If statement
            print(line) #Displays the data in the console if the day matches the if statement


# sales_reports(log_file) #Invoking the function, using the log_file text data as the parameter

def ten_melons(data):
    
    for line in data:   
        a = line.split(' ')
        if int(a[2]) > 10:
            print(a[2])

ten_melons(log_file)

