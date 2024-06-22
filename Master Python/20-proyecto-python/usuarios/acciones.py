import usuarios.usuario as modelo
import notas.acciones


class Acciones:

    def registro(self):
        print("\nSerá necesario que intruduzcas tus datos.")
    
        nombre = input("Dime tu nombre: ")
        apellidos = input("¿Cuales son tus apellidos?:  ")
        email = input("Tu correo:  ")
        password = input("Introduce una contraseña: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()
    
        if registro[0] >=1:
            print(f"\nSe consiguio {registro[1].nombre} te registraste con {registro[1].email}")
            

        else:
            print("\nAlgo falló")

    def login(self):
            print("\nIdenficate en el sistema:   ")
            try:
                email = input("Tu correo:  ")
                password = input("Introduce una contraseña: ") 

                usuario = modelo.Usuario('', '', email, password)
                login = usuario.identificar()


                if email == login[3]:
                    print(f"\nBienvenido {login[1]} te has registrado en el sistema {login[5]}")
                    self.proximasAcciones(login)
            except Exception as e:  
                print(type(e))
                print(type(e).__name__)  
                print("El login no es correcto")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)

        accion = input("¿Qué quieres hacer?:    ")
        hazEl = notas.acciones.Acciones()
        


        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)

        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        elif accion == "salir":
            print(f"Hasta luego {usuario[1]}.")
            exit()
            


         



        
