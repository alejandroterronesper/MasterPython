"""
Crear una lista con el contenido
de esta tabla:
ACCION  AVENTURA   DEPORTES
GTA     ASSASIN     FIFA
COD     CRASH       PRO
PUGB    PRINCES     MOTO GP 21

mostrar esta informacion ordenada es decir, mostrar primero: ACCION, AVENTURA y luego DEPORTES


"""

listado = [
    {
        "categoria": "ACCION",
        "juego": ["GTA" ,"COD" ,"PUBG"]

    },
    {
        "categoria": "AVENTURA",
        "juego": ["assasin", "crash", "princes"]
    },
    {
        "categoria": "DEPORTES",
        "juego": ["fifa", "pro", "moto gp21"]
    }
]


for recorrer in listado:
    print(f"----------------{recorrer['categoria']}----------------")
    for juegos in recorrer['juego']:
        print(juegos)
        