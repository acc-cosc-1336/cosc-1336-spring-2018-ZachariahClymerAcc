#Write import statements for classes invoice and invoice_item
from src.assignments.assignment9.invoice_item import InvoiceItem
from src.assignments.assignment9.invoice import Invoice

#from invoice_item import InvoiceItem
#from invoice import Invoice

'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''

invoice = Invoice('ABC Company', '03282018')

keep_going ='y'

while keep_going == 'y':
    description = input("Enter description: ")
    quantity = int(input("Enter quantity: "))
    cost = float(input("Enter cost: "))

    invoice_item = InvoiceItem(description, quantity, cost)
    invoice.add_invoice_item(invoice_item)

    keep_going = ("Enter y to keep going")
    if keep_going != 'y':
        invoice.print_invoice()
