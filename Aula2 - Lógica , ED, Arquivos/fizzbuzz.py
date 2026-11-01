def fizzbuzz(n, mensagem):

    for i  in range(n):
        i = i + 1
        if i % 3 == 0 and i % 5 == 0:
            m = "FizzBuzz"
        elif i % 3 == 0:
            m = "Fizz"
        elif i % 5 == 0:
            m = "Buzz"
        else:
            m = i

        mensagem.append(m)

    return mensagem

mensagem = []
n = int(input())

print(fizzbuzz(n,mensagem))