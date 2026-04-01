class Producto():
    
    #Constructor de la clase productos, que contiene nombre, precio, stock
    
    def __init__(self, nombre,precio,stock):
        self.nombre = nombre  #Atributo publico
        self.__precio = precio #Atributo privado
        self.__stock = stock #Atributo privado
        
        
    def menu(self):
        opciones = -1
        while opciones!=4:
            print("Bienvenido a Frutas,")
            print("1 - Mostrar información")
            print("2 - Reponer stock")
            print("3 - Vender productos")
            print("4 - salir")
            try:
                opciones = int(input(" escoja una de las siguientes opciones a consultar"))
            except ValueError:
                print("No se admite texto, solo caracteres numericos, vuelva a intentarlo por favor.")
                continue
            
            if opciones ==1:
                self.mostrar_informacion()
                
            elif opciones ==2:
                try:
                    nuevostock=int(input("Ingresa el nuevo stock"))
                    
                except ValueError:
                    print("No se admite texto, solo caracteres numericos, vuelva a intentarlo por favor.")
                    continue
                    
                if nuevostock>0:
                    print("Nuevas unidades ingresadas")
                    self.__stock +=nuevostock
                    
                else:
                    print("la cantidad ingresada no es correcta vuelva a intentarlo por favor")
                    
                
            elif opciones ==3:
                try:
                    venderproductos = int(input("Ingresa la cantidad a comprar"))
                except ValueError:
                    print("No se admite texto, solo caracteres numericos, vuelva a intentarlo por favor.")
                    continue
                
                if venderproductos> 0 and venderproductos<= self.__stock:
                    self.__stock -= venderproductos
                    print("Producto Vendido con exito")
                else:
                    print("la cantidad ingresada no es valida, vuelva a intentarlo por favor")
            
            elif opciones ==4:
                print("Programa terminado")
                
            else:
                print("opcion no valida")
                    
                
                
    
    def mostrar_informacion(self):
        print("Nombre", self.nombre)
        print("Precio", self.__precio)
        print("Stock", self.__stock)
        
    def get_stock(self):
        return self.__stock
        
    def set_stock(self, nuevostock):
        if nuevostock >= 0:
            self.__stock = nuevostock
        else:
            print("El stock debe ser mayor que 0.")
        
        
frutas = Producto("manzana",2000,40)
frutas.menu()
            