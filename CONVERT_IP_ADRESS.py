""" The idea of the project is to convert an IP adress in a way that the result is binary"""

# Enter an IP adress, each number is splited by '.'
print("Enter an IP adress: ")
ipadress = list(input().split('.'))

# Here binary representation of the numbers in IP adress will be stored
ipconverted = []

# Creating a loop that is converting the IP adress numbers
i = 0
while i in range(0, len(ipadress)):
    numberConverted = format(int(ipadress[i]), 'b')
    ipconverted.append(numberConverted)
    i+=1

# Printing binary repsentation of the IP adress entered by a user
print(ipconverted)