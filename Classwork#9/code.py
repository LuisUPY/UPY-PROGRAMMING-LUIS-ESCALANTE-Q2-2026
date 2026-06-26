pronombres = ['yo', 'tú', 'él/ella', 'nosotros', 'ustedes', 'ellos/ellas']

terminaciones = {
    'ar': ['o', 'as', 'a', 'amos', 'an', 'an'],
    'er': ['o', 'es', 'e', 'emos', 'en', 'en'],
    'ir': ['o', 'es', 'e', 'imos', 'en', 'en']
}

verbo = input("Ingresa el verbo: ")

raiz = verbo[:-2]
terminacion = verbo[-2:]

lista_terminaciones = terminaciones[terminacion]

for indice in range(len(pronombres)):
    print(pronombres[indice], raiz + lista_terminaciones[indice])