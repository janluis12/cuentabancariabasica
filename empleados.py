from io import open
class Empleados:
    def __init__(self, nombre):
        self.nombre = nombre
        self.lista_empleados = []  # Lista donde se almacena los empleados
        self.usuarios = {
                          "admin": {"password": "1234", "rol": "admin"},
                          "juan": {"password": "abc", "rol": "usuario"}
}
        

    def login(self):
        intentos = 3

        while intentos > 0:
            user = input("Usuario: ")
            password = input("Contraseña: ")

            if user in self.usuarios:
                if self.usuarios[user]["password"] == password:
                    print("Acceso correcto")
                    return user, self.usuarios[user]["rol"]
                else:
                    print("Contraseña incorrecta")
            else:
                print("Usuario no existe")

            intentos -= 1
            print(f"Intentos restantes: {intentos}")

        print("Acceso bloqueado")
        return None, None
                
                
        


    def guardar_empleados(self):
        mi_archivo = open("listaempleados.txt","w")
        for empleados in self.lista_empleados:
            mi_archivo.write(empleados + "\n")
        mi_archivo.close()
        print("empleados guardados con exito")

    def cargar_empleados(self):
        mi_archivo = open("listaempleados.txt","r")
        leer = mi_archivo.read()
        self.lista_empleados = leer.splitlines()
        mi_archivo.close()
        print("Empleados Cargados con exito")
        print("-", self.lista_empleados)

        
    def agregar_empleados(self):
        while True:
            nuevo = input("Agrega un empleado (o escribe 'salir'): ").capitalize() #Aqui le indicamos que cuando inserten nuevo empleados, sus iniciales seran en mayuscula

            if nuevo.lower() == "salir":
                break
            
            elif nuevo in self.lista_empleados:
                print("Ya se encuentra agregado el empleado")
                continue

            self.lista_empleados.append(nuevo)
            print(f"{nuevo} agregado correctamente")

        print("\nHas agregado", len(self.lista_empleados), "empleados")
        print("Lista final:")
        for persona in self.lista_empleados:
            print("-", persona)

    def eliminar_personas(self):
        eliminar = input("ingresa el empleado a eliminar").capitalize()

        if not self.lista_empleados:
            print("No hay empleados para eliminar")
            return
    
        if eliminar in self.lista_empleados:
            self.lista_empleados.remove(eliminar)
            print("Empleado eliminado con exito")
            self.guardar_empleados()
            print("Empleados actuales:")
            for e in self.lista_empleados:
                print("-",e)
        else:
            print("El empleado no existe")
                

    def menu(self):
        
        while True:
            print("1 - Agregar empleados")
            print("2 - Eliminar empleados")
            print("3 - guardar empleados")
            print("4 - Cargar empleados")
            print("5 - Salir")
            try:
                opciones=int(input("escoje una de las siguientes opciones"))
            except ValueError:
                print("No se aceptan caracteres de texto, solo numericos")
                continue
            
            if opciones == 1:
                self.agregar_empleados()

            elif opciones == 2:
                self.eliminar_personas()
            
            elif opciones == 3:
                self.guardar_empleados()

            elif opciones == 4:
                self.cargar_empleados()

            elif opciones == 5:
                print("Programa terminado con exito")
                break
                
empleados1 = Empleados("Empresa")
empleados1.login()
empleados1.cargar_empleados()   # primero cargar
empleados1.menu()               # luego trabajar
