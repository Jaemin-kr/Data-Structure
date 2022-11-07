print('1부터 n까지 정수의 합을 구합니다.')
n = int(input('n의 값을 입력하세요: '))

sum = 0


for i in range(1, n+1):
    sum += i

# sum = n*(n+1)//2
print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')