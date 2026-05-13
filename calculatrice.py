def additionner(a, b):
    return a + b

def soustraire(a, b):
    return a - b

def multiplier(a, b):
    return a * b

def diviser(a, b):
    try:
        if b == 0:
            raise ValueError("Pas divisible par 0")

        resultat = a / b
        print(resultat)
        return resultat

    except ValueError as e:
        print(e)

if __name__ == "__main__":
    print("Addition      : 2 + 3 =", additionner(2, 3))
    print("Soustraction  : 10 - 4 =", soustraire(10, 4))
    print("Multiplication: 3 x 4 =", multiplier(3, 4))
    print("Division      : 10 / 2 =", diviser(10, 2))
    print("Division      : 10 / 0 =", diviser(10, 0))
   
