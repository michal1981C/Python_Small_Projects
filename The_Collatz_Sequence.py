""" PROJECT: THE COLLATZ SEQUENCE
based on the book "Automate the boring stuff with Python"."""
# ---------------------------------------------------------------------

# ... import a module if needed

# Defining the finction
def collatz(number):
    if number % 2 == 0:
        return number // 2
    if number % 2 == 1:
        return number *3 +1

# Asking a user for a number to input
number = int(input("Enter a number: "))

# Creating the loop
while collatz(number) != 1:
    print(collatz(number))
    number = collatz(number)
    if collatz(number) == 1:
        print(collatz(number))
        break