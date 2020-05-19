def add(a, b):
    return a + b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b
def sub(a, b):
    return a - b
def pow1(a, b):
    if b == 0:
        return 1
    result = a
    for i in range(1, b):
        result = a * result
    return result
def calculate():
    num1 = int(input("введите первое число: "))
    num2 = int(input("введите второе число: "))
    operation = input("выберите операцию (*, /, +, -, ^): ")

    result = 0

    if operation == '*':
        result = mul(num1, num2)
    elif operation == '/':
        result = div(num1, num2)
    elif operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = sub(num1, num2)
    elif operation == '^':
        result = pow1(num1, num2)
    else:
        print("неподдерживаемая операция")
    print("результат: ", result )

# for i in range(2):
while True:
    # print("Запускаешься в " + str(i) + " раз!")
    calculate()


# arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# hash1 = { 'a' : 1, 'b' : 2}
