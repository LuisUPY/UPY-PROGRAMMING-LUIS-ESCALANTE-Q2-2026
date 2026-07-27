import os

config = {}

# Resolve paths relative to this script so it works from any working directory
base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, "config.txt")
csv_path = os.path.join(base_dir, "clase.csv")

try:
    archivo = open(config_path, 'r')
except FileNotFoundError:
    raise FileNotFoundError('No se encontró el archivo "config.txt".')

try:
    for linea in archivo:
        linea = linea.strip()
        if not linea or linea.startswith("#") or "=" not in linea:
            continue
        try:
            clave, valor = linea.split("=", 1)
            config[clave.strip()] = float(valor.strip())
        except ValueError:
            raise ValueError('Línea inválida en config.txt: "' + linea + '". Se esperaba el formato clave=valor.')
finally:
    archivo.close()

# Parsear los enteros
try:
    ancho, alto, max_iter = int(config["ancho"]), int(config["alto"]), int(config["max_iter"])
except KeyError as e:
    raise KeyError('Falta la clave ' + str(e) + ' en config.txt.')
except ValueError:
    raise ValueError('Los valores de ancho, alto o max_iter no son números enteros válidos.')

if ancho == 0 or alto == 0:
    raise ValueError('ancho y alto no pueden ser 0, ya que se usan como divisores.')

try:
    salida = open(csv_path, 'w')
except Exception as e:
    raise Exception('No se pudo crear/abrir el archivo "clase.csv": ' + str(e))

try:
    salida.write("fila, columna,iteraciones\n")
    for fila in range(alto):
        for columna in range(ancho):
            try:
                real = config["real_min"] + (columna / ancho) * (config["real_max"] - config["real_min"])
                imag = config["imag_min"] + (fila / alto) * (config["imag_max"] - config["imag_min"])
            except KeyError as e:
                raise KeyError('Falta la clave ' + str(e) + ' en config.txt.')

            c = complex(real, imag)

            z = 0 + 0j
            iteraciones = 0

            while (abs(z) <= 2) and (iteraciones < max_iter):
                z = z * z + c
                iteraciones += 1

            salida.write(f"{fila}, {columna},{iteraciones}\n")
finally:
    salida.close()

print("DONE")
