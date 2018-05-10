#create import statement for Customer class
from customer import Customer
'''
Create a GoodCustomer class that inherits from Customer class with parameters first_name, last_name, and phone_number.
Call the Customer(superclass) constructor method and pass all the parameters including self to the method.
In the constructor method create a new class attribute named discount and set value to .10 .
Create a get_discount_rate method that returns the attribute discount.
'''
class GoodCustomer(Customer):
    def __init__(self,first_name,last_name,phone_number):
        Customer.__init__(self,first_name,last_name,phone_number)
        self.discount = 0.10



    def get_discount_rate(self,discount):
        return self.discount
