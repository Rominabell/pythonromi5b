from tkinter import Tk, Menu, messagebox, simpledialog, Text
import pandas as pd


class MenuApp:
    def __init__(self, master):
        self.master = master
        self.create_menu()
        self.nombreArchivo="/home/quintob/Documentos/romi5b/pandas/tkint.pand.xls"
        self.estudiantes = pd.read_excel(self.nombreArchivo) 

        self.text_area=Text(master, wrap='word', height=20, width=60)
        self.text_area.pack(side='left',fill='both', expand=True)

    def create_menu(self):
        # Crear la barra de menú
        barra_menus = Menu(self.master)

        # Crear el menú "Excel"
        menu_excel = Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Excel", menu=menu_excel)

        calc_calculos= Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Cálculos", menu=calc_calculos)

        
        salir= Menu(barra_menus, tearoff=0)
        barra_menus.add_cascade(label="Salir")

        # Agregar opciones al menú "Excel"
        menu_excel.add_command(label="Todos", command=self.show_all)
        menu_excel.add_command(label="Nombre", command=self.show_name)
        menu_excel.add_command(label="Edad", command=self.show_age)
        menu_excel.add_command(label="Sexo", command=self.show_sex)
        menu_excel.add_command(label="catHermanos", command=self.show_brother)

        


        calc_calculos.add_command(label="Promedio", command=self.show_mean)
        calc_calculos.add_command(label="Mediana", command=self.show_median)
        calc_calculos.add_command(label="Moda", command=self.show_mode)
        

        # Configurar la barra de menú en la ventana principal
        self.master.config(menu=barra_menus)

    def clear_text_area(self):
        self.text_area.delete(1.0,'end')

    def show_all(self):
       self.clear_text_area()
       self.text_area.insert('end',str(self.estudiantes))

    def show_name(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["nombreApellido"]))

    def show_age(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["edad"]))

    def show_sex(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["sexo"]))

    def show_poli(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["estadoCivil"]))

    def show_brother(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["catHermanos"]))

    def show_median(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["edad"].median))
         
    def show_mode(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["edad"].mode))
         
    def show_mean(self):
        self.clear_text_area()
        self.text_area.insert('end',str(self.estudiantes["edad"].mean))
         

    
    
class App:
    def __init__(self):
        self.root = Tk()
        self.root.title("Aplicación con Menú Excel")
        
        # Crear el menú
        self.menu_app = MenuApp(self.root)

    def run(self):
        self.root.mainloop()

if __name__== "__main__":
    app = App()
    app.run()