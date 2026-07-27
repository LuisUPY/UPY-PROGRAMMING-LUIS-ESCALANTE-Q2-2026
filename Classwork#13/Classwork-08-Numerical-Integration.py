import math


class IntegrationError(Exception):
    pass


# INPUT
while True:
    try:
        a = input("write the left endpoint of the interval: ")
        b = input("write the right endpoint of the interval: ")
        f_x = input("write the function to integrate: ")
        method = input("Write the integration method (LRM/RRM/MRM/TRAP): ").upper()

        if "pi" in a:
            a = eval(a.replace("pi", str(math.pi)))
        else:
            a = float(a)

        if "pi" in b:
            b = eval(b.replace("pi", str(math.pi)))
        else:
            b = float(b)

        if method not in ("LRM", "RRM", "MRM", "TRAP"):
            raise ValueError("Invalid method selected. Choose LRM, RRM, MRM or TRAP.")

        # Test the expression once with a sample value to catch bad syntax early
        eval(f_x.replace("x", str(a)))

        break
    except ValueError as e:
        print(f"Error: {e}")
    except (SyntaxError, NameError, ZeroDivisionError) as e:
        print(f"Error in the function expression: {e}")

# PROCESS
n = 1000
h = (b - a) / n
area = 0.0
constant = 0
shift = 0
variable = 0

try:
    if method == "RRM":
        shift = 1

    if method == "MRM":
        constant = h / 2

    if method == "TRAP":
        variable = 1
        f_0 = f_x.replace("x", str(a))
        area += (h / 2) * eval(f_0)

        for i in range(variable, n):
            xi = a + i * h
            f_xi = f_x.replace("x", str(xi))
            area += (h / 2) * 2 * eval(f_xi)

        f_xn = f_x.replace("x", str(b))
        area += (h / 2) * eval(f_xn)

    else:
        for i in range(shift, n + shift):
            xi = a + i * h
            height = f_x.replace("x", str(xi + constant))
            area += h * eval(height)

except ZeroDivisionError:
    raise IntegrationError("Cannot complete the integration due to a division by zero.")
except Exception as e:
    raise IntegrationError(f"An unexpected error occurred while integrating: {e}")

# OUTPUT
print(f"the integration of {f_x} is {area}")
