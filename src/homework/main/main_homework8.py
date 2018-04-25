'''
Write a main function to create an empty dictionary and
a user-controlled loop to prompt for a widget name and quantity.
Add the values to the dictionary as key(widget name) and value(quantity) pairs.
After user decides to exit write data to file .
'''
def main():
    
    widgets = {}
    reply = 'Y'
    while reply == 'Y' or reply == 'y':
        widget_name = input ('Enter a widget name to add to dictionary: ')
        quantity = input ('Enter the quantity for widget name just entered: ')
        widgets[widget_name] = quantity
        reply = input('Enter Y or y to continue or anything else to stop.')

    import pickle
    output_file = open('widgets_dict.dat', 'wb')
    pickle.dump(widgets, output_file)
    output_file.close()
    

main()
