class RolInvalidoError(Exception):
    pass


# INPUT
rol_input = input("Escribe el rol: ")

# PROCESS
try:
    if rol_input.count('-') != 1:
        raise RolInvalidoError("Rol inválido: No tiene el formato XXXXXXXXX-X")

    rol_parte, dv_input = rol_input.split('-')

    if not rol_parte.isdigit():
        raise RolInvalidoError("Los digitos del rol deben ser numéricos")

    if len(dv_input) != 1 or (not dv_input.isdigit() and dv_input != 'K'):
        raise RolInvalidoError("El digito verificador debe ser numérico")

    if len(rol_parte) != 9:
        raise RolInvalidoError("Rol inválido: No tiene el formato XXXXXXXXX-X")

    rol_invertido = rol_parte[::-1]
    multiplicadores = [2, 3, 4, 5, 6, 7]
    suma = 0

    for i in range(len(rol_invertido)):
        digito = int(rol_invertido[i])
        multiplicador = multiplicadores[i % len(multiplicadores)]
        suma += digito * multiplicador

    resto = suma % 11
    dv_esperado = 11 - resto

    if dv_esperado == 11:
        dv_esperado = 0
    elif dv_esperado == 10:
        dv_esperado = 'K'

    dv_esperado_str = str(dv_esperado)

    if dv_input != dv_esperado_str:
        raise RolInvalidoError(f"El dígito verificador no conicide, se esperaba {dv_esperado}")

except RolInvalidoError as e:
    print(f"Error: {e}")
except ValueError:
    print("Rol inválido, no tiene el formato XXXXXXXXX-X")
else:
    # OUTPUT
    print(rol_input)
