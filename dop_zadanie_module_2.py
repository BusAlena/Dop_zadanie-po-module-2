#a = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
n= int(input( 'Введите число от 3 до 20 :'))
result = ""
for i in range(1, n):
    for j in range(1, n):
        if (i + j) % n == 0:
           if i<j:
               result += f"{i}{j}"
print("Верхняя табличка", n)
print("Нижняя табличка:", result)
print("Добро пожаловать на выход!")