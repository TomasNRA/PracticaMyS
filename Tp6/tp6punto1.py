import numpy as np

DIASHABILES = 250
COSTOMANTENER = 70
MINSTOCK = 50

def main():
    stock = 90
    turnosAdicionales = 0
    costoMantenimineto = 0

    for i in range(DIASHABILES):
        stock += 130
        demanda = int(np.random.normal(loc=150, scale=25))
        stock -= demanda
        if stock <= MINSTOCK:
            turnosAdicionales += 1
            stock += 130
        if stock > 0:
            costoMantenimineto += stock*COSTOMANTENER
    print(stock)
    print(turnosAdicionales)
    print(costoMantenimineto)


if __name__ == "__main__":
    main()
