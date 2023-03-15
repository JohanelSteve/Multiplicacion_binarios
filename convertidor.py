class Convertidor:
    def __init__(self, bits):
        self.bits = bits

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

    def sumar_binarios(self, a, b):
        """Suma dos números binarios y devuelve el resultado."""
        # Ajustar las longitudes de las listas para que tengan la misma longitud
        while len(a) < len(b):
            a.insert(0, 0)
        while len(b) < len(a):
            b.insert(0, 0)

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

        return resultado

    def multiplicacion_binaria(self, a, b):
        # Convertir los números a listas de dígitos binarios
        a = [int(d) for d in str(abs(a))]
        b = [int(d) for d in str(abs(b))]

        # Calcular el tamaño máximo del resultado y extender los números con ceros a la izquierda
        n = max(len(a), len(b))
        a = [0] * (n - len(a)) + a
        b = [0] * (n - len(b)) + b

        # Determinar los signos de los números y convertirlos a valores absolutos en complemento a dos
        signo_a = -1 if a[0] == 1 else 1
        signo_b = -1 if b[0] == 1 else 1
        a_abs = a if signo_a == 1 else self.complemento_a_dos(a)
        b_abs = b if signo_b == 1 else self.complemento_a_dos(b)

        # Realizar la multiplicación de los valores absolutos en complemento a dos
        resultado_abs = self.multiplicacion_binaria_abs(a_abs, b_abs)

        # Determinar el signo del resultado y convertirlo a complemento a dos si es negativo
        signo_resultado = -1 if signo_a * signo_b == -1 else 1
        resultado = resultado_abs if signo_resultado == 1 else self.complemento_a_dos(resultado_abs)

        return resultado

    def multiplicacion_binaria_abs(self, a, b):
        # Inicializar el resultado como una lista de ceros con longitud 2n
        n = len(a)
        resultado = [0] * (2*n)

        # Realizar la multiplicación de manera iterativa
        for i in range(n):
            for j in range(n):
                producto = a[i] * b[j]
                resultado[i+j] += producto

        # Realizar el acarreo y ajuste de los dígitos binarios
        for i in range(2*n-1):
            acarreo = resultado[i] // 2
            resultado[i] %= 2
            resultado[i+1] += acarreo

        # Eliminar los ceros sobrantes del resultado
        while resultado[-1] == 0 and len(resultado) > 1:
            resultado.pop()

        return resultado

    def complemento_a_dos(self, a):
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


"""a = 1111111111
b = 1000110111
resultado = multiplicacion_binaria(a, b)
print(f"{a} x {b} = {resultado} (esperado: 14031)")"""

