print('a부터 b까지 정수의 합을 구합니다.')
a = int(input('integer a input: '))
b = int(input('integer b input: '))

sum = 0

if a>b:
    a, b = b, a

for i in range(a, b+1):
    sum += a

print(f'{a}부터 {b}까지의 합은 {sum}입니다.')