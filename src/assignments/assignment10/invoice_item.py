from src.assignments.assigmnent10.product import Product
import unittest

class InvoiceItem:

    def __init__(self,product,quantity):
        '''
        ASSIGNMENT10: 
        Remove description and cost parameters. Replace with a product class
        '''

        #ASSIGNMENT10: update code to use product class
        self.product = product
        self.quantity = quantity
        
       


    def get_extended_cost(self):
        '''
        Write a statement to multiply quantity * cost and return the result
        :return:  extended cost
        '''
        #ASSIGNMENT10: MODIFY CODE TO GET THE COST FROM THE PRODUCT ATTRIBUTE
        return self.product.cost * self.quantity
    
    def get_description(self):
        #ASSIGNMENT10: MODIFY CODE TO GET THE NAME FROM THE PRODUCT ATTRIBUTE
        return self.product.name

if __name__ == "__main__":
    unittest.main()
