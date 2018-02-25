#write the import statements for homework5 functions

#With the functions created in homework5...
#Prompt user for number of sales records to input.
#Open a file for text writing.
#Iterate and prompt user for item name and price.
#Save item name and price to file in one line
#Calculate sum of price and write to file
#Calculate average price and write to file

#Open a file for text reading.
#Read the saved file and output table

from src.homework.homework5 import write_sales_data
from src.homework.homework5 import read_sales_data

def main():
    file_object = open('sales_data.txt', 'w')
    num_items = int(input('Enter how many items with prices you have: '))
    total = 0
    file_object.write ('Item' + '\t' +'\t' + 'Price'+ "\n")
    for num_items in range (1, num_items +1):
        item = input('Enter item: ')
        price = float(input('Enter price of item: '))
        write_sales_data(file_object, item, price)
        #total sums up all the prices
        total += price
    #avg_price takes the total of all prices and divides by num_items
    avg_price = total / num_items
    file_object.write ('Total'+ '\t'+'\t' + str(total)+"\n")
    file_object.write ('Avg Price'+ '\t' + str(avg_price)+"\n")
    file_object.close()

    file_object = open('sales_data.txt', 'r')
    read_sales_data(file_object)
    file_object.close()
 
main()
