def suma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    print(resultado)


suma(2, 5, 7)
suma(2, 5)
suma(2, 8, 7, 45, 32)
