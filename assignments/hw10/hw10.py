

def fibonacci(index):
    fib = [1, 1]
    if index < 1:
        return
    for i in range(2, index):
        fib.append(fib[i - 1] + fib[i - 2])
    index = index - 1
    return fib[index]


def double_investment(principal, rate):
    final = principal * 2
    current = principal
    timer = 0
    while current < final:
        timer += 1
        current = current * (1 + rate)

    return timer

def syracuse(num):
    seq = [num]
    while num != 1:
        if num % 2 == 0:
            num = num // 2
            seq.append(num)
        else:
            num = 3 * num + 1
            seq.append(num)
    return seq

def goldbach(num):
    if num % 2 == 1:
        return

    for i in range(1, num):
        primes = []
        prime1 = True
        prime2 = True
        for j in range(2, i):
            if i % j == 0:
                prime1 = False

        if prime1:
            primes.append(i)
            remainder = num - i
            for j in range(2, remainder):
                if remainder % j == 0:
                    prime2 = False
        if prime1 and prime2:
            primes.append(num - i)
            return primes



