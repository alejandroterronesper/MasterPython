mi_texto = " 'Doctor' "
mi_texto2 = "Soy \"Cañete\" "
mi_texto3 = ' "medico" '
texto_unido = mi_texto + "  " + mi_texto2 + "        " + mi_texto3
print(texto_unido)


# salto de línea \n

texto_unido = mi_texto + "\n" + mi_texto2 + "\n" + mi_texto3
print(texto_unido)


# tabulación \t

texto_unido = mi_texto + "\t" + mi_texto2 + "\t" + mi_texto3
print(texto_unido)


#borrar variable anterior

texto_unido = mi_texto + " \r  " + mi_texto2 
print(texto_unido)