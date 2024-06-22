import clase

persona = clase.Persona()
persona.setNombre("Alejandro")
persona.setApellidos("Terrones")
persona.setAltura("170 cm")
persona.setEdad("24 años")

print(f"La persona se llama: {persona.getNombre()} {persona.getApellidos()}")


print(persona.caminar())

print("----------------------")

informatico = clase.Informatico()
informatico.setNombre("Cañete")

print(f"Este tio es {informatico.getNombre()}")
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)
print("----------------------")

tecnico = clase.TecnicoRedes()
tecnico.setNombre("Manolo")
print(tecnico.auditarRedes,tecnico.getNombre(),tecnico.getLenguajes())
