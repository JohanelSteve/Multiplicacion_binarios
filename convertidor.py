from manejador_latex import *

class Convertidor:
    def __init__(self, bits):
        self.bits = bits
        self.pasos = []

    def binario_a_entero(self, n):
        """Convierte una lista de 0s y 1s en un entero."""
        return int(''.join(str(x) for x in n), 2)

    def entero_a_binario(self, n):
        """Convierte un entero en una lista de 0s y 1s."""
        expr = bin(n)[2:]
        extra = self.bits - len(expr)
        if extra > 0:
            expr = '0' * extra + expr
        elif extra < 0:
            expr = expr[abs(extra):]
        return [int(x) for x in expr]

    def hexadecimal_a_binario(self, n):
        """Convierte un número hexadecimal en una lista de 0s y 1s."""
        return self.entero_a_binario(int(n, 16))

    def caracter_es_digito(self, c):
        """Determina si un caracter es un dígito."""
        return c >= '0' and c <= '9'

    def convertir_a_binario(self, n):
        """Convierte un número en una lista de 0s y 1s junto con su signo al frente."""
        signo = 1
        primero = n[0]

        if self.caracter_es_digito(primero):
            return [signo, self.entero_a_binario(int(n))]
        
        resultado = None

        if (n[1] == 's' and n[2] == '-'):
            signo = -1
            n = n[3:]
        elif n[0] == 's' and n[1] == '-':
            signo = -1
            n = n[2:]
        else:
            n = n[1:]
        
        if primero == 'b':
            resultado = [int(x) for x in n]
        elif primero == 'h':
            resultado = self.hexadecimal_a_binario(n)
        else:
            resultado = self.entero_a_binario(int(n))

        return signo, resultado

    def sumar_binarios(self, a, b, bits=None):
        """Suma dos números binarios y devuelve el resultado."""
        if bits is None:
            bits = self.bits*2

        # Realizar la suma binaria
        carry = 0
        resultado = []
        for i in range(len(a)-1, -1, -1):
            suma = a[i] + b[i] + carry
            if suma == 2:
                resultado.insert(0, 0)
                carry = 1
            elif suma == 3:
                resultado.insert(0, 1)
                carry = 1
            else:
                resultado.insert(0, suma)
                carry = 0

        # Agregar un bit de carry si es necesario
        if carry == 1:
            resultado.insert(0, 1)

        return resultado[-bits:]

    def multiplicacion_binaria(self, nombre_a, a, signo_a, nombre_b, b, signo_b):
        """Realiza la multiplicación binaria de dos números binarios."""

        self.pasos.append(Paso("Tomar el valor absoluto de los números",
                            "Se toma el valor absoluto de los números para realizar la multiplicación.",
                            [Procedimiento('abs(' + nombre_a + ')', '=', a),
                                Procedimiento('abs(' + nombre_b + ')', '=', b)]))

        self.pasos.append(Paso("Multiplicación binaria",
                               "Se realiza la multiplicación binaria (de valor absoluto) de los dos números binarios.",
                               [Procedimiento(Procedimiento(Procedimiento(f"abs({nombre_a})", "*", f"abs({nombre_b})"), '=', Procedimiento(f"{a}", "*", f"{b}")), '=', "...")]))

        # Realizar la multiplicación de los valores absolutos en complemento a dos
        resultado_abs = self.multiplicacion_binaria_abs(a, b)

        # Determinar el signo del resultado y convertirlo a complemento a dos si es negativo
        resultado = resultado_abs if signo_a*signo_b == 1 else self.complemento_a_dos(resultado_abs)
        self.pasos.append(Paso("Aplicando negativos",
                               "Se determina el signo del resultado y se convierte a complemento a dos si es negativo.",
                               [Procedimiento(Procedimiento("", '+' if signo_a*signo_b == 1 else '-', resultado_abs), "=>", resultado)]))

        return resultado

    def multiplicacion_binaria_abs(self, a, b):
        """Realiza la multiplicación binaria de dos números binarios sin signo."""

        # Inicializar el resultado como una lista de ceros con longitud 2n

        self.pasos.append(Paso("Inicializar registro",
                               "Inicializar el resultado como una lista de ceros con longitud 2*self.bits.",
                               [Procedimiento("resultado", "=", [0] * (2*self.bits))]))
        resultado = [0] * (2*self.bits)


        # Realizar la multiplicación de manera iterativa
        for i in range(self.bits):
            # Si el bit de b es 1, sumar a * 2^i
            if b[self.bits - 1 - i] == 1:
                # Multiplicar a * 2^i y agregar 0s al inicio
                producto = [0] * (self.bits-i) + a + [0] * i

                # Agregar el resultado parcial a la lista de resultados
                resultado = self.sumar_binarios(resultado, producto)
                print(resultado)

        self.pasos.append(Paso("Recortar resultado",
                               "Recortar el resultado para la cantidad de bits en cuestión.",
                               [Procedimiento(resultado, '=', resultado[-self.bits:])]))
        return resultado[-self.bits:]

    def complemento_a_dos(self, a):
        """Convierte un número binario en complemento a dos."""

        # Calcular el complemento a uno invirtiendo los dígitos binarios
        complemento_uno = [1-d for d in a]

        # Sumar 1 al complemento a uno para obtener el complemento a dos
        n = len(complemento_uno)
        resultado = complemento_uno[:]
        for i in range(n-1, -1, -1):
            if complemento_uno[i] == 0:
                resultado[i] += 1
                break
            else:
                resultado[i] = 0

        return resultado
