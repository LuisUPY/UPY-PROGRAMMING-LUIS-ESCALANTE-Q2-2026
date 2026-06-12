print("CALCULADOR DE DÍGITO VERIFICADOR UTFSM")

rol = input("Ingrese el ROL sin guión ni dígito verificador: ")

# Invertir el número
rol_invertido = rol[::-1]

multiplicadores = [2, 3, 4, 5, 6, 7]
suma = 0

for i in range(len(rol_invertido)):
    digito = int(rol_invertido[i])
    multiplicador = multiplicadores[i % len(multiplicadores)]
    suma += digito * multiplicador

resto = suma % 11
dv = 11 - resto

# Casos especiales
if dv == 11:
    dv = 0
elif dv == 10:
    dv = "K"

print(f"El dígito verificador es: {dv}")
print(f"ROL completo: {rol}-{dv}")