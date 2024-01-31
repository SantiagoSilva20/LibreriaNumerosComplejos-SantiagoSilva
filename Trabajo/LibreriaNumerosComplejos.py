import math as mt


def SumaComplejos(X,Y):
    ParteReal = X[0] + Y[0]
    ParteImaginaria = X[1] + Y[1]
    return ParteReal, ParteImaginaria
def ProductoNumComplejos(X,Y):
    ParteReal = X[0] * Y[0] - X[1] * Y[1]
    ParteImaginaria = X[0] * Y[1] + Y[0] * X[1]
    return ParteReal, ParteImaginaria
def RestaComplejos(X,Y):
    ParteReal = X[0] - Y[0]
    ParteImaginaria = X[1] - Y[1]
    return ParteReal, ParteImaginaria
def DivisionComplejos(X,Y):
    ParteReal = (X[0]*Y[0] + X[1]*Y[1]) / (Y[0] ** 2 + Y[1] ** 2)
    ParteImaginaria = (Y[0] * X[1] - X[0] * Y[1]) / (Y[0] ** 2 + Y[1] ** 2)
    return ParteReal, ParteImaginaria
def ModuloComplejos(X):
    Modulo = (X[0] ** 2 + X[1] ** 2) ** (1 / 2)
    return Modulo
def ConjugadoComplejos(X):
    return X[0], X[1] * -1
def FaseNumComplejo(X):
    return mt.atan2(X[1], X[0])
def ConversionPolarACartesiano(X):
    return (ModuloComplejos(X), FaseNumComplejo(X))
def ConversionCartesianoAPolar(X):
    return (X[0]*mt.cos(X[1]), X[0]*mt.sin(X[1]))
