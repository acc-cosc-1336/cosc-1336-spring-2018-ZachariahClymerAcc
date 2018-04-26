from tkinter import Tk, Label
from converter import Converter 
class Win(Tk):
    def __init__(self):

        Tk.__init__(self, None, None)
        self.wm_title('Tk')
        self.km = 100
        self.convertor = Converter()
        

        self.label = Label(self, text = 'km:   ' + str(self.km)).grid(row=0)
        self.label = Label(self, text = 'miles:    ' + format(self.convertor.get_miles_from_km(100), '.2f')).grid(row=1)

        
        self.mainloop() 
