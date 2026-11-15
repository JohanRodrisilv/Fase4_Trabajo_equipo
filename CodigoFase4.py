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
