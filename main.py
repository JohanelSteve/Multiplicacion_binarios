

Archivo = open("input.txt", "r", encoding="utf-8")
for entrada in Archivo:
    print(entrada)
if __name__ == '__main__':    # SEPARO STRINGS DE ENTRADA Y LOS CONVIERTO EN UNA LISTA
    lista = entrada
    load = list(lista)

####################################################################
    input_digit = load[5]
    factor_mul = int(input_digit)   # FACTOR DE MULTIPLICACION (BITS DE ENTRADA)
    print(factor_mul)

    numA = load[11:13]
    baseA = load[9] # Base de conversion NUMERO A
    print(baseA)
#####################################################################
    signoA = load[10]
    signoB = load[17]
    print("signo de A",signoA)
    print("signo de B",signoB)
#####################################################################
    numb = load[18:20]
    baseb = load[16]  # Base de conversion NUMERO B
    print(baseb)
if __name__ == '__main__':

    unionA = numA
    Lista_digitoA = ''.join(unionA)
    Num_A = int(Lista_digitoA)
    Numero_A = []                     #Nombre de LISTA DIGITO A
    Numero_A.append(Num_A)
    print(Numero_A)


if __name__ == '__main__':

    unionB = numb
    Lista_digitoB = ''.join(unionB)
    Num_B = int(Lista_digitoB)
    Numero_B = []                       # Nombre de LISTA DIGITO A
    Numero_B.append(Num_B)
    print(Numero_B)


Archivo.close() ##Cerrar txt

