#Write import statements for classes invoice and invoice_item and PRODUCT
from invoice import  Invoice
from invoice_item import  InvoiceItem
#ASSIGNMENT10 Write import statements for classes product and customer
from customer import Customer
from product import Product

'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object 

In the loop:
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Create a new InvoiceItem, use the newly created product as a parameter argument 
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''
#ASSIGNMENT10: Make sure to change invoice bill_to argument to an instance of a Customer class
customer = Customer('John','Doe','111-222-3333')
invoice = Invoice(customer, '03012018')

keep_going = 'y'

while keep_going == 'y':

    description = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    cost = float(input("Enter cost: "))

    #ASSIGNMENT10: Create a product object and add description and cost as parameter arguments.
    #Quantity parameter remains same.
    invoice.add_invoice_item.Product(description, quantity, cost)

    keep_going = input("Enter another type y: ")


invoice.print_invoice()




