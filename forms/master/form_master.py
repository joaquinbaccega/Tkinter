import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl

class MasterPanel:
    
                                      
    def __init__(self):        
        self.ventana = tk.Tk()                             
        self.ventana.title('Master panel')                            
        self.ventana.geometry("1280x720")
        self.ventana.config(bg='white')
        self.ventana.resizable(width=0, height=0)            
        
        logo = utl.leer_imagen("./img/logo.png", (200, 200))
                        
        label = tk.Label( self.ventana, image=logo,bg='white' )
        label.place(x=0,y=0,relwidth=1, relheight=1)
        
        self.ventana.mainloop()