#Create a function named write_sales_data with file_object, item and price as parameters.
#The function should write item and price to a file.

#Create another function named read_sales_data with file_object as a parameter.
#The function will read the file line by line and display to screen to produce the table described in homework 5.

def write_sales_data(item,price):
    infile = open('sales_recordes.txt','w')
    item = ''
    price = ''
    infile.write(item + '\t' + price)
    inflie.close()


    
def read_sales_data(file_object):
    infile = open('salesrecord.txt', 'r')
    file_contents = infile.read()
    infile.close()
    return(file_contents)
