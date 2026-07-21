class VerboInvalidoError(Exception):
    pass


# Spanish Verb Conjugator

pronombres = ['yo', 'tú', 'él/ella', 'nosotros', 'ustedes', 'ellos/ellas']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'an', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'en', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'en', 'en']
}

# INPUT
while True:
    try:
        verbo = input("Ingresa el verbo: ").strip().lower()

        if len(verbo) < 3:
            raise VerboInvalidoError("El verbo es demasiado corto. Debe tener al menos 3 letras.")

        if not verbo.isalpha():
            raise VerboInvalidoError("El verbo debe contener solo letras.")

        terminacion = verbo[-2:]

        if terminacion not in terminaciones:
            raise VerboInvalidoError(f"'{verbo}' no es un infinitivo válido. Debe terminar en -ar, -er o -ir.")

        break
    except VerboInvalidoError as e:
        print(f"Verbo inválido: {e}")

# PROCESS
raiz = verbo[:-2]
lista_terminaciones = terminaciones[terminacion]

# OUTPUT
try:
    for indice in range(len(pronombres)):
        print(pronombres[indice], raiz + lista_terminaciones[indice])
except IndexError as e:
    raise VerboInvalidoError(f"Error generando conjugaciones: {e}")
