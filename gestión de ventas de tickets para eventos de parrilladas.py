import json

# Definición de clases

class Persona:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Comprador(Persona):
    pass

class Organizador(Persona):
    pass

class Evento:
    def __init__(self, nombre, fecha, lugar):
        self.nombre = nombre
        self.fecha = fecha
        self.lugar = lugar

    def mostrar_detalle(self):
        pass

class EventoParrillada(Evento):
    def mostrar_detalle(self):
        return f"Parrillada: {self.nombre}, Fecha: {self.fecha}, Lugar: {self.lugar}"

class EventoVIP(Evento):
    def __init__(self, nombre, fecha, lugar, beneficios):
        super().__init__(nombre, fecha, lugar)
        self.beneficios = beneficios

    def mostrar_detalle(self):
        return f"Evento VIP: {self.nombre}, Fecha: {self.fecha}, Lugar: {self.lugar}, Beneficios: {self.beneficios}"

class Venta:
    def __init__(self, comprador, evento, cantidad, precio_unitario):
        self.comprador = comprador
        self.evento = evento
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario

    def calcular_total(self):
        return self.cantidad * self.precio_unitario

class GestorVentas:
    def __init__(self):
        self.ventas = []

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def generar_reporte_por_evento(self):
        reporte = {}
        for venta in self.ventas:
            if venta.evento.nombre not in reporte:
                reporte[venta.evento.nombre] = []
            reporte[venta.evento.nombre].append(venta.calcular_total())
        return reporte

    def generar_reporte_total(self):
        total = sum(venta.calcular_total() for venta in self.ventas)
        return total

    def guardar_ventas(self, filename):
        with open(filename, 'w') as f:
            ventas_json = [venta.__dict__ for venta in self.ventas]
            json.dump(ventas_json, f, indent=4)

    def cargar_ventas(self, filename):
        try:
            with open(filename, 'r') as f:
                ventas_json = json.load(f)
                self.ventas = [Venta(**venta) for venta in ventas_json]
        except FileNotFoundError:
            raise FileNotFoundError("El archivo de ventas no se encontró.")
        except json.JSONDecodeError:
            raise ValueError("El archivo de ventas no es válido.")

# Excepciones personalizadas
class EventoAgotadoError(Exception):
    pass

class DatosInvalidosError(Exception):
    pass

class ArchivoVentasError(Exception):
    pass

# Interfaz de Usuario
def mostrar_menu():
    print("1. Comprar tickets")
    print("2. Ver reporte de ventas por evento")
    print("3. Ver reporte de ventas total")
    print("4. Guardar ventas en archivo")
    print("5. Cargar ventas desde archivo")
    print("6. Salir")

def comprar_tickets(gestor_ventas):
    print("Selecciona el tipo de evento:")
    print("1. Parrillada")
    print("2. Evento VIP")
    opcion = input("Opción: ")
    if opcion == "1":
        evento = EventoParrillada("Parrillada de Verano", "15/03/2024", "Parque Central")
    elif opcion == "2":
        evento = EventoVIP("Fiesta VIP", "20/03/2024", "Club Privado", ["Barra libre", "Zona VIP"])
    else:
        print("Opción no válida.")
        return

    cantidad = int(input("Ingrese la cantidad de tickets que desea comprar: "))
    precio_unitario = 50  # Precio ficticio
    comprador = Comprador("Nombre Comprador", "correo@ejemplo.com")
    venta = Venta(comprador, evento, cantidad, precio_unitario)
    gestor_ventas.agregar_venta(venta)
    print("¡Compra realizada con éxito!")

def main():
    gestor_ventas = GestorVentas()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            comprar_tickets(gestor_ventas)
        elif opcion == "2":
            print("Reporte de ventas por evento:")
            print(gestor_ventas.generar_reporte_por_evento())
        elif opcion == "3":
            print("Reporte de ventas total:")
            print(gestor_ventas.generar_reporte_total())
        elif opcion == "4":
            filename = input("Ingrese el nombre del archivo para guardar las ventas: ")
            gestor_ventas.guardar_ventas(filename)
            print("Ventas guardadas en el archivo.")
        elif opcion == "5":
            filename = input("Ingrese el nombre del archivo para cargar las ventas: ")
            gestor_ventas.cargar_ventas(filename)
            print("Ventas cargadas desde el archivo.")
        elif opcion == "6":
            print("¡Gracias por utilizar nuestro sistema de gestión de ventas!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()