import tkinter as tk
from tkinter import ttk
from tkinter.font import BOLD
import util.generic as utl

class FormLoginDesigner:
    def verificar(self):
        pass  

    def userRegister(self):
        pass


    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Inicio de Sesion')
        self.ventana.geometry("1280x720")
        self.ventana.config(bg='white')
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 1280, 720)

        logo = utl.leer_imagen("./img/logo.png", (200, 200))

        frame_form = tk.Frame(self.ventana, bd= 0, width=300, relief=tk.SOLID, padx=10, pady= 10, bg='white')
        frame_form.pack(side='left', expand=tk.NO, fill=tk.BOTH)
        label = tk.Label(frame_form, image=logo, bg='#fcfbe9')
        label.place(x=0, y=0, relwidth=1, relheight=1)


        frame_form = tk.Frame(self.ventana, bd= 0, relief=tk.SOLID, bg='white')
        frame_form.pack(side='right', expand=tk.YES, fill=tk.BOTH)

        frame_from_top = tk.Frame(frame_form, height= 50, bd= 0, relief= tk.SOLID, bg='black')
        frame_from_top.pack(side='top', fill=tk.X)
        tittle = tk.Label(frame_from_top, text='Inicio de Sesion', font=('Arial', 20, BOLD), fg='#666a88', bg='#fcfcfc', pady=50)
        tittle.pack(expand=tk.YES, fill=tk.BOTH)

        frame_form_fill = tk.Frame(frame_form, height= 50, bd= 0, relief=tk.SOLID, bg='#fcfcfc')
        frame_form_fill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        etiqueta_usuario = tk.Label(frame_form_fill, text="Usuario", font=('Times', 14) ,fg="#666a88",bg='#fcfcfc', anchor="w")
        etiqueta_usuario.pack(fill=tk.X, padx=20,pady=5)
        self.usuario = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.usuario.pack(fill=tk.X, padx=20,pady=10)

        etiqueta_password = tk.Label(frame_form_fill, text="Contraseña", font=('Times', 14),fg="#666a88",bg='#fcfcfc' , anchor="w")
        etiqueta_password.pack(fill=tk.X, padx=20,pady=5)
        self.password = ttk.Entry(frame_form_fill, font=('Times', 14))
        self.password.pack(fill=tk.X, padx=20,pady=10)
        self.password.config(show="*")

        inicio = tk.Button(frame_form_fill,text="Iniciar sesion",font=('Times', 15,BOLD),bg='#3a7ff6', bd=0,fg="#fff",command=self.verificar)
        inicio.pack(fill=tk.X, padx=20,pady=20)        
        inicio.bind("<Return>", (lambda event: self.verificar()))

        inicio = tk.Button(frame_form_fill, text="Registrarse", font=('Times', 15,BOLD), bg='#3a7ff6', bd=0, fg="#fff", command=self.userRegister)
        inicio.pack(fill=tk.X, padx=20, pady=20)
        inicio.bind("<Return>", (lambda event: self.userRegister()))


        self.ventana.mainloop()
