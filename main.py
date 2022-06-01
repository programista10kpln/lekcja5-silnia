from numpy import prod


def silnia(n):
    if n > 0:
        elementy = [n]
        while n > 1:
            elementy.append(n - 1)
            n -= 1
        return prod(elementy)
    elif n == 0:
        return 1
    else:
        return 'nie ma silni z ujemnej liczby'


while True:
    try:
        n = int(input('z czego chcesz silnie ziomek?\n'))
        break
    except ValueError:
        print('zła wartość')
        continue

print(silnia(n))
