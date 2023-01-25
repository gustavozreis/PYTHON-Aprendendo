# fibonacci sequence

# cada número é igual a soma dos 2 números anteriores da sequencia
total = input('Quantos passos devo calcular? ')
fib_total = int(total)

def fibonacci(fib_total):
    fib_list = [0,1]
    print(fib_list[0], end=', ')
    
    for n in range(1, fib_total):
        if n == fib_total - 1:
            print(fib_list[n], end='.')
        else:            
            print(fib_list[n], end=', ')
            next_num = fib_list[n] + fib_list[n-1]
            fib_list.append(next_num)

fibonacci(fib_total)