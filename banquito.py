# Declaramos la clase CuentaBancaria
# Esta clase representa una cuenta bancaria con titular y saldo
class CuentaBancaria:
    
    # Método constructor de la clase
    # Se ejecuta automáticamente cada vez que creamos un objeto
    # Sirve para dar valores iniciales a los atributos
    def __init__(self, titular, saldo):
        self.titular = titular      # Atributo público: se puede acceder directamente
        self.__saldo = saldo        # Atributo privado: solo debe usarse dentro de la clase
    
    # Método que muestra el menú principal del sistema bancario
    def menu(self):
        opcion = -1  # Valor inicial para que el while comience
        
        # El menú seguirá mostrándose hasta que el usuario elija 0
        while opcion != 0:
            # Mostramos las opciones disponibles
            print("\n--- Bienvenido al banco ---")
            print("1 - Consultar saldo")
            print("2 - Depositar saldo")
            print("3 - Retirar saldo")
            print("4 - Ver titular")
            print("5 - Cambiar titular")
            print("6 - Mostrar datos completos")
            print("0 - Salir")
            
            # Intentamos convertir lo que escribe el usuario a número entero
            # Si escribe texto, se captura el error
            try:
                opcion = int(input("Elige una opción: "))
            except ValueError:
                print("No se admiten textos, solo números. Vuelve a intentarlo.")
                continue  # Vuelve al inicio del while
            
            # Según la opción elegida, llamamos al método correspondiente
            if opcion == 1:
                self.consultar_saldo()   # Muestra el saldo actual
            elif opcion == 2:
                self.depositar_saldo()   # Permite depositar dinero
            elif opcion == 3:
                self.retirar_saldo()     # Permite retirar dinero
            elif opcion == 4:
                self.titular_cuenta()    # Muestra el nombre del titular
            elif opcion == 5:
                # Pedimos al usuario el nuevo nombre del titular
                nuevo_nombre = input("Ingresa el nuevo titular: ")
                self.cambiar_titular(nuevo_nombre)  # Llamamos al método para cambiarlo
            elif opcion == 6:
                self.mostrar_datos()  #Muestra el nombre y saldo del titular
            elif opcion == 0:
                print("Saliendo del sistema...")
            else:
                print("Opción no válida, intenta nuevamente.")
    
    # Getter del saldo
    # Devuelve el saldo privado para poder consultarlo de forma controlada
    def get_saldo(self):
        return self.__saldo
    
    # Método para cambiar el titular de la cuenta
    # Recibe como parámetro el nuevo nombre del titular
    def cambiar_titular(self, nuevotitular):
        self.titular = nuevotitular
        print("Nuevo titular:", self.titular)
        
    #Metodo para imprimit titular y saldo
    def mostrar_datos(self):
        print("Titular:", self.titular)
        print("Saldo:", self.get_saldo())
    
    # Método para mostrar el saldo actual
    def consultar_saldo(self):
        print("Saldo:", self.get_saldo())
    
    # Método para depositar dinero en la cuenta
    def depositar_saldo(self):
        # Intentamos convertir el monto ingresado a entero
        try:
            monto = int(input("Ingresa el monto a depositar: "))
        except ValueError:
            print("No se admiten textos, solo números. Vuelve a intentarlo.")
            return  # Salimos del método si hay error
        
        # Verificamos que el monto sea mayor que 0
        if monto > 0:
            self.__saldo += monto   # Sumamos el monto al saldo actual
            print("Tu nuevo saldo es:", self.get_saldo())
        else:
            print("El monto debe ser mayor que 0. Inténtalo nuevamente.")
    
    # Método para retirar dinero de la cuenta
    def retirar_saldo(self):
        # Intentamos convertir el monto ingresado a entero
        try:
            monto = int(input("Ingresa el monto a retirar: "))
        except ValueError:
            print("No se admiten textos, solo números. Vuelve a intentarlo.")
            return  # Salimos del método si hay error
        
        # Validamos que el monto sea correcto
        if monto <= 0:
            print("El monto debe ser mayor que 0.")
        elif monto <= self.__saldo:
            self.__saldo -= monto   # Restamos el monto del saldo actual
            print("Saldo retirado con éxito.")
            print("Tu saldo actual es:", self.get_saldo())
        else:
            print("El monto excede el saldo disponible. Inténtalo nuevamente.")
    
    # Método para mostrar el nombre del titular de la cuenta
    def titular_cuenta(self):
        print("Titular:", self.titular)


# Creamos un objeto de la clase CuentaBancaria
# "banco1" tendrá como titular a "janluis" y saldo inicial de 1000
banco1 = CuentaBancaria("janluis", 1000)

# Ejecutamos el menú del objeto
# Desde aquí el usuario podrá interactuar con la cuenta
banco1.menu()