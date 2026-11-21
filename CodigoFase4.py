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

def registrar_cliente():  # Valida y guarda el cliente que se escribió en el formulario.
    try:  # Inicia el intento de registrar el cliente.
        nombre = Entry_nombre.get().strip()  # Lee y limpia el nombre del formulario.
        correo = Entry_correo.get().strip()  # Lee y limpia el correo del formulario.
        if not nombre or not correo:  # Comprueba que ambos campos tengan datos.
            raise DatosInvalidosError("Escriba el nombre y el correo del cliente.")
        identificador = f"CLI-{len(sistema_fj.clientes) + 1:03d}"  # Genera el identificador del cliente.
        cliente = Cliente(identificador, nombre, correo)  # Crea el objeto Cliente.
        sistema_fj.registrar_cliente(cliente)  # Guarda el objeto en la lista del sistema.
    except (ErrorSistema, ValueError) as error:  # Controla los errores de validación o registro.
        logging.exception("No se pudo registrar el cliente")  # Guarda el error en el archivo de logs.
        messagebox.showwarning("Datos del cliente", str(error))  # Informa el motivo del error.
    else:  # Se ejecuta cuando el cliente se guardó correctamente.
        actualizar_listas_sistema()  # Refresca las listas y el selector de clientes.
        Entry_nombre.delete(0, tk.END)  # Limpia el campo del nombre.
        Entry_correo.delete(0, tk.END)  # Limpia el campo del correo.
        messagebox.showinfo("Cliente guardado", cliente.describir())  # Confirma que el cliente quedó guardado.
    finally:  # Se ejecuta al terminar el intento, haya éxito o error.
        logging.info("Terminó el intento de registrar un cliente")  # Anota el final del proceso.
boton_registrar = ttk.Button(ventana, text="Registrar cliente", command=registrar_cliente)  # Crea el botón y conecta su acción con el registro.
boton_registrar.grid(row=3, column=0, columnspan=2, pady=20)  # Ubica el botón debajo de los campos.


import logging  # Permite guardar mensajes sobre lo que pasa en el programa.

# Este archivo guarda los eventos y errores del sistema.
logging.basicConfig(  # Elige cómo se guardarán los mensajes del programa.
    filename="software_fj.log",  # Guarda los mensajes en este archivo.
    level=logging.INFO,  # Guarda los mensajes informativos y los errores.
    format="%(asctime)s - %(levelname)s - %(message)s"  # Muestra la fecha, el tipo de mensaje y su texto.
)  # Termina la configuración de los mensajes.


# Excepciones personalizadas para describir los errores del sistema.
class ErrorSistema(Exception):
    def __init__(self, mensaje):  # Prepara un error propio de este programa.
        logging.error(mensaje)  # Guarda el error en el archivo de mensajes.
        super().__init__(mensaje)  # Hace que Python también reconozca este error.


class DatosInvalidosError(ErrorSistema):
    pass  # Se usa cuando algún dato no es válido.


class ServicioNoDisponibleError(ErrorSistema):
    pass  # Se usa cuando no se puede usar un servicio.


class ReservaInvalidaError(ErrorSistema):
    pass  # Se usa cuando hay un problema con una reserva.


class OperacionNoPermitidaError(ErrorSistema):
    pass  # Se usa cuando se intenta hacer algo que no está permitido.


class Servicio(Entidad, ABC):
    """Clase abstracta que representa los servicios de Software FJ."""

    def __init__(self, identificador, nombre, tarifa):  # Recibe el código, el nombre y el precio del servicio.
        super().__init__(identificador)  # Guarda el código del servicio.
        if not nombre or not nombre.strip():  # Mira si el nombre está vacío.
            raise DatosInvalidosError("El nombre del servicio es obligatorio.")  # Muestra un error si falta el nombre.
        if tarifa <= 0:  # Mira si el precio es cero o menor.
            raise DatosInvalidosError("La tarifa debe ser mayor que cero.")  # Muestra un error si el precio no sirve.
        self.nombre = nombre.strip()  # Guarda el nombre sin espacios extra al comienzo o al final.
        self.tarifa = tarifa  # Guarda el precio del servicio.
        self.activo = True  # Indica que el servicio está disponible.

    @abstractmethod  # Indica que cada servicio debe revisar sus propios datos.
    def validar_parametros(self, participantes, cantidad_equipo, modalidad):  # Recibe los datos que se deben revisar.
        pass  # Cada tipo de servicio escribe aquí su propia revisión.

    @abstractmethod  # Indica que cada servicio debe tener su propio cálculo de precio.
    def calcular_costo_base(self, duracion, participantes, cantidad_equipo, modalidad):  # Recibe los datos para calcular el precio.
        pass  # Cada tipo de servicio hace el cálculo a su manera.

    @abstractmethod  # Indica que cada servicio debe poder mostrar sus datos.
    def describir(self):  # Prepara un texto sobre el servicio.
        pass  # Cada tipo de servicio escribe su propia descripción.

    def calcular_costo(self, duracion, impuesto=0, descuento=0,
                       participantes=1, cantidad_equipo=1, modalidad="virtual"):  # Calcula cuánto cuesta la reserva.
        # Los valores después del signo = se usan si no se entrega otro valor.
        if duracion <= 0:  # Mira si la duración es cero o menor.
            raise DatosInvalidosError("La duración debe ser mayor que cero.")  # Muestra un error si no hay duración válida.
        if impuesto < 0 or impuesto > 1:  # Mira si el impuesto está entre 0 y 1.
            raise DatosInvalidosError("El impuesto debe estar entre 0 y 1.")  # Muestra un error si el impuesto no sirve.
        if descuento < 0 or descuento > 1:  # Mira si el descuento está entre 0 y 1.
            raise DatosInvalidosError("El descuento debe estar entre 0 y 1.")  # Muestra un error si el descuento no sirve.
        self.validar_parametros(participantes, cantidad_equipo, modalidad)  # Revisa los datos de acuerdo con el servicio.
        subtotal = self.calcular_costo_base(  # Calcula primero el precio antes de impuesto y descuento.
            duracion, participantes, cantidad_equipo, modalidad  # Envía al cálculo los datos de esta reserva.
        )  # Termina de calcular el precio inicial.
        return round(subtotal * (1 - descuento) * (1 + impuesto), 2)  # Aplica descuento e impuesto y deja dos decimales.

    def reservar(self, participantes, cantidad_equipo, modalidad):  # Revisa si se puede hacer la reserva.
        if not self.activo:  # Mira si el servicio está disponible.
            raise ServicioNoDisponibleError("El servicio está inactivo.")  # Muestra un error si no está disponible.
        self.validar_parametros(participantes, cantidad_equipo, modalidad)  # Revisa los datos de la reserva.

    def liberar(self, cantidad_equipo):  # Se usa para devolver los equipos al cancelar.
        pass  # Este servicio no necesita hacer nada al liberar recursos.


class ServicioSala(Servicio):
    """Reserva de salas por horas."""

    def __init__(self, identificador, nombre, tarifa_hora, capacidad):  # Recibe los datos de una sala.
        super().__init__(identificador, nombre, tarifa_hora)  # Guarda el código, nombre y precio de la sala.
        if capacidad <= 0:  # Mira si la capacidad es cero o menor.
            raise DatosInvalidosError("La capacidad debe ser mayor que cero.")  # Muestra un error si la capacidad no sirve.
        self.capacidad = capacidad  # Guarda cuántas personas caben en la sala.

    def validar_parametros(self, participantes, cantidad_equipo, modalidad):  # Revisa cuántas personas usarán la sala.
        if participantes < 1 or participantes > self.capacidad:  # Mira si hay muy pocas o demasiadas personas.
            raise DatosInvalidosError(  # Muestra un error con la cantidad permitida.
                f"La sala admite entre 1 y {self.capacidad} participantes."  # Explica el límite de personas.
            )  # Termina el mensaje de error.

    def calcular_costo_base(self, duracion, participantes, cantidad_equipo, modalidad):  # Calcula el precio de la sala.
        return self.tarifa * duracion  # Multiplica el precio por hora por las horas reservadas.

    def describir(self):  # Prepara un texto con los datos de la sala.
        return f"Sala {self.nombre}: ${self.tarifa} por hora, capacidad {self.capacidad}"  # Devuelve el nombre, precio y capacidad.


class ServicioEquipo(Servicio):
    """Alquiler de equipos por días."""

    def __init__(self, identificador, nombre, tarifa_dia, unidades):  # Recibe el precio y la cantidad de equipos.
        super().__init__(identificador, nombre, tarifa_dia)  # Guarda el código, nombre y precio del equipo.
        if unidades < 0:  # Mira si la cantidad es menor que cero.
            raise DatosInvalidosError("Las unidades no pueden ser negativas.")  # Muestra un error si la cantidad no sirve.
        self.unidades = unidades  # Guarda cuántos equipos hay.

    def validar_parametros(self, participantes, cantidad_equipo, modalidad):  # Revisa cuántos equipos se quieren alquilar.
        if cantidad_equipo < 1:  # Mira si se pidió menos de un equipo.
            raise DatosInvalidosError("La cantidad de equipos debe ser mayor que cero.")  # Muestra un error si no se pidió ninguno.
        if cantidad_equipo > self.unidades:  # Mira si se pidieron más equipos de los que hay.
            raise ServicioNoDisponibleError("No hay suficientes equipos disponibles.")  # Avisa que faltan equipos.

    def reservar(self, participantes, cantidad_equipo, modalidad):  # Aparta los equipos para una reserva.
        super().reservar(participantes, cantidad_equipo, modalidad)  # Primero revisa que todo esté correcto.
        self.unidades = self.unidades - cantidad_equipo  # Resta los equipos que se apartaron.

    def liberar(self, cantidad_equipo):  # Devuelve los equipos cuando se cancela una reserva.
        self.unidades = self.unidades + cantidad_equipo  # Suma los equipos devueltos.

    def calcular_costo_base(self, duracion, participantes, cantidad_equipo, modalidad):  # Calcula el precio del alquiler.
        return self.tarifa * duracion * cantidad_equipo  # Multiplica precio, días y cantidad de equipos.

    def describir(self):  # Prepara un texto con los datos del equipo.
        return f"Equipo {self.nombre}: ${self.tarifa} por día, disponibles {self.unidades}"  # Muestra precio y cantidad disponible.


class ServicioAsesoria(Servicio):
    """Asesoría especializada virtual o presencial."""

    def validar_parametros(self, participantes, cantidad_equipo, modalidad):  # Revisa cómo será la asesoría.
        if modalidad != "virtual" and modalidad != "presencial":  # Mira si se eligió una de las dos opciones.
            raise DatosInvalidosError("La modalidad debe ser virtual o presencial.")  # Avisa cuáles opciones se pueden usar.

    def calcular_costo_base(self, duracion, participantes, cantidad_equipo, modalidad):  # Calcula el precio de la asesoría.
        costo = self.tarifa * duracion  # Multiplica el precio por la cantidad de horas.
        if modalidad == "presencial":  # Mira si la asesoría será cara a cara.
            costo = costo * 1.15  # Aumenta el precio un 15 por ciento.
        return costo  # Devuelve el precio calculado.

    def describir(self):  # Prepara un texto con los datos de la asesoría.
        return f"Asesoría {self.nombre}: ${self.tarifa} por hora"  # Muestra el nombre y el precio por hora.


class Reserva(Entidad):
    """Une un cliente con un servicio y controla su estado."""

    def __init__(self, identificador, cliente, servicio, duracion,
                 participantes=1, cantidad_equipo=1, modalidad="virtual"):  # Recibe la información de la nueva reserva.
        super().__init__(identificador)  # Guarda el código de la reserva.
        if not isinstance(cliente, Cliente):  # Mira si el cliente es del tipo correcto.
            raise ReservaInvalidaError("La reserva necesita un cliente válido.")  # Avisa si falta un cliente válido.
        if not isinstance(servicio, Servicio):  # Mira si el servicio es del tipo correcto.
            raise ReservaInvalidaError("La reserva necesita un servicio válido.")  # Avisa si falta un servicio válido.
        if duracion <= 0:  # Mira si la duración es mayor que cero.
            raise DatosInvalidosError("La duración debe ser mayor que cero.")  # Avisa si la duración no sirve.
        self.cliente = cliente  # Guarda quién hizo la reserva.
        self.servicio = servicio  # Guarda qué servicio se reservó.
        self.duracion = duracion  # Guarda por cuánto tiempo se reservó.
        self.participantes = participantes  # Guarda cuántas personas participarán.
        self.cantidad_equipo = cantidad_equipo  # Guarda cuántos equipos se pidieron.
        self.modalidad = modalidad  # Guarda si la asesoría será virtual o presencial.
        self.estado = "Pendiente"  # La reserva empieza sin confirmar.
        self.costo = 0  # El costo se calculará más adelante.

    def confirmar(self):  # Intenta confirmar la reserva.
        if self.estado != "Pendiente":  # Mira si la reserva todavía está pendiente.
            raise OperacionNoPermitidaError("Solo se confirma una reserva pendiente.")  # Avisa si ya no se puede confirmar.
        try:  # Intenta apartar el servicio.
            self.servicio.reservar(  # Pide al servicio que revise la solicitud.
                self.participantes, self.cantidad_equipo, self.modalidad  # Envía los datos de la reserva.
            )  # Termina la solicitud para apartar el servicio.
        except ErrorSistema as error:  # Se ejecuta si hubo un problema al apartar el servicio.
            logging.exception("No se pudo confirmar la reserva %s", self.identificador)  # Guarda el problema en el archivo.
            raise ReservaInvalidaError("La reserva no se pudo confirmar.") from error  # Muestra que no se pudo confirmar.
        else:  # Se ejecuta si todo salió bien.
            self.estado = "Confirmada"  # Cambia el estado de la reserva.
            logging.info("Reserva %s confirmada", self.identificador)  # Guarda que la reserva fue confirmada.
        finally:  # Se ejecuta haya salido bien o mal.
            logging.info("Terminó el intento de confirmar la reserva")  # Guarda que terminó el intento.

    def cancelar(self):  # Cancela la reserva.
        if self.estado != "Pendiente" and self.estado != "Confirmada":  # Mira si todavía se puede cancelar.
            raise OperacionNoPermitidaError("La reserva ya no se puede cancelar.")  # Avisa si ya no se permite cancelarla.
        if self.estado == "Confirmada":  # Mira si ya se habían apartado equipos.
            self.servicio.liberar(self.cantidad_equipo)  # Devuelve los equipos que se habían apartado.
        self.estado = "Cancelada"  # Cambia el estado para indicar que se canceló.
        logging.info("Reserva %s cancelada", self.identificador)  # Guarda que la reserva fue cancelada.

    def procesar(self, impuesto=0, descuento=0):  # Calcula el precio de la reserva.
        if self.estado != "Confirmada":  # Mira si la reserva ya fue confirmada.
            raise OperacionNoPermitidaError("La reserva debe estar confirmada.")  # Avisa que primero hay que confirmarla.
        try:  # Intenta calcular el precio.
            self.costo = self.servicio.calcular_costo(  # Pide al servicio que calcule cuánto cuesta.
                self.duracion, impuesto, descuento, self.participantes,  # Envía duración, impuesto, descuento y participantes.
                self.cantidad_equipo, self.modalidad  # Envía también equipos y modalidad.
            )  # Termina el cálculo.
        except Exception as error:  # Se ejecuta si ocurrió un problema al calcular.
            logging.exception("No se pudo procesar la reserva %s", self.identificador)  # Guarda el problema en el archivo.
            raise ReservaInvalidaError("No se pudo calcular el costo.") from error  # Informa que no se pudo calcular el precio.
        else:  # Se ejecuta si el cálculo salió bien.
            self.estado = "Completada"  # Indica que la reserva ya terminó.
            logging.info("Reserva %s completada", self.identificador)  # Guarda que la reserva fue completada.
            return self.costo  # Entrega el precio calculado.
        finally:  # Se ejecuta haya salido bien o mal.
            logging.info("Terminó el intento de procesar la reserva")  # Guarda que terminó el intento.

    def describir(self):  # Prepara un texto corto sobre la reserva.
        return (  # Junta las partes del texto.
            f"{self.identificador} - {self.cliente.nombre} - "  # Añade el código y el nombre del cliente.
            f"{self.servicio.nombre} - {self.estado}"  # Añade el servicio y el estado de la reserva.
        )  # Devuelve el texto completo.


class SistemaGestion:
    """Guarda los objetos en listas durante la ejecución."""

    def __init__(self):  # Prepara las colecciones que almacenan los datos en memoria.
        self.clientes = []  # Crea la lista de clientes registrados.
        self.servicios = []  # Crea la lista de servicios disponibles.
        self.reservas = []  # Crea la lista de reservas creadas.

    def registrar_cliente(self, cliente):  # Valida y agrega un cliente a la lista.
        if not isinstance(cliente, Cliente):  # Comprueba que se reciba una instancia de Cliente.
            raise DatosInvalidosError("Se debe registrar un objeto Cliente.")  # Rechaza objetos de otro tipo.
        correo = cliente.correo  # Obtiene el correo para validarlo.
        if " " in correo or "@" not in correo or "." not in correo:  # Busca espacios y partes básicas del formato del correo.
            raise DatosInvalidosError("El correo no tiene un formato válido.")  # Rechaza una dirección con formato incorrecto.
        for cliente_guardado in self.clientes:  # Revisa los clientes que ya están almacenados.
            if cliente_guardado.identificador == cliente.identificador:  # Compara el identificador con cada cliente existente.
                raise DatosInvalidosError("Ese cliente ya está registrado.")  # Evita guardar el mismo identificador dos veces.
        self.clientes.append(cliente)  # Agrega el cliente validado a la lista.
        logging.info("Cliente %s registrado", cliente.identificador)  # Registra el alta del cliente.
        return cliente  # Devuelve el objeto que se acaba de registrar.

    def registrar_servicio(self, servicio):  # Valida y agrega un servicio a la lista.
        if not isinstance(servicio, Servicio):  # Comprueba que el objeto pertenezca a la jerarquía Servicio.
            raise DatosInvalidosError("Se debe registrar un objeto Servicio.")  # Rechaza objetos que no sean servicios.
        for servicio_guardado in self.servicios:  # Recorre los servicios que ya están registrados.
            if servicio_guardado.identificador == servicio.identificador:  # Compara los identificadores de servicio.
                raise DatosInvalidosError("Ese servicio ya está registrado.")  # Evita duplicar el identificador.
        self.servicios.append(servicio)  # Guarda el servicio validado en la lista.
        logging.info("Servicio %s registrado", servicio.identificador)  # Registra el alta del servicio.
        return servicio  # Devuelve el servicio registrado.

    def buscar_cliente(self, identificador):  # Busca al cliente cuyo identificador se recibió.
        for cliente in self.clientes:  # Revisa cada cliente almacenado.
            if cliente.identificador == identificador:  # Comprueba si este cliente coincide con el identificador.
                return cliente  # Devuelve el primer cliente coincidente.
        raise DatosInvalidosError("No se encontró el cliente seleccionado.")  # Informa que no hubo coincidencias.

    def buscar_servicio(self, identificador):  # Busca el servicio cuyo identificador se recibió.
        for servicio in self.servicios:  # Revisa cada servicio almacenado.
            if servicio.identificador == identificador:  # Comprueba si el servicio actual coincide.
                return servicio  # Devuelve el servicio encontrado.
        raise DatosInvalidosError("No se encontró el servicio seleccionado.")  # Informa que no hubo coincidencias.

    def crear_reserva(self, id_cliente, id_servicio, duracion,
                      participantes=1, cantidad_equipo=1, modalidad="virtual"):  # Crea una reserva con los datos recibidos.
        cliente = self.buscar_cliente(id_cliente)  # Recupera el cliente asociado a la reserva.
        servicio = self.buscar_servicio(id_servicio)  # Recupera el servicio que se desea reservar.
        identificador = f"RES-{len(self.reservas) + 1:03d}"  # Genera un código secuencial con tres dígitos.
        reserva = Reserva(  # Construye el objeto de reserva.
            identificador, cliente, servicio, duracion,  # Pasa el código, el cliente, el servicio y la duración.
            participantes, cantidad_equipo, modalidad  # Pasa los parámetros específicos del servicio.
        )  # Termina la construcción de la reserva.
        self.reservas.append(reserva)  # Guarda la nueva reserva en la lista del sistema.
        logging.info("Reserva %s creada", identificador)  # Registra la creación de la reserva.
        return reserva  # Devuelve la reserva creada para poder operar con ella.


def simular_diez_operaciones(sistema_base):  # Ejecuta pruebas con datos actuales sin alterar el sistema real.
    """Realiza operaciones válidas e inválidas y continúa ante los errores."""
    if sistema_base.clientes:
        cliente_base = sistema_base.clientes[-1]
        origen_cliente = "cliente registrado"
    else:
        cliente_base = Cliente("CLI-BASE", "Cliente de prueba", "demo@example.com")
        origen_cliente = "datos de demostración (no hay clientes registrados)"
    sala_base = next(
        (servicio for servicio in sistema_base.servicios if isinstance(servicio, ServicioSala)),
        None,
    )
    equipo_base = next(
        (servicio for servicio in sistema_base.servicios if isinstance(servicio, ServicioEquipo)),
        None,
    )
    asesoria_base = next(
        (servicio for servicio in sistema_base.servicios if isinstance(servicio, ServicioAsesoria)),
        None,
    )
    if sala_base is None or equipo_base is None or asesoria_base is None:
        return "Se necesita una sala, un equipo y una asesoría registrados para simular."

    participantes_sala = min(5, sala_base.capacidad)
    sistema_demo = SistemaGestion()  # Crea un sistema separado para que la demostración no use los datos de la ventana.
    resultados = []  # Prepara una lista de mensajes para mostrar el resultado de cada prueba.
    aciertos = 0  # Inicializa el contador de operaciones exitosas.
    reserva_sala = None  # Reserva una variable para reutilizar la reserva creada en la operación 7.

    # Operación 1: registro válido de cliente.
    try:  # Intenta registrar un cliente con datos correctos.
        cliente_demo = Cliente("CLI-D1", cliente_base.nombre, cliente_base.correo)  # Usa los datos del último cliente registrado.
        sistema_demo.registrar_cliente(cliente_demo)  # Guarda al cliente en el sistema de demostración.
    except Exception as error:  # Captura cualquier error inesperado de esta prueba.
        logging.exception("Operación 1 fallida")  # Registra el error y su traza.
        resultados.append(f"1. Error: {error}")  # Añade el detalle del error a los resultados visibles.
    else:  # Se ejecuta si la operación terminó correctamente.
        aciertos = aciertos + 1  # Cuenta esta operación como exitosa.
        resultados.append(f"1. Cliente válido registrado: {cliente_demo.nombre}")  # Confirma el cliente usado como referencia.
    finally:  # Se ejecuta tanto si la operación tuvo éxito como si falló.
        logging.info("Terminó la operación 1")  # Registra el cierre de la prueba.

    # Operación 2: registro inválido de cliente.
    try:  # Prueba qué sucede al usar un correo sin formato válido.
        cliente_malo = Cliente("CLI-D2", "Luis", "correo-invalido")  # Crea un cliente con un correo incorrecto.
        sistema_demo.registrar_cliente(cliente_malo)  # Intenta guardar el cliente inválido.
    except ValueError as error:  # Captura el rechazo esperado del correo inválido.
        logging.exception("Operación 2 inválida controlada")  # Deja constancia de que el error fue controlado.
        aciertos = aciertos + 1  # Cuenta como correcta la detección del dato inválido.
        resultados.append("2. Error de cliente inválido controlado")  # Añade el resultado esperado a la lista.
    else:  # Se ejecuta si no se produjo el error que debía ocurrir.
        resultados.append("2. Cliente registrado")  # Informa que se registró el cliente.
    finally:  # Se ejecuta al terminar la prueba, haya fallado o no.
        logging.info("Terminó la operación 2")  # Registra el cierre de la prueba.

    # Operación 3: servicio correcto.
    try:  # Intenta registrar una sala con parámetros válidos.
        sala = ServicioSala("SAL-D1", sala_base.nombre, sala_base.tarifa, sala_base.capacidad)  # Usa los datos de una sala registrada.
        sistema_demo.registrar_servicio(sala)  # Añade la sala al sistema de demostración.
    except Exception as error:  # Captura cualquier error ocurrido al crear o registrar la sala.
        logging.exception("Operación 3 fallida")  # Registra el error y su traza.
        resultados.append(f"3. Error: {error}")  # Añade el detalle del error.
    else:  # Se ejecuta si el servicio se registró correctamente.
        aciertos = aciertos + 1  # Cuenta la operación como exitosa.
        resultados.append(f"3. Servicio de sala registrado: {sala.nombre} (${sala.tarifa})")  # Confirma los datos de la sala registrada.
    finally:  # Se ejecuta al terminar la prueba en cualquier caso.
        logging.info("Terminó la operación 3")  # Registra el cierre de la prueba.
   # Operación 4: servicio incorrecto.
    try:  # Prueba la validación del aforo de una sala.
        sala_mala = ServicioSala("SAL-D2", "Sala inválida", 10000, 0)  # Intenta crear una sala con capacidad cero.
        sistema_demo.registrar_servicio(sala_mala)  # Esta instrucción solo se alcanzaría si la sala fuera válida.
    except DatosInvalidosError as error:  # Captura el rechazo esperado de la capacidad no válida.
        logging.exception("Operación 4 inválida controlada")  # Registra la excepción controlada.
        aciertos = aciertos + 1  # Cuenta como correcta la detección del servicio inválido.
        resultados.append("4. Error de servicio inválido controlado")  # Informa que la validación rechazó la sala.
    else:  # Se ejecuta si no se produjo el error esperado.
        resultados.append("4. Servicio registrado")  # Informa que se registró el servicio.
    finally:  # Se ejecuta independientemente del resultado.
        logging.info("Terminó la operación 4")  # Registra el cierre de la prueba.

    # Operación 5: servicio de equipo.
    try:  # Intenta crear y agregar un servicio de alquiler de equipos.
        equipo = ServicioEquipo("EQU-D1", equipo_base.nombre, equipo_base.tarifa, equipo_base.unidades)  # Usa un equipo registrado.
        sistema_demo.registrar_servicio(equipo)  # Registra el proyector en el sistema de demostración.
    except Exception as error:  # Captura cualquier error de creación o registro.
        logging.exception("Operación 5 fallida")  # Registra el error y su traza.
        resultados.append(f"5. Error: {error}")  # Añade el detalle del error a los resultados.
    else:  # Se ejecuta cuando el registro fue exitoso.
        aciertos = aciertos + 1  # Cuenta la operación como exitosa.
        resultados.append(f"5. Servicio de equipo registrado: {equipo.nombre} (${equipo.tarifa})")  # Confirma los datos del equipo.
    finally:  # Se ejecuta al finalizar la operación.
        logging.info("Terminó la operación 5")  # Registra el cierre de la prueba.

    # Operación 6: servicio de asesoría.
    try:  # Intenta registrar un servicio de asesoría.
        asesoria = ServicioAsesoria("ASE-D1", asesoria_base.nombre, asesoria_base.tarifa)  # Usa una asesoría registrada.
        sistema_demo.registrar_servicio(asesoria)  # Agrega la asesoría al sistema de demostración.
    except Exception as error:  # Captura errores que puedan surgir al registrar el servicio.
        logging.exception("Operación 6 fallida")  # Registra el error y su traza.
        resultados.append(f"6. Error: {error}")  # Añade el detalle del error.
    else:  # Se ejecuta si la asesoría se registró correctamente.
        aciertos = aciertos + 1  # Cuenta la operación como exitosa.
        resultados.append(f"6. Servicio de asesoría registrado: {asesoria.nombre} (${asesoria.tarifa})")  # Confirma los datos de asesoría.
    finally:  # Se ejecuta tanto en caso de éxito como de error.
        logging.info("Terminó la operación 6")  # Registra el cierre de la prueba.

    # Operación 7: reserva confirmada.
    try:  # Crea una reserva de sala e intenta confirmarla.
        reserva_sala = sistema_demo.crear_reserva(  # Solicita al sistema generar una reserva nueva.
            "CLI-D1", "SAL-D1", 2, participantes=participantes_sala  # Usa los datos del cliente y la capacidad de la sala registrada.
        )  # Guarda la reserva creada para procesarla en la operación siguiente.
        reserva_sala.confirmar()  # Valida y confirma la reserva de la sala.
    except Exception as error:  # Captura cualquier error de creación o confirmación.
        logging.exception("Operación 7 fallida")  # Registra el error y su traza.
        resultados.append(f"7. Error: {error}")  # Añade el detalle del error a los resultados.
    else:  # Se ejecuta si la reserva pudo confirmarse.
        aciertos = aciertos + 1  # Cuenta la confirmación como exitosa.
        resultados.append(f"7. Reserva confirmada para {cliente_demo.nombre} en {sala.nombre}")  # Confirma los datos usados.
    finally:  # Se ejecuta siempre al terminar esta prueba.
        logging.info("Terminó la operación 7")  # Registra el cierre de la prueba.

    # Operación 8: cálculo con descuento e impuesto.
    try:  # Calcula el costo final de la reserva confirmada.
        costo = reserva_sala.procesar(impuesto=0.19, descuento=0.10)  # Aplica 19 % de impuesto y 10 % de descuento.
    except Exception as error:  # Captura cualquier error en el procesamiento.
        logging.exception("Operación 8 fallida")  # Registra el error y su traza.
        resultados.append(f"8. Error: {error}")  # Añade el detalle del fallo.
    else:  # Se ejecuta si el costo se calculó correctamente.
        aciertos = aciertos + 1  # Cuenta el procesamiento como operación exitosa.
        resultados.append(f"8. Reserva procesada por ${costo:.2f}")  # Añade el costo con dos decimales.
    finally:  # Se ejecuta independientemente de que el cálculo funcione.
        logging.info("Terminó la operación 8")  # Registra el cierre de la prueba.

    # Operación 9: reserva con duración inválida.
    try:  # Prueba que se rechace una duración de cero.
        sistema_demo.crear_reserva("CLI-D1", "SAL-D1", 0, participantes=2)  # Intenta crear una reserva con duración inválida.
    except DatosInvalidosError as error:  # Captura el rechazo esperado de la duración no positiva.
        logging.exception("Operación 9 inválida controlada")  # Registra la excepción que valida el caso.
        aciertos = aciertos + 1  # Cuenta como correcta la detección de la reserva inválida.
        resultados.append("9. Error de duración controlado")  # Informa que el dato inválido fue rechazado.
    else:  # Se ejecuta si la reserva fue creada pese al dato inválido.
        resultados.append("9. Reserva creada")  # Informa que la reserva llegó a crearse.
    finally:  # Se ejecuta al finalizar la prueba.
        logging.info("Terminó la operación 9")  # Registra el cierre de la prueba.

    # Operación 10: intento con equipo agotado.
    try:  # Simula una solicitud cuando el inventario está agotado.
        equipo.unidades = 0  # Establece en cero las unidades disponibles del proyector.
        reserva_equipo = sistema_demo.crear_reserva(  # Crea una reserva para intentar pedir el equipo.
            "CLI-D1", "EQU-D1", 1, cantidad_equipo=1  # Solicita un equipo durante un día.
        )  # Guarda la reserva creada para intentar confirmarla.
        reserva_equipo.confirmar()  # Intenta apartar el equipo y provoca el error si no hay existencias.
    except ReservaInvalidaError as error:  # Captura la reserva rechazada por falta de equipos.
        logging.exception("Operación 10 no disponible controlada")  # Registra la excepción de disponibilidad.
        aciertos = aciertos + 1  # Cuenta como correcta la detección de la falta de equipos.
        resultados.append("10. Falta de equipos controlada")  # Informa que el inventario agotado fue detectado.
    else:  # Se ejecuta si el sistema permitió confirmar el equipo.
        resultados.append("10. Reserva de equipo confirmada")  # Confirma la reserva en los resultados.
    finally:  # Se ejecuta al finalizar la prueba.
        logging.info("Terminó la operación 10")  # Registra el cierre de la prueba.

    # Operación 11: reserva cancelada.
    try:  # Crea una segunda reserva y la cancela después de confirmarla.
        reserva_cancelar = sistema_demo.crear_reserva(  # Solicita crear una reserva nueva de sala.
            "CLI-D1", "SAL-D1", 1, participantes=min(2, sala_base.capacidad)  # Ajusta los participantes a la capacidad registrada.
        )  # Guarda la reserva que se cancelará.
        reserva_cancelar.confirmar()  # Confirma la reserva y aparta el servicio.
        reserva_cancelar.cancelar()  # Cancela la reserva y libera los recursos si aplica.
    except Exception as error:  # Captura errores de creación, confirmación o cancelación.
        logging.exception("Operación 11 fallida")  # Registra el error y su traza.
        resultados.append(f"11. Error: {error}")  # Añade el detalle del error.
    else:  # Se ejecuta si la reserva fue confirmada y cancelada correctamente.
        aciertos = aciertos + 1  # Cuenta la operación como exitosa.
        resultados.append("11. Reserva confirmada y cancelada")  # Informa el resultado de la prueba.
    finally:  # Se ejecuta al terminar la operación en cualquier caso.
        logging.info("Terminó la operación 11")  # Registra el cierre de la prueba.

    resultados.append(  # Muestra qué datos reales sirvieron de base para estas pruebas.
        f"\nDatos de referencia: {cliente_base.nombre}, {sala_base.nombre}, "
        f"{equipo_base.nombre} y {asesoria_base.nombre}."
    )
    resultados.append(f"Origen del cliente de prueba: {origen_cliente}.")
    resultados.append(  # Indica cuántos registros reales hay al momento de simular.
        f"Reservas reales registradas: {len(sistema_base.reservas)}."
    )
    for reserva_real in sistema_base.reservas[-3:]:
        resultados.append(f"  {reserva_real.describir()} (costo: ${reserva_real.costo:.2f})")
    resultados.append(f"Operaciones correctas: {aciertos} de 11")  # Añade el total de operaciones exitosas.
    return "\n".join(resultados)  # Une los mensajes separados por saltos de línea y los devuelve.


# Los datos de negocio permanecen en las listas durante la ejecución.
sistema_fj = SistemaGestion()
sistema_fj.registrar_servicio(ServicioSala("SAL-01", "Sala principal", 25000, 20))
sistema_fj.registrar_servicio(ServicioEquipo("EQU-01", "Proyector", 40000, 5))
sistema_fj.registrar_servicio(ServicioAsesoria("ASE-01", "Asesoría especializada", 60000))

# Panel agregado para crear y administrar reservas.
ventana.geometry("1150x900")  # Amplía la ventana para que quepan los controles de reservas.
marco_sistema = ttk.LabelFrame(ventana, text="Servicios y reservas")  # Crea un panel con título para agrupar los controles.
marco_sistema.grid(row=4, column=0, columnspan=5, padx=12, pady=10, sticky="nsew")  # Ubica el panel debajo del formulario de cliente.
for columna in range(6):  # Recorre las seis columnas disponibles en el panel.
    marco_sistema.grid_columnconfigure(columna, weight=1)  # Permite que cada columna se expanda proporcionalmente.

lista_clientes_sistema = tk.Listbox(marco_sistema, height=4, width=45)  # Crea la lista visual de clientes registrados.
lista_clientes_sistema.grid(row=1, column=0, columnspan=3, padx=8, pady=4, sticky="nsew")  # Sitúa la lista en la mitad izquierda.
ttk.Label(marco_sistema, text="Clientes guardados").grid(row=0, column=0, columnspan=3)  # Añade el título de la lista de clientes.
lista_servicios_sistema = tk.Listbox(marco_sistema, height=4, width=60)  # Crea la lista visual de servicios.
lista_servicios_sistema.grid(row=1, column=3, columnspan=3, padx=8, pady=4, sticky="nsew")  # Sitúa los servicios en la mitad derecha.
ttk.Label(marco_sistema, text="Servicios disponibles").grid(row=0, column=3, columnspan=3)  # Añade el título de la lista de servicios.

marco_cliente = ttk.Frame(marco_sistema)  # Agrupa la etiqueta y el selector de cliente.
marco_cliente.grid(row=2, column=0, columnspan=2, padx=8, pady=(10, 4), sticky="ew")
marco_cliente.grid_columnconfigure(0, weight=1)
ttk.Label(marco_cliente, text="Cliente ID").grid(row=0, column=0, sticky="w")
selector_cliente = ttk.Combobox(marco_cliente, state="readonly", width=18)  # Crea un menú desplegable para elegir un cliente.
selector_cliente.grid(row=1, column=0, pady=(3, 0), sticky="ew")

marco_servicio = ttk.Frame(marco_sistema)  # Agrupa la etiqueta y el selector de servicio.
marco_servicio.grid(row=2, column=2, columnspan=2, padx=8, pady=(10, 4), sticky="ew")
marco_servicio.grid_columnconfigure(0, weight=1)
ttk.Label(marco_servicio, text="Servicio ID").grid(row=0, column=0, sticky="w")
selector_servicio = ttk.Combobox(marco_servicio, state="readonly", width=18)  # Crea un menú desplegable de servicios.
selector_servicio.grid(row=1, column=0, pady=(3, 0), sticky="ew")

marco_duracion = ttk.Frame(marco_sistema)  # Agrupa la etiqueta y el campo de duración.
marco_duracion.grid(row=2, column=4, columnspan=2, padx=8, pady=(10, 4), sticky="ew")
ttk.Label(marco_duracion, text="Duración").grid(row=0, column=0, sticky="w")  # Muestra el texto que identifica la duración.
entrada_duracion = ttk.Entry(marco_duracion, width=10)  # Crea el campo para introducir la duración.
entrada_duracion.insert(0, "1")  # Coloca una duración inicial de una unidad de tiempo.
entrada_duracion.grid(row=1, column=0, pady=(3, 0), sticky="w")  # Sitúa la casilla debajo de su etiqueta.

marco_participantes = ttk.Frame(marco_sistema)  # Agrupa la etiqueta y la cantidad de participantes.
marco_participantes.grid(row=3, column=0, columnspan=2, padx=8, pady=4, sticky="ew")
ttk.Label(marco_participantes, text="Participantes para sala").grid(row=0, column=0, sticky="w")  # Identifica el campo de asistentes.
entrada_participantes = ttk.Entry(marco_participantes, width=10)  # Crea la entrada para la cantidad de participantes.
entrada_participantes.insert(0, "2")  # Propone dos participantes como valor inicial.
entrada_participantes.grid(row=1, column=0, pady=(3, 0), sticky="w")  # Ubica el campo debajo de su etiqueta.

marco_equipos = ttk.Frame(marco_sistema)  # Agrupa la etiqueta y la cantidad de equipos.
marco_equipos.grid(row=3, column=2, columnspan=2, padx=8, pady=4, sticky="ew")
ttk.Label(marco_equipos, text="Equipos para alquilar").grid(row=0, column=0, sticky="w")  # Identifica el campo de unidades de equipo.
entrada_cantidad_equipo = ttk.Entry(marco_equipos, width=10)  # Crea el campo para la cantidad de equipos.
entrada_cantidad_equipo.insert(0, "1")  # Propone un equipo como cantidad inicial.
entrada_cantidad_equipo.grid(row=1, column=0, pady=(3, 0), sticky="w")  # Ubica el campo debajo de su etiqueta.

marco_modalidad = ttk.Frame(marco_sistema)  # Agrupa la etiqueta y el selector de modalidad.
marco_modalidad.grid(row=3, column=4, columnspan=2, padx=8, pady=4, sticky="ew")
ttk.Label(marco_modalidad, text="Modalidad asesoría").grid(row=0, column=0, sticky="w")  # Identifica el campo de modalidad.
selector_modalidad = ttk.Combobox(  # Crea un menú desplegable para elegir la modalidad de asesoría.
    marco_modalidad, state="readonly", width=16, values=("virtual", "presencial")
)  # Limita las opciones a las modalidades aceptadas por el sistema.
selector_modalidad.current(0)  # Selecciona virtual como modalidad inicial.
selector_modalidad.grid(row=1, column=0, pady=(3, 0), sticky="w")  # Ubica el selector debajo de su etiqueta.

lista_reservas_sistema = tk.Listbox(marco_sistema, height=4, width=100)  # Crea el área que mostrará las reservas registradas.
lista_reservas_sistema.grid(row=6, column=0, columnspan=6, padx=8, pady=4, sticky="nsew")  # Extiende la lista de reservas por todo el panel.
ttk.Label(marco_sistema, text="Reservas").grid(row=5, column=0, columnspan=6)  # Añade el título de la lista de reservas.
selector_reserva = ttk.Combobox(marco_sistema, state="readonly", width=14)  # Crea un selector para elegir una reserva por su código.
selector_reserva.grid(row=7, column=2, columnspan=2, padx=4, pady=8, sticky="ew")  # Ubica el selector debajo de la lista de reservas.


def actualizar_listas_sistema():  # Actualiza lo que muestran las listas y menús desplegables.
    lista_clientes_sistema.delete(0, tk.END)  # Borra los clientes mostrados anteriormente.
    for cliente in sistema_fj.clientes:  # Recorre los clientes guardados en el sistema principal.
        lista_clientes_sistema.insert(tk.END, cliente.describir())  # Muestra la descripción de cada cliente.
    lista_servicios_sistema.delete(0, tk.END)  # Borra los servicios mostrados anteriormente.
    for servicio in sistema_fj.servicios:  # Recorre los servicios registrados.
        lista_servicios_sistema.insert(tk.END, servicio.describir())  # Muestra la descripción de cada servicio.
    lista_reservas_sistema.delete(0, tk.END)  # Borra las reservas mostradas anteriormente.
    for reserva in sistema_fj.reservas:  # Recorre todas las reservas existentes.
        lista_reservas_sistema.insert(tk.END, reserva.describir())  # Muestra la descripción y estado de cada reserva.

    ids_clientes = []  # Prepara la lista de identificadores para el selector de clientes.
    for cliente in sistema_fj.clientes:  # Recorre los clientes disponibles.
        ids_clientes.append(cliente.identificador)  # Añade el código de cada cliente a la lista.
    selector_cliente["values"] = ids_clientes  # Carga los códigos en el menú desplegable de clientes.
    ids_servicios = []  # Prepara la lista de identificadores de servicios.
    for servicio in sistema_fj.servicios:  # Recorre los servicios disponibles.
        ids_servicios.append(servicio.identificador)  # Añade el código de cada servicio a la lista.
    selector_servicio["values"] = ids_servicios  # Carga los códigos en el menú desplegable de servicios.
    ids_reservas = []  # Prepara la lista de identificadores de reservas.
    for reserva in sistema_fj.reservas:  # Recorre las reservas registradas.
        ids_reservas.append(reserva.identificador)  # Añade el código de cada reserva a la lista.
    selector_reserva["values"] = ids_reservas  # Carga los códigos en el menú desplegable de reservas.


def crear_reserva_desde_formulario():  # Crea y confirma una reserva usando los datos de la interfaz.
    reserva = None
    try:  # Inicia la lectura y validación de los controles.
        duracion = float(entrada_duracion.get())  # Convierte el texto de duración a número decimal.
        participantes = int(entrada_participantes.get())  # Convierte el texto de participantes a entero.
        cantidad_equipo = int(entrada_cantidad_equipo.get())  # Convierte la cantidad de equipos a entero.
        modalidad = selector_modalidad.get()  # Lee la modalidad seleccionada.
        reserva = sistema_fj.crear_reserva(  # Pide al sistema construir una reserva con los datos ingresados.
            selector_cliente.get(), selector_servicio.get(), duracion,  # Pasa los identificadores seleccionados y la duración.
            participantes, cantidad_equipo, modalidad  # Pasa el resto de parámetros del servicio.
        )  # Guarda el objeto de reserva creado.
        reserva.confirmar()  # Valida la disponibilidad y confirma la reserva.
    except (ErrorSistema, ValueError) as error:  # Captura errores del sistema o conversiones numéricas incorrectas.
        logging.exception("No se pudo crear la reserva desde la ventana")  # Registra el fallo con su traza.
        if reserva is not None and reserva.estado == "Pendiente":
            sistema_fj.reservas.remove(reserva)
            logging.info("Se retiró la reserva %s porque no pudo confirmarse", reserva.identificador)
        actualizar_listas_sistema()  # Refresca las listas por si el estado cambió antes del error.
        messagebox.showwarning("Reserva no creada", str(error))  # Informa al usuario del motivo del fallo.
    else:  # Se ejecuta cuando la reserva se creó y confirmó correctamente.
        actualizar_listas_sistema()  # Muestra la nueva reserva y actualiza los selectores.
        messagebox.showinfo("Reserva creada", f"La reserva {reserva.identificador} está confirmada.")  # Confirma el resultado al usuario.
    finally:  # Se ejecuta al terminar el intento, con éxito o con error.
        logging.info("Terminó el intento de crear reserva")  # Registra el cierre del intento.


def procesar_reserva_seleccionada():  # Calcula el costo de la reserva elegida en el selector.
    try:  # Inicia la búsqueda y el procesamiento de la reserva.
        reserva = None  # Inicializa la variable para detectar si se encontró la reserva.
        for reserva_guardada in sistema_fj.reservas:  # Recorre todas las reservas registradas.
            if reserva_guardada.identificador == selector_reserva.get():  # Compara el identificador con la opción seleccionada.
                reserva = reserva_guardada  # Guarda la reserva que coincide con el selector.
        if reserva is None:  # Comprueba que se haya encontrado una reserva seleccionada.
            raise DatosInvalidosError("Seleccione una reserva.")  # Solicita una selección si no se encontró ninguna.
        costo = reserva.procesar(impuesto=0.19)  # Procesa la reserva aplicando un impuesto del 19 por ciento.
    except ErrorSistema as error:  # Captura errores de estado o validación del sistema.
        logging.exception("No se pudo procesar la reserva seleccionada")  # Registra la excepción y su traza.
        messagebox.showwarning("No se pudo procesar", str(error))  # Muestra el motivo por el que no se pudo procesar.
    else:  # Se ejecuta cuando el cálculo terminó sin errores.
        actualizar_listas_sistema()  # Refresca la lista para mostrar el nuevo estado de la reserva.
        messagebox.showinfo("Reserva procesada", f"Costo final: ${costo:.2f}")  # Muestra el costo final con dos decimales.
    finally:  # Se ejecuta al terminar el intento de procesamiento.
        logging.info("Terminó el intento de procesar reserva")  # Registra el cierre del intento.


def cancelar_reserva_seleccionada():  # Cancela la reserva elegida en el selector.
    try:  # Inicia la búsqueda de la reserva y su cancelación.
        reserva = None  # Inicializa la variable que contendrá la reserva encontrada.
        for reserva_guardada in sistema_fj.reservas:  # Revisa las reservas almacenadas.
            if reserva_guardada.identificador == selector_reserva.get():  # Comprueba si coincide con el identificador elegido.
                reserva = reserva_guardada  # Conserva la reserva coincidente.
        if reserva is None:  # Comprueba que se haya seleccionado una reserva existente.
            raise DatosInvalidosError("Seleccione una reserva.")  # Informa que debe elegirse una reserva.
        reserva.cancelar()  # Cambia el estado de la reserva a cancelada.
    except ErrorSistema as error:  # Captura errores si el estado no permite cancelar.
        logging.exception("No se pudo cancelar la reserva seleccionada")  # Registra la excepción con su traza.
        messagebox.showwarning("No se pudo cancelar", str(error))  # Informa al usuario por qué no se canceló.
    else:  # Se ejecuta cuando la cancelación terminó correctamente.
        actualizar_listas_sistema()  # Refresca las listas para mostrar el nuevo estado.
        messagebox.showinfo("Reserva cancelada", reserva.identificador)  # Confirma la cancelación con su código.
    finally:  # Se ejecuta al final del intento en cualquier caso.
        logging.info("Terminó el intento de cancelar reserva")  # Registra el cierre del intento.


def mostrar_simulacion():  # Ejecuta la simulación y muestra sus resultados en la ventana.
    try:  # Inicia la preparación del cuadro de texto de resultados.
        salida_operaciones.configure(state="normal")  # Habilita temporalmente la edición del cuadro.
        salida_operaciones.delete("1.0", tk.END)  # Borra el texto de la simulación anterior.
        salida_operaciones.insert(tk.END, simular_diez_operaciones(sistema_fj))  # Usa los datos actuales como base de las pruebas.
        salida_operaciones.configure(state="disabled")  # Impide que el usuario modifique el resultado mostrado.
    except Exception as error:  # Captura errores al ejecutar o mostrar la simulación.
        logging.exception("No se pudo mostrar la simulación")  # Registra el error y su traza.
        messagebox.showerror("Error", str(error))  # Muestra una ventana con el detalle del error.


ttk.Button(marco_sistema, text="Crear y confirmar reserva", command=crear_reserva_desde_formulario).grid(  # Crea y ubica el botón para reservar.
    row=7, column=0, columnspan=2, padx=8, pady=8, sticky="e"  # Coloca el botón al inicio de la fila de acciones.
)  # Finaliza la configuración de posición del botón.
ttk.Button(marco_sistema, text="Procesar", command=procesar_reserva_seleccionada).grid(  # Crea el botón para calcular el costo.
    row=7, column=4, padx=8, pady=8, sticky="e"  # Ubica el botón de procesamiento debajo de la lista.
)  # Finaliza la configuración de posición del botón.
ttk.Button(marco_sistema, text="Cancelar", command=cancelar_reserva_seleccionada).grid(  # Crea el botón para cancelar una reserva.
    row=7, column=5, padx=8, pady=8, sticky="w"  # Ubica el botón de cancelación junto al botón de procesamiento.
)  # Finaliza la configuración de posición del botón.
boton_simular = ttk.Button(  # Crea el botón que inicia las operaciones de demostración.
    ventana, text="Simular las 11 operaciones", command=mostrar_simulacion  # Define el texto del botón y la función que ejecuta.
)  # Guarda el botón para poder ubicarlo en la ventana.
boton_simular.grid(row=5, column=0, columnspan=5, pady=6)  # Sitúa el botón de simulación ocupando las cinco columnas.
salida_operaciones = tk.Text(ventana, height=9, wrap="word", state="disabled")  # Crea el cuadro no editable para mostrar resultados.
salida_operaciones.grid(row=6, column=0, columnspan=4, padx=12, pady=5, sticky="nsew")  # Ubica el cuadro de resultados debajo del botón.
scrollbar_operaciones = ttk.Scrollbar(ventana, orient="vertical", command=salida_operaciones.yview)  # Permite recorrer el reporte completo.
scrollbar_operaciones.grid(row=6, column=4, pady=5, sticky="ns")  # Ubica la barra al lado del reporte.
salida_operaciones.configure(yscrollcommand=scrollbar_operaciones.set)  # Sincroniza la barra con el contenido del reporte.
ventana.grid_rowconfigure(6, weight=1)  # Permite que la fila de resultados crezca al redimensionar la ventana.
actualizar_listas_sistema()  # Llena inicialmente las listas y selectores con los datos existentes.

ventana.mainloop()  # Mantiene abierta la ventana y atiende las acciones del usuario. 
