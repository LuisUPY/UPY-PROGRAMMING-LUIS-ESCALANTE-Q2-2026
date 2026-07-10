print("CW07 - Verifier Digit")

rol_input = input()

# Validar que hay exactamente un guión
if rol_input.count('-') != 1:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")
    exit()

rol_parte, dv_input = rol_input.split('-')

# Validar que los dígitos del rol sean numéricos
if not rol_parte.isdigit():
    print("Los digitos del rol deben ser numéricos")
    exit()

# Validar que el dígito verificador sea válido (numérico o K)
if len(dv_input) != 1 or (not dv_input.isdigit() and dv_input != 'K'):
    print("El digito verificador debe ser numérico")
    exit()

# Validar longitud de la parte del rol
if len(rol_parte) != 9:
    print("Rol inválido: No tiene el formato XXXXXXXXX-X")
    exit()

# Calcular el dígito verificador esperado
rol_invertido = rol_parte[::-1]
multiplicadores = [2, 3, 4, 5, 6, 7]
suma = 0

for i in range(len(rol_invertido)):
    digito = int(rol_invertido[i])
    multiplicador = multiplicadores[i % len(multiplicadores)]
    suma += digito * multiplicador

resto = suma % 11
dv_esperado = 11 - resto

# Casos especiales
if dv_esperado == 11:
    dv_esperado = 0
elif dv_esperado == 10:
    dv_esperado = 'K'

# Convertir a string para comparación
dv_esperado_str = str(dv_esperado)

# Validar que el dígito verificador coincida
if dv_input != dv_esperado_str:
    print(f"Error: El dígito verificador no conicide, se esperaba {dv_esperado}")
    exit()

# Si es válido, imprimir el ROL
print(rol_input)
