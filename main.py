num1 = float(input("Введите первое число: ")) #запрашивает у пользователя число
num2 = float(input("Введите второе число: "))#запрашивает у пользователя число
num3 = float(input("Введите третье число: "))#запрашивает у пользователя число
if num1 >= num2:  #проверяем, больше ли num1 чем num2
    if num1 >= num3: #если num1 также больше или равно num3, то переменной largest присваивается значение num1
        largest = num1
    else: #иначе переменной largest присваивается значение num3
        largest = num3
else: #если num1 не боьлше или равно num2, то проверяется num2 >= num3
    if num2 >= num3: #если num2 также больше или равно num3, то переменной largest присваивается значение num2
        largest = num2
    else: #иначе переменной largest присваивается значение num3
        largest = num3
print(f"Наибольшее число: {largest}") #вывод
