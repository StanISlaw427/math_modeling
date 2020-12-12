a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))
if a+b>c and b+c>a and a+c>b:
    if a==b or a==c or b==c:
        print("Этот треугольник равнобедренный")
    elif a==b==c:
        print("Этот треугольник равносторонний")
    else:
        print("Этот треугольник разносторонний")
else:
    print("Треугольник не существует")
    

