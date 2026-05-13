def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    if b == 0:
        raise ValueError("Pas divisible par 0")
    return a / b

def carre(nombre):
    return nombre * nombre

def modulo(a, b):
    return a % b

def puissance(a, b):
    return a ** b

if __name__ == "__main__":
    print("Addition      : 2 + 3 =", additionner(2, 3))
    print("Soustraction  : 10 - 4 =", soustraire(10, 4))
    print("Multiplication: 3 x 4 =", multiplier(3, 4))
    print("Division      : 10 / 2 =", diviser(10, 2))
    print("Carre         : 5 * 5 =", carre(5))
    print("Modulo        : 10 % 3 =", modulo(10, 3))
    print("Puissance     : 2 ^ 3 =", puissance(2, 3))
