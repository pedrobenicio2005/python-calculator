op = input("escolha o operador matematico( +,-,*,/ ): ")
num1 = float(input("digite o valor do primeiro numero: "))
num2 = float(input("digite o valor do segundo numero: "))

if op == "+":
    result = round(num1 + num2,2)
    print(result)
elif op == "-":
    result = round(num1 - num2,2)
    print(result)
elif op == "*":
    result = round(num1 * num2,2)
    print(result)
elif op == "/":
    result = round(num1/num2,2)
    print(result)
else:
    print("operador invalido...")
