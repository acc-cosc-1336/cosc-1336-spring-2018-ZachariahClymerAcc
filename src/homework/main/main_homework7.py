#write import statement for homework 7 file
from src.homework.homework7 import get_p_distance_matrix
import src.homework.homework7

'''
Write a main function to...
Read p_distance.dat file
From the file data, create a two-dimensional list like the following example:
[
 ['T','T','T','C','C','A','T','T','T','A'],
 ['G','A','T','T','C','A','T','T','T','C'],
 ['T','T','T','C','C','A','T','T','T','T'],
 ['G','T','T','C','C','A','T','T','T','A']
]
Pass the list to the get_p_distance_matrix function as an argument
Display the p distance matrix to screen
'''
def main():
    infile = open('p_distance.dat', 'r')
    string = ''
    for line in infile:
        string += line
    string = string.replace(' ', '')
    string = string.replace('\n','')
    a = []
    for i in string:
        a += i
    b = [
        a[:10],
        a[10:20],
        a[20:30],
        a[30:40]
        ]
    infile.close()
    print(get_p_distance_matrix(b))
main()
