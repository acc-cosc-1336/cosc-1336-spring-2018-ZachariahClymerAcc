#write import statement for reverse string function
from src.midterm.exam import reverse_string
'''
10 points
Write a main function to ....
Loop as long as user types y.
Prompt user for a string (assume user will always give you good data).
Pass the string to the reverse string function and display the reversed string

'''
def main():
    again = 'y'
    while again == 'y':
        value =(input('Enter name of String: '))

        print(reverse_string(value))

        again = input('y = yes, n = no: ')

main()
