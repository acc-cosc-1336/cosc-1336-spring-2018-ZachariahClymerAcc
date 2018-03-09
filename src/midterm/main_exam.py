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
    new_string = []
    again = 'y'
    while again == 'y':
        num =(input('Enter name of String: '))
        new_list.append(num)

        while again2 == 'y':
             num = int(input('Enter name of String: '))
             input('Enter String: ')
             new_string.append(num)
             print('Do you want to add another String?')
             again2 = input('y = yes, n = no: ')
             print()
        again = input('y = yes, n = no: ')
    return new_string
