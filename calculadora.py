n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
op = input("Digite a operação (+, -, *, /): ")

if op == "+":
    print(f"{n1} + {n2} = {n1 + n2}")
elif op == "-":
    print(f"{n1} - {n2} = {n1 - n2}")
elif op == "*":
    print(f"{n1} * {n2} = {n1 * n2}")
elif op == "/":        
    if n2 != 0:
        print(f"{n1} / {n2} = {n1 / n2}")     
    else:       
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, *, /.")