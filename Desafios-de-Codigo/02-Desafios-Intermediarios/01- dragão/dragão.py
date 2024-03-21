C = int(input())

D = 0

while D < C:

    for i in range(C):

        N = int(input())

        D += 1

        if N <= 8000:

            print('Inseto!')

        else:

                print('Mais de 8000!')