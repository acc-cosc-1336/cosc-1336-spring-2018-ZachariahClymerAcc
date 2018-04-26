from tkinter import Tk, Button, Label
from converter import Converter

class Win(Tk):

    def __init__(self):

        Tk.__init__(self, None, None)
        
        self.display_labels = Button(self, text='Display Conversion', \
                                      command=self.display_labels).grid(row=3, column=0)

        self.quit_button = Button(self, text='Quit', command=self.destroy).grid(row=3, column=1)
    
        self.mainloop()

    def display_labels(self):

        self.converter = Converter()
        km = 100
        miles = self.converter.get_miles_from_km (km)
        self.label = Label(self, text='km:' + ' ' + str(km)).grid(row=1)
        self.label = Label(self, text='miles:' +' ' + format(miles, '.2f')).grid(row=2)
