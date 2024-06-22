import notas.nota as modelo

class Acciones:

    def crear(self,usuario):
        print(f"\nVale {usuario[1]} vamos a crear una nota: ")

        titulo = input("\nIntroduce el título de tu nota: ")
        descripcion = input("\nMete el contenido de tu nota:  ")

        nota = modelo.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"\nPerfecto has guardado la nota: {nota.titulo}")

        else:
            print(f"\nNo se ha guardado la nota {usuario[1]}")

    def mostrar(self, usuario):
        print(f"\nVale {usuario[1]} aquí tienes tus notas:    ")

        nota = modelo.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("\n**************")
            print(nota[2])
            print(nota[3])
            print("\n**************")

    def borrar(self, usuario):
        print(f"\n Muy bien {usuario[1]} es hora de borrar las pruebas")


        titulo = input("Introduce el título de la nota: ")

        nota = modelo.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >=1:
            print(f"Hemos borrado la nota {nota.titulo}")
        else:
            print("La nota no se ha borrado intentalo otra vez.")