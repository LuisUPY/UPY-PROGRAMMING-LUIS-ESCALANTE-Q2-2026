import os
from PIL import Image

config = {}

# Resolve paths relative to this script so it works from any working directory
base_dir = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(base_dir, "config.txt")
csv_path = os.path.join(base_dir, "clase.csv")
image_path = os.path.join(base_dir, "mandelbrot-clase.png")

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
            valor = valor.strip()
            config[clave.strip()] = float(valor) if "." in valor else int(valor)
        except ValueError:
            raise ValueError('Línea inválida en "config.txt": ' + linea)
finally:
    archivo.close()

try:
    with open(csv_path, 'r') as data:
        datos = data.readlines()
except FileNotFoundError:
    raise FileNotFoundError('No se encontró el archivo "clase.csv".')

try:
    alto, ancho, max_iter = config["alto"], config["ancho"], config["max_iter"]
except KeyError as e:
    raise KeyError('Falta la clave ' + str(e) + ' en "config.txt".')

try:
    img = Image.new("HSV", (ancho, alto))
except Exception as e:
    raise Exception('No se pudo crear la imagen: ' + str(e))

# Quitar encabezados
try:
    encabezados = datos.pop(0)
except IndexError:
    raise IndexError('El archivo "clase.csv" está vacío.')

try:
    for dato in datos:
        dato = dato.strip()
        if not dato:
            continue
        try:
            fila, columna, iteraciones = map(int, dato.split(","))
        except ValueError:
            raise ValueError('Fila inválida en "clase.csv": ' + dato)

        brillo = 40 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)

        try:
            img.putpixel((columna, fila), (brillo, 255, 255))
        except IndexError:
            raise IndexError('Coordenadas fuera de rango: (' + str(columna) + ', ' + str(fila) + ')')
except ZeroDivisionError:
    raise ZeroDivisionError('"max_iter" no puede ser 0 en "config.txt".')

try:
    img_rgb = img.convert('RGB')
    img_rgb.save(image_path)
except Exception as e:
    raise Exception('No se pudo guardar la imagen: ' + str(e))

print("DONE")
