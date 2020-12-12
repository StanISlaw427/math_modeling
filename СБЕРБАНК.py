x = int(input('Введите количество денег'))
y = int(input('Введите процент'))
n = int(input('Введите количество лет'))
for i in range(1, n+1, 1):
    x=x+y*x/100
print(x)