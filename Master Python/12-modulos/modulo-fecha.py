#Vamos a ver los modulos mas importantes, como los de FECHA y CALCULADORA

#Modulo fechas: import datetime --> datetime.date.

import datetime


print(datetime.date.today())

fecha_completa = datetime.datetime.now()


print(fecha_completa)

print(fecha_completa.year)

print(fecha_completa.month)

print(fecha_completa.weekday())

print(fecha_completa.day)

#PERSONALIZAR FECHA  --> strftime %+d/m/Y 


custom = fecha_completa.strftime("%d/%m/%Y - %H:%M:%S ")
#todo en mayuscula menos el dia (d) y el mes (m)
print(f"Mi fecha personalidad:  {custom}")


print(datetime.datetime.now().timestamp())