# Declaramos la clase Televisor
# Esta clase representa un televisor con:
# marca, canal, volumen y estado de encendido
class Televisor():
    
    # Método constructor de la clase
    # Se ejecuta automáticamente cuando creamos un objeto
    # Sirve para dar valores iniciales a los atributos
    def __init__(self, marca, canal, volumen, encendido):
        self.marca = marca          # Marca del televisor
        self.__canal = canal          # Canal actual
        self.__volumen = volumen      # Volumen actual
        self.__encendido = encendido  # Estado del televisor: True o False

    # Método que muestra el menú principal
    def menu(self):
        opciones = -1  # Valor inicial para entrar al while
        
        # El menú se repetirá hasta que el usuario elija 0
        while opciones != 0:
            print("1 - Encender televisor")
            print("2 - Apagar televisor")
            print("3 - Cambiar canal")
            print("4 - Subir volumen")
            print("5 - Bajar volumen")
            print("6 - Mostrar estado")
            print("0 - Salir")

            # Intentamos convertir la opción ingresada a número entero
            # Si el usuario escribe texto, capturamos el error
            try:
                opciones = int(input("Escoge una de las siguientes opciones por favor: "))
            except ValueError:
                print("La opción ingresada no es válida, por favor solo considera números.")
                continue

            # Según la opción elegida, llamamos al método correspondiente
            if opciones == 1:
                self.encender_tv()
            
            elif opciones == 2:
                self.apagar_tv()

            elif opciones == 3:
                self.cambiar_canales()

            elif opciones == 4:
                self.subir_volumen()

            elif opciones == 5:
                self.bajar_volumen()
            
            elif opciones == 6:
                self.estado()

            elif opciones == 0:
                print("Programa terminado")
            
            else:
                print("Opción inválida, por favor inténtalo de nuevo")

    # Método para encender la TV
    def encender_tv(self):
        # Si ya está encendida, mostramos un mensaje
        if self.__encendido:
            print("La TV ya se encuentra encendida")
        else:
            # Si está apagada, cambiamos su estado a encendida
            self.__encendido = True
            print("TV encendida")

    # Método para apagar la TV
    def apagar_tv(self):
        # Si está encendida, la apagamos
        if self.__encendido:
            self.__encendido = False
            print("TV apagada")
        else:
            # Si ya estaba apagada, lo avisamos
            print("La TV ya se encuentra apagada")

    # Método para subir el volumen
    def subir_volumen(self):
        # Pedimos al usuario cuánto quiere subir el volumen
        try:
            nuevo_volumen = int(input("Ingresa cuánto volumen quieres subir: "))
        except ValueError:
            print("No se admiten textos, solo números. Inténtalo nuevamente.")
            return

        # Validamos que la TV esté encendida
        if not self.__encendido:
            print("Por favor verifica que la TV esté encendida")
        
        # Validamos que la cantidad a subir sea mayor que 0
        elif nuevo_volumen <= 0:
            print("La cantidad a subir debe ser mayor que 0")
        
        # Validamos que el volumen final no supere 100
        elif self.__volumen + nuevo_volumen <= 100:
            self.__volumen += nuevo_volumen
            print("El nuevo volumen es:", self.__volumen)
        
        # Si supera 100, no se permite
        else:
            print("El volumen no puede superar 100")

    # Método para bajar el volumen
    def bajar_volumen(self):
        # Pedimos al usuario cuánto quiere bajar el volumen
        try:
            bajando_volumen = int(input("Ingresa cuánto volumen quieres bajar: "))
        except ValueError:
            print("No se admiten textos, solo números. Inténtalo nuevamente.")
            return
    
        # Validamos que la TV esté encendida
        if not self.__encendido:
            print("Por favor verifica que la TV esté encendida")
        
        # Validamos que la cantidad a bajar sea mayor que 0
        elif bajando_volumen <= 0:
            print("La cantidad a bajar debe ser mayor que 0")
        
        # Validamos que el volumen final no quede bajo 0
        elif self.__volumen - bajando_volumen >= 0:
            self.__volumen -= bajando_volumen
            print("Volumen bajado a:", self.__volumen)
        
        # Si el volumen queda bajo 0, no se permite
        else:
            print("El volumen no puede quedar bajo 0")

    # Método para cambiar de canal
    def cambiar_canales(self):
        # Pedimos el nuevo canal
        try:
            nuevocanal = int(input("Ingresa el nuevo canal: "))
        except ValueError:
            print("La opción ingresada no es válida, por favor solo considera números")
            return
            
        # Validamos que la TV esté encendida
        # y que el canal sea mayor o igual a 1
        if self.__encendido and nuevocanal >= 1:
            self.__canal = nuevocanal
            print("Canal cambiado a:", self.__canal)
        else:
            print("El canal ingresado es incorrecto o la TV está apagada")

    # Método para mostrar el estado actual del televisor
    def estado(self):
        print("Marca:", self.marca)
        print("Canal:", self.__canal)
        print("Volumen:", self.__volumen)
        print("Encendido:", self.__encendido)


# Creamos un objeto de la clase Televisor
tv1 = Televisor("Sony", 1, 10, False)

# Ejecutamos el menú principal del televisor
tv1.menu()