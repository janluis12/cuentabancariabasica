# Declaramos la clase Producto
# Esta clase representa un producto con nombre, precio y stock
class Producto():
    
    # Método constructor de la clase
    # Se ejecuta automáticamente al crear un objeto
    # Sirve para dar valores iniciales a los atributos
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre        # Atributo público
        self.__precio = precio      # Atributo privado
        self.__stock = stock        # Atributo privado
        
    # Método que muestra el menú principal del programa
    def menu(self):
        opciones = -1  # Valor inicial para entrar al while
        
        # El menú seguirá mostrándose hasta que el usuario elija 0
        while opciones != 0:
            print("Bienvenido a Frutas,")
            print("1 - Mostrar información")
            print("2 - Reponer stock")
            print("3 - Vender productos")
            print("4 - Cambiar Precio")
            print("0 - Salir")
            
            # Intentamos convertir la opción ingresada a entero
            # Si el usuario escribe texto, capturamos el error
            try:
                opciones = int(input("Escoja una de las siguientes opciones a consultar: "))
            except ValueError:
                print("No se admite texto, solo caracteres numéricos. Vuelva a intentarlo por favor.")
                continue
            
            # Opción 1: mostrar la información del producto
            if opciones == 1:
                self.mostrar_informacion()
            
            # Opción 2: reponer stock
            elif opciones == 2:
                try:
                    nuevostock = int(input("Ingresa el nuevo stock: "))
                except ValueError:
                    print("No se admite texto, solo caracteres numéricos. Vuelva a intentarlo por favor.")
                    continue
                
                # Validamos que la cantidad sea válida
                if nuevostock >= 0:
                    print("Nuevas unidades ingresadas")
                    self.__stock += nuevostock
                else:
                    print("La cantidad ingresada no es correcta. Vuelva a intentarlo por favor.")
            
            # Opción 3: vender productos
            elif opciones == 3:
                try:
                    venderproductos = int(input("Ingresa la cantidad a comprar: "))
                except ValueError:
                    print("No se admite texto, solo caracteres numéricos. Vuelva a intentarlo por favor.")
                    continue
                
                # Validamos que la cantidad sea mayor que 0
                # y que no supere el stock disponible
                if venderproductos > 0 and venderproductos <= self.__stock:
                    self.__stock -= venderproductos
                    print("Producto vendido con éxito")
                else:
                    print("La cantidad ingresada no es válida. Vuelva a intentarlo por favor.")
            
            # Opción 0: salir del programa
            elif opciones == 0:
                print("Programa terminado")
            
            # Opción 4: cambiar precio
            elif opciones == 4:
                try:
                    nuevoprecio = int(input("Establece el nuevo precio: "))
                except ValueError:
                    print("No se admiten caracteres de texto, solo números. Vuelve a intentarlo por favor.")
                    continue
                
                # Validamos que el nuevo precio sea mayor que 0
                if nuevoprecio > 0:
                    print("Precio actualizado correctamente")
                    self.set_precio(nuevoprecio)
                else:
                    print("Monto no válido, vuelva a intentarlo por favor")
            
            # Si el usuario ingresa una opción fuera del menú
            else:
                print("Opción no válida")
    
    # Método para mostrar toda la información del producto
    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.get_precio())
        print("Stock:", self.get_stock())
    
    # Getter del stock
    # Devuelve el valor actual del stock
    def get_stock(self):
        return self.__stock
    
    # Setter del stock
    # Permite modificar el stock de forma controlada
    def set_stock(self, nuevostock):
        if nuevostock >= 0:
            self.__stock = nuevostock
        else:
            print("El stock debe ser mayor o igual que 0.")
    
    # Getter del precio
    # Devuelve el valor actual del precio
    def get_precio(self):
        return self.__precio
    
    # Setter del precio
    # Permite modificar el precio de forma controlada
    def set_precio(self, nuevoprecio):
        if nuevoprecio > 0:
            self.__precio = nuevoprecio
        else:
            print("El precio debe ser mayor que 0")


# Creamos un objeto de la clase Producto
frutas = Producto("manzana", 2000, 40)

# Ejecutamos el menú del producto
frutas.menu()