from PIL import Image

config = {}

archivo = open("Classwork#12/config.txt", 'r')
for linea in archivo:
    linea = linea.strip()
    if not linea or "=" not in linea:
        continue
    clave, valor = linea.split("=", 1)
    config[clave.strip()] = float(valor.strip()) if "." in valor else int(valor.strip())
archivo.close()

with open("Classwork#12/clase.csv", 'r') as data:
    datos = data.readlines()

max_iter = int(config["max_iter"])

# Quitar encabezados
datos.pop(0)

# Calcular dimensiones reales desde el CSV
filas_cols = [list(map(int, d.strip().split(","))) for d in datos if d.strip()]
max_fila = max(r[0] for r in filas_cols) + 1
max_col  = max(r[1] for r in filas_cols) + 1

img = Image.new("HSV", (max_col, max_fila))

for fila, columna, iteraciones in filas_cols:
    brillo = 40 if (iteraciones == max_iter) else int((iteraciones / max_iter) * 255)
    img.putpixel((columna, fila), (brillo, 255, 255))

img_rgb = img.convert('RGB')
img_rgb.save("mandelbrot-clase2.png")

print("DONE")