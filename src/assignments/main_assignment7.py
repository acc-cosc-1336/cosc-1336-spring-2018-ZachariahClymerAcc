#write the import for function for assignment7 sum_list_values
from src.assignments.assignment7 import sum_list_values
'''
Create a function named process_list that calls the sum_list_values function.
Prints the list values and the sum of the element in the list as follows:
joe 10 15 20 30 40 sum: 115
Create a main function.
In the function loop as long as user wants to add another list.
Prompt the user for name and append to the list.
Prompt the user for number of numeric values in the list.
Iterate the number of times the user enters and prompt end-user for n numeric values.
Call the main function
--------------------
joe 10 15 20 30 40
bill 23 16 19 22
sue 8 22 17 14 32 17 24 21 2 9 11 17
grace 12 28 21 45 26 10
john 14 32 25 16 89
'''
def process_list(list1):
    total = sum_list_values(list1)
    print((list1), 'sum: ', total, sep=' ')

def main():

    new_list = []
    again = 'Y'
    while again == 'y' or again == 'Y':
        #Prompt the user for name and append to the list.
        name = input(str('Enter a name: '))
        new_list.append(name)
        #Prompt the user for number of numeric values in the list.
        num = int(input('Enter the number of numeric values in the list list: '))
        #Iterate for num times, prompting user for numeric values, and then append the values to the list 
        for num in range(1,num+1):
            num_value = int(input('Enter number to add to the list: '))
            new_list.append(num_value)
        #call the process_list function
        process_list(new_list)
        print('Do you want to add another list?')
        again = input('y = yes, anything else = no: ')

main()
