# Hashir Mohammad
# July 1, 2021
# Project 6
# Python Programming
# Status: Complete
# -------------------------------------------------------------------------------------------------------------------
# Write a program that will find the total, average, max, min of the numbers.
# -------------------------------------------------------------------------------------------------------------------

#Reading the file
def main():
    numberList = [ ]
    header()
    fileRead = open("DATA.txt","r") # mode r for reading

    print('\nResults')
    print('The numbers entered in the file are:', )
    for line in fileRead:
        line = line.strip('\n') # get rid of eoln marker

# Calculations:
        if (len(line) > 0):  # will check for blank lines
            value = int(line) # converts the string to integer (int)
            numberList.append(value)
            print(value)

    average = sum (numberList) / len (numberList)
    maxValue = max(numberList)
    minValue = min(numberList)

# Results
    print('The count of numbers in file:', numberList)
    print('The sum of numbers in file:', numberList)
    print('They average value is:', average)
    print('Max values:', maxValue)
    print('Min values:', minValue)

# This function displays the heading of project    
def header():
    print('-----------------------------------------------')
    print('-------READ FILE-----')
    print('-----------------------------------------------')

main()
print('End of Project')
