numero = [0, 1, 2, 3, 4, 5, 6, 7]
# numero = [34, 56, 23, 11, 88, 17]
nu = sorted(numero)


def ordenar(lista):
    izquierda = []
    derecha = []
    for num in lista:
        if num is not None:
            if num % 2 == 0:
                izquierda.append(num)
            else:
                derecha.append(num)
    return izquierda + derecha


print(ordenar(numero))


def grados_a_radianes(grados):
    pi = 3.1415926535897932384
    return (pi*grados)/180


print(f"Lo radianes son {grados_a_radianes(60)}")


def factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact


print(f"Factorial {factorial(8)}")


def taylor_seno(x, n):
    sen = 0
    for i in range(0, n):
        sen += ((-1)**i * x**(2*i+1)) / factorial(2*i+1)
    return sen


pi = 3.1415926535897932384
print(f"seno  {taylor_seno(1.57*3,15)}")


def taylor_coseno(x, n):
    cos = 0
    for i in range(0, n):
        cos += ((-1)**i * x**(2*i)) / factorial(2*i)
    return cos


print(f"coseno  {taylor_coseno(1.57*3,15)}")


def dft(x):
    pi = 3.1415926535897932384
    N = len(x)
    X = [0]*N  # se crea el array lleno de ceros con la longitud N mientras se llena

    for k in range(N):
        for n in range(N):
            X[k] += x[n]*(taylor_coseno((2*pi*k*n)/N, N) -
                          1j*taylor_seno((2*pi*k*n)/N, N))
            # X[k] += x[n]*(taylor_coseno(grados_a_radianes((2*pi*k*(n/N)), N)
            #                           ) - 1j*taylor_seno(grados_a_radianes(2*pi*k*(n/N), N)))
    return X


print(f"La Dft de es {dft(numero)}")


def divide(lista):
    # Si la lista tiene solo un elemento, devolver la lista
    if len(lista) == 1:
        return dft(lista)
        # dft(lista[0], len(lista))

        # Encontrar el punto medio de la lista
    medio = len(lista) // 2
    print(f"medio {medio}")
    # Dividir la lista en dos partes
    derecha = lista[medio:]
    izquierda = lista[:medio]
    print(f"Izquierda {izquierda}")
    print(f"Derecha {derecha}")

    # Aplicar recursivamente la función divide a ambas partes
    resultados = []
    if izquierda is not None:
        # izquierda = sorted(izquierda)
        resultados += divide(izquierda)

    if derecha is not None:
        # derecha = sorted(derecha)
        resultados += divide(derecha)

    return resultados


# muestra = divide(ordenar(numero))
# print(f"La muestra es {muestra}")


# print(f"La DFT es {dft(0,8)}")
