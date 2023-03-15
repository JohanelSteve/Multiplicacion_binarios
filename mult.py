import sys, convertidor
from manejador_latex import *

def leer_archivo(archivo):
    data = None
    with open(archivo, "r") as f:
        data = f.readlines()[0].split(" ")
    return data[1:]

def leer_argumentos(argumentos):
    data = []
    for arg in argumentos[1:]:
        if arg[0] == '-':
            data.append(arg[1:])
        else:
            data.append(arg)
    return data

def procesar_entradas(informacion):
    informacion[2] = convertidor.convertir_a_binario(informacion[2])
    informacion[4] = convertidor.convertir_a_binario(informacion[4])

if __name__ == "__main__":
    argumentos = sys.argv[1:]
    informacion = None
    pasos = []
    if argumentos[0] == "-f":
        informacion = leer_archivo(argumentos[1])
    else:
        informacion = leer_argumentos(argumentos)
    pasos.append(Paso("Recepción de datos",
                    "Se recibe la cantidad de bits junto con las variables asociadas a sus respectivos valores.",
                    [Procedimiento("bits", '=', informacion[0]),
                        Procedimiento(informacion[1], '=', informacion[2]),
                        Procedimiento(informacion[3], '=', informacion[4])]))
    procesar_entradas(informacion)
    pasos.append(Paso("Convertir datos a binario",
                    "Se convierten los datos a listas de 0s y 1s para representar un valor binario.",
                    [Procedimiento("bits", '=', informacion[0]),
                        Procedimiento(informacion[1], '=', Procedimiento("", '+' if informacion[2][0] == 1 else -1, informacion[2][1])),
                        Procedimiento(informacion[3], '=', Procedimiento("", '+' if informacion[4][0] == 1 else -1, informacion[4][1]))]))
    print(informacion)
    crear_documento_latex("pasos", pasos)
    crear_pdf_latex("pasos")
