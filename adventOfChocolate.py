import random
import copy

chocolates =["rojo" for _ in range(7)]
chocolates +=["turquesa" for _ in range(6)]
chocolates +=["azul claro" for _ in range(7)]
chocolates +=["azul oscuro" for _ in range(7)]
chocolates +=["trufa" for _ in range(10)]
dia=int(input("¿Qué día es hoy? "))

random.seed(63 * 55321 ^ 28)
chocolate = ""
for i in range(dia):
    chocolate = random.choice(chocolates)
    chocolates.remove(chocolate)
    
    if i == dia - 1:
        break
    
    print(f'Día {i+1}: {chocolate}')
print("\nEl chocolate de hoy es: " + chocolate)
