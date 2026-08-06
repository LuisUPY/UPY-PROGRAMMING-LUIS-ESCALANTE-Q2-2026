def recursiva(n):
    try:
        if n < 0:
            return "Error: n no puede ser negativo"
        if n == 0:
            return "Done!"
        print(n)
        return recursiva(n - 1)
    except TypeError:
        return "Error: n debe ser un numero"

def fibonacci(n):
    try:
        if n < 0:
            return "Error: n no puede ser negativo"
        elif n == 0 or n == 1:
            return n
        anterior = fibonacci(n - 1)
        penultimo = fibonacci(n - 2)
        return anterior + penultimo
    except TypeError:
        return "Error: n debe ser un numero"

def factorial(n):
    try:
        if n < 0:
            return "Error: n no puede ser negativo"
        if n <= 1:
            return 1
        return n * factorial(n - 1)
    except TypeError:
        return "Error: n debe ser un numero"

def multiplicacion_recursiva(n, m):
    try:
        if m < 0:
            return "Error: m no puede ser negativo"
        if m == 0:
            return 0
        parcial = multiplicacion_recursiva(n, m - 1)
        return parcial + n
    except TypeError:
        return "Error: n y m deben ser numeros"

def division_entera_recursiva(dividendo, divisor):
    try:
        if divisor == 0:
            return "Error: no se puede dividir entre 0"
        resto = dividendo - divisor
        if resto < 0:
            return 0
        return 1 + division_entera_recursiva(resto, divisor)
    except TypeError:
        return "Error: dividendo y divisor deben ser numeros"

def potencia_recursiva(base, exponente):
    try:
        if exponente < 0:
            return "Error: exponente no puede ser negativo"
        elif exponente == 0:
            return 1
        else:
            return base * potencia_recursiva(base, exponente - 1)
    except TypeError:
        return "Error: base y exponente deben ser numeros"

def serie_collatz(n):
    try:
        if n <= 0:
            return "Error: n debe ser un entero positivo"

        if n == 1:
            print("END!")
            return 0

        siguiente = n // 2 if n % 2 == 0 else 3 * n + 1
        print(siguiente)
        return serie_collatz(siguiente)
    except TypeError:
        return "Error: n debe ser un entero"

def aplanar_json(diccionario, clave_padre='', separador='.'):
    try:
        pares = {}
        for key, value in diccionario.items():
            nueva_llave = key if not clave_padre else f"{clave_padre}{separador}{key}"
            if isinstance(value, dict):
                sub_pares = aplanar_json(value, nueva_llave, separador)
                pares.update(sub_pares)
            else:
                pares[nueva_llave] = value
        return pares
    except AttributeError:
        return "Error: se esperaba un diccionario"

if __name__ == "__main__":
    print(recursiva(5))
    print(fibonacci(7))
    print(factorial(5))
    print(multiplicacion_recursiva(4, 3))
    print(division_entera_recursiva(17, 5))
    print(potencia_recursiva(2, 5))
    print(serie_collatz(6))
    print(aplanar_json({"a": 1, "b": {"c": 2}}))
    print(recursiva(-3))
    print(recursiva("5"))
    print(fibonacci(-1))
    print(factorial(-2))
    print(multiplicacion_recursiva(4, -3))
    print(division_entera_recursiva(10, 0))
    print(potencia_recursiva(2, -2))
    print(serie_collatz(0))
    print(serie_collatz(-6))
    print(aplanar_json(["a", "b", "c"]))
