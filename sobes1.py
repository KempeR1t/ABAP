N = int(input('Введите любое целое положительное число '))
sum = 0

while N > 5:
    sum = sum + N // 5
    N = N // 5

print(sum)