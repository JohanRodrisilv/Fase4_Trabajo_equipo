import tkinter as tk  # Trae las herramientas básicas de Tkinter para crear la ventana.
from tkinter import ttk  # Permite usar botones, etiquetas y campos con un estilo moderno.
from abc import ABC, abstractmethod  # Sirve para crear una clase base y métodos obligatorios.
from tkinter import messagebox  # Permite mostrar avisos y mensajes en ventanas emergentes.

class Entidad(ABC):  # Define una base común para los elementos que tienen identificador.
    
    def __init__(self, identificador):  # Recibe el identificador cuando se crea una entidad.
        self.__identificador = identificador  # Guarda el identificador como un dato interno.
        
    @property  # Permite consultar el identificador sin modificarlo directamente.
    def identificador(self):  # Define la forma de acceder al identificador guardado.
        return self.__identificador  # Devuelve el identificador de esta entidad.
    
    @abstractmethod  # Obliga a las clases hijas a escribir su propia descripción.
    def describir(self):  # Declara el método que cada entidad debe implementar.
        pass  # Deja el método sin contenido porque se completará en la clase hija.

class Cliente(Entidad):  # Crea la clase Cliente usando la base común Entidad.
    def __init__(self, identificador, nombre, correo):  # Recibe los datos necesarios del cliente.
        super().__init__(identificador)  # Guarda el identificador usando el constructor de Entidad.
        if not isinstance(nombre, str) or not nombre.strip():  # Revisa que el nombre sea texto y no esté vacío.
            raise ValueError("El nombre no puede estar vacio y debe ser una cadena de texto.")  # Avisa si el nombre no es válido.
        if not isinstance(correo, str) or "@" not in correo:  # Comprueba que el correo sea texto y tenga el símbolo @.
            raise ValueError("El correo debe incluir el simbolo @ y no puede estar vacio.")  # Avisa si el correo no es válido.
        self.__nombre = nombre.strip()  # Guarda el nombre sin espacios al principio ni al final.
        self.__correo = correo.strip()  # Guarda el correo sin espacios al principio ni al final.

    @property  # Permite consultar el nombre sin cambiarlo directamente.
    def nombre(self):  # Define cómo obtener el nombre del cliente.
        return self.__nombre  # Devuelve el nombre guardado.
    
    @property  # Permite consultar el correo sin cambiarlo directamente.
    def correo(self):  # Define cómo obtener el correo del cliente.
        return self.__correo  # Devuelve el correo guardado.
    
    def describir(self):  # Completa el método que Entidad exige a sus clases hijas.
        return f"Cliente: {self.__nombre}, Correo: {self.__correo}"  # Crea un texto con los datos del cliente.
    
ventana = tk.Tk()  # Crea la ventana principal de la aplicación.
ventana.title("Sistema Integral")  # Coloca el título que aparece en la ventana.
ventana.geometry("1080x720")  # Establece el ancho y el alto iniciales de la ventana.
ventana.grid_columnconfigure(0, weight=1)  # Permite que la primera columna se ajuste al espacio disponible.
ventana.grid_columnconfigure(1, weight=1)  # Permite que la segunda columna se ajuste al espacio disponible.
ventana.grid_columnconfigure(2, weight=1)  # Permite que la tercera columna se ajuste al espacio disponible.
ventana.grid_columnconfigure(3, weight=1)  # Permite que la cuarta columna se ajuste al espacio disponible.
ventana.grid_columnconfigure(4, weight=1)  # Permite que la quinta columna se ajuste al espacio disponible.

titulo = ttk.Label(ventana, text="Sistema software FJ")  # Crea el texto principal de la ventana.
titulo.grid(row=0, column=0, columnspan=2, pady=20)  # Ubica el título en la primera fila, ocupando dos columnas.

Etiqueta_nombre = ttk.Label(ventana, text="Nombre del cliente:")  # Crea la etiqueta que indica dónde escribir el nombre.
Etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="e")  # Coloca la etiqueta junto al campo del nombre.
Entry_nombre = ttk.Entry(ventana)  # Crea el campo donde se escribirá el nombre.
Entry_nombre.grid(row=1, column=1, padx=10, pady=10, sticky="w")  # Ubica el campo del nombre en la ventana.

Etiqueta_correo = ttk.Label(ventana, text="Correo electronico:")  # Crea la etiqueta que indica dónde escribir el correo.
Etiqueta_correo.grid(row=2, column=0, padx=10, pady=10, sticky="e")  # Coloca la etiqueta junto al campo del correo.
Entry_correo = ttk.Entry(ventana)  # Crea el campo donde se escribirá el correo.
Entry_correo.grid(row=2, column=1, padx=10, pady=10, sticky="w")  # Ubica el campo del correo en la ventana.

def ajustar_ancho_casilla_nombre_y_correo(event):  # Ajusta el ancho del campo del nombre cuando se escribe.
    cantidad = len(Entry_nombre.get())  # Cuenta cuántos caracteres tiene el texto del nombre.
    Entry_nombre.config(width=max(20, cantidad + 1))  # Deja al menos 20 espacios y amplía el campo si hace falta.

Entry_nombre.bind("<KeyRelease>", ajustar_ancho_casilla_nombre_y_correo)  # Llama al ajuste cada vez que se suelta una tecla en el nombre.

def ajustar_ancho_casilla_correo(event):  # Ajusta el ancho del campo del correo cuando se escribe.
    cantidad = len(Entry_correo.get())  # Cuenta cuántos caracteres tiene el texto del correo.
    Entry_correo.config(width=max(20, cantidad + 1))  # Deja al menos 20 espacios y amplía el campo si hace falta.

Entry_correo.bind("<KeyRelease>", ajustar_ancho_casilla_correo)  # Llama al ajuste cada vez que se suelta una tecla en el correo.

def registrar_cliente():  # Reúne los datos escritos y valida que estén completos.
    nombre = Entry_nombre.get().strip()  # Lee el nombre y elimina los espacios de los extremos.
    correo = Entry_correo.get().strip()  # Lee el correo y elimina los espacios de los extremos.
    
    if not nombre or not correo:  # Comprueba si falta el nombre o el correo.
        messagebox.showwarning("Datos incompletos", "Por favor escriba el nombre y correo del cliente.")  # Muestra un aviso si falta algún dato.
        return  # Termina aquí para no continuar con datos incompletos.
    messagebox.showinfo("Datos registrados", f"Nombre: {nombre}\nCorreo: {correo}")  # Confirma el registro mostrando los datos ingresados.
    
boton_registrar = ttk.Button(ventana, text="Registrar cliente", command=registrar_cliente)  # Crea el botón y conecta su acción con el registro.
boton_registrar.grid(row=3, column=0, columnspan=2, pady=20)  # Ubica el botón debajo de los campos.

ventana.mainloop()  # Mantiene abierta la ventana y atiende las acciones del usuario.
