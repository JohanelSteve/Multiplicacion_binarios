import sys, convertidor
from manejador_latex import *

def leer_archivo(archivo):
    """Lee un archivo y devuelve su contenido en una lista."""
    data = None
    with open(archivo, "r") as f:
        data = f.readlines()[0].split(" ")
    return data[1:]

def leer_argumentos(argumentos):
    """Lee los argumentos de la línea de comandos y los devuelve en una lista."""
    data = []
    for arg in argumentos[1:]:
        if arg[0] == '-':
            data.append(arg[1:])
        else:
            data.append(arg)
    return data

def procesar_entradas(operador, informacion):
    """Procesa las entradas para convertirlas a binario."""
    informacion[2] = operador.convertir_a_binario(informacion[2])
    informacion[4] = operador.convertir_a_binario(informacion[4])

if __name__ == "__main__":
    # Iniciar ejecución

    argumentos = sys.argv[1:]
    informacion = None
    pasos = [] # La lista de pasos que se mostrarán en el documento .tex

    # Leer los argumentos de la línea de comandos
    if argumentos[0] == "-f":
        informacion = leer_archivo(argumentos[1])
    else:
        informacion = leer_argumentos(argumentos)

    # Crear el convertidor y procesar las entradas
    operador = convertidor.Convertidor(int(informacion[0]))

    operador.pasos.append(Paso("Recepción de datos",
                    "Se recibe la cantidad de bits junto con las variables asociadas a sus respectivos valores.",
                    [Procedimiento("bits", '=', informacion[0]),
                        Procedimiento(informacion[1], '=', informacion[2]),
                        Procedimiento(informacion[3], '=', informacion[4])]))
    
    procesar_entradas(operador, informacion)


    operador.pasos.append(Paso("Convertir datos a binario",
                    "Se convierten los datos a listas de 0s y 1s para representar un valor binario.",
                    [Procedimiento(informacion[1], '=', Procedimiento("", '+' if informacion[2][0] == 1 else '-', informacion[2][1])),
                        Procedimiento(informacion[3], '=', Procedimiento("", '+' if informacion[4][0] == 1 else '-', informacion[4][1]))]))
    
    # Multiplicar los números binarios
    resultado = operador.multiplicacion_binaria(informacion[1], informacion[2][1], informacion[2][0], informacion[3], informacion[4][1], informacion[4][0])
    operador.pasos.append(Paso("Resultado",
                               "Se muestra el resultado de la multiplicación binaria.",
                               [Procedimiento("Resultado", '=',
                                              Procedimiento(Procedimiento(informacion[1], '*',
                                                                          Procedimiento(informacion[3], '=',
                                                                                        Procedimiento(Procedimiento("", '+' if informacion[2][0] == 1 else '-', informacion[2][1]), '*',
                                                                                                      Procedimiento("", '+' if informacion[4][0] == 1 else '-', informacion[4][1])))), '=', resultado))]))

    # Crear el archivo .tex y el PDF
    crear_documento_latex("pasos", operador.pasos)
    crear_pdf_latex("pasos")
